import pygame 
from pygame.locals import *
from sys import exit

pygame.init() #inicia os modulos importados
pygame.display.set_caption('Jogo de tabuleiro') # titulo da tela

def criar_tela_selecao_de_jogo(largura, altura):
    
    tela = pygame.display.set_mode((largura, altura), pygame.RESIZABLE)
    
    tela.fill((0, 0, 0)) #preenche a tela de preto
    branco = (255, 255, 255)   
    
    fonte = pygame.font.Font('freesansbold.ttf', 40)
    frase = fonte.render("sudoku", False, branco)
    tela.blit(frase, (largura//2 -80, altura//3 - altura //6))
    
    frase = fonte.render("Hitori", False, branco)
    tela.blit(frase, (largura//2 -80, (altura//3)*2 - altura //6))
    
    frase = fonte.render("Inshi no Heya", False, branco)
    tela.blit(frase, (largura//2 -80, (altura//3)*3 - altura //6))
    
    pygame.display.flip()
    
    return tela

def criar_tela_selecao_de_jogo_loop():
    
    criar_tela_selecao_de_jogo(720, 480)#crio a tela entro no loop esperando inputs
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                largura, altura = event.size #pega o novo tamanho de tela
                
                #cria a nova tela
                tela = criar_tela_selecao_de_jogo(largura, altura)
                    
            if event.type == MOUSEBUTTONDOWN:
                print('mouse')
                print(event)
                #pygame.mouse.get_pos() #posicao
                
            if event.type == pygame.QUIT:
                raise SystemExit