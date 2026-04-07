import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def train_model(df):

    # Drop unnecessary columns and prevent leakage
    X = df.drop(['Customer_ID', 'churn', 'days_since_last_purchase'], axis=1)
    y = df['churn']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Model
    model = RandomForestClassifier(
        class_weight={0: 1, 1: 3},
        random_state=42
    )
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    print("\n  Classification Report:")
    print(classification_report(y_test, y_pred))

    feature_importance = pd.Series(model.feature_importances_, index=X.columns)
    print("\n📊 Feature Importance:")
    print(feature_importance.sort_values(ascending=False))

    return model
