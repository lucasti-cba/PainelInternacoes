# -*- coding: utf-8 -*-
import sys
import os
import time
import pygame
from bin.config import *
from sql_conector import *
from datetime import datetime



def renderQuerry(querry, font_size, cor, screen, position):
	pygame.font.init()
	fonte = pygame.font.get_default_font()
	fontesys = pygame.font.SysFont(fonte, font_size)
	txttela = fontesys.render(querry, 1, cor)
	return screen.blit(txttela,position)

def abreviaNome(nome):
	y = ''
	z = 0
	temp = []
	for n in nome + ' ':
		if n == ' ':
			z += 1
			temp.append(y)
			y = ''
		else:
			y += n
	cont = 0
	nome1 = ''
	for m in (temp):
		if cont > 0:
			if len(m) > 2:
				nome1 += m[0:1] + '. '
		else:
			nome1 += m + ' '
			cont += 1
	return nome1

def renderAlas(querry, local, cor1, position_tamanho, x):
	COR = cor[cor1]
	COR2 = 'branco'
	draw = pygame.draw.rect(local, COR, position_tamanho)
	draw
	renderQuerry(querry[19], 24, cor[COR2], tela, [10 , x] )
	try:
		renderQuerry(abreviaNome(querry[27]), 24, cor[COR2], tela, [90 , x] )
	except:
		pass
	renderQuerry(str(querry[0]), 24, cor[COR2], tela, [310 , x] )
	renderQuerry((querry[2]).strftime("%d/%m/%Y"), 24, cor[COR2], tela, [460 , x] )
	try:
		renderQuerry(abreviaNome(querry[26]), 24, cor[COR2], tela, [600 , x] )
	except:
		pass
	try:
		renderQuerry(abreviaNome(querry[35]), 24, cor[COR2], tela, [760 , x] )
	except:
		pass
	try:	
		renderQuerry([querry[13]], 24, cor[COR2], tela, [1060 , x] )
	except:
		pass	
	try:	
		renderQuerry(querry[-3], 24, cor[COR2],tela, [1260 , x] )
	except:
		pass

def bubbleSort(alist):
	for passnum in range(len(alist)-1,0,-1):
		for i in range(passnum):
			if alist[i][19]>alist[i+1][19]  :
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1]= temp

	return alist


def start_the_game():
	pygame.init()
	global tela
	infoObject = pygame.display.Info()
	tela = pygame.display.set_mode((infoObject.current_w-10, infoObject.current_h-10), pygame.SHOWN|pygame.RESIZABLE, 0)
	pygame.display.set_caption('Internação Hospitalar  - Hospital São Judas Tadeu ')
	clock = pygame.time.Clock()

	logo = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/bin/img/logo.png')
	img = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/bin/img/wpp2.jpg')
	clock.tick(1)
	key=pygame.key.get_pressed()  #checking pressed keys
	done = False
	while not done:
    	#events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

					
	### PAINEL PADRAO
		data_e_hora_atuais = datetime.now()
		mes = ['janeiro', 'fevereiro', 'março' , 'abril', 'maio', 'junho', 'julho','agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
		data = data_e_hora_atuais.strftime(', %d de '+mes[data_e_hora_atuais.month - 1 ]+' de %Y')
		hora = data_e_hora_atuais.strftime('%H:%M:%S')
		tela.fill(cor['verde1'])
		draw1 = pygame.draw.rect(tela, cor['branco'], [0, 0, infoObject.current_w + 800, 120])
		draw2 = pygame.draw.rect(tela, cor['verde2'], [0, 122, infoObject.current_w + 800, 30])
		draw1
		tela.blit(logo, (20, 20))
		draw2
		renderQuerry('Ocupação Hospitalar', 80, cor['verde2'], tela, [370,40] )
		renderQuerry('Clínico', 36, cor['verde2'], tela, [1000,20] )
		renderQuerry('Cirúrgico', 36, cor['verde2'], tela, [1000,60] )
		renderQuerry(data, 48, cor['verde2'], tela, [infoObject.current_w - 410, 20])
		renderQuerry(hora, 48, cor['verde2'], tela, [infoObject.current_w - 550, 20])
		renderQuerry('Leito', 36, cor['branco'], tela, [10, 123])
		renderQuerry('Paciente', 36, cor['branco'], tela, [90, 123])
		renderQuerry('Prontuario', 36, cor['branco'], tela, [310, 123])
		renderQuerry('Entrada', 36, cor['branco'], tela, [460, 123])
		renderQuerry('Médico', 36, cor['branco'], tela, [600, 123])
		renderQuerry('Procedimento', 36, cor['branco'], tela, [760, 123])
		renderQuerry('Convênio', 36, cor['branco'], tela, [1060, 123])
		renderQuerry('Observação', 36, cor['branco'], tela, [1260, 123])
		lista = getdados()
		lista = bubbleSort(lista)
		inicioy = 156
		cli = 0
		cir = 0
		livre = 0
	
		inicioy = 156
		for row in lista:
			inicio = [(0,inicioy),(infoObject.current_w + 1000, 20 )]
			renderAlas(row, tela, 'VERDE', inicio , inicioy+4)

			inicioy += 22
		renderQuerry(str(cli), 36, cor['verde2'], tela, [1200,20] )
		renderQuerry(str(cir), 36, cor['verde2'], tela, [1200,60] )	
		pygame.display.update()
		pygame.display.flip()
	pygame.quit()

while True:
	try:
		start_the_game()
	except:
		print('error')
		start_the_game()
