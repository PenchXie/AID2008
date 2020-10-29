import random

class GameController():
	def __init__(self):
		self.__list_merge = [2, 2, 0, 4]
		self.__map = [
			[0, 2, 4, 0],
			[2, 2, 4, 8],
			[4, 4, 0, 2],
			[0, 8, 0, 0]
		]
		# 补充新数字的标志
		self.__active = False

	@property
	def map(self):
		return self.__map

	def initialize_map(self):
		for i in range(len(self.__map)):
			for j in range(len(self.__map[i])):
				self.__map[i][j] = 0

		self.generate_new_num()
		self.generate_new_num()
	
	def generate_new_num(self):
		while True:
			i = random.choice(range(len(self.__map)))
			j =  random.choice(range(len(self.__map[i])))
			if self.__map[i][j] == 0:
				self.__map[i][j] = random.choice((2, 2, 2, 4))
				break

	def zero_to_end(self):
		# 创建一个临时变量储存移动前的列表
		self.__temp_list = self.__list_merge[:]
		for i in range(len(self.__list_merge) -1, -1, -1):
			if self.__list_merge[i] == 0:
				del self.__list_merge[i]
				self.__list_merge.append(0)
		if self.__list_merge != self.__temp_list:
			# 如果移动前后列表不同，补充标志为True
			self.__active = True

	def merge(self):
		self.zero_to_end()
		self.__temp_list = self.__list_merge[:]
		for i in range(len(self.__list_merge) - 1):
			if self.__list_merge[i] == self.__list_merge[i + 1]:
				self.__list_merge[i] += self.__list_merge[i + 1]
				del self.__list_merge[i + 1]
				self.__list_merge.append(0)
		if self.__list_merge != self.__temp_list:
			# 如果融合前后列表不同，补充标志为True
			self.__active = True

	def move_left(self):
		for i in range(len(self.__map)):
			self.__list_merge = self.__map[i]
			self.zero_to_end()
			self.merge()
		if self.__active:
			self.generate_new_num()
		# 完成一次移动后补充标志变回False
		self.__active = False

	def move_right(self):
		for map_list in self.__map:
			self.__list_merge = map_list[::-1]
			self.zero_to_end()
			self.merge()
			map_list[:] = self.__list_merge[::-1]
		if self.__active:
			self.generate_new_num()
		self.__active = False

	def matrix_transpose(self):
		for i in range(len(self.__map)):
			for j in range(i + 1, len(self.__map[i])):
				self.__map[i][j], self.__map[j][i] = self.__map[j][i], self.__map[i][j]

	def move_up(self):
		self.matrix_transpose()
		self.move_left()
		self.matrix_transpose()

	def move_down(self):
		self.matrix_transpose()
		self.move_right()
		self.matrix_transpose()


controller01 = GameController()
# controller01.generate_new_num()
# controller01.zero_to_end()

# controller01.merge()
# controller01.move_left()
# controller01.move_right()
# controller01.matrix_transpose()
# controller01.move_up()
controller01.move_down()

# print(controller01._GameController__list_merge)
print(controller01.map)