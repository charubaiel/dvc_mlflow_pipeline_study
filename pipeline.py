from ops.download import download_imdb_data
from ops.clean_data import clean_basics, get_eval_dataframe
from ops.evaluate import evaluate_run
from utils import *


logging.info('START Pipeline')
download_imdb_data(params=params_download)
logging.info('START Cleaning data')
clean_basics()
logging.info('START Collect data')
get_eval_dataframe()
logging.info('START Evaluating model')
evaluate_run(params=params_eval)