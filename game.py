import pygame as pg
import colors as c
import random
from textbox import TextBox
from wordtarget import WordTarget
from leaderboard import Leaderboard
import os

class Game:
	def __init__(self, game: str='python',debug: bool=False):

		# inicializa o pygame
		pg.init()
		# inicializa a biblioteca de fontes do pygame
		pg.font.init()
		# inicializa a biblioteca sonora do pygame
		pg.mixer.init()

		# Título da aplicação
		pg.display.set_caption('Typing Game')
		# Ícone da aplicação
		icon = pg.image.load(os.path.join('assets', 'img', 'logo32.png'))
		pg.display.set_icon(icon)

		# Defina a altura e a largura da janela
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


		# musica de fundo, com duas variações, o randint escolhe a musica
		self.BACK_SOUND = pg.mixer.Sound(os.path.join('assets', 'sfx', 'back'+str(random.randint(0,1))+'.mp3'))
		# caso o jogador continue jogando mesmo depois de a música acabar, ela reinicia
		self.BACK_SOUND_LOOPS = 1
		# pega o tempo em que a música deve reiniciar
		self.BACK_SOUND_TARGETTIME = ((self.BACK_SOUND.get_length()*1000) * self.BACK_SOUND_LOOPS)
		
		# musica de fim de jogo
		self.GAMEOVER_SOUND = pg.mixer.Sound(os.path.join('assets', 'sfx', 'gameover.mp3'))


		self.score = 0 # pontuação
		self.lives = 2 # vidas, o zero conta, então são 4
		self.level = 1 # o nível é usado para escalar com a dificuldade do jogo
		self.score_req = ((self.level+1)**3)*4 // 5 # score necessario para subir de nivel
		self.hits = 0 # conta quantos acertos o jogador teve
		self.char_hits = 0 # conta o numero de caracteres que o jogador acertou
		self.misses = 0 # conta quantos erros o jogador cometeu
		self.WPM = 0 # armazena o calculo de quantas palavras por minuto o jogador faz
		self.score_final = 0 # pontuação * precisão (a pontuação que vai para o ranking)


		self.words = [] # palavras que estão na tela

		self.word_list = [] # lista de todas as palavras disponiveis
		self.filename = game # nome do arquivo que contem as palavras
		file = open(os.path.join('word_lists', self.filename+'.txt'), 'r')
		for line in file:
			# adiciona palavra ao a lista de palavras
			# o 'strip()' serve para cortar o '\n' (new line) de cada palavra
			self.word_list.append(line.strip())
		self.TITLE = self.FONT.render(self.filename, 1, c.WHITE)

		self.running = True # checa se o jogo está rodando
		self.on_leaderboard = False # checa se o jogador está na leaderboard (no ranking)
		self.debug = debug # checa se o jogo foi rodado no modo debug
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
		
		# Escreve a ui para o jogador, os pontos, as vidas e o nível
		self.WIN.blit(self.FONT.render(f'Score: {self.score}', 1, c.WHITE), (10, self.HEIGHT-50))
		self.WIN.blit(self.FONT.render(f'{self.score_req}', 1, c.ORANGE), (100, self.HEIGHT-28))
		self.WIN.blit(self.FONT.render(f'Lives: {self.lives}', 1, c.WHITE), (250, self.HEIGHT-50))
		self.WIN.blit(self.FONT.render(f'Level: {self.level}', 1, c.WHITE), (250, self.HEIGHT-85))
		self.WIN.blit(self.FONT.render(f'WPM: {self.WPM}', 1, c.WHITE), (500, self.HEIGHT-85))
		# como não posso dividir por zero, o padrão será 100%, já que se não houver erros, a precisão é 100%
		if self.misses>0:
			self.WIN.blit(self.FONT.render(f'Accuracy: {round((self.hits-self.misses)/(self.hits+self.misses)*100,1)}%', 1, c.WHITE), (500, self.HEIGHT-50))
		else:
			self.WIN.blit(self.FONT.render(f'Accuracy: 100%', 1, c.WHITE), (500, self.HEIGHT-50))
		

		# desenha e move cada palavra
		for word in self.words:
			word.move()
			word.draw(self.WIN)

		# desenha a caixa de texto
		self.txt_input.draw(self.WIN)

		# atualiza a tela inteira
		pg.display.flip()

		# você poderia usar o 'pg.display.update()', porém ele só atualiza algumas regiões da tela
		# para poupar memória, por isso eu uso o 'flip()'
		# como é a função principal, o ideal é que atualize tudo


	# Cria uma nova palavra
	def create_word(self) -> None:

		# aqui ele define a altura da palavra, porém ele faz com que elas estejam organizadas
		# sempre em linhas corretas, para evitar qualquer tipo de erro
		y = random.randint(0, int((self.HEIGHT-26-self.GUI_SIZE-32)/24)) * 24 + 32

		# aqui ele testa a região escolhida para e compara com as 5 ultimas,
		# ou seja, as palavras nunca vão aparecer duas vezes seguidas na mesma linha
		# isso evita que elas fiquem uma em cima da outra
		while y in self.used_lines:
			y = random.randint(0, int((self.HEIGHT-26-self.GUI_SIZE-32)/24)) * 24 + 32
		if len(self.used_lines) >= self.used_lines_max:
			del self.used_lines[0]
		self.used_lines.append(y)


		# define a palavra
		word = WordTarget(self.word_list[random.randint(0, len(self.word_list)-1)], self.WIDTH, y, self.level)
		# adiciona o objecto 'word' a lista de objeto de palavras
		self.words.append(word)
		# define o novo target time
		self.target_time = self.current_time + random.randint(self.target_interval - 100,self.target_interval + 100)
		#print(self.used_lines)

	# valida a palavra digitada
	def validate_words(self) -> None:
		for word in self.words:
			# caso esteja em modo debug, ele ingora o que você digitou e te dá a pontuação direto
			if self.debug:
				self.hits += 1
				self.char_hits += len(word.text)
				self.txt_input.returned = ''
				self.score += len(word.text)*2
				if self.score >= self.score_req:
					self.levelup()
				self.CORRECT_SOUND.play()
				self.words.remove(word)
				self.create_word()
				return

				# caso o jogador acerte a palavra
			elif self.txt_input.returned == word.text:
				# soma nos acertos
				self.hits += 1
				# soma a quantidade de caracteres
				self.char_hits += len(word.text)
				# limpa o retono da caixa de texto
				self.txt_input.returned = ''
				# adiciona a pontuação
				self.score += len(word.text)*2
				# caso a pontuação para o próximo nível seja atingida, suba de nível
				if self.score >= self.score_req:
					self.levelup()
				self.CORRECT_SOUND.play()
				self.words.remove(word)
				self.create_word()
				return
		# caso nenhuma das palavras, tenha passado nos casos acima
		# adicione um para os erros
		self.misses += 1

	def check_words(self) -> None:
		for word in self.words:
			if word.x + word.get_width() < 0:
				self.lives -= 1 
				if self.lives < 0:
					self.game_over()
				self.WIN.fill(c.RED)
				pg.display.update()
				self.HURT_SOUND.play()
				self.words.remove(word)
				return

	def levelup(self) -> None:
		self.LEVELUP_SOUND.play()
		self.target_interval = int(self.target_interval * 0.99)
		self.level += 1
		self.score_req = ((self.level+1)**3)*4 // 5 + self.score_req//2
		# caso o nível seja multiplo de 3, adicione uma vida extra
		if self.level % 3 == 0:
			self.lives += 1


	
	def game_over(self) -> None:
		text = self.FONT_BIG.render('GAME OVER!', 1, c.WHITE)
		self.WIN.blit(text, (self.WIDTH/2 - text.get_width()/2, self.HEIGHT/2 - text.get_height()/2))
		self.DEATH_SOUND.play()
		pg.display.update()
		pg.time.delay(2000)
		self.on_leaderboard = True

		
	def show_leaderboard(self) -> None:
		if self.lb.new_entry:
			self.lb.draw_textbox(self.WIN, self.score, round((self.hits-self.misses)/(self.hits+self.misses),2))
			self.lb.update_textbox(self.WIN)
		else:
			self.lb.__init__(self.WIDTH//2 - 200, 20, 400, 400, self.filename, False)
			self.lb.draw(self.WIN)
		pg.display.update()

	# Calcula as palavras por minuto
	def calculate_wpm(self) -> int:
		return int((self.char_hits/5) / ((self.current_time/60000)))

	def start(self):
		# definindo a janela como o width e heigth (800x600)
		self.WIN = pg.display.set_mode((self.WIDTH, self.HEIGHT))
		# cria uma palavra
		self.create_word()
		# incia a música de fundo
		self.BACK_SOUND.play()

		while self.running: # game loop
			stop_sound = True
			while self.on_leaderboard:
				self.score_final = int(self.score * round((self.hits-self.misses)/(self.hits+self.misses),2))
				if stop_sound:
					pg.mixer.stop()
					self.GAMEOVER_SOUND.play()
					stop_sound = False
				self.CLOCK.tick(self.FPS)
				for event in pg.event.get():
					self.lb.txtbox.handle_event(event)
					if event.type == pg.QUIT: # evento para sair do pygame
						self.running = False
						self.on_leaderboard = False
					if event.type == pg.KEYDOWN:
						if self.lb.new_entry:
							if event.key == pg.K_RETURN:
								#print(self.lb.txtbox.returned)
								self.lb.save_score(self.lb.txtbox.returned, self.score_final)
								self.lb.new_entry = False
					
				self.show_leaderboard()


			self.CLOCK.tick(self.FPS) # definindo o limite de fps
			for event in pg.event.get():
				if event.type == pg.QUIT: # evento para sair do pygame
					self.running = False
				self.txt_input.handle_event(event) # evento da textbox
				if event.type == pg.KEYDOWN:
					if event.key == pg.K_RETURN:
						self.validate_words()
						self.WPM = self.calculate_wpm()
					if self.debug:
						if event.key == pg.K_SPACE:
							self.check_words()
						if event.key == pg.K_k:
							self.levelup()

			self.current_time = pg.time.get_ticks()

			# se o tempo 'target' chegar, crie uma nova palavra
			if self.current_time >= self.target_time:
				self.create_word()

			# aqui é o loop da música, eu fiquei com preguiça de testar, mas deve estar funcionando
			#print(str(self.current_time) + ' | ' + str(((self.BACK_SOUND.get_length()*1000) * self.BACK_SOUND_LOOPS) + 1000))
			
			if self.current_time > ((self.BACK_SOUND.get_length()*1000) * self.BACK_SOUND_LOOPS) + 1000:
				self.BACK_SOUND.play()
				self.BACK_SOUND_LOOPS += 1


			self.check_words()
			self.draw()
		pg.quit()