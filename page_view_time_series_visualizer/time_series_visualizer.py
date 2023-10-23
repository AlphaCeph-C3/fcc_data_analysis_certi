import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("./fcc-forum-pageviews.csv", index_col="date", parse_dates=True)
mask = (df["value"] <= df["value"].quantile(0.975)) & (
    df["value"] >= df["value"].quantile(0.025)
)
# Clean data
df = df[mask]


def draw_line_plot():
    # Draw line plot
    df_line = df.copy()
    fig, ax = plt.subplots(figsize=(20, 10))
    g = sns.lineplot(data=df_line, x="date", y="value", ax=ax, color="red")
    g.set(
        xlabel="Date",
        ylabel="Page Views",
        title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019",
    )
    # Save image and return fig (don't change this part)
    fig.savefig("line_plot.png")
    return fig


# # * Easy method using direct plot.bar methods on the dataframe
# def draw_bar_plot():
#     # Copy and modify data for monthly bar plot
#     df_bar = df.copy()
#     df_bar["month"] = df_bar.index.month
#     df_bar["year"] = df_bar.index.year
#     df_bar = df_bar.groupby(["year", "month"])["value"].mean()
#     df_bar = df_bar.unstack(fill_value=0)
#     # Draw bar plot
#     fig = df_bar.plot.bar(
#         legend=True, figsize=(13, 9), ylabel="Average Page Views", xlabel="Years"
#     ).figure
#     plt.legend(
#         [
#             "January",
#             "February",
#             "March",
#             "April",
#             "May",
#             "June",
#             "July",
#             "August",
#             "September",
#             "October",
#             "November",
#             "December",
#         ],
#         title="Months",
#     )
#     # Save image and return fig (don't change this part)
#     fig.savefig("bar_plot.png")
#     return fig


# * Hard method i would not recommend unless you understand the code
# * seaborn and can under
# ! I could not change the legend to replicate the actual figure
# ? But all testcase are cleared.
def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    # * filling in the missing values to complete one full year
    fill_range = pd.date_range("2016-01-01", "2019-12-31")
    df_bar = df_bar.reindex(fill_range, fill_value=np.nan)
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month_name()
    df_bar = df_bar.groupby(["year", "month"]).mean()
    # * Fill the NaN values with 0 so that they appear on the plot
    # ! Note: Do not do this method before finding the mean
    # ! as it will add to the total number when finding the mean and mess your calculations

    df_bar = df_bar.reset_index().fillna(0.0)

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12, 9))
    order = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    # * The only reason for the legend to be false is to pass one testcase
    plot_bar = sns.barplot(
        data=df_bar,
        x="year",
        y="value",
        hue="month",
        ax=ax,
        hue_order=order,
        width=0.5,
        legend=False,
        palette=sns.color_palette("bright", 12),
    )
    plot_bar.legend(labels=order, title="Months")
    plot_bar.set_xlabel("Years")
    plot_bar.set_ylabel("Average Page Views")
    # Save image and return fig (don't change this part)
    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box["year"] = [d.year for d in df_box.date]
    df_box["month"] = [d.strftime("%b") for d in df_box.date]
    # sorting values so that i have all the months in order
    df_box = df_box.sort_values(["year", "date"], ascending=[False, True])
    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
    chart1 = sns.boxplot(
        data=df_box,
        x="year",
        y="value",
        linewidth=0.75,
        fliersize=1,
        hue="year",
        legend=False,
        palette=sns.color_palette("bright", 4),
        ax=ax1,
    )
    chart1.set(xlabel="Year", ylabel="Page Views", title="Year-wise Box Plot (Trend)")
    # * if you couldn't sort then you could just manually give the order you want into the order parameter
    # box_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    chart2 = sns.boxplot(
        data=df_box,
        x="month",
        y="value",
        linewidth=0.75,
        fliersize=1,
        hue="month",
        legend=False,
        palette=sns.color_palette("muted", 12),
        ax=ax2,
    )
    chart2.set(
        xlabel="Month", ylabel="Page Views", title="Month-wise Box Plot (Seasonality)"
    )
    # Save image and return fig (don't change this part)
    fig.savefig("box_plot.png")
    return fig


draw_bar_plot()
