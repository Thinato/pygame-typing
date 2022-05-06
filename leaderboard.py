import pygame as pg
import colors as c
import os

class Leaderboard:
	def __init__(self, x: int, y: int, w: int, h: int, game: str):
		self.FONT = pg.font.SysFont('consolas', 24)
		self.game = game
		self.file = open(os.path.join('leaderboards', game+'.txt'), 'r')
		
		self.x = x
		self.y = y
		self.w = w
		self.h = h

		self.BACKGROUND = pg.Rect(x, y, w, h)


	def draw(self, screen) -> None:
		pg.draw.rect(screen, c.DARK_BLUE, self.BACKGROUND)
		txt_title = self.FONT.render(f'Leaderboard', 1, c.WHITE)
		screen.blit(txt_title, (self.x+self.w//2 - txt_title.get_width()//2, self.y+10))

		txt_name = self.FONT.render(f'Name', 1, c.WHITE)
		screen.blit(txt_name, (self.x+self.w*.3 - txt_name.get_width()//2, self.y+45))

		txt_score = self.FONT.render(f'Score', 1, c.WHITE)
		screen.blit(txt_score, (self.x+self.w*.8 - txt_score.get_width()//2, self.y+45))

