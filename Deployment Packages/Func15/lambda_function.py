import boto3
from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.externals import joblib
import joblib
import pandas as pd
from time import time
import os
import re

s3_client = boto3.client('s3')
tmp = '/tmp/'
cleanup_re = re.compile('[^a-z]+')


def cleanup(sentence):
    sentence = sentence.lower()
    sentence = cleanup_re.sub(' ', sentence).strip()
    return sentence

def lambda_handler(event, context):
    x = event['x']
    # x='The ambiance is magical. The food and service was nice! The lobster and cheese was to die for and our steaks were cooked perfectly.'

    dataset_object_key = event['dataset_object_key']
    dataset_bucket = event['dataset_bucket']

    model_object_key = event['model_object_key']  # example : lr_model.pk
    model_bucket = event['model_bucket']

    model_path = tmp + model_object_key
    # model_path ="lr_model.pk"
    if not os.path.isfile(model_path):
        s3_client.download_file(model_bucket, model_object_key, model_path)

    # dataset_path = 's3://'+dataset_bucket+'/'+dataset_object_key

    model_path_data = tmp + dataset_object_key
    s3_client.download_file(dataset_bucket, dataset_object_key, model_path_data)
    dataset = pd.read_csv(model_path_data)
    # dataset = pd.read_csv("reviews20mb.csv")

    start = time()

    df_input = pd.DataFrame()
    df_input['x'] = [x]
    df_input['x'] = df_input['x'].apply(cleanup)

    dataset['train'] = dataset['Text'].apply(cleanup)

    tfidf_vect = TfidfVectorizer(min_df=100).fit(dataset['train'])

    X = tfidf_vect.transform(df_input['x'])

    model = joblib.load(model_path)
    y = model.predict(X)
    print(y)

    latency = time() - start

    return latency

# print(lambda_handler("", ""))
