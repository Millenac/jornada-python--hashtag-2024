import time
import pyautogui
import pandas as pd

pyautogui.PAUSE = 0.5 #Estou atribuindo meio segundo de pause entre cada comando

# Abrindo o navegador
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

# Abrindo o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(2) #Estou colocando 2 segundo de espera devido a velocidade da internet em carregar o site

# Clicando na celula de login e colocando o email
pyautogui.click(x=747, y=354)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("email_de_teste@hotmail.com")

#Colocando a senha no site e fazendo login
pyautogui.press("tab")
pyautogui.write("senha_teste123")
pyautogui.press("enter")

time.sleep(2)

# Lendo o arquivo produtos
caminho_arquivo = r"c:\Users\milll\OneDrive\Documentos\Jornada Python\Dia 1 - Automatização de Tarefas\produtos.csv"

try:
    dados = pd.read_csv(caminho_arquivo)
except FileNotFoundError:
    print(f"O arquivo '{caminho_arquivo}' não foi encontrado.")


#Loop para cadastrar cada dados do arquivo produtos.csv
for i in dados.index:
    pyautogui.click(x=761, y=243)

    codigo = str(dados.loc[i, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = str(dados.loc[i, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = str(dados.loc[i, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(dados.loc[i, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(dados.loc[i, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(dados.loc[i, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(dados.loc[i, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    #Depois de cadastramos um produto precisamos voltar para o topo da pagina
    #Então usamos o comando scroll (Usamos valor positivo para subir o scroll)
    pyautogui.scroll(200)
    pyautogui.click(x=761, y=243)
