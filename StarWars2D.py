import pygame
import random
from funcoes import dormir, limpa_Tela, registro

acionamento = True
arroba = True

registro()

while True:
    limpa_Tela()
    print()
    print("BEM VINDO(A) AO STAR WARS X-WING ATTACK")
    print()
    print("Por Favor, digite Seu Nome e Endereço de E-mail")
    print()
    while acionamento == True:
        conteudo = registro()
        nome = input("Nome: ")
        while arroba == True:
            email = input(str("Email: "))
            if "@" in email and ".com" in email:
                conteudo = conteudo + nome + "\n" + email + "\n" + "\n"
                arroba = False
                acionamento = False
                break
            elif "@" not in email or ".com" not in email:
                print ("Por Favor digite um E-mail Válido")
                arroba = True
        
        arquivo = open("Registro de Login.txt", "w")
        arquivo.write(conteudo)
        arquivo.close()
        print("Registro de login salvo com sucesso!")
        dormir()
        if arroba == False:
            break
    if arroba == False:
        break

pygame.init()
largura = 1530
altura = 780
tamanho = (largura, altura)
pygameDisplay = pygame.display
pygameDisplay.set_caption("Star Wars")
gameDisplay = pygame.display.set_mode(tamanho)
gameIcon = pygame.image.load("assets/Vader.ico")
pygameDisplay.set_icon(gameIcon)

fundo = pygame.image.load("assets/fundo.jpeg")
fundoDeath = pygame.image.load("assets/navedestroyed.jpeg")
fundocomeco = pygame.image.load("assets/starwarsfundo.jpeg")

somlogin = pygame.mixer.Sound("assets/somLogin.mp3")
somlogin.set_volume(1)
trilha = pygame.mixer.Sound("assets/sound.mp3")
trilha.set_volume(1)
ImperialNavy = pygame.mixer.Sound("assets/ImperialNavy.mp3")
ImperialNavy.set_volume(1)
explosaoSound = pygame.mixer.Sound("assets/explode.ogg")
explosaoSound.set_volume(0.5)
yellow = (255, 255, 0)
red = (255, 0, 0)
green = (0, 255, 0)
clock = pygame.time.Clock()
eventos = pygame.event
jogar = False

def game_over(pontos):
    gameDisplay.blit(fundoDeath, (0, 0))
    pygame.mixer.Sound.stop(somlogin)
    pygame.mixer.Sound.stop(trilha)
    pygame.mixer.Sound.play(explosaoSound)
    pygame.mixer.Sound.play(ImperialNavy)
    fonte = pygame.font.Font("freesansbold.ttf", 50)
    fonteContinue = pygame.font.Font("freesansbold.ttf", 30)
    texto = fonte.render("Você Perdeu com "+str(pontos) + " pontos", True, red)
    textoContinue = fonteContinue.render("Aperte ESPAÇO para continuar ou X para Sair", True, green)
    gameDisplay.blit(textoContinue, (120, 700))
    gameDisplay.blit(texto, (120, 600))
    pygameDisplay.update()

def iniciar():
    pygame.mixer.Sound.play(somlogin)
    pygame.mixer.music.set_volume(1)
    gameDisplay.blit(fundocomeco, (0, 0))
    fonteContinue = pygame.font.Font("freesansbold.ttf", 30)
    textoContinue = fonteContinue.render("Aperte ESPAÇO para continuar ou X para Sair", True, green)
    gameDisplay.blit(textoContinue, (110, 700))
    pygameDisplay.update()

