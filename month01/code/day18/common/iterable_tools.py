class IterableHelper():
    @staticmethod
    def find_all(iterable, func_condition):
        """
            在可迭代对象中寻找所有符合条件的元素
        :param iterable: 可迭代对象
        :param func_condition: 条件
        :return: 生成器
        """
        for item in iterable:
            if func_condition(item):
                yield item

    @staticmethod
    def find_single(iterable, func_condition):
        """
            在可迭代对象中根据条件寻找一个元素
        :param iterable: 可迭代对象
        :param func_condition: 寻找条件
        :return: 元素
        """
        for item in iterable:
            if func_condition(item):
                return item

    @staticmethod
    def select(iterable, func_handle):
        """
            在可迭代对象中, 根据某些逻辑查询元素的成员
        :param iterable: 可迭代对象
        :param func_handle: 逻辑
        :return: 生成器
        """
        for item in iterable:
            yield func_handle(item)

    @staticmethod
    def get_count(iterable, func_condition):
        count = 0
        for item in iterable:
            if func_condition(item):
                count += 1
        return count

    @staticmethod
    def del_all(iterable, func_condition):
        """
            根据条件删除可迭代对象中多个元素
        :param iterable: 可迭代对象
        :param func_condition: 条件
        :return: 无
        """
        # for i in range(len(iterable) - 1, -1, -1):
        for i in range(-len(iterable), 0):
            if func_condition(iterable[i]):
                del iterable[i]

    @staticmethod
    def get_max(iterable, func_condition):
        max_emp = iterable[0]
        for i in range(1, len(iterable)):
            if func_condition(max_emp) < func_condition(iterable[i]):
                max_emp = iterable[i]
        return max_emp

    @staticmethod
    def ascending_order(iterable, func_condition):
        for i in range(len(iterable) - 1):
            for j in range(i + 1, len(iterable)):
                if func_condition(iterable[i]) > func_condition(iterable[j]):
                    iterable[i], iterable[j] = iterable[j], iterable[i]