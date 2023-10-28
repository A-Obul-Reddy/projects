import tkinter as tk

window = tk.Tk()
window.title("Tic Tac Toe")
window.geometry("500x500")
window.resizable(False, False)
window.configure(background="#61646e")

grid = [[None, None, None], [None, None, None], [None, None, None]]

player = 1


def evaluate():
    global grid
    for i in grid:
        if None not in i:
            if (i[0] == i[1]) and (i[1] == i[2]):
                if i[0] == 1:
                    label_result.configure(text="player 1 won")
                    return
                else:
                    label_result.configure(text="player 2 won")
                    return

    for i in range(3):
        for j in range(3):
            if None not in (grid[0][i], grid[1][i], grid[2][i]):
                if (grid[0][i] == grid[1][i]) and (grid[1][i] == grid[2][i]):
                    if grid[0][i] == 1:
                        label_result.configure(text="player 1 won")
                        return
                    else:
                        label_result.configure(text="player 2 won")
                        return

    if (grid[0][0]) and (grid[0][0] == grid[1][1]) and (grid[1][1] == grid[2][2]):
        if grid[0][0] == 1:
            label_result.configure(text="player 1 won")
            return
        else:
            label_result.configure(text="player 2 won")
            return

    if (grid[0][2]) and (grid[0][2] == grid[1][1]) and (grid[1][1] == grid[2][0]):
        if grid[0][2] == 1:
            label_result.configure(text="player 1 won")
            return
        else:
            label_result.configure(text="player 2 won")
            return

    c = 0
    for i in grid:
        for j in i:
            if j is not None:
                c += 1
    if c == 9:
        label_result.configure(text="tie")


def enter(s: int):
    global player, grid
    m = (s - 1) % 3
    n = (s - 1) // 3
    if grid[n][m] is None:
        grid[n][m] = player
        if player == 1:
            eval(f"b{s}.configure(text='O')")
            eval('label_result.configure(text="player 2")')
        else:
            eval(f"b{s}.configure(text='x')")
            eval('label_result.configure(text="player 1")')
        evaluate()
        player = 2 if player == 1 else 1


def reset():
    global grid, player
    grid = [[None, None, None], [None, None, None], [None, None, None]]
    player = 1
    for i in range(1, 10):
        eval(f"b{i}.configure(text='')")
    label_result.configure(text="player 1")


label_result = tk.Label(window, text="player 1", font=("arial", 30, "bold"), bg='black', fg='white')
label_result.place(x=155, y=10)

b1 = tk.Button(window, text="", width=5, height=1, fg="#f73c3b", bg="#4aff94", activebackground="#f73c3b",
               activeforeground="#4aff94", font=("arial", 30, "bold"), command=lambda: enter(1))
b1.place(x=10, y=110)
b2 = tk.Button(window, text="", width=5, height=1, fg="#f73c3b", bg="#4aff94", activebackground="#f73c3b",
               activeforeground="#4aff94", font=("arial", 30, "bold"), command=lambda: enter(2))
b2.place(x=170, y=110)
b3 = tk.Button(window, text="", width=5, height=1, fg="#f73c3b", bg="#4aff94", activebackground="#f73c3b",
               activeforeground="#4aff94", font=("arial", 30, "bold"), command=lambda: enter(3))
b3.place(x=330, y=110)

b4 = tk.Button(window, text="", width=5, height=1, fg="#f73c3b", bg="#4aff94", activebackground="#f73c3b",
               activeforeground="#4aff94", font=("arial", 30, "bold"), command=lambda: enter(4))
b4.place(x=10, y=210)
b5 = tk.Button(window, text="", width=5, height=1, fg="#f73c3b", bg="#4aff94", activebackground="#f73c3b",
               activeforeground="#4aff94", font=("arial", 30, "bold"), command=lambda: enter(5))
b5.place(x=170, y=210)
b6 = tk.Button(window, text="", width=5, height=1, fg="#f73c3b", bg="#4aff94", activebackground="#f73c3b",
               activeforeground="#4aff94", font=("arial", 30, "bold"), command=lambda: enter(6))
b6.place(x=330, y=210)

b7 = tk.Button(window, text="", width=5, height=1, fg="#f73c3b", bg="#4aff94", activebackground="#f73c3b",
               activeforeground="#4aff94", font=("arial", 30, "bold"), command=lambda: enter(7))
b7.place(x=10, y=310)
b8 = tk.Button(window, text="", width=5, height=1, fg="#f73c3b", bg="#4aff94", activebackground="#f73c3b",
               activeforeground="#4aff94", font=("arial", 30, "bold"), command=lambda: enter(8))
b8.place(x=170, y=310)
b9 = tk.Button(window, text="", width=5, height=1, fg="#f73c3b", bg="#4aff94", activebackground="#f73c3b",
               activeforeground="#4aff94", font=("arial", 30, "bold"), command=lambda: enter(9))
b9.place(x=330, y=310)

tk.Button(window, text="reset", width=5, height=1, fg="white", bg="black", activebackground="white",
          activeforeground="black", font=("arial", 30, "bold"), command=lambda: reset()).place(x=180, y=410)

window.mainloop()
