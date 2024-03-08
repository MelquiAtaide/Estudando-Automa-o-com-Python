import pyautogui as py
import time
import pandas

py.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
tabela = pandas.read_csv("produtos.csv")

py.press("win")
py.write("edge")
py.press("enter")

py.write(link)
py.press("enter")

time.sleep(2)

py.click(x=558, y=353)
py.write("python@gmail.com")
py.press("tab")
py.write("123456789")
py.press("enter")
time.sleep(2)


for i in tabela.index:
    py.click(x=580, y=238)

    # Código do produto
    py.write(tabela.loc[i, "codigo"])
    py.press("tab")

    # Marca
    py.write(tabela.loc[i, "marca"])
    py.press("tab")

    # Tipo
    py.write(tabela.loc[i, "tipo"])
    py.press("tab")

    # categoria
    py.write(str(tabela.loc[i, "categoria"]))
    py.press("tab")

    # Preço
    py.write(str(tabela.loc[i, "preco_unitario"]))
    py.press("tab")

    # Custo
    py.write(str(tabela.loc[i, "custo"]))
    py.press("tab")

    # Obs
    obs = tabela.loc[i, "obs"]
    if not pandas.isna(obs):
        py.write(obs)
    py.press("tab")

    #Enter
    py.press("enter")
    py.scroll(5000)
