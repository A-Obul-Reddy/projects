import tkinter as tk
import random

window = tk.Tk()
window.title("Password Generator")
window.geometry("400x300")
window.configure(bg="grey")
window.resizable(False, False)


def reset():
    label.configure(text="Enter the length of password")
    entry.configure(state="normal")
    entry.delete(0, tk.END)
    b.configure(text="Generate",width=10, command=lambda: generate_password())


def generate_password():
    n = entry.get()
    if n.isnumeric():
        n = int(n)
        alpha_upper = [chr(i) for i in range(65, 91)]
        alpha_lower = [chr(i) for i in range(97, 123)]
        digits = [str(i) for i in range(0, 10)]
        special_char = ["@", "#", "$", "%", "&", "~", "`", "^", "*", "(", ")", "-", "_", "=", "+", "?", "/", "<", ",",
                        ".",
                        ">", "{", "}", "[", "]", "\\", "|"]
        if (n >= 4) and (n < 24):
            password = []
            password.append(random.choice(alpha_upper))
            password.append(random.choice(alpha_lower))
            password.append(random.choice(digits))
            password.append(random.choice(special_char))
            if (n - 4) > 0:
                password.extend(random.choices(alpha_upper + alpha_lower + digits + special_char, k=(n - 4)))
            random.shuffle(password)
            label.configure(text="Your password is ")
            entry.delete(0, tk.END)
            entry.insert(0, "".join(password))
            entry.configure(state="disabled")
            b.configure(text="New password", width=16, command=lambda: reset())

        else:
            label.configure(text="Enter a number > 3 and < 24")
            entry.delete(0, tk.END)

    else:
        label.configure(text="Enter only number")
        entry.delete(0, tk.END)


label = tk.Label(window, text="Enter the length of password", font=("arial", 18, "bold"), bg="black",
                 fg="green")
label.pack(fill="x", padx=20, pady=20, ipadx=10, ipady=10)

entry = tk.Entry(window, width=24, font=("arial", 18, "bold"))
entry.pack(pady=20)

b = tk.Button(window, text="Generate", width=10, height=1, bg="grey", fg="green", activebackground="grey",
              font=("arial", 18, "bold"), activeforeground="red", command=lambda: generate_password())
b.pack(pady=20)
window.mainloop()
