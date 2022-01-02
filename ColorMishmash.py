from os.path import basename, splitext
import tkinter as tk
from tkinter import Scale, HORIZONTAL, Canvas, Frame, Entry, LEFT, S, END, StringVar

# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Foo"
    name = "ColorMishMash"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)

        self.bind("<Escape>", self.quit) #propojí klávesovou zkratku s nějakou funkcí (Esc spustí funkci quit())

        self.frameR = Frame(self)
        self.frameR.pack()
        self.frameG = Frame(self)
        self.frameG.pack()
        self.frameB = Frame(self)
        self.frameB.pack()

        self.labelR = tk.Label(self.frameR, text="R") #nápis co se tam zobrazuje (label)
        self.labelR.pack() #umístění napísu
        self.scaleR = Scale(self.frameR, from_ = 0, to = 255, orient = HORIZONTAL, length = 256, command = self.change)
        self.scaleR.pack()

        self.labelG = tk.Label(self.frameG, text="G")
        self.labelG.pack()
        self.scaleG = Scale(self.frameG, from_ = 0, to = 255, orient = HORIZONTAL, length = 256, command = self.change)
        self.scaleG.pack()

        self.labelB = tk.Label(self.frameB, text="B")
        self.labelB.pack()
        self.scaleB = Scale(self.frameB, from_ = 0, to = 255, orient = HORIZONTAL, length = 256, command = self.change)
        self.scaleB.pack()

        self.canvasMain = Canvas(self, width = 256, height = 100, background = "#000000")
        self.canvasMain.pack()


        self.btnQuit = tk.Button(self, text="Quit", command=self.quit)
        self.btnQuit.pack()


    def change(self, event):
        r = self.scaleR.get()
        g = self.scaleG.get()
        b = self.scaleB.get()
        self.canvasMain.config(background = f"#{r:02x}{g:02x}{b:02x}")

    def quit(self, event=None):
        super().quit()

app = Application()
app.mainloop()

 
 
