from tkinter import *
from colorama import Fore

root = Tk()

def hello(event):
    print(Fore.LIGHTGREEN_EX, 'Got Tag EVENT!')

text = Text()
text.config(font=('courier', 15, 'bold'))
text.config(width=20, height=12,background='grey')
text.pack(expand=YES, fill=BOTH)
text.insert(END, 'This is\n\nthe meaning\n\nof life.\n\n')

btn = Button(text, text='Check',background='blue', command=lambda: hello(0))
btn.pack()
text.window_create(END, window=btn)
text.insert(END, '\n\n')
img = PhotoImage(file='../pythonProject/hellopython.GIF')
text.image_create(END, image=img)

text.tag_add('demo', '1.5', '1.7')
text.tag_add('demo', '3.0', '3.3')
text.tag_add('demo', '5.3', '5.7')
text.tag_config('demo',background='yellow')
text.tag_config('demo', font=('times', 17, 'underline'))
text.tag_bind('demo', '<Double-1>', hello)
root.mainloop()