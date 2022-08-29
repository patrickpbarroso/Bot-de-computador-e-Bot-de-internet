import pyautogui
import time
import random
from selenium import webdriver

#Selenium


# Para uso do selenium -> no chrome se chama chromedriver e no firefox geckodriver

anaos = ["Thorin", "Balin", "Dwalin", "Fili", "Kili", "Dori", "Ori", "Nori", "Bifor", "Bofur", "Bombur", "Óin", "Glóin"]

decide = int(input("Qual tipo de bot você deseja?"
               "\n(1) Bot de computador"
               "\n(2) Bot de internet"))

if decide == 1:
    decide1 = input("O que você quer que o bot de computador faça?"
                       "\n(a) Fazer login no sistema do Excel"
                       "\n(b) Fazer login no League Of Legends"
                       "\n(c) Escrever em um bloco de notas uma citação do Senhor dos Anéis")

    if decide1 == 'a' or decide1 == 'A':
        pyautogui.PAUSE = 3
        # Abrir o excel
        pyautogui.press("win")
        pyautogui.write("login.xlsx")
        pyautogui.press("backspace")
        pyautogui.press("enter")
        # Preencher o login
        time.sleep(10)
        pyautogui.click(x=427, y=273)
        pyautogui.PAUSE = 2
        pyautogui.write("patrick")
        # Preencher a senha
        pyautogui.click(x=400, y=322)
        pyautogui.write("patrick123")
        # Clicar em login
        pyautogui.click(x=409, y=450)

    if decide1 == 'b' or decide1 == 'B':
        pyautogui.PAUSE = 2
        # Abrir a tela de login do LOL
        pyautogui.press("win")
        pyautogui.write("League of Legends")
        pyautogui.press("backspace")
        pyautogui.press("enter")
        # Preencher o login
        time.sleep(10)
        pyautogui.write("SyndraElfica")
        pyautogui.PAUSE = 2
        # Preencher a senha
        pyautogui.click(x=191, y=289)
        pyautogui.write("dormandor1")
        # Fazer login
        pyautogui.press("enter")

    if decide1 == 'c' or decide1 == 'C':
        pyautogui.PAUSE = 2
        # Abrir o bloco de notas
        pyautogui.press("win")
        pyautogui.write("bloco de notas")
        pyautogui.press("backspace")
        pyautogui.press("enter")
        # Sortear o número de 1 a 5 para selecionar aleatoriamente uma das frases
        num = random.randint(1,13)
        pyautogui.write("O sorteado da comitiva de Thorin Escudo de Carvalho foi " + anaos[num] + "!")

elif decide == 2:
    decide1 = input("O que você quer que o bot de internet faça?"
          "\n(a) Fazer login no hotmail"
          )
    if decide1 == 'a':
        navegador = webdriver.Chrome()
        navegador.get("https://login.live.com/")
        navegador.find_element('xpath', '//*[@id="i0116"]').send_keys("testetestando1@hotmail.com")
        navegador.find_element('xpath', '//*[@id="idSIButton9"]').click()

        time.sleep(1)

        navegador.find_element('xpath', '//*[@id="i0118"]').send_keys("senhasenhazinha1#")
        navegador.find_element('xpath', '//*[@id="idSIButton9"]').click()


