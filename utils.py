import pandas as pd
import requests as r
import re
import yaml
from sklearn import *
import pandas as pd
import numpy as np
import mlflow
import yaml
import logging
import joblib
import sys
import os
import click

sys.path.append(os.getcwd())

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

with open('ops/config.yml') as  w:
    params = yaml.safe_load(w)
    model_params = params['stage']['evaluate']['model']
    mlflow_params = params['stage']['evaluate']['mlflow']

