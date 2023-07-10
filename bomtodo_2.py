from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import pandas as pd

def full_page_screenshot(driver, file_path):
    # Obter a largura e altura da página inteira
    total_width = navegador.execute_script("return document.documentElement.scrollWidth")
    total_height = navegador.execute_script("return document.documentElement.scrollHeight")
    
    # Configurar o tamanho da janela do navegador para a largura e altura totais
    navegador.set_window_size(total_width, total_height)
    
    # Tirar uma captura de tela da página inteira
    navegador.save_screenshot(file_path)

navegador = webdriver.Firefox()
navegador.get('https://sv8.supervisao.com/Laudo/Listar')
wait = WebDriverWait(navegador, 10)

def login():
    login_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="Email"]'))).send_keys('x')
    password_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="Password"]'))).send_keys('x')
    enter_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="submit"]'))).click()

def arquivo():

    planilha = pd.read_excel(r'E:\\bom todo 2\placas_supervisao.xlsx')

    for i, placa in enumerate(planilha["placa"]):
        dropdown = navegador.find_element('xpath', '//*[@id="TipoIdentificacao"]')
        dd = Select(dropdown)
        sleep(2)
        dd.select_by_value('2')
        
        placa_element = navegador.find_element('css selector','input[id="NumDocVeiculo"]').send_keys(placa)
        sleep(5)
        #placa_element.clear()
        filtrar_element = navegador.find_element('css selector', 'button[class="btn btn-primary margin-top-30"]').click()
        try:
            sleep(5)
            imprimir = navegador.find_element('css selector', 'a[title="Imprimir"]').click()
            sleep(5)
            baixar_fotos = navegador.find_element('css selector', 'a[title="Baixar Fotos"] i[class="fa fa-download"]').click()
            sleep(5)
            fotos_extas = navegador.find_element('css selector', 'a[title="Foto Extra"] i[class="os-icon os-icon-paperclip"]').click()
            sleep(5)
            imprimir_pesquisa = navegador.find_element('css selector', 'a[title="Imprimir Pesquisa"]').click()
            sleep(5)
            limpar_dados =  navegador.find_element('css selector', 'button[id="limparFiltro"]').click()

            janelas = navegador.window_handles
            navegador.switch_to.window(janelas[1])
            full_page_screenshot(navegador, f'screenshot{placa}.png')
            
            sleep(3)
            navegador.switch_to.window(janelas[0])
        except NoSuchElementException:
            return   

if __name__ == '__main__':  
    login()   
    arquivo()
