import pandas as pd


def load_data(path):
    df = pd.read_csv(path)

    print("✅ Data Loaded Successfully")
    print("Shape:", df.shape)
    return df


def explore_data(df):
    print("\n📊 First 5 Rows:")
    print(df.head())

    print("\n📋 Column Names:")
    print(df.columns)

    print("\nℹ️ Data Info:")
    print(df.info())

    print("\n📉 Missing Values:")
    print(df.isnull().sum())


def clean_data(df):
    print("\n🧹 Cleaning Data...")

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.dropna()

    print("✅ Cleaning Done")
    print("New Shape:", df.shape)

    return df
