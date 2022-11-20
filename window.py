import tkinter as tk
from PIL import Image as PilImage
from PIL import ImageTk

#класс окно
class Window:
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

        home_img = PilImage.open("./src/home.png")
        home_img = home_img.resize((30,30),PilImage.ANTIALIAS)
        self.home_img = ImageTk.PhotoImage(home_img)

        operations_img = PilImage.open("./src/operations.png")
        operations_img = operations_img.resize((30,30),PilImage.ANTIALIAS)
        self.operations_img = ImageTk.PhotoImage(operations_img)

        analytics_img = PilImage.open("./src/analitics.png")
        analytics_img = analytics_img.resize((30,30),PilImage.ANTIALIAS)
        self.analytics_img = ImageTk.PhotoImage(analytics_img)

        self.navbar = tk.Frame()
        self.navbar.pack(side=tk.BOTTOM)
        self.draw_navbar()

        self.body = tk.Frame()
        self.body.pack()
        self.go_home()


    def go_home(self):
        for widget in self.body.winfo_children():
            widget.destroy()

        tk.Label(self.body, text="hi1").pack()
        tk.Label(self.body, text="hi2").pack()
        tk.Label(self.body, text="hi2").pack()


    def go_operations(self):
        for widget in self.body.winfo_children():
            widget.destroy()

        tk.Label(self.body, text="h3").pack()
        tk.Label(self.body, text="h5").pack()
        tk.Label(self.body, text="h6").pack()

    def go_analytics(self):
        for widget in self.body.winfo_children():
            widget.destroy()

        tk.Label(self.body, text="op1").pack()
        tk.Label(self.body, text="op2").pack()
        tk.Label(self.body, text="op3").pack()




    def draw_navbar(self):
        tk.Button(self.navbar,
                  image=self.home_img,
                  text="Главная",
                  font=("Roboto", 10),
                  width=40,
                  compound=tk.TOP,
                  command=self.go_home,
                  padx=10,
                  relief=tk.FLAT,
                  )\
            .pack(side=tk.LEFT)

        tk.Button(self.navbar,
                  image=self.operations_img,
                  text="Операции",
                  width=50,
                  font=("Roboto", 10),
                  compound=tk.TOP,
                  padx=20,
                  relief=tk.FLAT,
                  command=self.go_operations,

                  )\
            .pack(side=tk.LEFT)

        tk.Button(self.navbar,
                  image=self.analytics_img,
                  text="Аналитика",
                  width=50,
                  font=("Roboto", 10),
                  padx=20,
                  relief=tk.FLAT,
                  compound=tk.TOP,
                  command=self.go_analytics,
                  ).pack(side=tk.LEFT)

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = Window()
    app.start()
