# Cadastrar produtos num sistem de forma automatica pegando dados de um arquivo .csv

import pyautogui
import pandas
import time

pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=456, y=510)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=488, y=411)
pyautogui.write("luizeduardobiscolam@gmail.com")
pyautogui.press("tab")
pyautogui.write("1234")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(2)

tabela = pandas.read_csv("produtos.csv")

print(tabela)

linha = 0

for linha in tabela.index:

    pyautogui.click(x=560, y=293)

    codigo =tabela.loc[linha, "codigo"]
    pyautogui.write (str(codigo))
    pyautogui.press ("tab")

    marca =tabela.loc[linha, "marca"]
    pyautogui.write (str(marca))
    pyautogui.press ("tab")

    tipo =tabela.loc[linha, "tipo"]
    pyautogui.write (str(tipo))
    pyautogui.press ("tab")

    categoria =tabela.loc[linha, "categoria"]
    pyautogui.write (str(categoria))
    pyautogui.press ("tab")

    preco =tabela.loc[linha, "preco_unitario"]
    pyautogui.write (str(preco))
    pyautogui.press ("tab")

    custo =tabela.loc[linha, "custo"]
    pyautogui.write (str(custo))
    pyautogui.press ("tab")

    if not pandas.isna(tabela.loc[linha, "obs"]):
        #if not tabela.loc[linha, "obs"] = "NaN":
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)