# É preciso descobrir a posição dos campos login, senha e fazer login
import time
import pyautogui

time.sleep(5)
num = pyautogui.position()
print(num)