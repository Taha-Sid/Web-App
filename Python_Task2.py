class Users:
    def __init__(self,fName,sName,email,pwd):
        self.first_name = fName
        self.surname = sName
        self.email = email
        self.password = pwd

    def check_email(self):
        if '@gmail.com' in self.email or '@yahoo.com' in self.email or '@hotmail.com' in self.email:
            return True
        else:
            return False

    def check_password(self):
        capCheck = False
        lowCheck = False
        
        if len(self.password) >= 6 and len(self.password) <= 12:
            if 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 in self.password:
                for i in self.password:
                    if ord(i) >= 65 and ord(i) <= 90:
                        capCheck = True
                    if ord(i) >= 97 and ord(i) <= 122:
                        lowCheck = True
                if capCheck == True and lowCheck == True:
                    return True
        return False

fname = input('Enter First Name: ')
lname = input('Enter Last Name: ')
email = input('Enter Email: ')
pwd = input('Enter Password: ')
users = Users(fname, lname, email, pwd)

print('\n')
if users.check_email():
    print('Valid Email')
else:
    print('Invalid Email')
    
if users.check_password():
    print('Valid Password')
else:
    print('Invalid Password')