def jogo():
    direcaoNave = False
    pontos = 0
    posicaoXLaser = -175
    posicaoXLaser2 = 1530
    posicaoYLaser = random.randrange(0, altura-120)
    posicaoYLaser2 = random.randrange(0, altura-120)
    direcao = True
    speed = 7
    posicaoXNave = 650
    posicaoYNave = 300
    movimentoANave = 0
    movimentoDNave = 0
    movimentoWNave = 0
    movimentoSNave = 0

    laser = pygame.image.load("assets/laser.png")
    nave = pygame.image.load("assets/nave.png")
    laser = pygame.transform.flip(laser, True, False)

    pygame.mixer.Sound.stop(somlogin)
    pygame.mixer.Sound.stop(ImperialNavy)
    pygame.mixer.Sound.play(trilha)
    pygame.mixer.music.set_volume(1)
    laserSound = pygame.mixer.Sound("assets/laserSound.ogg")
    laserSound.set_volume(1)
    pygame.mixer.Sound.play(laserSound)

    larguraNave = 193
    alturaNave = 150
    larguraMissel = 220
    alturaMissel = 120
    dificuldade = 59
    jogando = True
        
    while True:

        for event in eventos.get():
            if event.type == pygame.QUIT:
                limpa_Tela()
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and jogando == False:
                    jogo()
                if event.key == pygame.K_x:
                    limpa_Tela()
                    pygame.quit()
                    quit()
                if event.key == pygame.K_a:
                    movimentoANave = -25
                elif event.key == pygame.K_d:
                    movimentoDNave = 25
                elif event.key == pygame.K_w:
                    movimentoWNave = -25
                elif event.key == pygame.K_s:
                    movimentoSNave = 25
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    movimentoANave = 0
                elif event.key == pygame.K_d:
                    movimentoDNave = 0
                elif event.key == pygame.K_w:
                    movimentoWNave = 0
                elif event.key == pygame.K_s:
                    movimentoSNave = 0
            
            if direcaoNave == True and movimentoANave + movimentoDNave < 0:
                nave = pygame.transform.flip(nave, True, False)
                direcaoNave = False
            elif direcaoNave == False and movimentoDNave + movimentoDNave > 0:
                nave = pygame.transform.flip(nave, True, False)
                direcaoNave = True

        if jogando == True:
            posicaoXNave = posicaoXNave + movimentoANave
            posicaoXNave = posicaoXNave + movimentoDNave
            posicaoYNave = posicaoYNave + movimentoWNave
            posicaoYNave = posicaoYNave + movimentoSNave
            if posicaoXNave < 0:
                posicaoXNave = 0
            elif posicaoXNave >= largura - larguraNave:
                posicaoXNave = largura - larguraNave

            if posicaoYNave < 0:
                posicaoYNave = 0
            elif posicaoYNave >= altura - alturaNave:
                posicaoYNave = altura - alturaNave

            if direcao == True:
                if posicaoXLaser < largura:
                    posicaoXLaser = posicaoXLaser + speed
                else:
                    pygame.mixer.Sound.play(laserSound)
                    direcao = False
                    posicaoYLaser = random.randrange(0, altura -120)
                    if speed <= 25:
                        speed = speed + 1
                    laser = pygame.transform.flip(laser, True, False)
                    pontos = pontos + 1
            else:
                if posicaoXLaser >= -220:
                    posicaoXLaser = posicaoXLaser - speed
                else:
                    pygame.mixer.Sound.play(laserSound)
                    direcao = True
                    posicaoYLaser = random.randrange(0, altura -120)
                    if speed <= 25:
                        speed = speed + 1
                    laser = pygame.transform.flip(laser, True, False)
                    pontos = pontos + 1

            if direcao == True and pontos >= 15:
                if posicaoXLaser2 < largura:
                    posicaoXLaser2 = posicaoXLaser2 + speed
                else:
                    posicaoYLaser2 = random.randrange(0, altura -120)    

            elif direcao == False and pontos >= 15:
                if posicaoXLaser2 >= -220:
                    posicaoXLaser2 = posicaoXLaser2 - speed
                else:
                    posicaoYLaser2 = random.randrange(0, altura -120)
                    
            gameDisplay.blit(fundo, (0, 0))
            gameDisplay.blit(laser, (posicaoXLaser, posicaoYLaser))
            if pontos >= 15:
                gameDisplay.blit(laser, (posicaoXLaser2, posicaoYLaser2))
            gameDisplay.blit(nave, (posicaoXNave, posicaoYNave))
            fonte = pygame.font.Font("freesansbold.ttf", 20)
            placar = fonte.render("Pontos: "+str(pontos), True, yellow)
            gameDisplay.blit(placar, (715, 5))

            pixelsYNave = list(range(posicaoYNave, posicaoYNave + alturaNave+1))
            pixelsXNave = list(range(posicaoXNave, posicaoXNave + larguraNave+1))

            pixelsYMissel = list(range(posicaoYLaser, posicaoYLaser + alturaMissel+1))
            pixelsXMissel = list(range(posicaoXLaser, posicaoXLaser + larguraMissel+1))

            pixelsYMissel2 = list(range(posicaoYLaser2, posicaoYLaser2 + alturaMissel+1))
            pixelsXMissel2 = list(range(posicaoXLaser2, posicaoXLaser2 + larguraMissel+1))
        
            if len(list(set(pixelsYMissel) & set(pixelsYNave))) > dificuldade:
                if len(list(set(pixelsXMissel) & set(pixelsXNave))) > dificuldade:
                    jogando = False
                    game_over(pontos)
            if len(list(set(pixelsYMissel2) & set(pixelsYNave))) > dificuldade:
                if len(list(set(pixelsXMissel2) & set(pixelsXNave))) > dificuldade:
                    jogando = False
                    game_over(pontos)

        pygameDisplay.update()
        clock.tick(60)

while True:        
    if jogar == False:
        iniciar()
    elif jogar == True:
        jogo()
    for event in eventos.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jogar == True
                jogo()
            elif event.key == pygame.K_x:
                limpa_Tela()
                pygame.quit()
                quit()
    if jogar == True:
        break
