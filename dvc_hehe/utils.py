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

logging.basicConfig(\
    # filename='../monitor_log.log',\
        level=logging.INFO,format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",encoding='utf-8')

