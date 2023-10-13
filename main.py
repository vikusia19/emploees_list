# Импорты
import tkinter as tk
from tkinter import ttk
import sqlite3

# Написание класса для главного окна
# Инициализация атрибутов класса
class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

# Метод для хранения и инициализации графических элеметов главного окна
# Настройки окна
    def init_main(self):
        toolbar = tk.Frame(bg='#AED6F1', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

# Создание кнопок на главном окне
# Кнопка, отвечающая за добавление сотрудника
        self.add_img = tk.PhotoImage(file='./img/add.png')
        btn_open = tk.Button(toolbar, bg='#AED6F1', bd=0, image=self.add_img, command=self.open)
        btn_open.pack(side=tk.LEFT)

# Кнопка, отвечающая за редактирование сотрудника
        self.update_img = tk.PhotoImage(file='./img/update.png')
        button_edit = tk.Button(toolbar, bg='#AED6F1', bd=0, image=self.update_img, command=self.open_update)
        button_edit.pack(side=tk.LEFT)

# Кнопка, отвечающая за удаление сотрудника
        self.delete_img = tk.PhotoImage(file='./img/delete.png')
        button_delete = tk.Button(toolbar, bg='#AED6F1', bd=0, image=self.delete_img, command=self.delete_records)
        button_delete.pack(side=tk.LEFT)

# Кнопка, отвечающая за поиск сотрудника
        self.search_img = tk.PhotoImage(file='./img/search.png')
        button_search = tk.Button(toolbar, bg='#AED6F1', bd=0, image=self.search_img, command=self.open_search)
        button_search.pack(side=tk.LEFT)

# Создание таблицы с данными о всех сотрудниках
        self.tree = ttk.Treeview(self, columns=('ID', 'name', 'phone', 'email', 'salary'), height=45, show='headings')

        self.tree.column('ID', width=30, anchor=tk.CENTER)
        self.tree.column('name', width=200, anchor=tk.CENTER)
        self.tree.column('phone', width=120, anchor=tk.CENTER)
        self.tree.column('email', width=120, anchor=tk.CENTER)
        self.tree.column('salary', width=120, anchor=tk.CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('name', text='ФИО')
        self.tree.heading('phone', text='Телефон')
        self.tree.heading('email', text='E-mail')
        self.tree.heading('salary', text='Зарплата')

        self.tree.pack(side=tk.LEFT)

# Метод для открытия дочернего окна
    def open(self):
        Child()

# Метод для введения данных
    def records(self, name, phone, email, salary):
        self.db.insert_data(name, phone, email, salary)
        self.view_records()

# Метод для обновления таблицы
    def view_records(self):
        self.db.cursor.execute('SELECT * FROM Emploees')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cursor.fetchall()]

# Метод для открытия дочернего окна (редактирование сотрудника)
    def open_update(self):
       Update()

# Метод для редактирования сотрудника
    def update_records(self, name, phone, email, salary):
        self.db.cursor.execute('UPDATE Emploees SET name=?, phone=?, email=?, salary=? WHERE id=?', (name, phone, email, salary, self.tree.set(self.tree.selection() [0], '#1')))
        self.db.conn.commit()
        self.view_records()

# Метод для удаления сотрудника
    def delete_records(self):
        for selection_items in self.tree.selection():
            self.db.cursor.execute('DELETE from Emploees WHERE id=?', (self.tree.set(selection_items, '#1')))
        self.db.conn.commit()
        self.view_records()

# Метод для открытия дочернего окна (поиск сотрудника)
    def open_search(self):
        Search()

# Метод для поиска по базе данных
    def search_records(self, name):
        name = ('%' + name + '%')
        self.db.cursor.execute('SELECT * from Emploees WHERE name LIKE ?', (name,))

        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cursor.fetchall()]

# Создание класса дочернего окна
class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app
    
# Метод для хранения и инициализации графических элеметов дочернего окна
# Настройки окна
    def init_child(self):
        self.title('Добавить')
        root.resizable(False, False)
        self.geometry('400x228')

# Обработка событий и фокусировка
        self.grab_set()
        self.focus_set()

