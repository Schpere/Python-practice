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
        #header.pack()
        a = tk.StringVar()
        b = tk.StringVar()
        sum_value = tk.StringVar()

        a_entry = ttk.Entry(self, width=7, textvariable=a)
        plus = ttk.Label(self, text="+")
        b_entry = ttk.Entry(self, width=7, textvariable=b)

        sum_text = ttk.Label(self, textvariable=sum_value)
        equals = ttk.Label(self, text="=")
        #a_entry.pack()
        #b_entry.pack()
        #sum_text.pack()
        #plus.pack()
        header.grid(column=0, row=0, columnspan=4, sticky=(tk.N, tk.W, tk.E, tk.S))
        b_entry.grid(column=3, row=1, sticky=tk.E)
        plus.grid(column=2, row=1, sticky=(tk.W, tk.E))
        a_entry.grid(column=1, row=1, sticky=tk.W)
        equals.grid(column=2, row=2, pady=5, sticky=(tk.W, tk.E))
        sum_text.grid(column=3, row=2, sticky=(tk.W, tk.E))


if __name__ == '__main__':
    root = tk.Tk()
    Adder(root)
    root.mainloop()
