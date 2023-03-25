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
    - cold starts for SCOPE 2 in different numbers of repetitions of the run interval:
    <img width="581" alt="image" src="https://user-images.githubusercontent.com/79156929/227688371-cd362c4f-42f4-4ebc-8aa7-e8a54d028858.png">
