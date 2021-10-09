import os
import mysql.connector

class Login:
    def __init__(self):
        self.ism = None
        self.familya = None
        self.yosh = None
        self.login = None
        self.parol = None
        self.parol_and_login = []
        self.loginlar = []
        self.parollar = []
        self.tekshirish()
    def tizimga_kirish(self):
        self.cls()
        self.ishora()
        lis = ['1', '2', '3', '4', '5']
        inp = input(">>> ").strip()
        while inp not in lis:
            self.cls()
            self.ishora()
            print("Xato qayta kiriting!")
            inp = input(">>> ").strip()
        if inp == lis[0]:
            self.registratsiya()
        elif inp == lis[1]:
            self.log_in()
        elif inp == lis[2]:
            self.chage_login()
        elif inp == lis[3]:
            self.delete_login()
        else:
            self.log_out()
    def registratsiya(self):
        self.cls()
        ism = input("Ism: ").strip().lower()
        while not ism.isalpha():
            self.cls()
            ism = input("Ism: ").strip().lower()
        self.cls()
        familya = input("Familya: ").strip().lower()
        while not familya.isalpha():
            self.cls()
            familya = input("Familya: ").strip().lower()
        self.cls()
        yosh = input("yosh: ").strip()
        while not yosh.isdigit():
            self.cls()
            yosh = input("yosh: ").strip()
        self.cls()
        log = input("Login: ").strip().lower()
        while not log.isalnum() or log in self.loginlar:
            self.cls()
            log = input("Login: ").strip().lower()
        self.cls()
        parol = input("Parol: ").strip().lower()
        parol1 = input("Qayta kiriting: ").strip().lower()
        while self.emty_str(parol) or parol != parol1 or parol in self.parollar:
            self.cls()
            parol = input("Parol: ").strip().lower()
            parol1 = input("Qayta kiriting: ").strip().lower()
        self.cls()
        self.ism = ism
        self.familya = familya
        self.yosh = yosh
        self.login = log
        self.parol = parol
        mydb = self.database()
        mycursor = mydb.cursor()
        mycursor.execute(f"insert into login(ism, familya, yosh, login, parol)values('{self.ism}', '{self.familya}', '{self.yosh}', '{self.login}', '{self.parol}')")
        mydb.commit()
        self.cls()
        print("Tizimga hush kelibsiz!")
    def log_in(self):
        self.cls()
        log = input("Login: ").strip().lower()
        while log not in self.loginlar:
            self.cls()
            log = input("Login: ").strip().lower()
        mydb = self.database()
        mycursor = mydb.cursor()
        mycursor.execute(f"select parol from login where login='{log}'")
        db_pass = None
        for i in mycursor:
            db_pass = i[0]
        self.cls()
        parol = input("Parol: ").strip().lower()
        while parol != db_pass:
            self.cls()
            parol = input("Parol: ").strip().lower()
        self.cls()
        print("Tizimga hush kelibsiz!")
    def chage_login(self):
        self.cls()
        log = input("Login: ").strip().lower()
        while log not in self.loginlar:
            self.cls()
            log = input("Login: ").strip().lower()
        mydb = self.database()
        mycursor = mydb.cursor()
        mycursor.execute(f"select parol from login where login='{log}'")
        db_pass = None
        for i in mycursor:
            db_pass = i[0]
        self.cls()
        parol = input("Parol: ").strip().lower()
        while parol != db_pass:
            self.cls()
            parol = input("Parol: ").strip().lower()
        self.cls()
        new_log = input("Yangi login: ").strip().lower()
        while not new_log.isalnum() or new_log in self.loginlar:
            self.cls()
            new_log = input("Yangi login: ").strip().lower()
        self.cls()
        new_pass = input("Yangi parol: ").strip().lower()
        parol1 = input("Qayta kiriting: ").strip().lower()
        while self.emty_str(new_pass) or new_pass != parol1 or new_pass in self.parollar:
            self.cls()
            new_pass = input("Yangi parol: ").strip().lower()
            parol1 = input("Qayta kiriting: ").strip().lower()
        self.cls()
        my_db = self.database()
        mycursor = my_db.cursor()
        mycursor.execute(f"update login set login='{new_log}',parol='{new_pass}' where login='{log}'")
        my_db.commit()
        self.cls()
        print("Login muvofaqiyatli yangiladi!")
    def log_out(self):
        self.cls()
        print("Tizimdan chiqdingiz!")
        exit()
    def delete_login(self):
        self.cls()
        log = input("Login: ").strip().lower()
        while log not in self.loginlar:
            self.cls()
            log = input("Login: ").strip().lower()
        mydb = self.database()
        mycursor = mydb.cursor()
        mycursor.execute(f"select parol from login where login='{log}'")
        db_pass = None
        for i in mycursor:
            db_pass = i[0]
        self.cls()
        parol = input("Parol: ").strip().lower()
        while parol != db_pass:
            self.cls()
            parol = input("Parol: ").strip().lower()
        self.cls()
        my_db = self.database()
        mycursor = my_db.cursor()
        mycursor.execute(f"delete from login where login='{log}'")
        my_db.commit()
        input("Enter")
        print("Login o'chirildi!")
    def tekshirish(self):
        mydb = self.database()
        mycursor = mydb.cursor()
        mycursor.execute("select login,parol from login")
        for i in mycursor:
            self.parol_and_login.append(i)
        for j in self.parol_and_login:
            self.loginlar.append(j[0])
            self.parollar.append(j[1])
    @staticmethod
    def database():
        return mysql.connector.connect(
        host="localhost",
        user="Avazbek",
        password="12345678",
        database="users"
        )
    @staticmethod
    def ishora():
        print("""
                 ---A M D---                         
            ----------------------
             Register         [1]  
            ----------------------
             Login            [2]  
            ----------------------
             Change Login     [3]  
            ----------------------
             Delete login     [4]
            ----------------------
             Log out          [5]  
            ----------------------
        """)
    @staticmethod
    def emty_str(str_):
        return not bool(str_)
    @staticmethod
    def cls():
        os.system("clear")
obyekt = Login()
obyekt.tizimga_kirish()






























