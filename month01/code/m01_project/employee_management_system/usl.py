from bll import EmployeeController
from model import EmployeeModel


class EmployeeView():
	def __init__(self):
		self.__contorller = EmployeeController()
		self.__active = True

	def __display_selections(self):
		print("1.添加员工信息")
		print("2.查看员工信息")
		print("3.删除员工信息")
		print("4.修改员工信息")
		print("5.退出")

	def __input_selection(self):
		selection = input("请输入选项:")
		if selection == "1":
			self.__add_employee_info()
		elif selection == "2":
			self.__show_employee_info()
		elif selection == "3":
			self.__del_employee_info()
		elif selection == "4":
			self.__modify_employee_info()
		elif selection == "5":
			self.__active = False

	def __get_number(self, message) -> int:
		while True:
			try:
				number = int(input(message))
				return number
			except ValueError:
				print("输入错误")

	def __add_employee_info(self):
		employee = EmployeeModel()
		employee.name = input("请输入员工姓名:")
		employee.salary = self.__get_number("请输入员工薪水:")
		employee.did = self.__get_number("请输入员工部门编号:")
		self.__contorller.add_employee(employee)

	def __show_employee_info(self):
		for employee in self.__contorller.employee_list:
			print("%s员工编号%d, 部门编号%d, 工资%d" %
				(employee.name, employee.eid, employee.did, employee.salary))

	def __del_employee_info(self):
		eid = self.__get_number("请输入要删除的员工编号:")
		if self.__contorller.remove_employee(eid):
			print("删除成功")
		else:
			print("删除失败")

	def __modify_employee_info(self):
		employee = EmployeeModel()
		employee.eid = self.__get_number("请输入要修改信息的员工编号:")
		employee.name = input("请输入员工新的姓名:")
		employee.did = self.__get_number("请输入员工新的部门编号:")
		employee.salary = self.__get_number("请输入员工新的工资:")
		if self.__contorller.modify_employee(employee):
			print("修改成功")
		else:
			print("修改失败")

	def main(self):
		while self.__active:
			self.__display_selections()
			self.__input_selection()