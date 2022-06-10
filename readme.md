
## Steps

MLFlow server run:
```
mlflow ui --backend-store-uri sqlite:///data/mlflow/mlruns.db\
            --default-artifact-root data/mlflow/registry
```

Pipeline full run:
```
python3 pipeline.py
```

## ETC:
### steps

Download:
    - Done

Data cleaning:
    - ratings (done)
    - basics (done)
    - principals (omw)
        (person = rating_vector | film_vector)

Services:
    - Mlflow (done)
    - Docker (done)
    - Deploy (done)
    - DVC (halfdone)

### deploy
[reference to compose IaC for deploy](https://github.com/charubaiel/mlops_compose/tree/master)
'''
deploy version #5
s3
postgres
mlflow
'''


MLFlow:
    runs and serve locally:
    '''
    mlflow models serve --no-conda -m mlflow-artifacts:/0/69853daacf7b4fe69bd8482adcc0a99e/artifacts/models -h 0.0.0.0 -p 8001
    '''

    build and serve on docker:~3.5 gb
    '''
     mlflow models build-docker -m mlflow-artifacts:/0/69853daacf7b4fe69bd8482adcc0a99e/artifacts/models -n 'elastic_docker'
        docker run -p 5001:8080 "elastic_docker" -d
    '''
