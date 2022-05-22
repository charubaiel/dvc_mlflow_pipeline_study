from download import download_imdb_data
from clean_data import clean_basics, get_eval_dataframe
from evaluate import evaluate_run
from utils import *


with open('config.yml') as  w:
    params = yaml.safe_load(w)
    params_download = params['stage']['download']['params']
    params_eval = params['stage']['evaluate']['params']


download_imdb_data(params=params_download)

clean_basics()

get_eval_dataframe()

evaluate_run(params=params_eval)