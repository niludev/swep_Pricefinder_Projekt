import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from django.conf import settings

DATASET_PATH = 'datasets/car_price_prediction.csv'
data = pd.read_csv(DATASET_PATH)

selected_columns = [
    'price', 'manufacturer', 'model', 'prod.year', 'category', 'leather interior', 'fuel type', 'engine volume',
    'mileage', 'cylinders', 'gear box type', 'drive wheels', 'color', 'airbags'
]

data = data[selected_columns]
data = data.dropna()
#data['mileage'].fillna(value=data['mileage'].mean(), inplace=True)

numerical_features = ['Mileage', 'Engine volume', 'Cylinders', 'Airbags', 'Prod. year']
categorical_features = ['Manufacturer', 'Model', 'Category', 'Leather interior', 'Fuel type', 'Gear box type', 'Drive wheels', 'Color']
data = pd.get_dummies(data, columns=categorical_features)  # ['manufacturer', 'model', 'gear.box.type', 'drive.wheels', 'color']

scaler = StandardScaler()
data[numerical_features] = scaler.fit_transform(data[numerical_features])


y = data['price']
x = data.drop('price',axis=1)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)