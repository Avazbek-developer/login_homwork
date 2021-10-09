import os

class Login:
    pass
    def tizimga_kirish(self):
        self.cls()
        self.ishora()
        lis = ['1', '2', '3', '4', '5']
        inp = input(">>> ")
        while inp not in lis:
            self.cls()
            self.ishora()
            print("Xato qayta kiriting!")
            inp = input(">>> ")
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
        ism = input("Ism: ")
        while not ism.isalpha():
            self.cls()
            ism = input("Ism: ")
        familya = input("Familya: ")
        while not familya.isalpha():
            self.cls()
            familya = input("Familya: ")
        yosh = input("yosh: ")
        while not yosh.isdigit():
            self.cls()
            yosh = input("yosh: ")
        log = input("Login: ")
        while not log.isalnum():
            self.cls()
            log = input("Login: ")
        parol = input("Parol: ")
        while self.emty_str(parol):
            self.cls()
            parol = input("Parol: ")

    def log_in(self):
        pass

    def chage_login(self):
        pass

    def log_out(self):
        pass

    def delete_login(self):
        pass

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






























