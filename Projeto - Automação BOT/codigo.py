import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5

#Passo a passo do projeto
   #print(pyautogui.KEYBOARD_KEYS) - Mostra os nomes das teclas do teclado
#1. Abrir o sistema da empresa


pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('enter')
pyautogui.hotkey('win', 'up')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(3)

#2. Fazer loguin
pyautogui.click(x=681, y=405)
pyautogui.write('gambit_1557@hotmail.com')
pyautogui.press('tab')
pyautogui.write('kamus157')
pyautogui.press('tab')
pyautogui.press('enter')

#3 Abrir/Importar a base de dados de produtos para cadastrar
tabela = pd.read_csv('produtos.csv')

for linha in tabela.index:
    #tabela.index = linhas da tabela, tabela.colluns (colunas)

    pyautogui.click(x=594, y=289)
    pyautogui.write(str(tabela.loc[linha, 'codigo']))

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))

    pyautogui.press('tab')
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan' :
        pyautogui.write(obs)

    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(50000)
    




