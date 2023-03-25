# SCOPE: Performance Testing for Serverless Computing

- Dataset:
    - The details of relevant research papers: 
        - see the file "Executed serverless functions.xlsx", containing CSRankings category, conference, publication venue, and paper titile.
    - The details of relevant serverless functions:
        - see the file "Relevant Serverless Functions.xlsx", containing function name, tested input, executed serverless platform, programming language, timeout time, memory size, code link, corresponding research papers.
        - see the directory “input”, containing the large tested inputs for specific serverless functions.
    - The performance data of serverless functions:
        - see the file "Performance Data.xlsx", containing 1,000 points about performance results for each serverless function.

- Code：
    - The implementation of state-of-the-art techniques: PT4Cloud and Metior
        - see the file "**state-of-the-arts.py**" and use the methods "fse19method" and "ase21method"
    -  The implmentation of our approach SCOPE
        - see the file "**SCOPE.py**" and use the mothod "determineStopRun" with different variants: general, bootstrapping, and block bootstrapping.
        
        
        
        
- Other results:
    - Cold starts for SCOPE 2 in different numbers of repetitions of the run interval:
        - <img width="581" alt="image" src="https://user-images.githubusercontent.com/79156929/227688371-cd362c4f-42f4-4ebc-8aa7-e8a54d028858.png">
    - Warm starts:
        - different constrains of the stop criterion: PT4Cloud, Meitor
            - <img width="433" alt="image" src="https://user-images.githubusercontent.com/79156929/227689330-3dcb1d45-00c3-41c8-a56a-faaef77ab1b6.png">
            - <img width="434" alt="image" src="https://user-images.githubusercontent.com/79156929/227689333-4f671f96-e3f8-44bf-952b-fae470956c5d.png">
        
        - different numbers of repetitions of the run interval: PT4Cloud, Meitor
            - <img width="434" alt="image" src="https://user-images.githubusercontent.com/79156929/227689359-5bf495cb-c8b5-4a45-8510-68a46a4252e3.png">
            - <img width="434" alt="image" src="https://user-images.githubusercontent.com/79156929/227689371-a55d03ab-d739-4496-9576-39e135fe9ec1.png">
        
        - different constrains of our stop criterion: SCOPE 1, SCOPE 2, SCOPE 3
            - <img width="434" alt="image" src="https://user-images.githubusercontent.com/79156929/227689416-5c02c6a1-e523-4100-b35c-5516a65e4b00.png">
            - <img width="434" alt="image" src="https://user-images.githubusercontent.com/79156929/227689427-d759c104-fdae-4e79-8382-6b02feadf312.png">
            - <img width="434" alt="image" src="https://user-images.githubusercontent.com/79156929/227689438-ff132f94-563f-44ed-8733-9e66a61d0d5f.png">
        
        - different numbers of repetitions of the run interval: SCOPE 1, SCOPE 2, SCOPE 3
            - <img width="434" alt="image" src="https://user-images.githubusercontent.com/79156929/227689449-45dd4649-4464-4411-a703-83c2a9c94b78.png">
            - <img width="434" alt="image" src="https://user-images.githubusercontent.com/79156929/227689465-bbc1d72b-ad27-48e3-ae1c-c7f9dc88491d.png">
            - <img width="434" alt="image" src="https://user-images.githubusercontent.com/79156929/227689486-0045944d-2875-4da2-8144-9b7a20fd99c0.png">





        






