#/usr/bin/env python3

from tkinter import filedialog
import tkinter as tk
from tkinter import ttk,N,E,S,W

class Composer(ttk.Frame):
    """Gui and functions for composing music"""
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.pack()
        self.init_gui()

    def init_gui(self):
        """Builds GUI"""
        self.root.title("Beethoven music composer")

        self.header = ttk.Frame(self, padding="3 2 12 12", borderwidth=5)
        self.header.grid(column=0, row=0, columnspan=5, sticky=(N, W, E))
        self.header_text = ttk.Label(self.header, text="\nWelcome to the "
                "Beethoven music composer! Here you can create your own "
                "music and Beethoven will help you parse the notes in a "
                "way that Beep can understand")
        self.header_text.grid(columnspan=5, sticky=(N, W, E))

        self.create_compose_frame()
        self.create_file_frame()

    def create_compose_frame(self):
        """Builds the top of the compose frame, used for definining global
        attributes of the music"""
        self.compose_frame = ttk.Frame(self, padding="3 3 12 12", borderwidth=2)
        self.compose_frame.grid(column=0, row=1, sticky=(N, W, E, S))
        self.create_global_config()

        sep = ttk.Separator(self.compose_frame, orient=tk.HORIZONTAL)
        self.create_sheet_music()
        #sep.grid(column=0, row=2, columnspan=4, sticky=(W, E))


    def create_global_config(self):

        ttk.Label(self.compose_frame, text="Tempo:").grid(column=0, row=0,
                                                     sticky=(N, W))
        self.tempo = tk.StringVar()
        self.tempo_entry = ttk.Entry(self.compose_frame, width=4,
                                     textvariable=self.tempo)
        self.tempo_entry.grid(column=1, row=0, sticky=(N, W))

        self.key_picker = ttk.Frame(self.compose_frame, padding="3 3 12 12")
        self.key_picker.grid(column=2, row=0, sticky=(N, E))

        self.intonation = tk.StringVar()
        self.flat_pitch = ttk.Radiobutton(self.key_picker, text='b',
                            variable=self.intonation, value='flat')
        self.sharp_pitch = ttk.Radiobutton(self.key_picker, text='#',
                            variable=self.intonation, value='sharp')

        self.flat_pitch.grid(column=0, row=0, sticky=(N, E, S, W))
        self.sharp_pitch.grid(column=1, row=0, sticky=(N, E, S, W))

        self.note_picker_frame = ttk.Frame(self.compose_frame, padding="3 3 12 12")
        self.note_picker_frame.grid(column=3, row=0, sticky=(N, W))

        self.C_pitch = tk.BooleanVar()
        self.D_pitch = tk.BooleanVar()
        self.E_pitch = tk.BooleanVar()
        self.F_pitch = tk.BooleanVar()
        self.G_pitch = tk.BooleanVar()
        self.A_pitch = tk.BooleanVar()
        self.H_pitch = tk.BooleanVar()

        self.C_check = ttk.Checkbutton(self.note_picker_frame, text='C',
                            variable=self.C_pitch, onvalue=True, offvalue=False)
        self.C_check.grid(column=0, row=0, sticky=(N, W))

        self.D_check = ttk.Checkbutton(self.note_picker_frame, text='D',
                            variable=self.D_pitch, onvalue=True, offvalue=False)
        self.D_check.grid(column=1, row=0, sticky=(N, W))

        self.E_check = ttk.Checkbutton(self.note_picker_frame, text='E',
                            variable=self.E_pitch, onvalue=True, offvalue=False)
        self.E_check.grid(column=2, row=0, sticky=(N, W))

        self.F_check = ttk.Checkbutton(self.note_picker_frame, text='F',
                            variable=self.F_pitch, onvalue=True, offvalue=False)
        self.F_check.grid(column=3, row=0, sticky=(N, W))

        self.G_check = ttk.Checkbutton(self.note_picker_frame, text='G',
                            variable=self.G_pitch, onvalue=True, offvalue=False)
        self.G_check.grid(column=4, row=0, sticky=(N, W))

        self.A_check = ttk.Checkbutton(self.note_picker_frame, text='A',
                            variable=self.A_pitch, onvalue=True, offvalue=False)
        self.A_check.grid(column=5, row=0, sticky=(N, W))

        self.H_check = ttk.Checkbutton(self.note_picker_frame, text='H',
                            variable=self.A_pitch, onvalue=True, offvalue=False)
        self.H_check.grid(column=6, row=0, sticky=(N, W))


    def create_sheet_music(self):
        v = ttk.Scrollbar(self.compose_frame, orient=tk.VERTICAL)
        number_of_note_lines = 5
        self.music_sheet = tk.Canvas(self.compose_frame, height=700,
                                     yscrollcommand=v.set)
        v['command'] = self.music_sheet.yview
        self.music_sheet.grid(column=0, row=1, columnspan=4, sticky=(N, W, S, E))
        v.grid(column=4, row=1, sticky=(W,E))
        self.compose_frame.grid_columnconfigure(0, weight=1)
        self.compose_frame.grid_rowconfigure(0, weight=1)

        for note_line in range(number_of_note_lines):
            for line in range(5):
                y = (note_line + 1) * 60 + line*6
                self.music_sheet.create_line(10, y, 300, y)

        self.music_sheet.create_line(10, 40, 10, number_of_note_lines*60+24)

    def create_file_frame(self):

        self.file_frame = ttk.Frame(self, padding="3 3 12 12", borderwidth=2,
                                  relief='sunken')
        self.file_frame.grid(column=1, row=1, sticky=(N, W, E, S))

        self.preview_text = tk.StringVar()
        self.preview_text_field = tk.Text(self.file_frame, width=50, height=30,
                               state='disabled')
        self.preview_text_field.grid(column=0, row=0, columnspan=2, sticky=(N, W, E, S))

        #self.save_path = tk.StringVar()
        #self.save_path_field = tk.Entry(self.file_frame, textvariable=self.save_path,
        #                             width=40)
        #self.save_path_field.grid(column=0, row=1, columnspan=2, sticky=(N, W))

        ttk.Button(self.file_frame, text="Save",
                   command=self.save_file).grid(column=1, row=1)

    def save_file(self):
        file_name = filedialog.asksaveasfilename()
        print(file_name)
        if file_name:
            with open(file_name, 'w') as write_file:
                write_file.write(str(self.preview_text))




if __name__ == '__main__':
    root = tk.Tk()
    app = Composer(root)

    app.mainloop()
