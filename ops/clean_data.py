from __init__ import *
from utils import *


def clean_basics(csv_path='data/title_basics.csv'):
    basics = pd.read_csv(csv_path)
    basics['genres'] = basics['genres'].str.split(',')

    basics['startYear'] = basics['startYear'].replace('\\N',None).astype(int)
    basics['runtimeMinutes'] = basics['runtimeMinutes'].replace('\\N',None).astype(int)

    genres_vec = pd.get_dummies(basics.explode('genres'),columns=['genres']).filter(regex='genre').groupby(level=0).max()
    basics = basics.drop(['genres','endYear','originalTitle'],axis=1).join(genres_vec)

    basics = basics[basics['titleType'].isin(['movie','tvMovie','tvMiniSeries'])]
    basics = pd.get_dummies(basics,columns=['titleType'])
    
    basics.to_csv(csv_path,index=False)



def get_eval_dataframe(data_folder='data'):
    ratings = pd.read_csv(f'{data_folder}/title_ratings.csv')
    basics = pd.read_csv(f'{data_folder}/title_basics.csv')

    df = basics.merge(ratings, on= 'tconst').set_index('tconst').drop('primaryTitle',axis=1)
    df.to_csv(f'{data_folder}/eval_df.csv')



if __name__ == '__main__':
    clean_basics()
    get_eval_dataframe()