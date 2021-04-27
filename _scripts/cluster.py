from sklearn.cluster import OPTICS
from _scripts.metadata import *

def cluster(df):
    brain = OPTICS(min_samples=c_min_samples, metric=c_metric, xi=c_xi)
    df.loc[:, cluster_key] = brain.fit_predict(df[clustering_features])
    df = df[df[cluster_key] >= 0]

    return df
