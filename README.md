# 🚀 Projeto de Limpeza Automatizada de Texto (PLN)

Este repositório contém meu primeiro projeto prático de **Processamento de Linguagem Natural (PLN)**. O script foi desenvolvido para automatizar a etapa de pré-processamento de dados textuais, essencial em projetos de Inteligência Artificial (AI) e Machine Learning (Aprendizado de Máquina).

Este trabalho marca a conclusão dos meus estudos iniciais na área de PNL, mas especificamente no curso livre de Introdução ao Processamento de Linguagem Natural pela Escola Nacional de Administração Pública (ENAP), onde obtive como Nota Final: 9,25 na Enap! 🎓.

## 📝 Descrição do Projeto
O script utiliza a biblioteca **NLTK (Natural Language Toolkit)** para ler múltiplos arquivos de texto brutos, remover ruídos linguísticos e salvar os resultados estruturados. A automação foi pensada para lidar com grandes volumes de documentos de forma sequencial.

## 🛠️ Conceitos de PLN Aplicados
* **Tokenização:** Divisão do texto em unidades mínimas (tokens) através do modelo 'punk tab'.
* **Normalização:** Conversão de todo o texto para letras minúsculas.
* **Remoção de Stop Words:** Filtragem de palavras funcionais (como "o", "de", "que", "em") que não agregam valor semântico à análise de dados.
* **Limpeza de Caracteres:** Remoção de pontuações e símbolos não alfanuméricos.

## 📊 Exemplo de Processamento
| Entrada (Original) | Saída (Processado) |
| :--- | :--- |
| "O Processamento de Linguagem Natural ajuda o computador a entender os humanos." | "processamento linguagem natural ajuda computador entender humanos" |

## 📂 Estrutura de Pastas
* '\entrada': Coloque aqui seus arquivos '.txt' originais.
* '\saida': Pasta onde o script salvará automaticamente os arquivos limpos.
* 'limpeza_automatica.py': Script principal em Python.

## ⚙️ Como Executar o Projeto
1. Certifique-se de ter o **Python** instalado.
2. Instale a biblioteca necessária via terminal (CMD):
   ```bash
   pip install nltk
       
Execute o script: 
python limpeza_automatica.py

Autora: Fabiola Nunes Salgueiro
Parte do Portfólio do Curso de Introdução ao Processamento de Linguagem Natural do ENAP/DF, com carga horária de 25 horas, iniciado em 08/12/2025 a 19/12/2025.
Conteúdo Programático:
Módulo 1: Introdução ao PLN;
Módulo 2: Preparação de Dados para PLN;
Módulo 3: Aplicações para PLN;
Módulo 4: Aplicações em Python para PLN;
Módulo 5: Aplicações em R para PLN.
