
grade= Grade()
grade.criar_regioes(9)

class Grade ():
    def __init__(self) -> None:
        
        self.cabeca #onde ficam armazenado as regiões
        self.erros
        
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
            
        cabeca = self.cabeca
        
        x = 0
        y = 0
        p = 0
        
        for c in range (0, n):
            cabeca.criar_blocos(p,x,y)
            #da esquerda para a direita
            

class Regiao (p,x,y):
    def __init__(self) -> None:
        
        self.cabeca #onde ficam armazenado os blocos
        self.posicao = p #a posicao dele na grade
        self.proximo 
        self.x = x #valor usado em calculo para melhorar desempenho na hora de verificar as regiões / blocos
        self.y = y #valor usado em calculo para melhorar desempenho na hora de verificar as regiões / blocos
    
    def criar_blocos(self,p,x,y):
        
        self.cabeca = Bloco(p,x,y) # 0
        cabeca = self.cabeca
        
        for c in range(1,9):#1 ao 8
            cabeca.proximo = Bloco(p,x,y)
            
            
    
    
class Bloco (p,x,y):
    def __init__(self) -> None:
        
        self.posicao = p #a posicao dele na grade
        self.proximo
        self.x = x #valor usado em calculo para melhorar desempenho na hora de verificar as regiões / blocos
        self.y = y #valor usado em calculo para melhorar desempenho na hora de verificar as regiões / blocos