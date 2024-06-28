import tkinter as tk
from tkinter import messagebox

class mygui:
    def __init__(self):

        self.root = tk.Tk()
        self.label=tk.Label(self.root,text="msg pls", font=("arial",20))
        self.label.pack(padx=10,pady=10)
        self.textbox=tk.Text(self.root,height=5, font=("arial",15))
        self.textbox.bind("<KeyPress>", self.shortcut)

        self.textbox.pack(padx=10,pady=10)


        self.check_state=tk.IntVar()

        self.check= tk.Checkbutton(self.root,text="msg pls", font=("arial",15),variable=self.check_state)
        self.check.pack(padx=10,pady=10)

        self.btn=tk.Button(self.root,text="msg pls", font=("arial",20),command = self.show_msg)#not passing as a funtion but as an obj
        self.btn.pack(padx=10,pady=10)

        self.root.mainloop()
    def show_msg(self):
        if (self.check_state.get()) == 0:
            print(self.textbox.get("1.0",tk.END))
        else:
            messagebox.showinfo(title="msg",message=self.textbox.get("1.0",tk.END))

    def shortcut(self,event):
        if event.state==12 and event.keysym=="Return":
            self.show_msg()

mygui()

