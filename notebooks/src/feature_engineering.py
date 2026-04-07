import numpy as np

def create_features(df):

    print("\n Feature Engineering Started...")

    # Convert loyalty_member to numeric
    df['loyalty_member'] = df['loyalty_member'].map({'Yes': 1, 'No': 0})

    #  Define CHURN (VERY IMPORTANT)
    df['churn'] = np.where(df['days_since_last_purchase'] > 90, 1, 0)

    # Additional useful features
    df['avg_value_per_order'] = df['avg_order_value']

    print(" Features Created")

    print("\n Churn Distribution:")
    print(df['churn'].value_counts())

    return df