# Создание надписи и поля для ввода для записи данных
        label_name = tk.Label(self, text='ФИО:')
        label_name.place(x=50, y=50)
        label_phone = tk.Label(self, text='Телефон:')
        label_phone.place(x=50, y=80)
        label_email = tk.Label(self, text='E-mail:')
        label_email.place(x=50, y=110)
        label_salary = tk.Label(self, text='Зарплата:')
        label_salary.place(x=50, y=140)

        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=200, y=50)
        self.entry_phone = ttk.Entry(self)
        self.entry_phone.place(x=200, y=80)
        self.entry_email = ttk.Entry(self)
        self.entry_email.place(x=200, y=110)
        self.entry_salary = ttk.Entry(self)
        self.entry_salary.place(x=200, y=140)

# Создание кнопки для закрытия окна
        self.button_destroy = ttk.Button(self, text='Закрыть', command=self.destroy)
        self.button_destroy.place(x=220, y=170)

# Создание кнопки, которая добавляет данные в базу данных
        self.button_ok = ttk.Button(self, text='Добавить')
        self.button_ok.place(x=300, y=170)

        self.button_ok.bind('<Button-1>', lambda event:
                            self.view.records(self.entry_name.get(),
                                              self.entry_phone.get(),
                                              self.entry_email.get(),
                                              self.entry_salary.get(),
                                              ))

# Написание класса для поиска сотрудника
# Инициализация атрибутов класса
class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

# Реализация поиска сотрудника
# Настройки окна
    def init_search(self):
        self.title('Поиск сотрудника')
        self.geometry('300x100')
        self.resizable(False, False)
    
# Создание надписи
        label_search = tk.Label(self, text='Имя:')
        label_search.place(x=50, y=20)

# Создание поля для ввода
        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=100, y=20, width=150)

# Создание кнопки для закрытия окна
        button_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        button_cancel.place(x=185, y=50)

# Создание кнопки для поиска сотрудника
        button_search = ttk.Button(self, text='Найти')
        button_search.place(x=105, y=50)
        button_search.bind('<Button-1>', lambda event:
                           self.view.search_records(self.entry_search.get()))
        button_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

# Написание класса для базы данных
# Метод для инициализации базы данных
class Db():
    def __init__(self):
        self.conn = sqlite3.connect('db.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS Emploees(
            ID INTEGER PRIMARY KEY,
            name TEXT,
            phone TEXT,
            email TEXT,
            salary TEXT)'''
            )
        self.conn.commit()

# Метод для добавления данных в базу данных
    def insert_data(self, name, phone, email, salary):
        self.cursor.execute('INSERT INTO Emploees(name, phone, email, salary) VALUES(?, ?, ?, ?)', (name, phone, email, salary))
        self.conn.commit()

# Создание класса дочернего окна (редактирование сотрудника)
# Инициализация атрибутов класса
class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app
        self.db = db
        self.default_data()

# Реализация редактирования сотрудника
    def init_edit(self):
        self.title('Редактирование сотрудника')
        button_edit = ttk.Button(self, text='Редактировать')
        button_edit.place(x=205, y=170)
        button_edit.bind('<Button-1>', lambda event:
                         self.view.update_records(self.entry_name.get(),
                                                  self.entry_phone.get(),
                                                  self.entry_email.get(),
                                                  self.entry_salary.get(),
                                                  ))
        button_edit.bind('<Button-1>', lambda event: self.destroy(), add='+')
        self.button_ok.destroy()

# Метод для подрузки данных в поле редактирования
    def default_data(self):
        self.db.cursor.execute('SELECT * FROM Emploees WHERE id=?', self.view.tree.set(self.view.tree.selection() [0], '#1'))
        row = self.db.cursor.fetchone()
        self.entry_name.insert(0, row[1])
        self.entry_phone.insert(0, row[2])
        self.entry_email.insert(0, row[3])
        self.entry_salary.insert(0, row[4])

# Создание бесконечного цикла окна приложения
if __name__ == '__main__':
    root = tk.Tk()
    db = Db()
    app = Main(root)
    app.pack()
    root.title('Список сотрудников компании')
    root.geometry('665x450')
    root.resizable(False, False)
    root.mainloop()