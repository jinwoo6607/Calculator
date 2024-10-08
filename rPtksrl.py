import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Elegant Calculator")
        master.geometry("400x600")
        master.configure(bg="#1D3557")  # 짙은 네이비 배경색

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        # 입력창
        self.display = tk.Entry(master, textvariable=self.result_var, font=("Helvetica", 36), bd=0, justify='right', bg="#F1FAEE", fg="#333")
        self.display.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            '√', 'x²', 'C', '←'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            button_color = "#A8DADC"  # 기본 숫자 버튼 색상 (연한 파란색)
            if button in {'/', '*', '-', '+'}:
                button_color = "#F1C40F"  # 연산자 색상 (연한 주황색)

            btn = tk.Button(self.master, text=button, padx=20, pady=20, font=("Helvetica", 24),
                            command=lambda b=button: self.on_button_click(b),
                            bg=button_color, fg="#333", borderwidth=0,
                            activebackground="#457B9D", highlightthickness=0)
            btn.grid(row=row_val, column=col_val, padx=10, pady=10, sticky="nsew")

            # 버튼의 마우스 오버 색상 효과
            btn.bind("<Enter>", lambda e: e.widget.config(bg="#457B9D"))
            btn.bind("<Leave>", lambda e, color=button_color: e.widget.config(bg=color))

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # 그리드 열 및 행 크기 조정
        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.master.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == '=':
            try:
                expression = self.result_var.get()
                result = eval(expression)
                self.result_var.set(result)
            except Exception:
                messagebox.showerror("Error", "Invalid Expression")
                self.result_var.set("0")
        elif char == 'C':
            self.result_var.set("0")
        elif char == '←':
            current = self.result_var.get()
            if len(current) > 1:
                self.result_var.set(current[:-1])
            else:
                self.result_var.set("0")
        elif char == '√':
            try:
                current = float(self.result_var.get())
                self.result_var.set(current ** 0.5)
            except ValueError:
                messagebox.showerror("Error", "Invalid Input")
                self.result_var.set("0")
        elif char == 'x²':
            try:
                current = float(self.result_var.get())
                self.result_var.set(current ** 2)
            except ValueError:
                messagebox.showerror("Error", "Invalid Input")
                self.result_var.set("0")
        else:
            current = self.result_var.get()
            if current == "0":
                self.result_var.set(char)
            else:
                self.result_var.set(current + char)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
