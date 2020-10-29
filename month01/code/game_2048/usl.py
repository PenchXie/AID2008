from bll import GameController

class GameView():
	def __init__(self):
		self.__controller = GameController()
		# 游戏活动标志
		self.__active = True

	def __start_game(self):
		self.__controller.initialize_map()

	def __show_map(self):
		for i in range(len(self.__controller.map)):
			for j in range(len(self.__controller.map[i])):
				print(self.__controller.map[i][j], end='\t')
			print()

	def __show_selections(self):
		print("1.up")
		print("2.down")
		print("3.left")
		print("4.right")
		print("5.restart")
		print("6.quit")

	def __get_number(self, msg) -> int:
		while True:
			try:
				num = int(input(msg))
				return num
			except ValueError:
				print("Incorrect input")

	def __input_selection(self):
		selection = self.__get_number("Please enter selection:")
		if selection == 1:
			self.__controller.move_up()
		elif selection == 2:
			self.__controller.move_down()
		elif selection == 3:
			self.__controller.move_left()
		elif selection == 4:
			self.__controller.move_right()
		elif selection == 5:
			self.__controller.initialize_map()
		elif selection == 6:
			self.__active = False

	def main(self):
		while self.__active:
			self.__show_map()
			self.__show_selections()
			self.__input_selection()

