
class Grade:
    def __init__(self, n) -> None:
        self.cabeca = None #onde ficam armazenado as regiões
        self.erros = 0
        #self.maximo = n*n
        #self.preenchido = 0
        self.blocos_em_branco = n*n
        
    def criar_regioes(self,n):
        x = 0
        y = 0
        p = 0
        self.cabeca = Regiao(p,x,y) #0
        cabeca = self.cabeca
        
        for c in range(1 , n): #1 ao 8 se n = 9
            x += 1
            y += 1
            p += 1
            cabeca.proximo = Regiao(p,x//3 ,y//3)
            cabeca= cabeca.proximo
            
        cabeca = self.cabeca
        
    def contar_regioes(self):
        
        cabeca = self.cabeca
        
        x=0
        while cabeca:#
            x+=1
            print(x-1)
            #print(f'{x}')
            cabeca= cabeca.proximo
            
        print(f'{x} regiões')


class Regiao:
    def __init__(self,p,x,y) -> None:
        
        self.cabeca = None #onde ficam armazenado os blocos
        self.posicao = p #a posicao dele na grade
        self.proximo = None
        self.x = x #valor usado em calculo para melhorar desempenho na hora de verificar as regiões / blocos
        self.y = y #valor usado em calculo para melhorar desempenho na hora de verificar as regiões / blocos
    
    def criar_blocos(self,p,x,y):
        
        self.cabeca = Bloco(p,x,y) # 0
        cabeca = self.cabeca
        
        for c in range(1,9):#1 ao 8
            cabeca.proximo = Bloco(p,x,y)
        
        '''
        x = 0
        y = 0
        p = 0
        
        for c in range (0, n):
            cabeca.criar_blocos(p,x,y)
            #da esquerda para a direita
            
        '''
            
            
    
    
class Bloco:
    def __init__(self,p,x,y) -> None:
        
        self.posicao = p #a posicao dele na grade
        self.proximo
        self.x = x #valor usado em calculo para melhorar desempenho na hora de verificar as regiões / blocos
        self.y = y #valor usado em calculo para melhorar desempenho na hora de verificar as regiões / blocos
        

grade= Grade(9)
grade.criar_regioes(9)#criei
grade.contar_regioes()#verifiquei
#criar blocos nas regioes
#verificar
#preencher os blocos
#plotar
#registrar o clique (localizar atravez do clique qual bloco vai ser alterado)
#input do valor atravez do teclado ( range 1,9)
#verificar se pode adicionar
#verificar se esta certo #se sim ,adiciona e plota na tela #se nao , não adiciona
#verificar se ganhou # preenchido = maximo da grade

