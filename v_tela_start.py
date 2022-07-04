# recebe o numero de displays pygame.display.get_num_displays()

import pygame 
from pygame.locals import *
from sys import exit

from v_tela_selecao_de_jogo import *

pygame.init() #inicia os modulos importados
pygame.display.set_caption('Jogo de tabuleiro') # titulo da tela

largura = 720
altura = 480

def criar_tela_start(largura, altura):
    
    tela = pygame.display.set_mode((largura, altura), pygame.RESIZABLE)
    
    tela.fill((0, 0, 0)) #preenche a tela de preto
    branco = (255, 255, 255)   
    
    fonte = pygame.font.Font('freesansbold.ttf', 28)
    frase = fonte.render("Start", False, branco)
    
    tela.blit(frase, (largura//2 -28, altura//2 -28))
    pygame.display.flip()
    return tela

def criar_tela_start_loop():
    largura =720
    altura =480
    criar_tela_start(720, 480)#crio a tela entro no loop esperando inputs
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                largura, altura = event.size #pega o novo tamanho de tela
                
                #cria a nova tela
                tela = criar_tela_start(largura, altura)
            
            if event.type == KEYDOWN:
                print('teclado')
                print(event.key)
                
                if event.key == 13:
                    criar_tela_selecao_de_jogo_loop(largura, altura)
                    #inicia o jogo
                    
            if event.type == MOUSEBUTTONDOWN:
                print(event)
                criar_tela_selecao_de_jogo_loop(largura, altura)
                
            if event.type == pygame.QUIT:
                raise SystemExit
