import tkinter as tk

class Game:

    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Tic-Tac-Toe")
        self.win.grid()
        self.timer = tk.Label(self.win, height=2, width=10)
        self.setup()
        self.TURN = ["X","O"]
        self.TIMER = [0,0]
        self.update_timer()

    def setup(self):
        location = []

        self.timer.grid(row=0, column=1)

        for x in range(3):
            temp = []
            for y in range(3):
                new = tk.Button(self.win)
                new.config(height=5, width=10, command=lambda button=new:self.update_button(button))
                new.grid(row=x+1, column=y+1)
                temp.append(new)
            location.append(temp)

    def update_button(self, button):
        button.config(text=self.TURN[0])
        print(button.winfo_name())
        self.TURN.reverse()

    def update_timer(self):
        self.TIMER[1] += 1
        if self.TIMER[1] == 60:
            self.TIMER[0] += 1
            self.TIMER[1] = 0
        if self.TIMER[1] < 10:
            self.timer.config(text="Timer: " + str(self.TIMER[0]) + ":0" + str(self.TIMER[1]))
        else:
            self.timer.config(text="Timer: " + str(self.TIMER[0]) + ":" + str(self.TIMER[1]))
        self.win.after(1000, self.update_timer)

    def run(self):
        self.win.mainloop()