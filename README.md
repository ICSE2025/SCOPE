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
        - <img width="1344" alt="image" src="https://github.com/FSE24/SCOPE/assets/79156929/b6c30ec8-7966-4a53-8558-e8aa30863135">

    - **Warm starts**:
        - Different constraints of the stop criterion: PT4Cloud, Metior
            - <img width="1346" alt="image" src="https://github.com/FSE24/SCOPE/assets/79156929/3a7b3ecc-5a6d-44d0-a30c-851e31fe3ba2">
            - <img width="1342" alt="image" src="https://github.com/FSE24/SCOPE/assets/79156929/57161a20-69c1-42e0-8b74-8009466bdf73">

        
        - Different numbers of repetitions of the run interval: PT4Cloud, Metior
            - <img width="1342" alt="image" src="https://github.com/FSE24/SCOPE/assets/79156929/ec266241-4c2a-4dfd-bd72-7552b9be8ff4">
            - <img width="1342" alt="image" src="https://github.com/FSE24/SCOPE/assets/79156929/db7121d2-c911-4286-8d61-5e545d5fcb83">

        
        - Different constraints of our stop criterion: SCOPE 1, SCOPE 2, SCOPE 3
            - <img width="1346" alt="image" src="https://github.com/FSE24/SCOPE/assets/79156929/69a270ff-7007-41d2-b117-d1c70c05150e">
            - <img width="1346" alt="image" src="https://github.com/FSE24/SCOPE/assets/79156929/573e53ee-85f5-4bd8-a7b8-3359edd34fab">
            - <img width="1346" alt="image" src="https://github.com/FSE24/SCOPE/assets/79156929/c170facd-3da8-40f7-9df3-4e09b378bd38">

        
        - Different numbers of repetitions of the run interval: SCOPE 1, SCOPE 2, SCOPE 3
            - <img width="1343" alt="image" src="https://github.com/FSE24/SCOPE/assets/79156929/f391f65a-2571-445b-bedf-ce4213a3e533">
            - <img width="1346" alt="image" src="https://github.com/FSE24/SCOPE/assets/79156929/5311ec18-f5e7-437a-be19-32e3f756ffd8">
            - <img width="1346" alt="image" src="https://github.com/FSE24/SCOPE/assets/79156929/f66ffd6c-94e2-4d7e-8357-1c304c3194fa">



## Function types and performance testing results (examples under cold starts)
|  FuncID   | Type  | Pt4Cloud | Metior | SCOPE |
|  ----  | ----  | ----  | ----  | ----  |
| Func5 | Image processing | 27.55%  | 8.79% | 95.53% |
| Func5 | Image processing | 27.55%  | 8.79% | 95.53% |




