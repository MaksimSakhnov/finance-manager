import tkinter as tk
from PIL import Image as PilImage
from PIL import ImageTk
from add_window import add_window

# класс окно
class APP:
    #
    def __init__(self):
        self.root = tk.Tk()
        # установка названия приложения
        self.root.title("Домашняя бухгалтерия")
        # вычисляем высоту, ширину экрана
        monitor_height = self.root.winfo_screenheight()
        monitor_width = self.root.winfo_screenwidth()
        # следующая строка выводит окно размером 500 на 600 по середине экрана
        self.root.geometry(f"500x600+{int((monitor_width - 500) / 2)}+{int((monitor_height - 600) / 2)}")
        # ставим запрет на изменение размеров
        self.root.resizable(False, False)
        # устанавливаем иконку
        self.root.iconbitmap('./src/programm-icon.ico')

        # настройка изображений
        home_img = PilImage.open("./src/home.png")
        home_img = home_img.resize((30, 30), PilImage.ANTIALIAS)
        self.home_img = ImageTk.PhotoImage(home_img)

        operations_img = PilImage.open("./src/operations.png")
        operations_img = operations_img.resize((30, 30), PilImage.ANTIALIAS)
        self.operations_img = ImageTk.PhotoImage(operations_img)

        analytics_img = PilImage.open("./src/analitics.png")
        analytics_img = analytics_img.resize((30, 30), PilImage.ANTIALIAS)
        self.analytics_img = ImageTk.PhotoImage(analytics_img)

        add_img = PilImage.open("./src/add.png")
        add_img = add_img.resize((30, 30), PilImage.ANTIALIAS)
        self.add_img = ImageTk.PhotoImage(add_img)

        minus_img = PilImage.open("./src/minus.png")
        minus_img = minus_img.resize((28, 28), PilImage.ANTIALIAS)
        self.minus_img = ImageTk.PhotoImage(minus_img)

        # создаем рамку для навбара, будет снизу, методом draw_navbar отображаем виджеты навбара
        self.navbar = tk.Frame(self.root, bg='#f9f9f9')
        self.navbar.pack(side=tk.BOTTOM, fill="both")
        self.draw_navbar()

        # создаем рамку для хэдера, будет сверху, методом draw_header отображаем виджеты хэдера
        self.header = tk.Frame(self.root, bg='#f9f9f9')
        self.header.pack(side=tk.TOP, fill="both")
        self.balance = 0
        self.draw_header()

        # создаем рамку для тела программы и отрисовываем домашний
        self.body = tk.Frame(self.root, bg="#FBFFFF")
        self.body.pack(fill="both", expand=True)
        self.go_home()

    # отрисовывает виджеты экрана ГЛАВНАЯ
    def go_home(self):
        self.home_btn["state"] = tk.DISABLED
        self.operations_btn["state"] = tk.NORMAL
        self.analitycs_btn["state"] = tk.NORMAL

        for widget in self.body.winfo_children():
            widget.destroy()
        tk.Label(self.body, text="Последние операции", bg="#FBFFFF").pack()
        tk.Label(self.body, text="hi1", bg="#FBFFFF").pack()
        tk.Label(self.body, text="hi2", bg="#FBFFFF").pack()
        tk.Label(self.body, text="hi2", bg="#FBFFFF").pack()


    def call_add_window(self):
        add_window(self.root)

    # отрисовывает виджеты экрана Операции
    def go_operations(self):
        self.home_btn["state"] = tk.NORMAL
        self.operations_btn["state"] = tk.DISABLED
        self.analitycs_btn["state"] = tk.NORMAL

        for widget in self.body.winfo_children():
            widget.destroy()

        self.operations_header = tk.Frame(self.body, bg="#FBFFFF")
        self.operations_header.pack(side=tk.TOP, fill="both")
        tk.Button(self.operations_header,
                  image=self.minus_img,
                  bg="#FBFFFF",
                  relief=tk.FLAT,
                  border="0").pack(side=tk.RIGHT, padx=10, pady=10)

        tk.Button(self.operations_header,
                  image=self.add_img,
                  bg="#FBFFFF",
                  relief=tk.FLAT,
                  command=self.call_add_window,
                  border="0").pack(side=tk.RIGHT, padx=10, pady=10)

    # отрисовывает виджеты экрана Анализ
    def go_analytics(self):
        self.home_btn["state"] = tk.NORMAL
        self.operations_btn["state"] = tk.NORMAL
        self.analitycs_btn["state"] = tk.DISABLED

        for widget in self.body.winfo_children():
            widget.destroy()

        tk.Label(self.body, text="op1", bg="#FBFFFF").pack()
        tk.Label(self.body, text="op2", bg="#FBFFFF").pack()
        tk.Label(self.body, text="op3", bg="#FBFFFF").pack()

    #
    def edit_balance(self):
        self.balance += 100
        self.balance_lbl["text"] = f"{str(self.balance)} Р\n Баланс"

    # отрисовка header
    def draw_header(self):
        self.balance_lbl = tk.Label(self.header,
                                    text=f"{str(self.balance)} Р\n Баланс",
                                    font=("Roboto", 10),
                                    bg='#f9f9f9',
                                    padx=20)
        self.balance_lbl.pack(side=tk.LEFT)

    # отрисовка навбара
    def draw_navbar(self):
        self.home_btn = tk.Button(self.navbar,
                                  image=self.home_img,
                                  text="Главная",
                                  font=("Roboto", 10),
                                  width=70,
                                  compound=tk.TOP,
                                  command=self.go_home,
                                  relief=tk.FLAT,
                                  bg='#f9f9f9',
                                  border="0"
                                  )
        self.home_btn.pack(side=tk.LEFT, padx=45, )

        self.operations_btn = tk.Button(self.navbar,
                                        image=self.operations_img,
                                        text="Операции",
                                        width=70,
                                        font=("Roboto", 10),
                                        compound=tk.TOP,
                                        relief=tk.FLAT,
                                        command=self.go_operations,
                                        bg='#f9f9f9',
                                        border="0"
                                        )
        self.operations_btn.pack(side=tk.LEFT, padx=45, )

        self.analitycs_btn = tk.Button(self.navbar,
                                       image=self.analytics_img,
                                       text="Аналитика",
                                       width=70,
                                       font=("Roboto", 10),
                                       relief=tk.FLAT,
                                       compound=tk.TOP,
                                       command=self.go_analytics,
                                       bg='#f9f9f9',
                                       border="0",
                                       )

        self.analitycs_btn.pack(side=tk.LEFT, padx=45, )

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = APP()
    app.start()
