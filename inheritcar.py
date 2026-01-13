class User:

    #hidden Variable
    __password="Abc@123"

    def __init__(self,name,email,username):
        self.name=name
        self.email=email
        self.username=username

    def getPassword(self):
        return self.__password
    
    def setPassword(self):
        old_password=input("enter your old password")
        if old_password == self.__password:
            new_password=input("Enter a new password")
            self.__password=new_password
        else:
            print("Please enter correct password!!")

mathis =User("Mathis","mathis3@gmail.com","mathis3")
print(mathis.name)
print(mathis.getPassword())
mathis.setPassword()
