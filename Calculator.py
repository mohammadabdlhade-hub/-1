import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("آلة حاسبة")
        self.root.geometry("320x460")
        self.root.resizable(False, False)
        self.root.configure(bg="#212121")

        self.expression = ""

        # شاشة العرض
        self.display_var = tk.StringVar(value="0")
        
        display_frame = tk.Frame(root, bg="#212121")
        display_frame.pack(expand=True, fill="both", padx=10, pady=10)

        self.display = tk.Label(
            display_frame,
            textvariable=self.display_var,
            font=("Arial", 28, "bold"),
            bg="#333333",
            fg="white",
            anchor="e",
            padx=15,
            relief="flat"
        )
        self.display.pack(expand=True, fill="both", ipady=15)

        # إطار الأزرار (تم إضافة زر ⌫ الحذف التدريجي بجانب C)
        buttons_frame = tk.Frame(root, bg="#212121")
        buttons_frame.pack(expand=True, fill="both", padx=10, pady=5)

        buttons = [
            ["C", "⌫", "(", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="]
        ]

        # تخصيص الألوان
        btn_bg = "#424242"
        op_bg = "#ff9800"
        clear_bg = "#f44336"
        back_bg = "#d32f2f" # لون مميز لزر المسح الفردي
        text_color = "white"

        for row_idx, row in enumerate(buttons):
            for col_idx, btn_text in enumerate(row):
                # اختيار لون الزر حسب نوعه
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
                    font=("Arial", 18, "bold"),
                    bg=bg,
                    fg=text_color,
                    activebackground="#616161",
                    activeforeground="white",
                    bd=0,
                    relief="flat",
                    command=lambda t=btn_text: self.on_button_click(t)
                )
                
                # استخدام Grid لترتيب الأزرار مع مراعاة تخطيط الصف الأول
                if btn_text == "0":
                    btn.grid(row=row_idx, column=col_idx, columnspan=2, sticky="nsew", padx=3, pady=3)
                elif btn_text == ".":
                    btn.grid(row=row_idx, column=col_idx + 1, sticky="nsew", padx=3, pady=3)
                elif btn_text == "=":
                    btn.grid(row=row_idx, column=col_idx + 1, sticky="nsew", padx=3, pady=3)
                else:
                    btn.grid(row=row_idx, column=col_idx, sticky="nsew", padx=3, pady=3)

        # ضبط أبعاد الصفوف والأعمدة لتدعم التمدد المتساوي
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
            # زر مسح رقم واحد (Backspace)
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
