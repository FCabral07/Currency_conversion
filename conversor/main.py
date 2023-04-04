import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
import requests

def convert():
    # Get the latest exchange rate
    real_input = entry_value.get()
    response = requests.get('https://economia.awesomeapi.com.br/json/last/BRL-USD')
    exchange_rate = response.json()['BRLUSD']['bid']
    dollars_output = "{:.2f}".format(real_input / float(exchange_rate))
    output_string.set(dollars_output)

# Creating a new window
window = ttk.Window(themename = 'solar')
window.title('Currency converter')

# heightxwidth
window.geometry('450x200')

# title
title_label = ttk.Label(master = window, text = 'American Dollars (USD) to Brazilian Real (BRL)', font = 'Fredoka 17')
title_label.pack()

# input
input_frame = ttk.Frame(master = window)
entry_value = tk.DoubleVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_value)
entry.pack(side = 'left', padx = 10)
button = ttk.Button(master = input_frame, text = 'Convert', command = convert)
button.pack(side = 'left')
input_frame.pack(pady = 15)

# Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, 
                         text = 'Value: ', 
                         font = 'Fredoka 15', 
                         textvariable = output_string)
output_label.pack(pady = 5)

# run
window.mainloop()