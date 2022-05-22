
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
    - DVC (omw)
