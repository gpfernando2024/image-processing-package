"""Objetivo: redimensionar uma imagem com base em uma proporção especificada, 
             mantendo a qualidade da imagem redimensionada através do uso de anti-aliasing
    Resultado esperado:
        - O resultado será uma imagem redimensionada de acordo com a proporção fornecida.
        - Se a proporção for 0.5, a imagem será redimensionada para 50% do tamanho original 
          (metade da altura e metade da largura).
        - O retorno será a imagem redimensionada, com dimensões ajustadas de forma proporcional.
    Exemplo de Entrada e Saída:
        - Suponha que você tenha uma imagem com dimensões 1000x800 pixels
        - Se chamar resize_image(image, 0.5), a função retornará uma nova imagem com dimensões
          500x400 pixels (50% do tamanho original).
"""
from skimage.transform import resize
# Importa a função resize do módulo skimage.transform, que é usada para redimensionar imagens.

def resize_image(image, proportion):
    # Define a função resize_image, que redimensiona uma imagem com base em uma proporção.

    assert 0 <= proportion <= 1, "Specify a valid proportion between 0 and 1."
    # Verifica se a proporção está entre 0 e 1; se não estiver, gera um erro.

    height = round(image.shape[0] * proportion)
    # Calcula a nova altura da imagem, multiplicando a altura original pela proporção fornecida.

    width = round(image.shape[1] * proportion)
    # Calcula a nova largura da imagem, multiplicando a largura original pela proporção fornecida.

    image_resized = resize(image, (height, width), anti_aliasing=True)
    # Redimensiona a imagem usando a nova altura e largura calculadas. O parâmetro anti_aliasing=True suaviza os possíveis artefatos gerados durante o redimensionamento.

    return image_resized
    # Retorna a imagem redimensionada.
