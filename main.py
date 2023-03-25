from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time
import telebot

# Substitua o token do bot pelo token fornecido pela nova plataforma de API
TOKEN = '6148275362:AAEGcIuyW5B-ZbiD_32oU7OfRaWhJ8qgQxc'
chat_id = '-1001754951616'

# Inicializa o driver do Chrome
chrome_options = Options()
chrome_options.add_argument('--headless')  # modo headless
driver = webdriver.Chrome(options=chrome_options)

# Abre o site
driver.get('https://tipminer.com/estrelabet/aviator')

# Define uma variável para armazenar o último resultado do Crash
bot = telebot.TeleBot(TOKEN)

crash_value = []

while True:
    

    # Espera até que o elemento que contém a classe 'crash-single' seja carregado na página
    crash_elements = driver.find_elements(By.XPATH, '//div[@id="crash"]//div[contains(@class, "number")]')
    element = [float(e.text.strip("X")) if e.text.strip("X").replace('.', '').replace(',', '').isdigit() else 0 for e in crash_elements[:10]]

    if element != crash_value:
        # Verifica se a lista atual é diferente da lista anterior antes de atualizar a variável crash_value
        if crash_value:
            # Se a lista anterior existir, verifica se a lista atual é igual à lista anterior
            if element == crash_value:
                # Se a lista atual for igual à lista anterior, aguarda por 1 segundo e reinicia o loop
                time.sleep(2)
                continue
        crash_value = element
    else:
        # Se os valores não mudaram, aguarda por 1 segundo e reinicia o loop
        time.sleep(2)
        continue

        # Imprime o valor do crash
    print(crash_value)
##############################################################################################################################################
    # Verifica se o último resultado foi menor ou igual a 1.0 e o resultado atual é maior que 1.0
    if crash_value[0] <= 1.09 and crash_value[1] <= 1.80:

        # Envia mensagem via Telegram
        message = f'🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹\n ♻️ FAZER ATÉ 5 RECUPERAÇÕES\n🎯Possivel 🌹🌹🌹 nas proximas 5 velas\n🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹\n BETPIX365 link:https://m.betpix365.com/ptb/authentication/signup?referenceCode=byGHYiOSDBb1 \nESPORTE DA SORTElink:https://www.esportesdasorte.com/ptb/bet/main'
        bot.send_message(chat_id, message)
        time.sleep(5)

    if crash_value[0] >= 2.50 and crash_value[1] <= 1.30 and crash_value[2] >= 2.50 and crash_value[3] <= 1.30:

        # Envia mensagem via Telegram
        message = f'⏰ ENTRAR APÓS O CRASH {crash_value[0]}\n💨 SAIR NO 5x\n ♻️ FAZER ATÉ 5 RECUPERAÇÕES\nBETPIX365 link:https://m.betpix365.com/ptb/authentication/signup?referenceCode=byGHYiOSDBb1 \nESPORTE DA SORTElink:https://www.esportesdasorte.com/ptb/bet/main'
        time.sleep(5)

    if crash_value[0] >= 4.0 and crash_value[1] <= 4.0 and crash_value[2] <= 1.60 and crash_value[3] >= 4.0 and crash_value[4] <= 1.5:
    
        # Envia mensagem via Telegram
        message = f'⏰ ENTRAR APÓS O CRASH {crash_value[0]}\n💨 SAIR NO 5x\n ♻️ FAZER ATÉ 5 RECUPERAÇÕES\nBETPIX365 link:https://m.betpix365.com/ptb/authentication/signup?referenceCode=byGHYiOSDBb1 \nESPORTE DA SORTElink:https://www.esportesdasorte.com/ptb/bet/main'
        bot.send_message(chat_id, message)
        time.sleep(5)
