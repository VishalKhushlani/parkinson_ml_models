import pandas as pd                 # pandas is a dataframe library
import matplotlib.pyplot as plt      # matplotlib.pyplot plots data


def plot_corr(df, size=24):
    corr = df.corr()  # data frame correlation function
    fig, ax = plt.subplots(figsize=(size, size))
    ax.matshow(corr)  # color code the rectangles by correlation value
    print(plt.xticks(range(len(corr.columns)), corr.columns))  # draw x tick marks
    print(plt.yticks(range(len(corr.columns)), corr.columns))  # draw y tick marks


if __name__ == "__main__":
    df = pd.read_csv("./parkinsons.data")
    print(df.shape) # rows and columns of data
    # print(df.isnull().values.any()) # checking for null values
    del df['name']  # Deleting the column name
    print(df.shape)
    plot_corr(df)






