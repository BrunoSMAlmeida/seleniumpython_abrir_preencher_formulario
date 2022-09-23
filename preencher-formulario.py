from selenium import webdriver

# Instalação do driver para abrir o navegador de modo automatizado.
# O código pode ser o usado sempre, em qualquer automatização do Chrome.

navegador = webdriver.Chrome(executable_path=r"C:\Users\Objectedge\Desktop\Sellenium - Python\chromedriver.exe")

# Passo 1: Acessar uma página especifica automatizada.
# Criamos uma variável pro nosso código ficar um pouco mais limpo, organizado.
navegador.get("https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_8AMNaVt0z_M")

# Passo 2: Após acessarmos a página, preenchemos os campos disponíveis usando find_element.
# Podemos usar qualquer método pra localizar o elemento, mas preferencialmente usamos o Xpath pra ser preciso.
# Abaixo, note que preenchemos dois campos: nome e email. Usando send_keys pra passar a informação que queremos preencher.
navegador.find_element('xpath',
                       '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys("Bruno Almeida")
navegador.find_element('xpath',
                       '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input').send_keys("bruno4893@hotmail.com")

navegador.find_element('xpath',
                       '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/button/span/b').click()