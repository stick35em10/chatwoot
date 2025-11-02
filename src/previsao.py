import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

def treinar_modelo(dados):
    X = pd.get_dummies(dados[['product_category_name_english', 'price']])
    y = dados['review_score']
    modelo = RandomForestRegressor(n_estimators=10, random_state=42)
    modelo.fit(X, y)
    os.makedirs('models', exist_ok=True)
    joblib.dump(modelo, 'models/modelo_vendas.pkl')
    print("Modelo treinado e salvo em models/modelo_vendas.pkl")
    return modelo

if __name__ == "__main__":
    # Carrega dataset de exemplo
    df = pd.read_csv('data/olist_dataset.csv', nrows=1000)
    treinar_modelo(df)
