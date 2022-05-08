import pygame as pg
import colors as c

class WordTarget:
	def __init__(self, text: str, x: int, y: int, level: int):
		self.FONT = pg.font.SysFont('consolas', 24)
		self.COLOR = c.GREEN

		self.text = text
		self.txt_surface = self.FONT.render(text, True, self.COLOR)
		self.speed = 1.3 + level//20
		self.x = x
		self.y = y

	def draw(self, screen) -> None:
		# Escreve o texto na tela
		screen.blit(self.txt_surface, (self.x, self.y))

	def move(self) -> None: 
		# move a palavra para a esquerda
		self.x -= self.speed

	def get_width(self) -> int: 
		# retorna o comprimento da palavra
		return self.txt_surface.get_width()

#	def delete(self):
#		pass




