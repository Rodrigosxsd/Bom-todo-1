from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import pandas as pd
import img2pdf
from PIL import Image

def full_page_screenshot(driver, file_path):
    # Obter a largura e altura da página inteira.
    total_width = navegador.execute_script("return document.documentElement.scrollWidth")
    total_height = navegador.execute_script("return document.documentElement.scrollHeight")
    
    # Configurar o tamanho da janela do navegador para a largura e altura totais.
    navegador.set_window_size(total_width, total_height)
    
    # Configuração para realizar o print.
    navegador.save_screenshot(file_path)

def convert_to_pdf(image_path, pdf_path):
    
    # Configuração para converter foto em PDF.
    image = Image.open(image_path)
    image.save(pdf_path, "PDF", resolution=100.0)    

# Dados para acessar o site.
navegador = webdriver.Firefox()
navegador.get('https://sv8.supervisao.com/Laudo/Listar')
wait = WebDriverWait(navegador, 10)

def login():
    # Elemenos para realizar o login.
    login_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="Email"]'))).send_keys('RODRIGO SOUZA')
    password_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="Password"]'))).send_keys('86170000589')
    enter_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="submit"]'))).click()

def arquivo():

    # Planilha para inserir as placas para realizar o download dos arquivos.
    planilha = pd.read_excel(r'E:\\bom todo 2\placas_supervisao.xlsx')

    for i, placa in enumerate(planilha["placa"]):

        # Seleciona o tipo de pesquisa Chassi ou Placa.
        dropdown = navegador.find_element('css selector', 'select[id="TipoIdentificacao"]')
        dd = Select(dropdown)
        sleep(5)
        dd.select_by_visible_text('Chassi')
        sleep(2)
        # Elementos para pesquisar e limpar a busca dos arquivos.
        placa_element = navegador.find_element('css selector','input[id="NumDocVeiculo"]').send_keys(placa)
        sleep(5)
        filtrar_element = navegador.find_element('css selector', 'button[class="btn btn-primary margin-top-30"]').click()
        try:
            #Elementos dos arquivos que precisam ser baixados.
            sleep(7)
            imprimir = navegador.find_element('css selector', 'a[title="Imprimir"]').click()
            sleep(7)
            baixar_fotos = navegador.find_element('css selector', 'a[title="Baixar Fotos"] i[class="fa fa-download"]').click()
            sleep(7)
            fotos_extas = navegador.find_element('css selector', 'a[title="Foto Extra"] i[class="os-icon os-icon-paperclip"]').click()
            sleep(7)
            imprimir_pesquisa = navegador.find_element('css selector', 'a[title="Imprimir Pesquisa"]').click()
            sleep(7)
            limpar_dados =  navegador.find_element('css selector', 'button[id="limparFiltro"]').click()

            # Função para ir para a página da Pesquisa Veícular.
            janelas = navegador.window_handles
            navegador.switch_to.window(janelas[1])
            
            # Tirar print da página da Pesquisa Veícular. 
            screenshot_path = f'{placa}.png'
            full_page_screenshot(navegador, screenshot_path)
            
            # Converter o print em PD.
            pdf_path = f'{placa}.pdf'
            convert_to_pdf(screenshot_path, pdf_path)

            sleep(3)
            # Retorna para o página das pesquisas do laudo.
            navegador.switch_to.window(janelas[0])
            navegador.refresh()
        except NoSuchElementException:
            # Caso nenhum arquivo esteja disponivel, ele continue com a busca e não quebre a automação. 
            limpar_dados  =  navegador.find_element('css selector', 'button[id="limparFiltro"]').click()
            navegador.refresh()
            continue   

if __name__ == '__main__':  
    login()   
    arquivo()
