import tkinter as tk

def press(key):
    current = entry_var.get()
    entry_var.set(current + key)

def equal():
    try:
        expression = entry_var.get().replace('×', '*').replace('÷', '/')
        result = eval(expression)
        entry_var.set(str(result))
    except:
        entry_var.set("Error")


def clear():
    entry_var.set("")

root = tk.Tk()
root.title("Calculator")
root.geometry("330x450")
root.resizable(False, False)

entry_var = tk.StringVar()


entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 24), bd=10, insertwidth=2, width=14,
                 borderwidth=4, relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=20)

buttons = [
    ['7', '8', '9', '÷'],
    ['4', '5', '6', '×'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for i, row in enumerate(buttons):
    for j, button in enumerate(row):
        if button == '=':
            tk.Button(root, text=button, padx=30, pady=20, font=('Arial', 14),
                      bg="#007acc", fg="white", command=equal).grid(row=i+1, column=j, sticky="nsew")
        else:
            tk.Button(root, text=button, padx=30, pady=20, font=('Arial', 14),
                      command=lambda b=button: press(b)).grid(row=i+1, column=j, sticky="nsew")

tk.Button(root, text="C", padx=30, pady=20, font=('Arial', 14),
          bg="#ff5c5c", fg="white", command=clear).grid(row=5, column=0, columnspan=4, sticky="nsew")


for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
