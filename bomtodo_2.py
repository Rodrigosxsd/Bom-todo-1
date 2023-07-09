from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

navegador = webdriver.Chrome()
navegador.get('https://sv8.supervisao.com/Laudo/Listar')
wait = WebDriverWait(navegador, 10)   

def login():

    login_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="Email"]'))).send_keys('RODRIGO SOUZA')
    password_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="Password"]'))).send_keys('86170000589')
    enter_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="submit"]'))).click()

def arquivo():
    dropdown = navegador.find_element('xpath', '//*[@id="TipoIdentificacao"]')
    dd = Select(dropdown)
    dd.select_by_value('2')
    placa_element = navegador.find_element('xpath', '//*[@id="NumDocVeiculo"]')

    while True:
        list = []
        placa_element.send_keys(input('Placa a ser pesquisada: \n'))
        list.append(placa_element)
        filtrar_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="btn btn-primary margin-top-30"]'))).click() 
        placa_element.clear()  
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[title="Imprimir"]'))).click()
            
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[title="Baixar Fotos"]'))).click()
           
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="Foto Extra"]'))).click()
            
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i[class="fa fa-file-powerpoint-o"]'))).click()

            handles = navegador.window_handles
            navegador.switch_to.window(handles[1])

        except NoSuchElementException:
            placa_element.clear()  
            return   



#def arquivos():




if __name__ == '__main__':
    login()   
    arquivo()