# 24ds1000012@ds.study.iitm.ac.in
# Purpose: Demonstrate interactive, self-documenting data analysis in Marimo

import marimo

__generated_with = "0.9.15"
app = marimo.App()


# --- Cell 1: Import libraries and load dataset ------------------------
# This cell prepares the dataset and makes it available for analysis.
@app.cell
def __():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    # Generate synthetic dataset
    np.random.seed(42)
    df = pd.DataFrame({
        "x": np.linspace(0, 10, 100),
        "noise": np.random.normal(0, 1, 100)
    })
    df["y"] = 2 * df["x"] + df["noise"]

    df.head()
    return df, np, pd, plt
# ----------------------------------------------------------------------


# --- Cell 2: Slider widget for slope adjustment -----------------------
# This cell creates an interactive slider. The output of this slider
# is used by the plotting cell to adjust the regression line.
@app.cell
def __():
    import marimo as mo

    slope_slider = mo.ui.slider(start=1, stop=5, step=0.1, value=2.0, label="Adjust slope")
    slope_slider
    return slope_slider,
# ----------------------------------------------------------------------


# --- Cell 3: Visualization --------------------------------------------
# This cell depends on:
#   - df from Cell 1 (dataset)
#   - slope_slider from Cell 2 (widget state)
# It generates a scatterplot with a regression line whose slope
# changes dynamically with the slider.
@app.cell
def __(df, slope_slider, plt, np):
    slope = slope_slider.value

    plt.figure(figsize=(6, 4))
    plt.scatter(df["x"], df["y"], alpha=0.6, label="Data points")
    plt.plot(df["x"], slope * df["x"], color="red", label=f"y = {slope:.1f}x")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Interactive Regression Line")
    plt.legend()
    plt.grid(True)
    plt.show()
# ----------------------------------------------------------------------


# --- Cell 4: Dynamic Markdown -----------------------------------------
# This cell produces a textual summary that updates whenever
# the slider state changes.
@app.cell
def __(slope_slider):
    import marimo as mo

    slope = slope_slider.value
    mo.md(f"""
    ### 📊 Dynamic Analysis Summary

    - Current regression slope (from slider): **{slope:.2f}**
    - This slope is applied to the regression line in the plot above.
    - Try adjusting the slider to see how the line changes!
    """)
# ----------------------------------------------------------------------


if __name__ == "__main__":
    app.run()


