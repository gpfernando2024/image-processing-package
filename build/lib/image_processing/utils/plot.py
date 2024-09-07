"""
   Objetivo do Código:
     O código tem como objetivo plotar imagens e seus histogramas de cores (RGB) usando a 
     biblioteca matplotlib.pyplot. Ele contém três funções principais:
        * plot_image: exibe uma única imagem em escala de cinza.
        * plot_result: exibe várias imagens lado a lado, com títulos para cada uma.
        * plot_histogram: exibe histogramas de cada canal de cor (vermelho, verde e azul) de uma imagem
"""

import matplotlib.pyplot as plt
# Importa a biblioteca matplotlib.pyplot para criar gráficos e exibir imagens.

def plot_image(image):
    # Define a função plot_image, que exibe uma única imagem.

    plt.figure(figsize=(12, 4))
    # Cria uma figura com um tamanho específico (12x4 polegadas).

    plt.imshow(image, cmap='gray')
    # Exibe a imagem passada como argumento. O parâmetro 'cmap=gray' define a exibição em escala de cinza.

    plt.axis('off')
    # Remove os eixos para que não sejam exibidos.

    plt.show()
    # Mostra a imagem na tela.

def plot_result(*args):
    # Define a função plot_result, que exibe várias imagens lado a lado.

    number_images = len(args)
    # Calcula o número de imagens passadas como argumento.

    fig, axis = plt.subplots(nrows=1, ncols=number_images, figsize=(12, 4))
    # Cria uma figura com várias subplots (número de colunas igual ao número de imagens).

    names_lst = ['Image {}'.format(i) for i in range(1, number_images)]
    # Gera uma lista de nomes (Image 1, Image 2, etc.) para cada imagem, exceto a última.

    names_lst.append('Result')
    # Adiciona o título 'Result' à última imagem.

    for ax, name, image in zip(axis, names_lst, args):
        # Para cada eixo, nome e imagem, define o título e plota a imagem.

        ax.set_title(name)
        # Define o título de cada subplot.

        ax.imshow(image, cmap='gray')
        # Exibe a imagem em escala de cinza.

        ax.axis('off')
        # Remove os eixos de cada imagem.

    fig.tight_layout()
    # Ajusta o layout da figura para que os subplots não se sobreponham.

    plt.show()
    # Exibe a figura com todas as imagens.

def plot_histogram(image):
    # Define a função plot_histogram, que exibe os histogramas dos canais de cor (RGB) de uma imagem.

    fig, axis = plt.subplots(nrows=1, ncols=3, figsize=(12, 4), sharex=True, sharey=True)
    # Cria uma figura com 3 subplots (um para cada canal de cor) e compartilha os eixos x e y.

    color_lst = ['red', 'green', 'blue']
    # Lista de cores representando os canais de cor (vermelho, verde e azul).

    for index, (ax, color) in enumerate(zip(axis, color_lst)):
        # Para cada eixo, cor e índice, exibe o histograma do canal de cor correspondente.

        ax.set_title('{} histogram'.format(color.title()))
        # Define o título de cada subplot com o nome da cor correspondente.

        ax.hist(image[:, :, index].ravel(), bins=256, color=color, alpha=0.8)
        # Exibe o histograma para o canal de cor específico (vermelho, verde ou azul), com 256 bins.

    fig.tight_layout()
    # Ajusta o layout da figura para que os subplots não se sobreponham.

    plt.show()
    # Exibe a figura com os histogramas.
