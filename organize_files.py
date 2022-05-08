import os

class Organize:
	def __init__(self):
		self.files = []
		self.PATH = os.path.join('leaderboards')
		for i in os.listdir(self.PATH):
			if i[-4:] == '.txt':
				self.files.append(i)


	def organize_all(self) -> None:
		for fname in self.files:
			file = open(os.path.join(self.PATH, fname), 'r')
			lines = file.readlines()
			lines.sort(reverse=True, key=lambda x:int(x.split(';')[-1]))

			file.close()
			file = open(os.path.join(self.PATH, fname), 'w')
			file.write(''.join(lines))

	def organize_file(self, filename: str) -> None:
		file = open(os.path.join(self.PATH, filename), 'r')
		lines = file.readlines()
		lines.sort(reverse=True, key=lambda x:int(x.split(';')[-1]))

		file.close()
		file = open(os.path.join(self.PATH, filename), 'w')
		file.write(''.join(lines))


if __name__ == '__main__':
	o = Organize()
	o.organize_all()