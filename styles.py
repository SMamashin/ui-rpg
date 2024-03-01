from tkinter import *
from tkinter import ttk

def setup_button_styles():
    style = ttk.Style()
    style.configure('TButton', font=('Arial', 18), borderwidth='8')
    style.map('TButton',
              foreground=[('pressed', 'orange'), ('active', 'pink')],
              background=[('pressed', '!disabled', 'black'), ('active', 'pink')]
             )