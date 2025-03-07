from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep
import pandas as pd
import img2pdf
from PIL import Image
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import io

def full_page_screenshot(driver, file_path):
    # Obter a largura e altura da página inteira
    total_width = navegador.execute_script("return document.documentElement.scrollWidth")
    total_height = navegador.execute_script("return document.documentElement.scrollHeight")
    
    # Configurar o tamanho da janela do navegador para a largura e altura totais
    navegador.set_window_size(total_width, total_height)
    
    # Tirar uma captura de tela da página inteira
    screenshot = navegador.get_screenshot_as_png()
    
    # Abrir a captura de tela como imagem
    image = Image.open(io.BytesIO(screenshot))
    
    # Salvar a imagem em formato JPEG
    image = image.convert("RGB")
    image.save(file_path, 'JPEG')
    
def convert_to_pdf(image_path, pdf_path):
    
    # Configuração para converter foto em PDF.
    image = Image.open(image_path)
    image.save(pdf_path, "PDF", resolution=100.0)    

# Dados para acessar o site.
webdriver_manager = GeckoDriverManager()
navegador = webdriver.Firefox()
navegador.get('https://sv8.supervisao.com/Laudo/Listar')
wait = WebDriverWait(navegador, 30)

def login():
    # Elemenos para realizar o login.
    login_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="Email"]'))).send_keys('LUCIMARA.BRUNELLE')
    password_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="Password"]'))).send_keys('01674248580')
    enter_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="submit"]'))).click()
def arquivo():
    # Planilha para inserir as placas para realizar o download dos arquivos.
    planilha = pd.read_excel(r'E:\\bom todo 2\placas_supervisao.xlsx')

    for i, placa in enumerate(planilha["placa"]):

        # Seleciona o tipo de pesquisa Chassi ou Placa.
        sleep(5)
        dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'select[id="TipoIdentificacao"]')))
        dd = Select(dropdown)
        sleep(7)
        dd.select_by_visible_text('Chassi')
        # Elementos para pesquisar e limpar a busca dos arquivos.
        placa_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input[id="NumDocVeiculo"]'))).send_keys(placa)
        filtrar_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="btn btn-primary margin-top-30"]'))).click()
        try:
            #Elementos dos arquivos que precisam ser baixados.
            sleep(5)
            imprimir = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[title="Imprimir"]'))).click()
            wait.until(EC.invisibility_of_element_located((By.ID, 'modalCarregando')))
            baixar_fotos = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[title="Baixar Fotos"] i[class="fa fa-download"]'))).click()
            fotos_extras = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[title="Foto Extra"] i[class="os-icon os-icon-paperclip"]'))).click()
            sleep(7)
            imprimir_pesquisa = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[title="Imprimir Pesquisa"]'))).click()
            
            # Função para ir para a página da Pesquisa Veícular.
            janelas = navegador.window_handles
            navegador.switch_to.window(janelas[1])
        
            # Tirar print da página da Pesquisa Veícular. 
            sleep(5)
            screenshot_path = f'{placa}.JPEG'
            full_page_screenshot(navegador, screenshot_path)
            
            # Converter o print em PDF.
            sleep(5)
            pdf_path = f'{placa}.pdf'
            convert_to_pdf(screenshot_path, pdf_path)

            sleep(5)
            # Retorna para o página das pesquisas do laudo.
            navegador.switch_to.window(janelas[0])
            navegador.refresh()
        except:
            # Caso nenhum arquivo esteja disponivel, ele continue com a busca e não quebre a automação. 
            sleep(5)
            limpar_dados = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[id="limparFiltro"]'))).click()
            navegador.refresh()
            continue   

if __name__ == '__main__':  
    login()   
    arquivo()
