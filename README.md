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
        - see the file "state-of-the-arts.py" and use the methods "fse19method" and "ase21method"
    -  The implmentation of our approach SCOPE
        - see the file "SCOPE.py" and use the mothod "determineStopRun" with different variants: general, bootstrapping, and block bootstrapping.