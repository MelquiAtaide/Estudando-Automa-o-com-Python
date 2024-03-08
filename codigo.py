import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
tabela = pandas.read_csv("produtos.csv")

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")

time.sleep(2)

pyautogui.click(x=558, y=353)
pyautogui.write("python@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456789")
pyautogui.press("enter")
time.sleep(2)

pyautogui.click(x=580, y=238)
