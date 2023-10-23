import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("./epa-sea-level.csv", index_col="Year")
    # Create scatter plot
    plt.figure(figsize=(14, 9))
    plt.scatter(df.index, df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    line1_res = linregress(df.index, df["CSIRO Adjusted Sea Level"])
    line1_x_values = np.arange(1880, 2051)
    line1_y_values = line1_res.slope * line1_x_values + line1_res.intercept
    plt.plot(line1_x_values, line1_y_values, "-.", color="black")
    # Create second line of best fit
    recent_years_df = df[df.index >= 2000]
    line2_res = linregress(
        recent_years_df.index, recent_years_df["CSIRO Adjusted Sea Level"]
    )
    line2_x_values = np.arange(2000, 2051)
    line2_y_values = line2_res.slope * line2_x_values + line2_res.intercept
    plt.plot(line2_x_values, line2_y_values, "--", color="red", label="since 2000 data")
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
