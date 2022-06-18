import pygame
import random
pygame.init()
largura = 1520
altura = 770
tamanho = (largura, altura)
pygameDisplay = pygame.display
pygameDisplay.set_caption("Star Wars")
gameDisplay = pygame.display.set_mode(tamanho)
fundo = pygame.image.load("assets/fundo.png")
laser = pygame.image.load("assets/laser.png")
nave = pygame.image.load("assets/nave.png")
laser = pygame.transform.flip(laser, True, False)
eventos = pygame.event
clock = pygame.time.Clock()
white = (255, 255, 255)
pontos = 0
posicaoXLaser = 0
posicaoYLaser = random.randrange(0, altura-120)
direcao = True
speed = 2
posicaoXNave = 650
posicaoYNave = 300
movimentoXNave = 0
movimentoYNave = 0

pygame.mixer.music.load("assets/sound.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1)

while True:

    for event in eventos.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                movimentoXNave = -25
            elif event.key == pygame.K_d:
                movimentoXNave = 25
            elif event.key == pygame.K_w:
                movimentoYNave = -25
            elif event.key == pygame.K_s:
                movimentoYNave = 25
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s:
                movimentoXNave = 0
                movimentoYNave = 0

    posicaoXNave = posicaoXNave + movimentoXNave
    posicaoYNave = posicaoYNave + movimentoYNave

    gameDisplay.blit(fundo, (0, 0))

    if direcao == True:
        if posicaoXLaser < largura -0:
            posicaoXLaser = posicaoXLaser + speed
        else:
            direcao = False
            posicaoYLaser = random.randrange(0, altura -120)
            speed = speed + 1
            laser = pygame.transform.flip(laser, True, False)
            pontos = pontos + 1
    else:
        if posicaoXLaser >= -150:
            posicaoXLaser = posicaoXLaser - speed
        else:
            direcao = True
            posicaoYLaser = random.randrange(0, altura -120)
            speed = speed + 1
            laser = pygame.transform.flip(laser, True, False)
            pontos = pontos + 1

    gameDisplay.blit(laser, (posicaoXLaser, posicaoYLaser))
    gameDisplay.blit(nave, (posicaoXNave, posicaoYNave))
    fonte = pygame.font.Font("freesansbold.ttf", 20)
    placar = fonte.render("Pontos: "+str(pontos), True, white)
    gameDisplay.blit(placar, (10, 10))
    pygameDisplay.update()
    clock.tick(60)
