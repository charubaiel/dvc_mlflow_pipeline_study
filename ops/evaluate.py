from __init__ import *
from utils import *
from mlflow.models.signature import infer_signature



mlflow.set_tracking_uri(mlflow_params['tracking_server'])
mlflow.set_experiment(mlflow_params['experiment_name'])


def evaluate_run(params,path_to_df:str='data/eval_df.csv'):


    with mlflow.start_run(run_name='dvc_test'):


        df = pd.read_csv(path_to_df).set_index('tconst')
        data = df.drop('averageRating',axis=1)
        target = df['averageRating']

        x,xv,y,yv = model_selection.train_test_split(data,target,train_size=.7)

        mlflow.log_params(params)

        lr = linear_model.ElasticNet(**params)

        lr.fit(x,y)
        singaturka = infer_signature(xv,yv)

        model_info = mlflow.sklearn.log_model(lr,
                                artifact_path=mlflow_params['models_path'],
                                registered_model_name="dvc_test-elastic_movie_score_pred",
                                signature=singaturka)


        

        mae_clip = np.mean(np.abs(np.round(lr.predict(xv),0) - yv.round(0)))
        mae = np.mean(np.abs(lr.predict(xv) - yv))

        mlflow.log_metric('MAE_clip',mae_clip)
        mlflow.log_metric('MAE',mae)

        result = mlflow.evaluate(
                                model_info.model_uri,
                                xv.assign(label=yv.values),
                                targets="label",
                                model_type="regressor",
                                dataset_name="imdb",
                                evaluators=["default"],
                            )
if __name__ == '__main__':
    evaluate_run(params = model_params)