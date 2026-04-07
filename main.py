from src.data_preprocessing import load_data, explore_data, clean_data
from src.feature_engineering import create_features

def main():
    df = load_data("data/dataset.csv")

    explore_data(df)

    df = clean_data(df)

    df = create_features(df)

if __name__ == "__main__":
    main()