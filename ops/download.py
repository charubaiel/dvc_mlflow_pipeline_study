from __init__ import *
from utils import *

def download_imdb_data(params):

    datasets_urls = ['https://datasets.imdbws.com/title.basics.tsv.gz',
                    'https://datasets.imdbws.com/title.principals.tsv.gz',
                    'https://datasets.imdbws.com/title.ratings.tsv.gz']

    ratings = pd.read_csv("https://datasets.imdbws.com/title.ratings.tsv.gz",sep='\t',compression='gzip')
    ratings = ratings[ratings['numVotes']>params['minimal_num_votes']].set_index('tconst')


    for index,url in enumerate(datasets_urls,1):

        tmp_df = pd.read_csv(url,compression='gzip',sep='\t',chunksize=100000)
        tmp_ttl_df = pd.DataFrame()

        for sample in tmp_df:
            tmp_ttl_df = tmp_ttl_df.append(sample[sample['tconst'].isin(ratings.index)])

        name = url.replace('.tsv.','').replace('gz','').replace('.','_').split('com/')[1]
        tmp_ttl_df.to_csv('data/'+name+'.csv',index=False)

        logging.info(f'COMPLETE {name} {index}/{len(datasets_urls)} download step')


if __name__ == '__main__':
    download_imdb_data(params_download)