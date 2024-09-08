"""
    Objetivo do Código: 
       Comparar duas imagens e destacar suas diferenças: 
       1 A função find_difference converte as duas imagens para escala de cinza, 
         calcula a similaridade estrutural entre elas, e gera uma imagem que destaca as diferenças normalizadas entre as duas imagens
       2 Igualar o histograma de uma imagem com outra: 
         - A função transfer_histogram ajusta os níveis de intensidade de uma imagem para que seu histograma (distribuição de tons e cores) corresponda ao histograma de uma segunda imagem, criando uma correspondência visual entre as duas 
"""

import numpy as np
# Importa a biblioteca NumPy, usada para operações matemáticas e manipulação de arrays.

from skimage.color import rgb2gray
# Importa a função rgb2gray da biblioteca skimage para converter imagens RGB em escala de cinza.

from skimage.exposure import match_histograms
# Importa a função match_histograms da biblioteca skimage, usada para igualar o histograma de duas imagens.

from skimage.metrics import structural_similarity
# Importa a função structural_similarity da biblioteca skimage, usada para calcular a similaridade estrutural entre duas imagens.

def find_difference(image1, image2):
    # Define a função find_difference, que encontra as diferenças estruturais entre duas imagens.

    assert image1.shape == image2.shape, "Specify 2 images with the same shape."
    # Verifica se as duas imagens têm o mesmo formato; caso contrário, gera um erro.

    gray_image1 = rgb2gray(image1)
    # Converte a primeira imagem de RGB para escala de cinza.

    gray_image2 = rgb2gray(image2)
    # Converte a segunda imagem de RGB para escala de cinza.

    (score, difference_image) = structural_similarity(gray_image1, gray_image2, full=True)
    # Calcula a similaridade estrutural entre as duas imagens em escala de cinza. A função retorna a pontuação de similaridade e a imagem de diferença.

    print("Similarity of the images:", score)
    # Exibe no console a pontuação de similaridade entre as imagens.

    normalized_difference_image = (difference_image-np.min(difference_image))/(np.max(difference_image)-np.min(difference_image))
    # Normaliza a imagem de diferença para que os valores fiquem entre 0 e 1, facilitando a visualização.

    return normalized_difference_image
    # Retorna a imagem de diferença normalizada.

def transfer_histogram(image1, image2):
    # Define a função transfer_histogram, que ajusta o histograma de uma imagem para combinar com outra.

    matched_image = match_histograms(image1, image2,channel_axis=-1)
    # Ajusta o histograma da primeira imagem (image1) para que corresponda ao da segunda (image2). O parâmetro 'multichannel=True' indica que a imagem tem múltiplos canais (por exemplo, RGB).

    return matched_image
    # Retorna a imagem ajustada com o histograma transferido.
