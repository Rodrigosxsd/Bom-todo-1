from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


navegador = webdriver.Chrome()
navegador.get('https://sv8.supervisao.com/Laudo/Listar')

def login():
    sleep(2)
    login_element = navegador.find_element('css selector', 'input[name="Email"]')
    sleep(2)
    password_element = navegador.find_element('css selector', 'input[name="Password"]')
    sleep(2)
    enter_element = navegador.find_element('css selector', 'input[type="submit"]')

    login_element.send_keys(input('Digite o login: \n'))
    password_element.send_keys(input('Digite a senha: \n'))
    enter_element.click()
    
def arquivos():
    sleep(3)
    dropdown = navegador.find_element('xpath', '//*[@id="TipoIdentificacao"]')
    sleep(3)
    dd = Select(dropdown)
    sleep(3)
    dd.select_by_value('2')
    sleep(3)
    placa_element = navegador.find_element('xpath', '//*[@id="NumDocVeiculo"]')

    while True:
        list = []
        placa_element.send_keys(input('Placa a ser pesquisada: \n'))
        list.append(placa_element)
        sleep(3)
        filtrar_element = navegador.find_element('css selector', 'button[class="btn btn-primary margin-top-30"]').click()
        sleep(25)
        placa_element.clear()  
        try:
            sleep(10)
            navegador.find_element('css selector', 'tr[class="odd"] a[title="Imprimir"]').click()
            sleep(10)
            navegador.find_element('css selector', 'tr[class="odd"] a[title="Baixar Fotos"]').click()
            sleep(10)
            navegador.find_element('css selector', 'tr[class="even"] a[title="Imprimir"]').click()
            sleep(10)
            navegador.find_element('css selector', 'tr[class="even"] a[title="Baixar Fotos"]').click() 
        except NoSuchElementException:
            return               

if __name__ == '__main__':
    login()   
    arquivos()