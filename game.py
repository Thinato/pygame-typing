import pygame as pg
import colors as c
import random
from textbox import TextBox
from wordtarget import WordTarget
from leaderboard import Leaderboard
import os

class Game:
	def __init__(self, debug: bool=False):

		# inicializa o pygame
		pg.init()
		# inicializa a biblioteca de fontes do pygame
		pg.font.init()
		# inicializa a biblioteca sonora do pygame
		pg.mixer.init()



		self.WIDTH, self.HEIGHT = 800, 600
		self.WIN = None

		# Frames Per Second, velocidade na qual o jogo vai rodar
		self.FPS = 60
		# clock usado para registrar o tempo do jogo
		self.CLOCK = pg.time.Clock()

		# Fontes usadas dentro do jogo normal/grande
		self.FONT = pg.font.SysFont('consolas', 24)
		self.FONT_BIG = pg.font.SysFont('consolas', 80)
		

		# GUI se refere ao espaço azul na parte inferior da tela
		self.GUI_SIZE = 100
		self.GUI_BACK = pg.Rect(0, self.HEIGHT-self.GUI_SIZE, self.WIDTH, self.GUI_SIZE)


		# Efeitos sonoros
		# quando o jogador acerta uma palavra
		self.CORRECT_SOUND = pg.mixer.Sound(os.path.join('assets', 'sfx', 'correct.wav'))
		self.CORRECT_SOUND.set_volume(0.5)
		# quando uma palavra passa do limite da tela e o jogador perde uma vida
		self.HURT_SOUND = pg.mixer.Sound(os.path.join('assets', 'sfx', 'hurt1.wav'))
		# quando o jogador perde todas as vidas
		self.DEATH_SOUND = pg.mixer.Sound(os.path.join('assets', 'sfx', 'death.wav'))
		# quando o jogador sobe de nível
		self.LEVELUP_SOUND = pg.mixer.Sound(os.path.join('assets', 'sfx', 'levelup.wav'))
		self.LEVELUP_SOUND.set_volume(0.3)

		self.BACK_SOUND = pg.mixer.Sound(os.path.join('assets', 'sfx', 'back.mp3'))



		self.score = 0 # pontuação
		self.lives = 3 # vidas, o zero conta, então são 4
		self.level = 0 # o nível é usado para escalar com a dificuldade do jogo
		self.score_req = 20 # score necessario para subir de nivel

		self.words = [] # palavras que estão na tela

		self.word_list = []
		self.filename = 'python'
		file = open(os.path.join('word_lists', self.filename+'.txt'), 'r')
		for line in file:
			# adiciona palavra ao a lista de palavras
			# o 'strip()' serve para cortar o '\n' (new line) de cada palavra
			self.word_list.append(line.strip())
		self.TITLE = self.FONT.render(self.filename, 1, c.WHITE)

		self.running = True
		self.on_leaderboard = False
		self.debug = debug
		self.current_time = 0 # tempo do jogo em MS
		self.target_time = 0 # tempo que a proxima palavra vai aparecer
		self.target_interval = 2000

		# essa variável salva as ultimas {used_lines_max} linhas usadas para criar palavras
		# isso impede que as palavras acabem se misturando muito
		self.used_lines = [] 
		self.used_lines_max = 5



		self.txt_input = TextBox(10, self.HEIGHT-90, 200)
		self.lb = Leaderboard(self.WIDTH//2 - 200, 20, 400, 400, self.filename, True)


	def draw(self) -> None:
		# atualiza a caixa de texto
		#self.txt_input.update()

		# Plano de fundo
		self.WIN.fill(c.BLACK)
		pg.draw.rect(self.WIN, c.DARK_BLUE, self.GUI_BACK)
		
		# Título, o tema do jogo, depende da linguagem escolhida
		self.WIN.blit(self.TITLE, (10, 10))
		

		self.WIN.blit(self.FONT.render(f'Score: {self.score}', 1, c.WHITE), (10, self.HEIGHT-50))
		self.WIN.blit(self.FONT.render(f'Lives: {self.lives}', 1, c.WHITE), (250, self.HEIGHT-50))
		self.WIN.blit(self.FONT.render(f'Level: {self.level}', 1, c.WHITE), (250, self.HEIGHT-85))
		


		for word in self.words:
			word.move()
			word.draw(self.WIN)
		self.txt_input.draw(self.WIN)

		pg.display.flip()

	# Cria uma nova palavra
	def create_word(self):
		y = random.randint(0, int((self.HEIGHT-26-self.GUI_SIZE-32)/24)) * 24 + 32
		while y in self.used_lines:
			y = random.randint(0, int((self.HEIGHT-26-self.GUI_SIZE-32)/24)) * 24 + 32
		if len(self.used_lines) >= self.used_lines_max:
			del self.used_lines[0]
		self.used_lines.append(y)
		word = WordTarget(self.word_list[random.randint(0, len(self.word_list)-1)], self.WIDTH, y, self.level)
		# adiciona o objecto 'word' a lista de objeto de palavras
		self.words.append(word)
		# define o novo target time
		self.target_time = self.current_time + random.randint(self.target_interval - 100,self.target_interval + 100)
		#print(self.used_lines)

	def check_words(self) -> None:
		for word in self.words:
			if self.debug:
				self.txt_input.returned = ''
				self.score += len(word.text)*2
				if self.score >= self.score_req:
					self.levelup()
				self.CORRECT_SOUND.play()
				self.words.remove(word)
				self.create_word()
				return
			if word.x + word.get_width() < 0:
				self.lives -= 1 
				if self.lives < 0:
					self.game_over()
				self.WIN.fill(c.RED)
				pg.display.update()
				self.HURT_SOUND.play()
				self.words.remove(word)

				# caso o jogador acerte a palavra
			elif self.txt_input.returned == word.text:
				#print('Correct!')
				self.txt_input.returned = ''
				self.score += len(word.text)*2
				if self.score >= self.score_req:
					self.levelup()
				self.CORRECT_SOUND.play()
				self.words.remove(word)
				self.create_word()

	def levelup(self) -> None:
		self.LEVELUP_SOUND.play()
		self.target_interval = int(self.target_interval * 0.99)
		self.level += 1
		self.score_req = (self.level**3)*4 //5


	
	def game_over(self) -> None:
		text = self.FONT_BIG.render('GAME OVER!', 1, c.WHITE)
		self.WIN.blit(text, (self.WIDTH/2 - text.get_width()/2, self.HEIGHT/2 - text.get_height()/2))
		self.DEATH_SOUND.play()
		pg.display.update()
		pg.time.delay(2000)
		self.on_leaderboard = True


	def show_leaderboard(self):
		if self.lb.new_entry:
			self.lb.draw_textbox(self.WIN)
			self.lb.update_textbox(self.WIN)
		else:
			self.lb.__init__(self.WIDTH//2 - 200, 20, 400, 400, self.filename, False)
			self.lb.draw(self.WIN)
		pg.display.update()


	def start(self):
		self.WIN = pg.display.set_mode((self.WIDTH, self.HEIGHT))
		self.create_word()
		self.BACK_SOUND.play()

		while self.running: # game loop
			while self.on_leaderboard:
				self.CLOCK.tick(self.FPS)

				for event in pg.event.get():
					if event.type == pg.QUIT: # evento para sair do pygame
						self.running = False
						self.on_leaderboard = False
					if event.type == pg.KEYDOWN:
						if self.lb.new_entry:
							if event.key == pg.K_RETURN:
								print(self.lb.txtbox.returned)
								self.lb.save_score(self.lb.txtbox.returned, self.score)
								self.lb.new_entry = False
					self.lb.txtbox.handle_event(event)
				self.show_leaderboard()


			self.CLOCK.tick(self.FPS) # definindo o limite de fps
			for event in pg.event.get():
				if event.type == pg.QUIT: # evento para sair do pygame
					self.running = False
				self.txt_input.handle_event(event) # evento da textbox
				if event.type == pg.KEYDOWN:
					if self.debug:
						if event.key == pg.K_SPACE:
							self.check_words()
						if event.key == pg.K_k:
							self.levelup()

			self.current_time = pg.time.get_ticks()

			# se o tempo 'target' chegar, crie uma nova palavra
			if self.current_time >= self.target_time:
				self.create_word()



			if not self.debug:
				self.check_words()
			self.draw()
		pg.quit()

