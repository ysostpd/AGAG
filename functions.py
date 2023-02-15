import tkinter
import tkinter as tk
import customtkinter


def rututut():

    def __init__(self):
        self.root2 = tk.Tk()
        self.root2.title("kathAwit 2.0")
        self.root2.resizable(False, False)
        self.root2.geometry("400x400")
        self.root2.iconbitmap('resources/jukebox.ico')
        self.root2.config(bg="#3c3f41")

        self.root2.fr_tops = tkinter.Frame(bg="#3c3f41")
        self.root2.fr_tops.pack()

        self.root2.lbl_HMMm = customtkinter.CTkLabel(self.root2.fr_tops, text="via Hidden Markov Model\n (v. 1.0)",
                                                  text_font=("Roboto Light", -12),
                                                  text_color="white")  # font name and size in px
        self.root2.lbl_HMMm.grid(row=1, column=0, padx=10)

        self.root2.mainloop()

def testingan(a):
    a+=75
    return a