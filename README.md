# SuperFlow: Performance Testing for Serverless Computing

- Dataset:
    - The details of relevant research papers (59 papers): 
        - see the file "Relevant Research Papers.xlsx", containing CSRankings category, conference, publication venue, and paper titile.
    - The details of relevant serverless functions (65 serverless functions):
        - see the file "Relevant Serverless Functions.xlsx", containing function name, tested input, executed serverless platform, programming language, timeout time, memory size, **code link**, corresponding research papers.
        - see the directory “input”, containing the large tested inputs for specific serverless functions.
    - The performance data of serverless functions:
        - see the file "Performance Data.xlsx", containing 1,000 points about performance results for each serverless function.

- Code：
    - The implementation of state-of-the-art techniques: PT4Cloud and Metior
        - see the file "**state-of-the-arts.py**" and use the methods "fse19method" and "ase21method". Moreovre, **the evaluation of testing results is included.**
    -  The implmentation of our approach SuperFlow
        - see the file "**SuperFlow.py**" and use the mothod "determineStopRun" with different variants: general, bootstrapping, and block bootstrapping. Moreovre, **the evaluation of testing results is included.**
        
        
        
        
- Other results:
    - Cold starts for SuperFlow 2 in different numbers of repetitions of the run interval:
        - <img width="581" alt="image" src="https://user-images.githubusercontent.com/79156929/227688371-cd362c4f-42f4-4ebc-8aa7-e8a54d028858.png">
    - Warm starts:
        - different constrains of the stop criterion: PT4Cloud, Meitor
            - <img width="433" alt="image" src="https://user-images.githubusercontent.com/79156929/227689330-3dcb1d45-00c3-41c8-a56a-faaef77ab1b6.png">
            - <img width="434" alt="image" src="https://user-images.githubusercontent.com/79156929/227689762-c5ca9ae7-efd5-4e7f-a48d-8fb5d9666b34.png">
        
        - different numbers of repetitions of the run interval: PT4Cloud, Meitor
            - <img width="434" alt="image" src="https://user-images.githubusercontent.com/79156929/227689777-1f6efa89-b240-48b4-b3f5-075e3f4e1081.png">
            - <img width="434" alt="image" src="https://user-images.githubusercontent.com/79156929/227689815-3a433bef-5860-4eca-8f15-9d4a6480efc9.png">
        
        - different constrains of our stop criterion: SuperFlow 1, SuperFlow 2, SuperFlow 3
            - <img width="434" alt="image" src="https://user-images.githubusercontent.com/79156929/227689416-5c02c6a1-e523-4100-b35c-5516a65e4b00.png">
            - <img width="434" alt="image" src="https://user-images.githubusercontent.com/79156929/227689427-d759c104-fdae-4e79-8382-6b02feadf312.png">
            - <img width="434" alt="image" src="https://user-images.githubusercontent.com/79156929/227689438-ff132f94-563f-44ed-8733-9e66a61d0d5f.png">
        
        - different numbers of repetitions of the run interval: SuperFlow 1, SuperFlow 2, SuperFlow 3
            - <img width="434" alt="image" src="https://user-images.githubusercontent.com/79156929/227689449-45dd4649-4464-4411-a703-83c2a9c94b78.png">
            - <img width="434" alt="image" src="https://user-images.githubusercontent.com/79156929/227689465-bbc1d72b-ad27-48e3-ae1c-c7f9dc88491d.png">
            - <img width="434" alt="image" src="https://user-images.githubusercontent.com/79156929/227689486-0045944d-2875-4da2-8144-9b7a20fd99c0.png">





        






