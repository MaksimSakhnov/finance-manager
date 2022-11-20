import tkinter as tk

class add_window():
    def __init__(self, parent):
        self.root = tk.Toplevel(parent)
        # установка названия приложения
        self.root.title("Добавить операцию")
        # вычисляем высоту, ширину экрана
        monitor_height = self.root.winfo_screenheight()
        monitor_width = self.root.winfo_screenwidth()
        # следующая строка выводит окно размером 500 на 600 по середине экрана
        self.root.geometry(f"400x200+{int((monitor_width - 200) / 2)}+{int((monitor_height - 300) / 2)}")
        # ставим запрет на изменение размеров
        self.root.resizable(False, False)
        # устанавливаем иконку
        self.root.iconbitmap(None)
        self.grab_focus()

    def grab_focus(self):
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()

