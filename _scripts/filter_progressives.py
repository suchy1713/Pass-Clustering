import numpy as np
from _scripts.metadata import *

def euclidean(x1, y1, x2, y2):
    return np.sqrt(np.power((x1-x2), 2) + np.power((1-y2), 2))


def filter_progressives(df):
    df.loc[:, start_goal_dist_key] = euclidean(
        df[start_x_key], df[start_y_key],
        field_length, field_width/2
    )

    df.loc[:, end_goal_dist_key] = euclidean(
        df[end_x_key], df[end_y_key],
        field_length, field_width/2
    )

    df.loc[:, advanced_percent_key] = (df[start_goal_dist_key] - df[end_goal_dist_key])/df[start_goal_dist_key]
    filtered_df = df[df[advanced_percent_key] > progressive_min_dist_percent]
    filtered_df = filtered_df.drop(columns=[start_goal_dist_key, end_goal_dist_key, advanced_percent_key])

    print(f'All Passes: {len(df)}\nProgressive Passes: {len(filtered_df)} ({np.round(len(filtered_df)/len(df)*100, 2)}%)')

    return filtered_df
