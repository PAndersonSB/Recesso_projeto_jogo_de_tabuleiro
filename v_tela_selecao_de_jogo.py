from re import A
import pygame 
from pygame.locals import *
from sys import exit

pygame.init() #inicia os modulos importados
pygame.display.set_caption('Jogo de tabuleiro') # titulo da tela

def criar_tela_selecao_de_jogo(largura, altura):
    
    tela = pygame.display.set_mode((largura, altura), pygame.RESIZABLE)
    
    tela.fill((0, 0, 0)) #preenche a tela de preto
    branco = (255, 255, 255)   
    
    fonte = pygame.font.Font('freesansbold.ttf', 60)
    
    
    #desenha os circulos com numeros
    #tela , cor , localizacao , tamanho
    desl_al = altura// 100
    desl_la = largura// 100
    
    # ART (x, y, width, height)
    c= 0
    multi = 9     #m 8 10 12 14 16 18
    while c < 18: #c 0 1  2  3  4  5  
        if c == 6 or  c == 12:
            multi += 18                                                         
            
        pygame.draw.rect(tela, (218,165,32), [desl_la*multi, desl_al*0 ,   desl_la*1, desl_al *130], 0)
        multi += 2
        c+=1
    
    #########
    
    pygame.draw.circle(tela, (0,0,0), [desl_la*15 , desl_al*18 ], 60, 0)
    pygame.draw.circle(tela, (0,0,0), [desl_la*45 , desl_al*54 ], 60, 0)
    pygame.draw.circle(tela, (0,0,0), [desl_la*75 , desl_al*90 ], 60, 0)
    
    #ciruclo 1
    pygame.draw.circle(tela, (218,165,32), [desl_la*15 , desl_al*18 ], 55, 3)
    pygame.draw.circle(tela, (218,165,32), [desl_la*15 , desl_al*18 ], 50, 0)
    
    #frase = fonte.render("1", False, branco)
    #tela.blit(frase, ( (largura//100)*7 ,(altura//100)*11 ))
    
    #ciruclo 2
    pygame.draw.circle(tela, (218,165,32), [ desl_la*45 , desl_al*54], 55, 3)
    pygame.draw.circle(tela, (218,165,32), [desl_la*45 , desl_al*54], 50, 0)
    
    #ciruclo 3 75
    pygame.draw.circle(tela, (218,165,32), [ desl_la*75 , desl_al*90], 55, 3)
    pygame.draw.circle(tela, (218,165,32), [desl_la*75 , desl_al*90], 50, 0)
    
    #escreve os nomes nomes
    fonte = pygame.font.Font('freesansbold.ttf', 40)
    frase = fonte.render("sudoku", False, branco)
    tela.blit(frase, (desl_la*20 , desl_al*14))
    
    frase = fonte.render("Inshi no Heya", False, branco)
    tela.blit(frase, ( desl_la*50 , desl_al*50) )
    
    frase = fonte.render("Hitori", False, branco)
    tela.blit(frase, ( desl_la*80 , desl_al*86) )
    
    pygame.display.flip()
    
    return tela

def criar_tela_selecao_de_jogo_loop(largura, altura):
    
    criar_tela_selecao_de_jogo(largura, altura)#crio a tela entro no loop esperando inputs
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                largura, altura = event.size #pega o novo tamanho de tela
                
                #cria a nova tela
                tela = criar_tela_selecao_de_jogo(largura, altura)
                    
            if event.type == MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos() #posicao
    
                if x > (largura//100)*11 and y > (altura//100)*12 and x < (largura//100)*15 and y < (altura//100)*23 :#1366 705
                    print('jogo 1')
                
                if x > (largura//100)*42 and y > (altura//100)*49 and x < (largura//100)*47 and y < (altura//100)*58 :#1366 705
                    print('jogo 2')
                
                if x > (largura//100)*72 and y > (altura//100)*84 and x < (largura//100)*75 and y < (altura//100)*94 :#1366 705
                    print('jogo 3')
            
            if event.type == pygame.QUIT:
                raise SystemExit