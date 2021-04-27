import matplotlib.pyplot as plt
from _scripts.metadata import *

def plot_arrow(ax, start_x, start_y, end_x, end_y, color, arrow_type):
    ax.arrow(
        x=start_x,
        y=start_y,
        dx=end_x-start_x,
        dy=end_y-start_y,
        width=arrow_type.width,
        head_width=3*1.3*arrow_type.width,
        head_length=1.5*1.3*(3*1.3*arrow_type.width),
        alpha=arrow_type.opacity,
        length_includes_head=True,
        color=color,
        zorder=arrow_type.zorder
    )


def add_ax_title(ax, team, column):
    title_txt = f'{team}{ax_title_txts[column]}'
    ax.set_title(
        title_txt.upper(),
        color=font_color,
        alpha=0.75,
        weight=600,
        fontsize=15,
        pad=8.5,
        zorder=-2,
        bbox=dict(
            facecolor='#262626',
            edgecolor='#0d0d0d',
            linewidth=4,
            alpha=1,
            boxstyle='Square,pad=0.55'
        )
    )


def add_title(fig, title):
    fig.text(
        0.5, 0.963, title.upper(),
        color=font_color, alpha=0.85, weight=600, fontsize=26,
        ha='center'
    )


def add_subtitle(fig, subtitle):
    fig.text(
        0.5, 0.937, subtitle.upper(),
        color=font_color, alpha=0.65, weight=600, fontsize=14,
        ha='center'
    )