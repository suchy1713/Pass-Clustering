import numpy as np
from _scripts.plt_utils import plot_arrow
from _scripts.metadata import *
from _scripts.field import draw_field

def plot_cluster(ax, df, color):
    for _, row in df.iterrows():
        plot_arrow(
            ax, row[start_x_key], row[start_y_key], row[end_x_key], row[end_y_key],
            color, PassArrow
        )

    plot_arrow(
        ax, df[start_x_key].mean(), df[start_y_key].mean(), df[end_x_key].mean(), df[end_y_key].mean(),
        color, AvgArrow
    )


def plot_clusters(ax, df):
    draw_field(ax)

    clusters_to_plot = df[cluster_key].value_counts().index[:n_top_clusters_to_plot]
    np.random.shuffle(cluster_colors)

    for i in range(len(clusters_to_plot)):
        cluster = clusters_to_plot[i]
        color = cluster_colors[i]

        cluster_df = df[df[cluster_key] == cluster]
        plot_cluster(ax, cluster_df, color)