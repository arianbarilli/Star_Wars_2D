import pygame
import random
pygame.init()
largura = 1520
altura = 770
tamanho = (largura, altura)
pygameDisplay = pygame.display
pygameDisplay.set_caption("Star Wars")
gameDisplay = pygame.display.set_mode(tamanho)
gameIcon = pygame.image.load("assets/R2D2.ico")
pygameDisplay.set_icon(gameIcon)

fundo = pygame.image.load("assets/fundo.jpg")
fundoDeath = pygame.image.load("assets/navedestroyed.jpg")

explosaoSound = pygame.mixer.Sound("assets/explode.ogg")
explosaoSound.set_volume(0.5)
yellow = (255, 255, 0)
green = (0, 255, 0)
clock = pygame.time.Clock()
eventos = pygame.event

def dead(pontos):
    gameDisplay.blit(fundoDeath, (0, 0))
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(explosaoSound)
    fonte = pygame.font.Font("freesansbold.ttf", 50)
    fonteContinue = pygame.font.Font("freesansbold.ttf", 30)
    texto = fonte.render("Você Perdeu com "+str(pontos) +
                         " pontos", True, yellow)
    textoContinue = fonteContinue.render(
        "Aperte ENTER para continuar...", True, green)
    gameDisplay.blit(textoContinue, (200, 700))
    gameDisplay.blit(texto, (200, 600))
    pygameDisplay.update()

def jogo():
    pontos = 0
    posicaoXLaser = 0
    posicaoYLaser = random.randrange(0, altura-120)
    direcao = True
    speed = 2
    posicaoXNave = 650
    posicaoYNave = 300
    movimentoXNave = 0
    movimentoYNave = 0

    laser = pygame.image.load("assets/laser.png")
    nave = pygame.image.load("assets/nave.png")
    laser = pygame.transform.flip(laser, True, False)
    pygame.mixer.music.load("assets/sound.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1)

    laserSound = pygame.mixer.Sound("assets/laserSound.ogg")
    laserSound.set_volume(1)
    pygame.mixer.Sound.play(laserSound)

    larguraNave = 193
    alturaNave = 150
    larguraMissel = 220
    alturaMissel = 120
    dificuldade = 63
    jogando = True

    while True:
        for event in eventos.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    jogo()
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

        if jogando == True:
            posicaoXNave = posicaoXNave + movimentoXNave
            posicaoYNave = posicaoYNave + movimentoYNave
            if posicaoXNave < 0:
                posicaoXNave = 0
            elif posicaoXNave >= largura - larguraNave:
                posicaoXNave = largura - larguraNave

            if posicaoYNave < 0:
                posicaoYNave = 0
            elif posicaoYNave >= altura - alturaNave:
                posicaoYNave = altura - alturaNave


            gameDisplay.blit(fundo, (0, 0))

            if direcao == True:
                if posicaoXLaser < largura -0:
                    posicaoXLaser = posicaoXLaser + speed
                else:
                    pygame.mixer.Sound.play(laserSound)
                    direcao = False
                    posicaoYLaser = random.randrange(0, altura -120)
                    speed = speed + 1
                    laser = pygame.transform.flip(laser, True, False)
                    pontos = pontos + 1
            else:
                if posicaoXLaser >= -150:
                    posicaoXLaser = posicaoXLaser - speed
                else:
                    pygame.mixer.Sound.play(laserSound)
                    direcao = True
                    posicaoYLaser = random.randrange(0, altura -120)
                    speed = speed + 1
                    laser = pygame.transform.flip(laser, True, False)
                    pontos = pontos + 1

            gameDisplay.blit(laser, (posicaoXLaser, posicaoYLaser))
            gameDisplay.blit(nave, (posicaoXNave, posicaoYNave))
            fonte = pygame.font.Font("freesansbold.ttf", 20)
            placar = fonte.render("Pontos: "+str(pontos), True, green)
            gameDisplay.blit(placar, (10, 10))

            pixelsYNave = list(
                range(posicaoYNave, posicaoYNave + alturaNave+1))
            pixelsXNave = list(
                range(posicaoXNave, posicaoXNave + larguraNave+1))

            pixelsYMissel = list(range(posicaoYLaser, posicaoYLaser+alturaMissel+1))
            pixelsXMissel = list(range(posicaoXLaser, posicaoXLaser+larguraMissel+1))

            if len(list(set(pixelsYMissel) & set(pixelsYNave))) > dificuldade:
                if len(list(set(pixelsXMissel) & set(pixelsXNave))) > dificuldade:
                    jogando = False
                    dead(pontos)

        pygameDisplay.update()
        clock.tick(60)

jogo()
