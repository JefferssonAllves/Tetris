import pygame
from random import randint
from time import sleep

#IDs DAS FIGURAS:
#1 FIGURA 2x2
#2 FIGURA 'L'      
# 40

TAMANHO_JANELA = (640, 880)
TAMANHO_BLOCO= 20

TELA = pygame.display.set_mode(TAMANHO_JANELA)

GRID = 40
MULTIPLICADOR_GRID = 22

class Figura():
    def __init__(self, tipo_figura):
        self.tipo_figura = tipo_figura
        self.posicoes_blocos = self.escolher_figura()
        self.lista_blocos = []


    def escolher_figura(self):
        posicoes_blocos = []
        match randint(0, 3):
            case 0:
                posicoes_blocos = [(1, 1), (2, 1), (1, 2), (1, 3)]
            case 1:
                posicoes_blocos = [(1, 1), (1, 2), (2, 1), (2, 2)]
            case 2:
                posicoes_blocos = [(1, 2), (2, 2), (3, 2), (2, 1)]
            case 3:
                posicoes_blocos = [(1, 1)]
        return posicoes_blocos

    def posicao(self, posx, posy):
        self.posx = posx
        self.posy = posy 
    
    def desenhar(self):
        for i in self.posicoes_blocos:
            self.lista_blocos.append(pygame.draw.rect(TELA, (255, 0, 0), ((i[0] + self.posx) * MULTIPLICADOR_GRID, (i[1] + self.posy)  * MULTIPLICADOR_GRID, TAMANHO_BLOCO, TAMANHO_BLOCO)))

    def __str__(self) -> str:
        return self.posicoes_blocos

def desenhar_piso():
    chao = []
    for i in range(0, 29):
        chao.append(pygame.draw.rect(TELA, (0, 200, 0), (i * MULTIPLICADOR_GRID, 860, TAMANHO_BLOCO, TAMANHO_BLOCO)))
    return chao 

def main():
    figura = None
    posx, posy = randint(0, 29), 0
    figuras_desenhadas = []

    clock = pygame.time.Clock()
    while True:
        clock.tick(20)
        TELA.fill((0, 0, 0))
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()

        if figura is None:
            figura = Figura("quadrado")


        if pygame.key.get_pressed()[pygame.K_d]:
            posx += 1
        elif pygame.key.get_pressed()[pygame.K_a]:
            posx -= 1

        figura.posicao(posx, posy)
        figura.desenhar()
        posy += 1

        #teste = pygame.draw.rect(TELA, (0, 0, 0), (0, 0, 0, 0))
        #teste.colliderect()
        for i in figura.lista_blocos:
            if i.y >= 820:
                figuras_desenhadas.append(figura)
                posx, posy = randint(0, 29), 0
                figura = None
            

        figuras_desenhadas = [x for x in figuras_desenhadas if x is not None]
        
        for fig in figuras_desenhadas:
            fig.desenhar()

        desenhar_piso()
        pygame.display.update()        


if __name__ == "__main__":
    main()