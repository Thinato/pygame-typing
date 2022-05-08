import pygame as pg
import colors as c
from organize_files import Organize
from textbox import TextBox
import os


class Leaderboard:
	def __init__(self, x: int, y: int, w: int, h: int, game: str, new_entry: bool=False):
		self.FONT = pg.font.SysFont('consolas', 24)
		self.game = game
		self.new_entry = new_entry

		o = Organize()
		# se eu tivesse mais arquivos no 'leaderboads' eu iria colocar o 'organize_file'
		# mas como são poucos uso o 'organize_all' mesmo

		o.organize_all()
		# o.organize_file(game+'.txt')

		self.file = open(os.path.join('leaderboards', self.game+'.txt'), 'r')
		self.scores = []
		for line in self.file:
			self.scores.append(line.strip())

		self.x = x
		self.y = y
		self.w = w
		self.h = h



		self.BACKGROUND = pg.Rect(x, y, w, h)
		self.BACKGROUND_TEXTBOX = pg.Rect(x, y, w, 32+12)
		self.txtbox = TextBox(self.x+6, self.y+6, self.w-12)

	def draw_textbox(self, screen):
		pg.draw.rect(screen, c.DARK_BLUE, self.BACKGROUND_TEXTBOX)

	def update_textbox(self, screen):
		self.txtbox.draw(screen)

	def save_score(self, name: str, score: int):
		with open(os.path.join('leaderboards', self.game+'.txt'), 'a') as file:
			file.write(name+';'+str(score)+'\n')

		pass

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




