"""
    创建函数,在终端中打印矩形
"""
def print_rect(int_number, fill_char, content_char):
    for i in range(int_number):
        print(f"{fill_char}{content_char * (int_number - 2)}{fill_char}" if i in range(1, int_number - 1)
              else f"{fill_char * int_number}")

print_rect(5, 'X', 'D')