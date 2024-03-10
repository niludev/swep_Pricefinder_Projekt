from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from joblib import dump
import pandas as pd

# Load data
data = pd.read_csv('datasets/car_price_prediction.csv')

# Definieren Sie numerische und kategorische Spalten
numerical_cols = ['Mileage', 'Engine volume', 'Cylinders', 'Airbags', 'Prod. year']
categorical_cols = ['Manufacturer', 'Model', 'Category', 'Leather interior', 'Fuel type', 'Gear box type', 'Drive wheels', 'Color']

# Entfernen von 'km' und Umwandeln von 'Mileage' in float
data['Mileage'] = data['Mileage'].str.replace(' km', '').astype(float)

# Entfernen von 'Turbo' und anderen nicht numerischen Zeichen aus 'Engine volume'
data['Engine volume'] = data['Engine volume'].str.extract('(\d+\.\d+|\d+)')[0].astype(float)

# One-Hot-Encode kategorische Variablen
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ]
)

# Fitting the preprocessor
preprocessor.fit(data)

# Speichern des Preprocessors
dump(preprocessor, 'preprocessor.joblib')
