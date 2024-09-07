""" Objetivo: 
      Ler e salvar imagens utilizando as funções da biblioteca skimage.io. 
      A função read_image permite carregar uma imagem de um arquivo, 
      com a opção de convertê-la para escala de cinza, enquanto a função save_image salva uma imagem em 
      um arquivo no caminho especificado
"""


from skimage.io import imread, imsave
# Importa as funções imread e imsave da biblioteca skimage.io.
# 'imread' é usada para ler uma imagem de um arquivo.
# 'imsave' é usada para salvar uma imagem em um arquivo.

def read_image(path, is_gray=False):
    # Define a função read_image, que lê uma imagem de um caminho especificado.
    # O parâmetro 'is_gray' define se a imagem será carregada em escala de cinza (padrão é False, ou seja, imagem colorida).

    image = imread(path, as_gray=is_gray)
    # Usa a função imread para ler a imagem do caminho especificado.
    # Se 'is_gray' for True, a imagem será convertida para escala de cinza.

    return image
    # Retorna a imagem carregada.

def save_image(image, path):
    # Define a função save_image, que salva uma imagem em um caminho especificado.

    imsave(path, image)
    # Usa a função imsave para salvar a imagem no caminho fornecido.

