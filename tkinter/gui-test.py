#!/usr/bin/env python3
import tkinter as tk

class App(tk.Frame):

    def __init__(self, master=None):

        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self, text="Hello World\n(click me)",
                                  command=self.say_hi)
        #self.hi_there['text'] = "Hello World\n(click me)"
        #self.hi_there['command'] = self.say_hi
        self.hi_there.pack(side='top', expand=0)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side='bottom')

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = App(master=root)

app.master.title("Awesome program!")
app.master.maxsize(1000, 400)

app.mainloop()
