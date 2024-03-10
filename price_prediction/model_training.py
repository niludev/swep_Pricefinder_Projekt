from joblib import load
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from joblib import dump, load
from preprocessing import data

# Load preprocessor
preprocessor = load('preprocessor.joblib')

# Train-test-split
X = data.drop('Price', axis=1)
y = data['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Transform data
X_train_transformed = preprocessor.transform(X_train)
X_test_transformed = preprocessor.transform(X_test)

# Train the model
model = LinearRegression()
model.fit(X_train_transformed, y_train)

# Evaluate model
predictions = model.predict(X_test_transformed)
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse}")



# # exams
# print('Scaler mean:', scaler.mean_)
# print('Scaler scale:', scaler.scale_)
#
# print('Train set shape:', X_train.shape)
# print('Test set shape:', X_test.shape)
#
# train_categorical = set(X_train.columns) - set(numerical_features)
# test_categorical = set(X_test.columns) - set(numerical_features)
# difference = train_categorical.symmetric_difference(test_categorical)
# print('Categorical feature difference:', difference)


# Calculate the prediction errors
errors = y_test - predictions

# Examine the statistics of the errors
print(errors.describe())

# Find examples with large errors
large_errors = errors.abs().nlargest(5)
print(large_errors)

# Examine the corresponding data points
print(X_test.loc[large_errors.index])




# Save the trained model
dump(model, 'trained_model.joblib')
