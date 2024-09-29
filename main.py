#ex21: faca um programa em python que abra e reproduza um arquivo mp3
import pygame
import sys
from pygame.locals import *
from random import randint

pygame.init()
pygame.mixer.init()

#
fonte = pygame.font.SysFont('arial', 50, True, False)
#


tela = pygame.display.set_mode((1440, 1080))

#constante↓
tam = tela.get_width()-200

#listas com as informações das musicas e dos botoes de play
controles = ['media/img/play.png', 'media/img/pause.png', 'media/img/plus.png', 'media/img/minus.png', 'media/img/tema.png','media/img/play1.png', 'media/img/pause1.png', 'media/img/plus1.png', 'media/img/minus1.png', 'media/img/tema1.png']

musica = ['media/sounds/HK Radiance.mp3', 'media/sounds/HK Main Theme.mp3', 'media/sounds/HK Dirtmouth.mp3', 'media/sounds/HK Greenpath.mp3', 'media/sounds/HK Soul Sanctum.mp3']

imagem = ['media/img/HK_R.png', 'media/img/HK_M.png', 'media/img/HK_D.png',  'media/img/HK_G.png',  'media/img/HK_S.png' ]

caption = ['Hollow Knigth - Radiance','Hollow Knigth - Tema','Hollow Knigth - Dirtmouth',' Hollow Knigth - Caminho Verde','Hollow Knigth - Santuário das Almas']

indice=randint(0, len(musica))


pygame.mixer.music.load(musica[indice])
pygame.mixer.music.play()

coverBack = pygame.image.load(imagem[indice])
cover = pygame.transform.scale(coverBack, (tam, tam))

play = pygame.image.load(controles[0])
pause = pygame.image.load(controles[1])
plus = pygame.image.load(controles[2])
minus = pygame.image.load(controles[3])
tema = pygame.image.load(controles[4])
v=0.5

r,g,b = 255, 255, 255
rt,gt,bt = 5,5,5

#main loop↓
while True:
	pygame.mixer.music.set_volume(v)
	tela.fill((r, g, b))
	titulo = f'{caption[indice]}'
	texto = fonte.render(titulo, True, (rt,gt,bt))
	
	control_play = pygame.draw.rect(tela, (r,g,b), (tam-750,tam+400, 60,60))
	control_pause = pygame.draw.rect(tela, (r,g,b), (tam-525,tam+400, 60,60))
	control_vol_plus = pygame.draw.rect(tela, (r,g,b), (tam-325,tam+400, 60,60))
	control_vol_minus = pygame.draw.rect(tela, (r,g,b), (tam-100,tam+400, 60,60)) 
	control_tema = pygame.draw.rect(tela, (r,g,b), (tam+80, tam+380, 80,80))
	

	for event in pygame.event.get():
	# botões do player
		if event.type == pygame.MOUSEBUTTONDOWN:
			if control_play.collidepoint(event.pos):
				pygame.mixer.music.unpause()
			
			if control_pause.collidepoint(event.pos):
				pygame.mixer.music.pause()
				
			if control_vol_plus.collidepoint(event.pos):
				v=v+0.1
				
			if control_vol_minus.collidepoint(event.pos):
				v=v-0.1
				
			if control_tema.collidepoint(event.pos):
				if r==255:
					r,g,b = 50,50,50
					rt,gt,bt = 255,255,255
					play = pygame.image.load(controles[5])
					pause = pygame.image.load(controles[6])
					plus = pygame.image.load(controles[7])
					minus = pygame.image.load(controles[8])
					tema = pygame.image.load(controles[9])
					
				else:
					r,g,b = 255,255,255
					rt,gt,bt = 5,5,5
					play = pygame.image.load(controles[0])
					pause = pygame.image.load(controles[1])
					plus = pygame.image.load(controles[2])
					minus = pygame.image.load(controles[3])
					tema = pygame.image.load(controles[4])
			
	
	tela.blit(play, (tam-750,tam+400))
	tela.blit(pause, (tam-525,tam+400))
	tela.blit(plus, (tam-325,tam+400))
	tela.blit(minus, (tam-100,tam+400))
	tela.blit(tema, (tam+80, tam+380))
	
	tela.blit(texto, (tam-750, tam+200))
	tela.blit(cover, (tam-800, tam-800))
	pygame.display.update()
