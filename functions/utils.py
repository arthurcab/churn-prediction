"""
This file contains the custom functions defined to clean-up, prepare and visualize the data.
"""

import pandas as pd
import matplotlib.pyplot as plt

def identify_empty_cols(df):
    """
    Identifies columns containing only 0s, only NaNs, or a combination of both.

    Args:
        df: The DataFrame to check.

    Returns:
        A dictionary with three keys: 'all_zero', 'all_nan', and 'mixed',
        where the values are lists of the corresponding column names.
    """
    result = {
        'all_zero': [],
        'all_nan': [],
        'mixed': [] 
    }

    for col in df.columns:
        if (df[col] == 0).all():
            result['all_zero'].append(col)
        elif df[col].isna().all():
            result['all_nan'].append(col)
        elif (df[col].isna() | (df[col] == 0)).all() and not df[col].isna().all():
            result['mixed'].append(col)

    return result

def zscore_outlier_removal(df, cols, thresh=3):
      """
  Identifies outliers based on z-scores exceeding a threshold and updates the dataframe 

  Args:
      data (pd.Series): The pandas Series containing your data.
      cols (list): A list of strings with the target column names
      thresh (float, optional): The standard deviation threshold for outliers. Default 3.

  Returns:
      A copy of the trimmed dataframe 
  """
      df_copy = df.copy()
      
      for col in cols:
        mean = df_copy[col].mean()
        std = df_copy[col].std()
        z_scores = (df_copy[col] - mean) / std
        df_copy = df_copy[abs(z_scores) <= thresh]  # Remove outliers beyond threshold in standard deviations
    
      return df_copy


def create_comparison_boxplots(X, Y, xlabel, titles=("Before", "After"), figsize=(10, 5)):
    """
    Creates side-by-side boxplots for comparing two datasets.

    Args:
        X (array-like): Data for the first boxplot.
        Y (array-like): Data for the second boxplot.
        xlabel (string): The x label for the charts.
        titles (tuple, optional): Titles for the subplots. Defaults to ("Before", "After").
        figsize (tuple, optional): Size of the figure. Defaults to (10, 5).
    """

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)  

    bp1 = ax1.boxplot(X, vert=False)
    bp2 = ax2.boxplot(Y, vert=False)

    ax1.set_xlabel(xlabel)
    ax1.set_title(titles[0])
    ax2.set_xlabel(xlabel)
    ax2.set_title(titles[1])

    fig.suptitle('Boxplot comparison')
    plt.tight_layout()
    plt.show()  

def create_comparison_histograms(X, Y, xlabel, titles=("Before", "After"), figsize=(10, 5)):
    """
    Creates side-by-side histograms for comparing two datasets.

    Args:
        X (array-like): Data for the first histogram.
        Y (array-like): Data for the second histogram.
        xlabel (string): The x label for the charts.
        titles (tuple, optional): Titles for the subplots. Defaults to ("Before", "After").
        figsize (tuple, optional): Size of the figure. Defaults to (10, 5).
    """

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)  

    ax1.hist(X)
    ax2.hist(Y)

    ax1.set_xlabel(xlabel)
    ax1.set_title(titles[0])
    ax2.set_xlabel(xlabel)
    ax2.set_title(titles[1])

    fig.suptitle('Histogram comparison')
    plt.tight_layout()
    plt.show()