from typing import List
from model import EmployeeModel


class EmployeeController():
	def __init__(self):
		self.__employee_list = []  # type: List[EmployeeModel]
		self.__eid = 1000

	@property
	def employee_list(self):
		return self.__employee_list

	def add_employee(self, employee):
		if isinstance(employee, EmployeeModel):
			employee.eid = self.__eid
			self.__eid += 1
			self.__employee_list.append(employee)

	def remove_employee(self, eid):
		for i in range(len(self.__employee_list)):
			if self.__employee_list[i].eid == eid:
				del self.__employee_list[i]
				return True
		return False

	def modify_employee(self, employee):
		for item in self.__employee_list:
			if item.eid == employee.eid:
				item.__dict__ = employee.__dict__
				return True
		return False