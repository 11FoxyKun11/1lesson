# def name(name):
#     print("Name:", name)
# name("Danylo")

# def mnozenia(num):
#     for i in range(1, 11):
#         print(num, "*", i, "=", num * i)
# mnozenia(5)

# def sums(num1,num2):
#     result = 0
#     for i in range(num1, num2 + 1):
#         result += i # result = result + i
#     print(result)
# sums(1, 18)

# def average(num1 = 0, num2 = 0, num3 = 0):
#     print(num1, num2,  num3)
# average()

# def info(name, surname, age, instragram = "No insta", phone_number):
#     print(name, surname, age, instragram, phone_number)
# info("Danylo", "hogihot", 24, 546234098)

# def sums(*args):
#     result = 0
#     for i in args:
#         result += i
#     print(result)
# sums(4, 3, 6, 3, 4, 6)

# def sums(*args):
#     result = 0
#     for i in args:
#         result += i
#     print(result / 5)
# sums(4, 4, 4, 4, 4)



# def info():
#     name = "Bogdan lube kakish"
#     print(name)
#     def main():
#         print(123)
#     main()
# info()

# print("hello", 5)
# name = "Danylo"
# print(f"hello {name}")

# name = "Danylo"
# surname = "JHNj"
# print(f"Hello {name} {surname}")

# a = 8
# b = 3
# print(f"{a} + {b} = {a + b}")
# print(f"{a} - {b} = {a - b}")
# print(f"{a} * {b} = {a * b}")
# print(f"{a} / {b} = {a / b}")

# name = "Danylo"
# surname = "JHNj"
# print("\tHello\" \n{} \n{}".format(name, surname))

# a = 0
# print(f"Number: {for i in}")



# import tkinter as tk
# window = tk.Tk()
# label1 = tk.Label(
#     text = "Hello world!",
#     fg = "Black",
#     bg = "Red",
#     width = 30
# )
# enter_name = tk.Entry(
#     width = 50,
#     fg = "green",
#     bg = "cyan"
# )
# name = enter_name.get()
# enter_desk = tk.Text()
#
# enter_desk.pack()
# label1.pack()
# enter_name.pack()
# window.mainloop()

# import tkinter as tk
# def print_hello():
#     print(f"Hello {enter_name.get()} {enter_surname.get()}!")
# window = tk.Tk()
# label2 = tk.Label(
#     text = "Enter name:",
#     fg = "Black",
#     bg = "white",
#     width = 50
# )
# enter_name = tk.Entry(
#     width = 50,
#     fg = "green",
#     bg = "cyan"
# )
# label3 = tk.Label(
#     text = "Enter surname:",
#     fg = "Black",
#     bg = "white",
#     width = 50
# )
# enter_surname = tk.Entry(
#     width = 50,
#     fg = "green",
#     bg = "cyan"
# )
# button_send = tk.Button(
#     text = "Send",
#     command = print_hello
# )
# name = enter_name.get()
# enter_desk = tk.Text()
#
# label2.pack()
# enter_name.pack()
# label3.pack()
# enter_surname.pack()
# button_send.pack()
# window.mainloop()



# import datetime
# date = datetime.datetime(2022, 9, 22)
# print(date)

# import datetime
# date = datetime.datetime.now()
# date = datetime.datetime.today()
# date = datetime.datetime.date.today()
# print(date)

# import datetime
# date = datetime.datetime.today()
# print(date)

# import datetime
# dete = datetime.datetime.now()
# weekday = date.weekday()
# weekday = date.isoweekday()
# print(weekday)

# import datetime
# date = datetime.datetime.today()
# date_format = date.strftime("%H:%M:%S")
# print(date_format)

# import datetime
# date_formate = datetime.datetime.now().strftime('%Y %B % %H:%M:%S')
# print(date_formate)

# import datetime
# x = int(input("Enter year: "))
# o = int(input("Enter month: "))
# y = int(input("Enter day: "))
# date = datetime.datetime(x, o, y)
# print(date.strftime("%B"))



# import re
# a = "Hello my Hello my Hello my World"
# reg = re.compile("my")
# result = reg.search(a)
# print(result)

# import re
# a = "Hello my Hello my Hello my World"
# reg = re.compile("my")
# result = reg.finditer(a)
# for i in result:
#     print(i)

# import re
# a = "Hello my Hello my Hello my World"
# reg = re.compile("my")
# result = reg.findall(a)
# print(result)

# import re
# a = "Hello my Hello my Hello my World"
# reg = re.compile("my")
# b = reg.sub("I", a, 1)
# print(b)

# import re
# a = "Hello my Hello my Hello my World"
# reg = re.compile("my")
# b = reg.split(a)
# print(b)

