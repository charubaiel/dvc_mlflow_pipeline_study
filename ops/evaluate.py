from __init__ import *
from utils import *



def evaluate_run(params,path_to_df='data/eval_df.csv'):

    mlflow.set_tracking_uri("http://localhost:5000")

    with mlflow.start_run(run_name='exp1'):

        df = pd.read_csv(path_to_df).set_index('tconst')
        data = df.drop('averageRating',axis=1)
        target = df['averageRating']

        x,xv,y,yv = model_selection.train_test_split(data,target,train_size=.7)

        mlflow.log_param('alpha',params['alpha'])

        lr = linear_model.ElasticNet(alpha=params['alpha'])

        lr.fit(x,y)
        mlflow.sklearn.log_model(lr,
                                params['models_path'],
                                registered_model_name="elastic-model")

        mae_clip = np.mean(np.abs(np.round(lr.predict(xv),0) - yv.round(0)))
        mae = np.mean(np.abs(lr.predict(xv) - yv))

        mlflow.log_metric('MAE_clip',mae_clip)
        mlflow.log_metric('MAE',mae)


if __name__ == '__main__':
    evaluate_run(params_eval)