import pygame
from pygame.locals import *
from sys import exit
from random import randint
 
pygame.init()

pygame.mixer.music.set_volume(0.5)
musica_de_fundo = pygame.mixer.music.load("musicas\All Too Well (10 Minute Version) (Taylor's Version) (From The Vault) (Lyric Video) (128 kbps).mp3")
pygame.mixer.music.play(5)

barulho_colisão = pygame.mixer.Sound('musicas\smw_coin.wav')
barulho_colisão.set_volume(0.5)

#Proporção
largura = 600
altura = 520

#Inicio da cobra
x_cobra = int(largura / 2)
y_cobra = int(altura / 2)

#Velocidade do movimento
velocidade = 7
x_controle = velocidade
y_controle = 0

#Inicio da maça
x_maça = randint(27, 560)
y_maça = randint(68, 477)

#Design
pontos = 0
fonte = pygame.font.SysFont('arial', 20, bold=True, italic=True) 
# fonte2 = pygame.font.SysFont('arial', 9, bold=True, italic=True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake game Taylor's Version")

img = pygame.image.load('imagens/fundovermelho.jpeg')
img_maça = pygame.image.load('imagens/loirinha.png') 

relogio = pygame.time.Clock()

#lista fora do loop para não ficar sendo deletada
lista_cobra = [] 

comprimento_inicial = 5
morreu = False

#função para aumentar cobra
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        #XeY = [x, y]
        #XeY[0] = x
        #XeY[1] = y
        pygame.draw.rect(tela, (48, 10, 10), (XeY[0], XeY[1], 22, 22))

def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeça, x_maça, y_maça, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(largura/2)
    y_cobra = int(altura/2)
    lista_cobra = []
    lista_cabeça = []
    x_maça = randint(27, 560)
    y_maça = randint(60, 477)
    # x_maça = randint(int(laurgura/2))
    # y_maça = randint(int(altura/2))
    morreu = False

while True:
    relogio.tick(30)
    tela.blit(img, (0, 0))
    # tela.fill((255,255,255))

    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255,255,255))
    # taylor = fonte2.render("Snake game Taylor's Version", True, (0,0,0))


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
 
#Controle
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_RIGHT:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_UP:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_DOWN:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle

    cobra = pygame.draw.rect(tela, (12, 61, 31), (x_cobra, y_cobra, 20, 20))
    maça = tela.blit(img_maça, (x_maça, y_maça))
    line1 = pygame.draw.line(tela, (0, 0, 0), (23,68), (577,68), 3)
    line2 = pygame.draw.line(tela, (0, 0, 0), (23,68), (23,497), 3)
    line3 = pygame.draw.line(tela, (0, 0, 0), (577,68), (577,497), 3)
    line4 = pygame.draw.line(tela, (0, 0, 0), (23, 497), (577,497), 3)

#Lista dentro do loop
    lista_cabeça = []
    lista_cabeça.append(x_cobra)
    lista_cabeça.append(y_cobra)
    
    lista_cobra.append(lista_cabeça)

#Colisões
    if cobra.colliderect(maça):
        x_maça = randint(24, 563)
        y_maça = randint(65, 480)
        pontos += 1
        barulho_colisão.play()
        comprimento_inicial = comprimento_inicial + 3

    if lista_cobra.count(lista_cabeça) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game Over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (255, 255, 255))
        ret_texto = texto_formatado.get_rect()
        pygame.mixer.music.stop()

        morreu =  True
        while morreu:
            tela.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.mixer.music.play()
            pygame.display.update()

    if cobra.colliderect(line1):
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game Over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (255, 255, 255))
        ret_texto = texto_formatado.get_rect()
        pygame.mixer.music.stop()
        
        morreu =  True
        while morreu:
            tela.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.mixer.music.play()
            pygame.display.update()
    
    if cobra.colliderect(line2):
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game Over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (255, 255, 255))
        ret_texto = texto_formatado.get_rect()
        pygame.mixer.music.stop()

        morreu =  True
        while morreu:
            tela.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.mixer.music.play()
            pygame.display.update()

    if cobra.colliderect(line3):
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game Over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (255, 255, 255))
        ret_texto = texto_formatado.get_rect()
        pygame.mixer.music.stop()

        morreu =  True
        while morreu:
            tela.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.mixer.music.play()
            pygame.display.update()
    
    if cobra.colliderect(line4):
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game Over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (255, 255, 255))
        ret_texto = texto_formatado.get_rect()
        pygame.mixer.music.stop()

        morreu =  True
        while morreu:
            tela.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.mixer.music.play()
            pygame.display.update()

    # if x_cobra > largura:
    #     x_cobra = 0
    # if x_cobra < 0:
    #     x_cobra = largura
    # if y_cobra < 0:
    #     y_cobra = altura
    # if y_cobra > altura:
    #     y_cobra = 0

#Impedir que a cobra aumente infinitamente sem comer a maça 
    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

#chamando a função dentro do loop 
    aumenta_cobra(lista_cobra)

#Localização do texto de pontos 
    tela.blit(texto_formatado, (40, 30))
    # tela.blit(taylor, (445,505))

    pygame.display.update()