# import re
# a = input("Text: ")
# reg = re.compile("my")
# result = reg.finditer(a)
# for i in result:
#     print(i.span())

# import tkinter as tk
# import re
# a = input("Text: ")
# reg = re.compile("my")
# b = reg.split(a)
# print(b)



# from telegram.ext import Updater
# def main():
#     updater = Updater("5683718680:AAGoenlK1_AxLp3UyBFuOfZt7pc3DI8VJBg")
#     updater.start_polling()
#     updater.idle()
# main()



# cars = ["BMW", "Porche", "Audi", "Ford", "Toyota"]
# # print(cars[0])
# print(cars[len(cars)-1])

# cars = ["BMW", "Porche", "Audi", "Ford", "Toyota"]
# cars.append("Ferrari")
# cars.append("Subaru")
# print(cars[len(cars)-1])

# i = 0
# while i < 5:
#     print("Hello!")
#     i += 1 #i = i+1

# for i in 1, 2, 3, 4, 5:
#     print(i)

# for i in range(0, 13, 2):
#     print(i)

# numberes = []
# i = 1
# while i != 0:
#     i = int(input("Number: "))
#     if i == 0:
#         break
#     numberes.append(i)
# print(numberes)

# numberes = []
# i = 1
# while i != 0:
#     i = int(input("Number: "))
#     if i == 0:
#         break
#     numberes.append(i)
# print(numberes)
# print(sum(numberes))

# numberes = []
# i = 1
# m = 0
# while i != 0:
#     i = int(input("Number: "))
#     if i == 0:
#         break
#     if i > m:
#         m = i
#     numberes.append(i)
#
# print(numberes)
# print(m)



# import tkinter as tk
# import random
# random_true = [
#     'Скільки в тебе бабок?',
#     'Скільки ти см?',
#     'Багато заробляєш?',
#     'Прогулюєш?'
# ]
# random_dare = [
#     'Віджатися 10000000000000000000 раз',
#     'Попууууууууууууууууукати',
#     'Випий пляшку energy drink'
# ]
# def true():
#     print(random.choice(random_true))
# def dare():
#     print(random.choice(random_dare))
# window = tk.Tk()
# button_true = tk.Button(
#     text = 'Правда',
#     command = true,
#     width = 10,
#     height = 5
# )
# button_true.pack()
# button_dare = tk.Button(
#     text = 'Дія',
#     command = dare,
#     width = 10,
#     height = 5,
# )
# button_dare.pack()
# window.mainloop()



# from tkinter import *
# from decimal import *
# root = Tk()
# root.title('Calculator')
# buttons = (('7', '8', '9', '/', '4'),
#            ('4', '5', '6', '*', '4'),
#            ('1', '2', '3', '-', '4'),
#            ('0', '.', '=', '+', '4')
#            )
# activeStr = ''
# stack = []
# def calculate():
#     global stack
#     global label
#     result = 0
#     operand2 = Decimal(stack.pop())
#     operation = stack.pop()
#     operand1 = Decimal(stack.pop())
#     if operation == '+':
#         result = operand1 + operand2
#     if operation == '-':
#         result = operand1 - operand2
#     if operation == '/':
#         result = operand1 / operand2
#     if operation == '*':
#         result = operand1 * operand2
#     label.configure(text=str(result))
# def click(text):
#     global activeStr
#     global stack
#     if text == 'CE':
#         stack.clear()
#         activeStr = ''
#         label.configure(text='0')
#     elif '0' <= text <= '9':
#         activeStr += text
#         label.configure(text=activeStr)
#     elif text == '.':
#         if activeStr.find('.') == -1:
#             activeStr += text
#             label.configure(text=activeStr)
#     else:
#         if len(stack) >= 2:
#             stack.append(label['text'])
#             calculate()
#             stack.clear()
#             stack.append(label['text'])
#             activeStr = ''
#             if text != '=':
#                 stack.append(text)
#         else:
#             if text != '=':
#                 stack.append(label['text'])
#                 stack.append(text)
#                 activeStr = ''
#                 label.configure(text='0')
# label = Label(root, text='0', width=35)
# label.grid(row=0, column=0, columnspan=4, sticky="nsew")
# button = Button(root, text='CE',  command=lambda text='CE': click(text))
# button.grid(row=1, column=3, sticky="nsew")
# for row in range(4):
#     for col in range(4):
#         button = Button(root, text=buttons[row][col],
#               command = lambda row=row, col=col: click(buttons[row][col]))
#         button.grid(row=row + 2, column=col, sticky="nsew")
# root.grid_rowconfigure(6, weight=1)
# root.grid_columnconfigure(4, weight=1)
# root.mainloop()
































a= 5
print(a)