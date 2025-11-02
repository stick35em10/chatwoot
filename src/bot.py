from flask import Flask, request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import joblib
import pandas as pd

app = Flask(__name__)

def send_whatsapp_message(phone_number, message):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(), options=options)
    driver.get(f"https://web.whatsapp.com/send?phone={phone_number}&text={message}")
    print("Acessando WhatsApp Web...")
    time.sleep(10) # Wait for page to load

    try:
        send_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="send"]'))
        )
        send_button.click()
        print("Mensagem enviada com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")
    finally:
        driver.quit()

def predict_sales():
    model = joblib.load('models/modelo_vendas.pkl')
    new_data = pd.DataFrame({
        'product_category_name_english': ['bed_bath_table', 'electronics'],
        'price': [100, 500]
    })
    new_data = pd.get_dummies(new_data)
    for col in model.feature_names_in_:
        if col not in new_data.columns:
            new_data[col] = 0
    new_data = new_data[model.feature_names_in_]
    forecast = model.predict(new_data)
    return forecast

@app.route('/send_forecast', methods=['GET'])
def send_forecast_route():
    phone_number = request.args.get('to')
    if not phone_number:
        return "Erro: Número de telefone não fornecido.", 400
    try:
        forecast = predict_sales()
        message = f"📊 Previsão de vendas: {forecast}"
        send_whatsapp_message(phone_number, message)
        return "Previsão enviada com sucesso!"
    except Exception as e:
        return f"Erro: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)