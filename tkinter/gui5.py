import tkinter as tk
from tkinter import ttk

root = tk.Tk()
l = tk.Listbox(root, height=5)
l.grid(column=0, row=0, sticky=(tk.N,tk.W,tk.E,tk.S))
s = ttk.Scrollbar(root, orient=tk.VERTICAL, command=l.yview)
s.grid(column=1, row=0, sticky=(tk.N,tk.S))
l['yscrollcommand'] = s.set
ttk.Sizegrip().grid(column=1, row=1, sticky=(tk.S,tk.E))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
for i in range(1,101):
    l.insert('end', 'Line %d of 100' % i)
root.mainloop()
