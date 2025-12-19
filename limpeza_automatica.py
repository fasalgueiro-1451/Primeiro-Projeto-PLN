import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Baixa os recursos necessários (só precisa rodar uma vez)
nltk.download('punkt')
nltk.download('stopwords')

def limpar_texto(texto):
    # 1. Tokenização e conversão para minúsculas
    tokens = word_tokenize(texto.lower())
    
    # 2. Carregar stop words em português
    stops = set(stopwords.words('portuguese'))
    
    # 3. Filtrar palavras (remove stop words e pontuação)
    limpo = [w for w in tokens if w not in stops and w.isalnum()]
    
    return " ".join(limpo)

# Caminhos das pastas
pasta_entrada = 'entrada'
pasta_saida = 'saida'

# O "Coração" da Automação: Loop pelos arquivos
print("Iniciando limpeza...")

for arquivo in os.listdir(pasta_entrada):
    if arquivo.endswith(".txt"):
        # Ler o arquivo original
        with open(os.path.join(pasta_entrada, arquivo), 'r', encoding='utf-8') as f:
            conteúdo = f.read()
        
        # Processar o texto
        texto_processado = limpar_texto(conteúdo)
        
        # Salvar o novo arquivo na pasta de saída
        nome_saida = f"limpo_{arquivo}"
        with open(os.path.join(pasta_saida, nome_saida), 'w', encoding='utf-8') as f:
            f.write(texto_processado)
            
        print(f"Sucesso: {arquivo} processado!")

print("Processo concluído! Verifique a pasta 'saida'.")