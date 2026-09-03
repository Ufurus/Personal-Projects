""""
This is where all buttons are created and mapped, and rendered
on the screen.
"""

from calculations import render_result
from canvas import app

import tkinter as tk


def render_number_button_screen():

    button_1 = tk.Button(app, text='1', command=render_result("1"))
    button_1.place(x=0, y=200, width=60, height=70)
    button_2 = tk.Button(app, text='2')
    button_2.place(x=60, y=200, width=60, height=70)
    button_3 = tk.Button(app, text='3')
    button_3.place(x=120, y=200, width=60, height=70)
    button_4 = tk.Button(app, text='4')
    button_4.place(x=180, y=200, width=60, height=70)
    button_5 = tk.Button(app, text='5')
    button_5.place(x=240, y=200, width=60, height=70)
    button_6 = tk.Button(app, text='6')
    button_6.place(x=300, y=200, width=60, height=70)
    button_7 = tk.Button(app, text='7')
    button_7.place(x=0, y=270, width=60, height=70)
    button_8 = tk.Button(app, text='8')
    button_8.place(x=60, y=270, width=60, height=70)
    button_9 = tk.Button(app, text='9')
    button_9.place(x=120, y=270, width=60, height=70)

def render_operations_buttons():

    plus_sign_button = tk.Button(app, text='+')
    plus_sign_button.place(x=180, y=270, width=60, height=70)
    minus_sign_button = tk.Button(app, text='-')
    minus_sign_button.place(x=240, y=270, width=60, height=70)
    division_button = tk.Button(app, text='/')
    division_button.place(x=300, y=270, width=60, height=70)
    multiplication_button = tk.Button(app, text='X')
    multiplication_button.place(x=0, y=340, width=60, height=70)
    division_module_button = tk.Button(app, text='%')
    division_module_button.place(x=60, y=340, width=60, height=70)
    integer_divison_button = tk.Button(app, text='//')
    integer_divison_button.place(x=120, y=340, width=60, height=70)
    square_root_button = tk.Button(app, text='*')
    square_root_button.place(x=180, y=340, width=60, height=70)
    result_button = tk.Button(app, text='=')
    result_button.place(x=240, y=340, width=60, height=70)

def render_deleting_buttons():

    delete_button = tk.Button(app, text='CE')
    delete_button.place(x=300, y=340, width=60, height=70)
