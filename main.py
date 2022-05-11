# inspirado no wspeed do bisqwit

from game import Game
import sys


def main(word_list: str):
	# altere a word_list aqui
	g = Game(word_list)
	g.start()

if __name__ == '__main__':
	word_list = str(sys.argv[1])
	main(word_list)