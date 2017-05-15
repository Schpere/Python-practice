#/usr/bin/env python3

import tkinter as tk
from tkinter import ttk

class Adder(ttk.Frame):
    """GUI and functions for Adder"""
    def calculate(self, *args):
        try:
            valueA = float(a.get())
            valueB = float(b.get())
            sum_value.set(valueA + valueB)
        except:
            pass

    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.pack()
        self.init_gui()

    def init_gui(self):
        """Builds GUI"""
        self.root.title('Number Adder')
        header = ttk.Label(self, text="Let's add two numbers!", padding =
                          5)
        header.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        header.pack()
        a = tk.StringVar()
        b = tk.StringVar()
        sum_value = tk.StringVar()

        a_entry = ttk.Entry(self, width=7, textvariable=a)
        a_entry.grid(column=1, row=2, sticky=tk.W)
        plus = ttk.Label(self, text="+")
        plus.grid(column=2, row=2, sticky=(tk.W, tk.E))
        b_entry = ttk.Entry(self, width=7, textvariable=b)
        b_entry.grid(column=3, row=2, sticky=tk.E)

        sum_text = ttk.Label(self, textvariable=sum_value)
        sum_text.grid(column=2, row=3, sticky=(tk.W, tk.E))
        a_entry.pack()
        b_entry.pack()
        sum_text.pack()
        plus.pack()


if __name__ == '__main__':
    root = tk.Tk()
    Adder(root)
    root.mainloop()
