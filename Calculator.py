import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("آلة حاسبة للهاتف")
        self.root.geometry("320x480")
        self.root.minsize(280, 400)
        self.root.configure(bg="#1e1e1e")

        self.expression = ""

        # شاشة العرض
        self.display_var = tk.StringVar(value="0")
        
        display_frame = tk.Frame(root, bg="#1e1e1e")
        display_frame.pack(fill="x", padx=10, pady=10)

        self.display = tk.Label(
            display_frame,
            textvariable=self.display_var,
            font=("Arial", 28, "bold"),
            bg="#2d2d2d",
            fg="#ffffff",
            anchor="e",
            padx=15
        )
        self.display.pack(fill="both", ipady=15)

        # إطار الأزرار
        buttons_frame = tk.Frame(root, bg="#1e1e1e")
        buttons_frame.pack(expand=True, fill="both", padx=10, pady=5)

        buttons = [
            ["C", "⌫", "(", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="]
        ]

        # الألوان
        btn_bg = "#333333"
        op_bg = "#ff9500"
        clear_bg = "#d32f2f"
        back_bg = "#555555"
        text_color = "white"

        for row_idx, row in enumerate(buttons):
            for col_idx, btn_text in enumerate(row):
                if btn_text in ["/", "*", "-", "+", "="]:
                    bg = op_bg
                elif btn_text == "C":
                    bg = clear_bg
                elif btn_text == "⌫":
                    bg = back_bg
                else:
                    bg = btn_bg

                btn = tk.Button(
                    buttons_frame,
                    text=btn_text,
                    font=("Arial", 16, "bold"),
                    bg=bg,
                    fg=text_color,
                    activebackground="#666666",
                    activeforeground="white",
                    bd=0,
                    relief="flat",
                    command=lambda t=btn_text: self.on_button_click(t)
                )
                
                # توزيع متناسق وصحيح 100% للأزرار (خصوصاً الصف الأخير: 0، والنقطة، ويسوي)
                if row_idx == 4:
                    if btn_text == "0":
                        btn.grid(row=row_idx, column=0, columnspan=2, sticky="nsew", padx=3, pady=3)
                    elif btn_text == ".":
                        btn.grid(row=row_idx, column=2, sticky="nsew", padx=3, pady=3)
                    elif btn_text == "=":
                        btn.grid(row=row_idx, column=3, sticky="nsew", padx=3, pady=3)
                else:
                    btn.grid(row=row_idx, column=col_idx, sticky="nsew", padx=3, pady=3)

        # ضبط تمدد الصفوف والأعمدة بالتساوي لتناسب شاشة الموبايل
        for i in range(5):
            buttons_frame.rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.columnconfigure(i, weight=1)

    def on_button_click(self, char):
        current_display = self.display_var.get()
        
        if char == "C":
            self.expression = ""
            self.display_var.set("0")
        elif char == "⌫":
            if current_display in ["خطأ", "خطأ: القسمة على صفر"]:
                self.expression = ""
                self.display_var.set("0")
            elif len(self.expression) > 1:
                self.expression = self.expression[:-1]
                self.display_var.set(self.expression)
            else:
                self.expression = ""
                self.display_var.set("0")
        elif char == "=":
            try:
                result = str(eval(self.expression))
                if result.endswith(".0"):
                    result = result[:-2]
                self.display_var.set(result)
                self.expression = result
            except ZeroDivisionError:
                self.display_var.set("خطأ: القسمة على صفر")
                self.expression = ""
            except Exception:
                self.display_var.set("خطأ")
                self.expression = ""
        else:
            if current_display in ["0", "خطأ", "خطأ: القسمة على صفر"]:
                self.expression = ""
            
            self.expression += char
            self.display_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
