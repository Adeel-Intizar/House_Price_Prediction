
"""
Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FyMIY_pO7NJFa0rBzfmv9dTy5QrOBryj
"""

import numpy as np
import pandas as pd

df = pd.read_csv('housing.csv')
df.head()

"""# **Scikit-learn Models**"""

from sklearn.ensemble import GradientBoostingRegressor

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import mean_squared_error, r2_score

from sklearn.pipeline import Pipeline
from joblib import dump

"""# **Using All Features**"""

X = df.drop('MEDV', axis=1)
y = df['MEDV']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = GradientBoostingRegressor()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(f'Accuracy: {model.score(X_test, y_test)*100:.3}%')
print(f'RMSE: {np.sqrt(mean_squared_error(y_test, y_pred))}')

steps = [('Gradient Boosting Regressor', GradientBoostingRegressor(n_estimators=500, max_depth=6))]
model = Pipeline(steps)
model.fit(X_train, y_train)
print('Accuracy: {:.0f}%'.format(model.score(X_test, y_test) * 100))

dump(model, 'sklearn_model.pkl')

"""# **Keras Models**"""

from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
from sklearn.metrics import r2_score

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

def model():
  model = Sequential()
  model.add(Dense(256, activation='relu', kernel_initializer='he_normal', input_dim=13))
  model.add(Dropout(0.2))
  model.add(Dense(128, activation='relu', kernel_initializer='he_normal'))
  model.add(Dropout(0.3))
  model.add(Dense(16, activation='relu', kernel_initializer='he_normal'))
  model.add(Dense(1))
  
  model.compile(loss='mse', optimizer='adam')
  
  return model

model = model()
model.fit(X_train, y_train, shuffle=True, epochs=1000, verbose=0)
print('RMSE : {:.2f}'.format(np.sqrt(model.evaluate(X_test, y_test))))

y_pred = model.predict(X_test)
print(f'Accuracy: {r2_score(y_test, y_pred)*100:.2f}%')

