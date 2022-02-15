# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 15:12:10 2021

@author: shaya
"""
#updated version of tic tac toe 
#referenced from https://pythonguides.com/create-a-game-using-python-pygame/
#coded by Shayan Aziz, Chris Fortini, Diego Roti and Jonathan Zambrano

import pygame, sys
import numpy as np
pygame.init()
#Importing the two libraries needed to create tic tac toe

width = 500
height = 500
line_width = 12
win_line_width = 12

ss = 175 #size of square
circle_rad = 54
circle_width = 12
cross_width = 22
space = 50
board_Rows = 3
board_columns = 3
#outlined dimensions of the board
colour = (0, 255, 0)
background_c = (112, 41, 99)
line_colour = (23, 145, 135)
circle_colour = (239, 231, 200)
x_colour = (239, 231, 200)
#colours
screen = pygame.display.set_mode( (width, height) )
pygame.display.set_caption( 'TICKY TACKY TOES' )
screen.fill( background_c )
#setting up the new window that pops up when the code is run, width and height 
#defines how large the window is and display.set_caption is the text that pops up at the top
board = np.zeros( (board_Rows, board_columns) )
#the board will be created using "np.zeros()"
def drlines():
	#this function is exclusively used to draw out the lines that we defined previously
	pygame.draw.line( screen, line_colour, (0, ss), (width, ss), line_width)
	
	pygame.draw.line( screen, line_colour, (0, 2 *ss), (width, 2 *ss), line_width )

	pygame.draw.line( screen, line_colour, (ss, 0), (ss, height), line_width )

	pygame.draw.line( screen, line_colour, (2 * ss, 0), (2 * ss, height), line_width )

def drfigures():
      #this function is used to draw out the two elements to the game, x and o
	for row in range(board_Rows):
		for col in range(board_columns):
			if board[row][col] == 1:
				pygame.draw.circle( screen, circle_colour, (int( col * ss + ss//2 ), int( row * ss + ss//2 )), circle_rad, circle_width )
			elif board[row][col] == 2:
				pygame.draw.line( screen, circle_colour, (col * ss + space, row * ss + ss - space), (col * ss + ss - space, row * ss + space), cross_width )	
				pygame.draw.line( screen, circle_colour, (col * ss + space, row * ss + space), (col * ss + ss - space, row * ss + ss - space), cross_width )

def marks__square(row, col, player):
      #used to mark the board
	board[row][col] = player

def available__square(row, col):
      #checks if the spot on the board is available, returns false if there is none and true if there is
	return board[row][col] == 0

def isBoardFull():
      #this function loops through the rows and columns chekcing if the board is full, if it is, returns true
      #if not returns false
	for row in range(board_Rows):
		for col in range(board_columns):
			if board[row][col] == 0:
				return False

	return True

def check_win(player):
      #goes through the win conditions of tic tac toe
	for col in range(board_columns):
		if board[0][col] == player and board[1][col] == player and board[2][col] == player:
			draw_vertical_winning_line(col, player)
			return True

	for row in range(board_Rows):
		if board[row][0] == player and board[row][1] == player and board[row][2] == player:
			draw_horizontal_winning_line(row, player)
			return True

	if board[2][0] == player and board[1][1] == player and board[0][2] == player:
		draw_asc_diagonal(player)
		return True

	if board[0][0] == player and board[1][1] == player and board[2][2] == player:
		draw_desc_diagonal(player)
		return True

	return False

def draw_vertical_winning_line(col, player):
      #this function draws out the winning vertical line for when the player achieves three in a row
	posX = col * ss + ss//2

	if player == 1:
		color = circle_colour
	elif player == 2:
		color = x_colour

	pygame.draw.line( screen, color, (posX, 15), (posX, height - 15), line_width )

def draw_horizontal_winning_line(row, player):
      #this function draws out the winning horizontal line
	posY = row * ss + ss//2

	if player == 1:
		color = circle_colour
	elif player == 2:
		color = x_colour

	pygame.draw.line( screen, color, (15, posY), (width - 15, posY), win_line_width)

def draw_asc_diagonal(player):
	if player == 1:
		color = circle_colour
	elif player == 2:
		color = x_colour

	pygame.draw.line( screen, color, (15, height - 15), (width - 15, 15), win_line_width )

def draw_desc_diagonal(player):
	if player == 1:
		color = circle_colour
	elif player == 2:
		color = x_colour
#the previous two functions draw out the ascending and descending diagonal winning lines
	pygame.draw.line( screen, color, (15, 15), (width - 15, height - 15), win_line_width )

def restart():
      #when your game ends and you desire to play again
	screen.fill( background_c )
	drlines()
	for row in range(board_Rows):
		for col in range(board_columns):
			board[row][col] = 0

#while loop utilizing the functions to create the game
drlines()
player = 1
game_over = False
#originally game_over is false, as the game has just begun
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
            #quitting the game

		if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

			mouseX = event.pos[0] 
			mouseY = event.pos[1] 

			clicked_row = int(mouseY // ss)
			clicked_col = int(mouseX // ss)

			if available__square( clicked_row, clicked_col ):

				marks__square( clicked_row, clicked_col, player )
				if check_win( player ):
					game_over = True
				player = player % 2 + 1

				drfigures()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				restart()
				player = 1
				game_over = False

	pygame.display.update()