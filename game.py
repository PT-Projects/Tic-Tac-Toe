import tkinter as tk

class Game:

    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Tic-Tac-Toe")
        self.win.grid()
        self.setup()
        self.TURN = ["X","O"]

    def setup(self):
        location = []

        for x in range(3):
            temp = []
            for y in range(3):
                new = tk.Button(self.win)
                new.config(height=5, width=10, command=lambda button=new:self.update(button))
                new.grid(row=x, column=y)
                temp.append(new)
            location.append(temp)

    def update(self, button):
        button.config(text=self.TURN[0])
        print(button.winfo_name())
        self.TURN.reverse()

    def run(self):
        self.win.mainloop()