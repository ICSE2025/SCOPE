# SCOPE: Performance Testing for Serverless Computing

- Data:
    - The details of serverless functions from an existing dataset (including 65 serverless functions):
        - see the file "**Dataset - Serverless Functions.xlsx**", containing the function ID, function name, tested input, executed serverless platform, programming language, timeout time (second), memory size (MB), and code link.
    - The performance data of serverless functions:
        - see the file "**Performance Data.xlsx**", containing 1,000 performance results of each serverless function that is repeatedly executed.

- Code：
    - We made publicly available the deployment packages for the 65 serverless functions we used.
        - see the directory "**Deployment Packages**", containing the source code from func1 to func65.
        - see the included directory "**input**", containing the long input payload sample about func20, func29, func54, func56, func57, and func60.
    - Invocation scripts for serverless functions are included in the directory "**scripts**", which have the invocation code for serverless functions hosted in serverless platforms (AWS Lambda and Google Cloud Functions).
      - "**invokeAWSFunction-run1.py**" and **invokeAWSFunction-run2.py**" are the scripts that invoke serverless functions executed on AWS Lambda
      - "**invokeGoogleFunction.py**" is the script that invokes serverless functions executed on Google Cloud Functions
    - The implementation of state-of-the-art techniques: PT4Cloud and Metior
        - see the file "**state-of-the-arts.py**" and use the methods "fse19method" and "ase21method". Moreover, **the evaluation of testing results is in the method - identifyEffectiveness.**
    -  The implementation of our approach SCOPE
        - see the file "**SCOPE.py**" and use the method "determineStopRun" with different variants: general, bootstrapping, and block bootstrapping. Moreover, **the evaluation of testing results is in the method - identifyEffectiveness.**
        
        
- Other figure results:
    - **Cold starts** for SCOPE 2 in different numbers of repetitions of the run interval:
        - <img width="581" alt="image" src="https://user-images.githubusercontent.com/79156929/227688371-cd362c4f-42f4-4ebc-8aa7-e8a54d028858.png">
    - **Warm starts**:
        - Different constraints of the stop criterion: PT4Cloud, Metior
            - <img width="433" alt="image" src="https://user-images.githubusercontent.com/79156929/227689330-3dcb1d45-00c3-41c8-a56a-faaef77ab1b6.png">
            - <img width="434" alt="image" src="https://user-images.githubusercontent.com/79156929/227689762-c5ca9ae7-efd5-4e7f-a48d-8fb5d9666b34.png">
        
        - Different numbers of repetitions of the run interval: PT4Cloud, Metior
            - <img width="434" alt="image" src="https://user-images.githubusercontent.com/79156929/227689777-1f6efa89-b240-48b4-b3f5-075e3f4e1081.png">
            - <img width="434" alt="image" src="https://github.com/FSE24/SCOPE/assets/79156929/f04d45bd-5a9b-470f-94e7-4c8a898bf42f">
        
        - Different constraints of our stop criterion: SCOPE 1, SCOPE 2, SCOPE 3
            - <img width="434" alt="image" src="https://user-images.githubusercontent.com/79156929/227689416-5c02c6a1-e523-4100-b35c-5516a65e4b00.png">
            - <img width="434" alt="image" src="https://user-images.githubusercontent.com/79156929/227689427-d759c104-fdae-4e79-8382-6b02feadf312.png">
            - <img width="434" alt="image" src="https://user-images.githubusercontent.com/79156929/227689438-ff132f94-563f-44ed-8733-9e66a61d0d5f.png">
        
        - Different numbers of repetitions of the run interval: SCOPE 1, SCOPE 2, SCOPE 3
            - <img width="434" alt="image" src="https://user-images.githubusercontent.com/79156929/227689449-45dd4649-4464-4411-a703-83c2a9c94b78.png">
            - <img width="434" alt="image" src="https://user-images.githubusercontent.com/79156929/227689465-bbc1d72b-ad27-48e3-ae1c-c7f9dc88491d.png">
            - <img width="434" alt="image" src="https://user-images.githubusercontent.com/79156929/227689486-0045944d-2875-4da2-8144-9b7a20fd99c0.png">





