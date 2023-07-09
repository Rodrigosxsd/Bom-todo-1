from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


navegador = webdriver.Chrome()
navegador.get('https://sv8.supervisao.com/Laudo/Listar')

def login():
    sleep(2)
    login_element = navegador.find_element('css selector', 'input[name="Email"]').send_keys('RODRIGO SOUZA')
    sleep(2)
    password_element = navegador.find_element('css selector', 'input[name="Password"]').send_keys('86170000589')
    sleep(2)
    enter_element = navegador.find_element('css selector', 'input[type="submit"]').click()
    
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
            sleep(5)
            navegador.find_element('css selector', 'a[title="Imprimir"]').click()
            sleep(5)
            navegador.find_element('css selector', 'a[title="Baixar Fotos"]').click()
            sleep(5)
            navegador.find_element('css selector', '[title="Foto Extra"]').click()
            sleep(5)
            navegador.find_element('css selector', 'i[class="fa fa-file-powerpoint-o"]').click() 
            sleep(2)
            handles = navegador.window_handles
            navegador.switch_to.window(handles[1])

        except NoSuchElementException:
            return               

if __name__ == '__main__':
    login()   
    arquivos()