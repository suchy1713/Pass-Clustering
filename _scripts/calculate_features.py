import numpy as np
from _scripts.metadata import *

# calculate the pass angle in relation to the horizontal ax of the field
def pass_angle(df):
    vector1 = [
        df[end_x_key] - df[start_x_key],
        df[end_y_key] - df[start_y_key]
    ]
    vector2 = [1, 0]

    cosTh = np.dot(vector1, vector2)
    sinTh = np.cross(vector1, vector2)

    return np.rad2deg(np.arctan2(sinTh,cosTh))  


def calculate_features(df):
    df.loc[:, angle_key] = df.apply(pass_angle, axis=1)
    return df
