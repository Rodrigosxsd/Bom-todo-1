from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.command import Command
 
navegador = webdriver.Firefox()

navegador.get('https://smart.dekra.com.br/PortalParceiro/Login')

login_path = '//*[@id="Login"]'
password_path = '//*[@id="Senha"]'
enter_path = '//*[@id="btSubmit"]/div[2]'
chassi_path = '//*[@id="Chassi"]'
pesquisar_path = '//*[@id="FuncPesquisa"]'
pdf_path = 'div[class="ui-grid-canvas"] div[ng-click]'
block_path = 'div[class = "block-ui-overlay"]'

def login():
    sleep(2)
    login_element = navegador.find_element('xpath', login_path)
    sleep(2)
    password_element = navegador.find_element('xpath', password_path)
    sleep(2)
    enter_element = navegador.find_element('xpath', enter_path)

    login_element.send_keys('pdekra.fandrade')
    password_element.send_keys('Napist@2022')
    enter_element.click()

def chassi():
    sleep(5)
    chassi_element = navegador.find_element('xpath', chassi_path)
    sleep(5)
    pesquisar_element = navegador.find_element('xpath', pesquisar_path)

    while True:
        list = []
        chassi_element.send_keys(input('Chassi a ser pesquisado: \n'))
        list.append(chassi_element)
        sleep(20)
        pesquisar_element.click()
        sleep(20) 
        chassi_element.clear()    
        try:
         sleep(5)   
         navegador.find_element('css selector', pdf_path).click()   
        except NoSuchElementException:
            continue
        
if __name__ == '__main__':
    login()
    chassi()
