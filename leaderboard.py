import pygame as pg
import colors as c
import os

class Leaderboard:
	def __init__(self, x: int, y: int, w: int, h: int, game: str):
		self.FONT = pg.font.SysFont('consolas', 24)
		self.game = game
		self.file = open(os.path.join('leaderboards', game+'.txt'), 'r')
		self.scores = []
		for line in self.file:
			self.scores.append(line.strip())

		self.x = x
		self.y = y
		self.w = w
		self.h = h



		self.BACKGROUND = pg.Rect(x, y, w, h)


	def draw(self, screen) -> None:
		pg.draw.rect(screen, c.DARK_BLUE, self.BACKGROUND)
		txt_title = self.FONT.render('Leaderboard', 1, c.WHITE)
		screen.blit(txt_title, (self.x+self.w//2 - txt_title.get_width()//2, self.y+10))

		txt_name = self.FONT.render('Name', 1, c.WHITE)
		screen.blit(txt_name, (self.x+self.w*.3 - txt_name.get_width()//2, self.y+45))

		txt_score = self.FONT.render('Score', 1, c.WHITE)
		screen.blit(txt_score, (self.x+self.w*.8 - txt_score.get_width()//2, self.y+45))

		# Linhas brancas
		pg.draw.rect(screen, c.WHITE, pg.Rect(self.x+10, self.y+40, self.w-20, 2)) # horizontal
		pg.draw.rect(screen, c.WHITE, pg.Rect(self.x+10, self.y+70, self.w-20, 2)) # horiontal
		pg.draw.rect(screen, c.WHITE, pg.Rect(self.x+self.w*.6, self.y+40, 2, self.h-40-20)) # vertical

		# Nomes e pontos
		count = 0
		vertical_spacing = 24 # mesmo tamanho da fonte
		for score in self.scores:
			if count > 12:
				break
			text = score.split(';')
			n = self.FONT.render(str(count+1).rjust(2)+'. '+ text[0][:12], 1, c.WHITE)
			s = self.FONT.render(text[1][:10], 1, c.WHITE)
			screen.blit(n, (self.x+20, self.y+80 + (vertical_spacing*count)))
			screen.blit(s, (self.x+self.w*.8 - s.get_width()//2, self.y+80 + (vertical_spacing*count)))
			count += 1




