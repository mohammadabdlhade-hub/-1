class Calculator:
    """كلاس متقدم لتمثيل آلة حاسبة تدعم العمليات الأساسية."""
    
    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("خطأ: لا يمكن القسمة على الصفر!")
        return a / b

    def power(self, a: float, b: float) -> float:
        return a ** b


def get_number(prompt: str) -> float:
    """دالة مساعدة لضمان إدخال رقم صحيح من قبل المستخدم."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ إدخال غير صالح. الرجاء إدخال رقم حقيقي.")


def main():
    calc = Calculator()
    
    print("=" * 40)
    print("      مرحباً بك في الآلة الحاسبة الذكية      ")
    print("=" * 40)

    while True:
        print("\nالعمليات المتاحة:")
        print("1. جمع (+)")
        print("2. طرح (-)")
        print("3. ضرب (*)")
        print("4. قسمة (/)")
        print("5. أس (^) ")
        print("6. خروج")

        choice = input("\nاختر رقم العملية (1-6): ").strip()

        if choice == '6':
            print("شكراً لاستخدامك الآلة الحاسبة. إلى اللقاء!")
            break

        if choice in ('1', '2', '3', '4', '5'):
            num1 = get_number("أدخل الرقم الأول: ")
            num2 = get_number("أدخل الرقم الثاني: ")

            try:
                if choice == '1':
                    result = calc.add(num1, num2)
                    op = "+"
                elif choice == '2':
                    result = calc.subtract(num1, num2)
                    op = "-"
                elif choice == '3':
                    result = calc.multiply(num1, num2)
                    op = "*"
                elif choice == '4':
                    result = calc.divide(num1, num2)
                    op = "/"
                elif choice == '5':
                    result = calc.power(num1, num2)
                    op = "^"

                # طباعة النتيجة (إزالة الفاصلة العشرية إذا كان الرقم عدداً صحيحاً)
                if result.is_integer():
                    result = int(result)
                
                print(f"\n✨ النتيجة: {num1} {op} {num2} = {result}")

            except ValueError as e:
                print(f"\n⚠️ {e}")
        else:
            print("\n❌ خيار غير صحيح، الرجاء الاختيار من القائمة (1 إلى 6).")


if __name__ == "__main__":
    main()
