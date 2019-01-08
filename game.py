import tkinter as tk
from tkinter.messagebox import showinfo

class Game:

    def __init__(self):
        self.TURN = ["X","O"]
        self.TIMER = [0,0]
        self.BOARD = []

        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.grid()

        self.timer = tk.Label(self.window, height=2, width=10)
        self.turn = tk.Label(self.window, height=2, width=10)
        self.update_timer()
        self.update_turn()

        self.setup()

    def setup(self):
        location = []

        self.timer.grid(row=0, column=1)
        self.turn.grid(row=0, column=3)

        for x in range(3):
            temp = []
            for y in range(3):
                new = tk.Button(self.window)
                new.config(height=5, width=10, bd=4, font='bold', command=lambda button=new:self.update_button(button))
                new.grid(row=x+1, column=y+1)
                temp.append(new)
            location.append(temp)

        for i in location:
            self.BOARD.append(i)

    def update_button(self, button):
        button.config(text=self.TURN[0])
        button.config(state='disabled')
        print(button.winfo_name())
        self.TURN.reverse()
        self.check_win()

    def update_timer(self):
        self.TIMER[1] += 1
        if self.TIMER[1] == 60:
            self.TIMER[0] += 1
            self.TIMER[1] = 0
        if self.TIMER[1] < 10:
            self.timer.config(text="Timer: " + str(self.TIMER[0]) + ":0" + str(self.TIMER[1]))
        else:
            self.timer.config(text="Timer: " + str(self.TIMER[0]) + ":" + str(self.TIMER[1]))
        self.window.after(1000, self.update_timer)

    def update_turn(self):
        self.turn.config(text="Turn: " + self.TURN[0])
        self.window.after(200, self.update_turn)

    def check_win(self):
        store = []
        for x in range(len(self.BOARD)):
            temp = []
            for y in range(len(self.BOARD[x])):
                text = self.BOARD[x][y].cget('text')
                temp.append(text)
            store.append(temp)
        for i in store:
            print(i)

        # Perpendicular Win #
        for i in store:
            if i[0] != '':
                if i[0] == i[1] == i[2]:
                    self.win(i[0])

        # Vertical Win #
        check = []
        for x in range(3):
            temp = []
            for i in store:
                temp.append(i[x])
            check.append(temp)
        for i in check:
            if i[0] != '':
                if i[0] == i[1] == i[2]:
                    self.win(i[0])

        # Diagonal Win #
        check = []
        temp = []
        for x in range(3):
            temp.append(store[x][x])
        check.append(temp)
        temp = [store[0][2], store[1][1], store[2][0]]
        check.append(temp)
        for i in check:
            if i[0] != '':
                if i[0] == i[1] == i[2]:
                    self.win(i[0])

        # Draw Win #
        draw = True
        for i in store:
            if '' in i:
                draw = False
        if draw:
            self.draw()

    def win(self, player):
        print(player + " wins")
        showinfo("WINNER", "Player: " + player + " Wins!")
        self.stop()

    def draw(self):
        print("draw")
        showinfo("DRAW", "Its a Draw!")
        self.stop()

    def run(self):
        self.window.mainloop()

    def stop(self):
        self.window.destroy()
        exit(0)