from tkinter import Frame, Canvas, Label, ALL, Tk


class main:

    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack(fill="both", expand=True)
        self.canvas = Canvas(self.frame, width=300, height=300)
        self.canvas.pack(fill="both", expand=True)
        self.label = Label(self.frame, text='Tic Tac Toe Game', height=6, bg='black', fg='red')
        self.label.pack(fill="both", expand=True)

        self._draw_board()
        self.setup()

    def setup(self):
        self.canvas.delete(ALL)
        self.label['text'] = ('Tic Tac Toe Game')
        self.canvas.bind("<ButtonPress-1>", self.check_click_event)
        self._draw_board()
        self.TTT = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.i = 0
        self.j = False

    def end(self):
        self.canvas.unbind("<ButtonPress-1>")
        self.j = True

    def _draw_board(self):
        self.canvas.create_rectangle(0, 0, 300, 300, outline="black")
        self.canvas.create_rectangle(100, 300, 200, 0, outline="black")
        self.canvas.create_rectangle(0, 100, 300, 200, outline="black")

    def _draw_circle(self, X, Y):
        self.canvas.create_oval(X + 25, Y + 25, X - 25, Y - 25, width=4, outline="black")

    def _draw_x(self, X, Y):
        self.canvas.create_line(X + 20, Y + 20, X - 20, Y - 20, width=4, fill="black")
        self.canvas.create_line(X - 20, Y + 20, X + 20, Y - 20, width=4, fill="black")

    def check_click_event(self, event):
        print(event)
        for k in range(0, 300, 100):
            for j in range(0, 300, 100):
                if event.x in range(k, k + 100) and event.y in range(j, j + 100):
                    if self.canvas.find_enclosed(k, j, k + 100, j + 100) == ():
                        if self.i % 2 == 0:
                            X = (2 * k + 100) / 2
                            Y = (2 * j + 100) / 2
                            X1 = int(k / 100)
                            Y1 = int(j / 100)
                            self._draw_circle(X, Y)
                            self.TTT[Y1][X1] += 1
                            self.i += 1
                        else:
                            X = (2 * k + 100) / 2
                            Y = (2 * j + 100) / 2
                            X1 = int(k / 100)
                            Y1 = int(j / 100)
                            self._draw_x(X, Y)
                            self.TTT[Y1][X1] += 9
                            self.i += 1
        self.check()

    def check(self):
        # horizontal check
        # vertical check
        # check for diagonal wins
        # check for draws
        return


root = Tk()
app = main(root)
root.mainloop()

if __name__ == '__main__':
    main.__init__()
