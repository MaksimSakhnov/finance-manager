import tkinter as tk
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from database import add_operation
from datetime import timedelta, datetime


class filter_window():
    def __init__(self, parent):
        self.parent = parent
        self.root = tk.Toplevel(parent)
        # установка названия приложения
        self.root.title("Добавить расход")
        # вычисляем высоту, ширину экрана
        monitor_height = self.root.winfo_screenheight()
        monitor_width = self.root.winfo_screenwidth()
        # следующая строка выводит окно размером 500 на 600 по середине экрана
        self.root.geometry(f"300x150+{int((monitor_width - 200) / 2)}+{int((monitor_height - 300) / 2)}")
        # ставим запрет на изменение размеров
        self.root.resizable(False, False)
        # устанавливаем иконку
        self.root.iconbitmap(None)

        self.draw_widgets()

        self.grab_focus()

    # рисуем виджеты
    def draw_widgets(self):
        tk.Label(self.root, text="Тип").grid(row=0, column=0, ipadx=20)
        # выпадающий список
        self.type = Combobox(self.root, values=('Расход',
                                                'Доход',))
        self.type.grid(row=0, column=1, ipadx=20, stick='ew')

        tk.Label(self.root, text="От").grid(row=1, column=0, ipadx=20)
        # отдельный элемент, календарь, в котором мы можем выбирать дату
        self.cal = DateEntry(self.root, selectmode='day')
        self.cal.grid(row=1, column=1, ipadx=20, stick='ew')

        tk.Label(self.root, text="До").grid(row=2, column=0, ipadx=20)
        # отдельный элемент, календарь, в котором мы можем выбирать дату
        self.cal_to = DateEntry(self.root, selectmode='day')
        self.cal_to.grid(row=2, column=1, ipadx=20, stick='ew')

        self.add_btn = tk.Button(self.root, text="Применить", command=self.get_data)
        self.add_btn.grid(row=3, column=0, columnspan=2, pady=20)

    def get_data(self):
        temp_type = self.type.get()
        temp_date_1 = self.cal.get_date()
        temp_date_2 = self.cal_to.get_date()
        filter = [temp_type, temp_date_1, temp_date_2]
        self.root.destroy()


    def grab_focus(self):
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()
