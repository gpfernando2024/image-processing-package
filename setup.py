""" 
  Descrição do Código
  O código fornecido é um script setup.py usado para configurar e 
  instalar um pacote Python chamado package_processamento_imagem. 
  Ele utiliza a biblioteca setuptools para definir os parâmetros necessários para a criação e 
  instalação do pacote
"""
from setuptools import setup, find_packages
# Importa as funções `setup` e `find_packages` do pacote `setuptools`.
# `setup` é usado para configurar a instalação do pacote,
# e `find_packages` é utilizado para localizar todos os pacotes dentro do diretório do projeto.

with open("README.md", "r") as f:
    page_descripton = f.read()
# Abre o arquivo `README.md` em modo de leitura e armazena seu conteúdo na variável `page_descripton`.
# O conteúdo do README será usado para fornecer uma descrição mais longa do pacote.

with open("requirements.txt") as f:
    requirements = f.read().splitlines()
# Abre o arquivo `requirements.txt` em modo de leitura e armazena as linhas do arquivo na lista `requirements`.
# Cada linha no `requirements.txt` representa uma dependência do pacote que será instalada.

setup(
    name="package_processamento_imagem",
    # Nome do pacote a ser instalado.
    
    version="0.0.1",
    # Versão do pacote. Usualmente segue o formato major.minor.patch.

    author="Fernando Flavio F Ribeiro",
    # Nome do autor do pacote.
    
    author_email="fernandoffribeirosistemas@gmail.com",
    # Email de contato do autor do pacote.
    
    description="biblioteca de processamento de imagens em Python que oferece uma ampla gama de ferramentas para a análise e manipulação de imagens",
    # Breve descrição do pacote. Descreve o propósito e as funcionalidades principais do pacote.
    
    long_description=page_descripton,
    # Descrição longa do pacote. Utiliza o conteúdo do `README.md` para fornecer uma visão mais detalhada.
    
    long_description_content_type="text/markdown",
    # Tipo do conteúdo da descrição longa. Especifica que o `long_description` está no formato Markdown.
    
    url="https://github.com/gpfernando2024/image-processing-package",
    # URL do repositório do pacote, onde os usuários podem encontrar o código-fonte e mais informações.
    
    packages=find_packages(),
    # Encontra e inclui todos os pacotes dentro do diretório do projeto.
    
    install_requires=requirements,
    # Lista de dependências do pacote que devem ser instaladas. Lê as dependências do arquivo `requirements.txt`.
    
    python_requires='>=3.8'
    # Especifica a versão mínima do Python necessária para executar o pacote.
)
   