from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

# Configura as opções do Chrome para anexar à sessão existente
chrome_options = Options()
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_options.add_argument("--remote-debugging-port=9222")

# Inicia o driver do Chrome usando as opções configuradas
# driver = webdriver.Chrome(executable_path='C:/Program Files (x86)/TrendingApps/WaSenderSetUp/chromedriver', options=chrome_options)
service = Service('C:/chromedriver/chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

# Neste ponto, o driver está anexado à sessão existente do Chrome
# Encontra a tabela pelo ID
tabela = driver.find_element(By.ID, "example3")

# Encontra todas as linhas dentro do corpo da tabela
linhas = tabela.find_elements(By.XPATH, ".//tbody/tr")

# Inicializa listas para armazenar os dados
nomes = []
telefones = []

# Itera sobre as linhas para extrair o nome e o telefone
for linha in linhas:
    # Encontra a coluna dos Dados de Cadastro (3ª coluna)
    dados_cadastro = linha.find_element(By.XPATH, "./td[3]/b").text
    # Encontra a coluna dos Dados de Contato (4ª coluna)
    dados_contato = (linha.find_element(By.XPATH, "./td[4]").text.split()[0].replace('(', '').replace(')', '') + linha.find_element(By.XPATH, "./td[4]").text.split()[1].replace('-',''))
    print(dados_contato)
    
    # Armazena os dados extraídos
    nomes.append(dados_cadastro)
    telefones.append(dados_contato)
# antiga planilha
oldData = pd.read_excel('dados_extraidos.xlsx')
for old in oldData.values:
    nomes.append(old[0])
    telefones.append(old[1])
    # print(old[0])

print(telefones)
# Cria um DataFrame com os dados extraídos
df = pd.DataFrame({
    'Nome': nomes,
    'Telefone': telefones
})

# Salva os dados em uma planilha Excel
df.to_excel('dados_extraidos.xlsx', index=False)

# Fecha o navegador
driver.quit()