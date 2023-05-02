import pandas_datareader as pdr
import numpy as np
from sklearn.linear_model import LinearRegression

# Définir la plage de dates pour les données historiques
start_date = '2000-01-01'
end_date = '2023-04-25'

# Récupérer les données historiques de l'indice S&P 500 (SPX) à partir de Yahoo Finance
spx_data = pdr.get_data_yahoo('^GSPC', start=start_date, end=end_date)

# Séparer les données en ensembles d'entraînement et de test
split_date = '2022-01-01'
train_data = spx_data[spx_data.index < split_date]
test_data = spx_data[spx_data.index >= split_date]

# Créer un modèle de régression linéaire et entraîner sur les données d'entraînement
model = LinearRegression()
X_train = np.array(train_data.index).reshape(-1, 1)
y_train = train_data['Adj Close']
model.fit(X_train, y_train)

# Faire des prévisions sur les données de test
X_test = np.array(test_data.index).reshape(-1, 1)
y_test = test_data['Adj Close']
y_pred = model.predict(X_test)

# Tracer le graphique des données historiques et des prévisions
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(12,6))
ax.plot(train_data.index, train_data['Adj Close'], label='Données d\'entraînement')
ax.plot(test_data.index, test_data['Adj Close'], label='Données de test')
ax.plot(test_data.index, y_pred, label='Prévisions')
ax.set_title('Prévisions de l\'indice S&P 500')
ax.set_xlabel('Date')
ax.set_ylabel('Prix de clôture ajusté')
ax.legend()
plt.show()