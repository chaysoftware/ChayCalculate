# Импорт ТК
from tkinter import *
import tkinter as tk

# Создаю окно
root = Tk()
root.geometry('240x300')
root.config(bg='#242424')
root.title('EARLCALC')
root.resizable(width=False, height=False)


# Создаю поле для ввода
entryCalc = tk.Entry(root, bd=0, justify=tk.RIGHT, font=('Arial', 14))
entryCalc.grid(row=0, column=0, columnspan=4, stick='we', padx=5)

# Получение цифр
def sym(num):
    value = entryCalc.get() + str(num)
    entryCalc.delete(0, tk.END)
    entryCalc.insert(0, value )

# Получение операций
def oper(operation):
    value = entryCalc.get() + str(operation)
    entryCalc.delete(0, tk.END)
    entryCalc.insert(0, value)

# Решение
def calculate():
    value = entryCalc.get()
    if value[-1] in '+-*/':
        operation = value[-1]
        value = value[:-1]+operation+value[:-1]
    entryCalc.delete(0, tk.END)
    entryCalc.insert(0, eval(value))

# Чистка
def clear():
    entryCalc.delete(0, tk.END)

# Ссылка на sym
def make_number(num):
    return Button(root, text=num, bd=0, command=lambda : sym(num), font=('Arial', 14))

# Ссылка на oper
def make_operation(operation):
    return Button(root, text=operation, bd=0, command=lambda : sym(operation), font=('Arial', 14))

# Ссылка на calculate
def make_res(operation):
    return Button(root, text=operation, bd=0, command=calculate)

# Ссылка на clear
def make_clear(operation):
    return Button(root, text=operation, bd=0, command=clear)

# Выложить на экран цифровой блок
make_number('1').grid(row=1, column=0, stick="wens", padx=5, pady=5)
make_number('2').grid(row=1, column=1, stick="wens", padx=5, pady=5)
make_number('3').grid(row=1, column=2, stick="wens", padx=5, pady=5)
make_number('4').grid(row=2, column=0, stick="wens", padx=5, pady=5)
make_number('5').grid(row=2, column=1, stick="wens", padx=5, pady=5)
make_number('6').grid(row=2, column=2, stick="wens", padx=5, pady=5)
make_number('7').grid(row=3, column=0, stick="wens", padx=5, pady=5)
make_number('8').grid(row=3, column=1, stick="wens", padx=5, pady=5)
make_number('9').grid(row=3, column=2, stick="wens", padx=5, pady=5)
make_number('0').grid(row=4, column=0, stick="wens", padx=5, pady=5)

# Выложить на экран блок с операциями
make_operation('+').grid(row=1, column=3, stick="wens", padx=5, pady=5)
make_operation('-').grid(row=2, column=3, stick="wens", padx=5, pady=5)
make_operation('*').grid(row=3, column=3, stick="wens", padx=5, pady=5)
make_operation('/').grid(row=4, column=3, stick="wens", padx=5, pady=5)

# Выложить на экран блок с чисткой и решением
make_res('=').grid(row=4, column=2, stick="wens", padx=5, pady=5)
make_clear('c').grid(row=4, column=1, stick="wens", padx=5, pady=5)

# Оптимизация блока
root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)
root.grid_columnconfigure(3, minsize=60)
root.grid_rowconfigure(0, minsize=60)
root.grid_rowconfigure(1, minsize=60)
root.grid_rowconfigure(2, minsize=60)
root.grid_rowconfigure(3, minsize=60)

# Основной цикл
root.mainloop()
