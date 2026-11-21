class PasswordManager:

    def __init__(self, password):
        self.__password = password
        self.changecount = 0
        self.set_password(password)
    
    def set_password(self, newpassword):
        if len(newpassword) >= 8:
            self.__password = newpassword
        else:
            print("Password should be 8 characters or more")

    def check_password(self, password):
        return self.__password == password

    def change_password(self, old, new):
        if self.__password != old:
            print("Incorrect old password")
            return False

        if len(new) < 8:
            print("Insuffiecient amount of characters")
            return False

        self.__password = new
        self.changecount += 1
        return True

pm = PasswordManager("secret123")

print(pm.check_password("secret123"))   # True

pm.change_password("secret123", "newpass456")

print(pm.check_password("newpass456"))   # True

print(pm.changecount) 
    



