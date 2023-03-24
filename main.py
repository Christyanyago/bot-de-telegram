from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time
import os
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

while True:
    try:
        # Limpa a tela do terminal
        os.system('cls' if os.name == 'nt' else 'clear')

        # Espera até que o elemento que contém a classe 'crash-single' seja carregado na página
        crash_elements = driver.find_elements(By.XPATH, '//div[@id="crash"]//div[contains(@class, "number")]')
        crash_value = [float(e.text.strip("X")) if e.text.strip("X").replace('.', '').replace(',', '').isdigit() else 0 for e in crash_elements[:20]]


        # Imprime o valor do crash
        print(crash_value)
##############################################################################################################################################
        # Verifica se o último resultado foi menor ou igual a 1.0 e o resultado atual é maior que 1.0
        if crash_value[0] <= 1.09 and crash_value[1] <= 1.80:

            # Envia mensagem via Telegram
            message = f'⏰ ENTRAR APÓS O CRASH {crash_value[0]}\n💨 SAIR NO 10x\n ♻️ FAZER ATÉ 5 RECUPERAÇÕES\n🎯Possivel pink nas proximas 5 velas\n BETPIX365 link:https://Seulink.digital/z8NiTEEp\nESTRELABET link:https://Seulink.digital/hQrAEJ!'
            bot.send_message(chat_id, message)
            time.sleep(5)
    
        if crash_value[0] >= 2.50 and crash_value[1] <= 1.30 and crash_value[2] >= 2.50 and crash_value[3] <= 1.30:

            # Envia mensagem via Telegram
            message = f'⏰ ENTRAR APÓS O CRASH {crash_value[0]}\n💨 SAIR NO 5x\n ♻️ FAZER ATÉ 5 RECUPERAÇÕES\n🎯Possivel pink nas proximas 5 velas\n BETPIX365 link:https://Seulink.digital/z8NiTEEp\nESTRELABET link:https://Seulink.digital/hQrAEJ!'
            bot.send_message(chat_id, message)
            time.sleep(5)

        if crash_value[0] >= 4.0 and crash_value[1] <= 4.0 and crash_value[2] <= 1.60 and crash_value[3] >= 4.0 and crash_value[4] <= 1.5:
        
            # Envia mensagem via Telegram
            message = f'⏰ ENTRAR APÓS O CRASH {crash_value[0]}\n💨 SAIR NO 5x\n ♻️ FAZER ATÉ 5 RECUPERAÇÕES\n🎯Possivel pink nas proximas 5 velas\n BETPIX365 link:https://Seulink.digital/z8NiTEEp\nESTRELABET link:https://Seulink.digital/hQrAEJ!'
            bot.send_message(chat_id, message)
            time.sleep(5)

        # Espera 5 segundos para que a página carregue completamente
        driver.implicitly_wait(5)

        # Extrai os valores de crash das últimas 5 rodadas
        crash_elements = driver.find_elements(By.CLASS_NAME, 'crash-single')[1:10]
        crash_values = [element.text.strip() for element in crash_elements]

        # Imprime os valores de crash das últimas  5 rodadas
        for i, value in enumerate(crash_values, start=1):
            print(f'{value}', end=' ')

        print('') # Imprime uma quebra de linha para separar as iterações

    except TimeoutException:
        # Trata a exceção TimeoutException e continua o loop
        print('Elemento crash-single não encontrado')

    # Espera 10 segundos antes de fazer uma nova iteração
    time.sleep(10)

# Fecha o navegador
driver.quit()