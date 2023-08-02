from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.firefox import GeckoDriverManager
import pandas as pd
from PIL import Image
import io
import os
from time import sleep
import requests

def full_page_screenshot(driver, file_path):
    total_width = driver.execute_script("return document.documentElement.scrollWidth")
    total_height = driver.execute_script("return document.documentElement.scrollHeight")
    driver.set_window_size(total_width, total_height)
    screenshot = driver.get_screenshot_as_png()
    image = Image.open(io.BytesIO(screenshot))
    image = image.convert("RGB")
    
    # Certificar-se de que a pasta "screenshots" existe
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    image.save(file_path, 'JPEG')

def salvar_screenshot_como_pdf(caminho_imagem, caminho_pdf):
    image = Image.open(caminho_imagem)
    image.save(caminho_pdf, "PDF", resolution=100.0)

def baixar_pdf(url, file_path):
    response = requests.get(url)
    with open(file_path, 'wb') as f:
        f.write(response.content)

def fazer_login():
    webdriver_manager = GeckoDriverManager()
    navegador = webdriver.Firefox()
    navegador.get('https://sv8.supervisao.com/Laudo/Listar')
    wait = WebDriverWait(navegador, 30)
    login_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="Email"]'))).send_keys('LUCIMARA.BRUNELLE')
    password_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="Password"]'))).send_keys('01674248580')
    enter_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="submit"]'))).click()
    return navegador, wait

def processar_linha(navegador, wait, linha):
    placa = linha["placa"]
    dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'select[id="TipoIdentificacao"]')))
    wait.until(EC.invisibility_of_element_located((By.ID, 'modalCarregando')))
    dd = Select(dropdown)
    dd.select_by_visible_text('Chassi')
    placa_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="NumDocVeiculo"]'))).send_keys(placa)
    filtrar_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="btn btn-primary margin-top-30"]'))).click()
    try:
        imprimir = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[title="Imprimir"]')))
        navegador.execute_script("arguments[0].click();", imprimir)  # Clicar usando JavaScript
        wait.until(EC.invisibility_of_element_located((By.ID, 'modalCarregando')))
        
        baixar_fotos = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[title="Baixar Fotos"] i[class="fa fa-download"]')))
        navegador.execute_script("arguments[0].click();", baixar_fotos)  # Clicar usando JavaScript
        wait.until(EC.invisibility_of_element_located((By.ID, 'modalCarregando')))
        
        fotos_extras = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[title="Foto Extra"] i[class="os-icon os-icon-paperclip"]')))
        navegador.execute_script("arguments[0].click();", fotos_extras)  # Clicar usando JavaScript
        wait.until(EC.invisibility_of_element_located((By.ID, 'modalCarregando')))
        
        # Clicar no botão "Imprimir Pesquisa" usando JavaScript
        imprimir_pesquisa = navegador.find_element(By.CSS_SELECTOR, 'i[class="fa fa-file-powerpoint-o"]')
        navegador.execute_script("arguments[0].click();", imprimir_pesquisa)
        
        # Mudar o foco para a nova janela
        for handle in navegador.window_handles:
            if handle != navegador.current_window_handle:
                navegador.switch_to.window(handle)
                break
        
        sleep(5)
        if "pdf" in navegador.current_url.lower():
            pdf_path = f'pdfs/{placa}.pdf'
            baixar_pdf(navegador.current_url, pdf_path)
        else:
            screenshot_path = f'screenshots/{placa}.JPEG'
            full_page_screenshot(navegador, screenshot_path)
            pdf_path = f'pdfs/{placa}.pdf'
            salvar_screenshot_como_pdf(screenshot_path, pdf_path)
        navegador.close()
        
        # Mudar o foco de volta para a janela principal
        navegador.switch_to.window(navegador.window_handles[0])
        navegador.refresh()
    except:
        # Ao clicar no botão "Limpar Filtro", use JavaScript para evitar o erro de TimeoutException
        limpar_dados = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[id="limparFiltro"]')))
        navegador.execute_script("arguments[0].click();", limpar_dados)  # Clicar usando JavaScript
        navegador.refresh()
        pass

if __name__ == '__main__':
    # Cria a pasta "pdfs" se não existir
    os.makedirs("pdfs", exist_ok=True)
    planilha = pd.read_excel(r'E:\\bom todo 2\placas_supervisao.xlsx')
    navegador, wait = fazer_login()
    for _, linha in planilha.iterrows():
        processar_linha(navegador, wait, linha)
    navegador.quit()
