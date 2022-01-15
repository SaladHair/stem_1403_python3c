"""
[Homework]
Date: 2021-12-04
Due date: 2021-12-10
1. Programming practice in OO
Project:	User Account and Login
Description:
A User has an account for a web application (such as google, youtube, amazon, etc.)
Users have to sign up before using the web app.
Users have to sign in each time to access web pages in the web app.
When a user signs up, he/she is asked to input username, password, date of birth and to check the checkbox of agreement of terms of use and privacy policies.
The system will store the credentials as well as other user info. into store media permanently.
After the user signs up, he/she then logins into the web app freely.
Each time the user must input username and password correctly, otherwise the system denies to pass.
When a user wants to exit from the web app, he/she can log out.
Requirement:
Creating a class named UserAccount
Finding attributes (or properties)
Finding methods
Concerning information hiding and encapsulation
Write a main program to create a user account for a user.
Let the user sign up.
Let the user sign in.
Let the user sign out.
"""

import os


class AccountService:
    @staticmethod
    def create_account():
        name = input("Please enter your desired username: ")
        if os.path.isfile(name):
            return 0  # 0 is error code for username already in use
        pwd = input("Please enter your desired password: ")
        confirm_pwd = input("Please confirm your password: ")
        if pwd != confirm_pwd:
            return 1  # 1 is error code for pwd confirm not matching
        date_of_birth = input("Please enter your date of birth: ")
        if os.path.isfile(name):
            return 0  # double check
        else:
            credentials_file = open(name, "w")
            credentials_file.write(f"{name} {pwd} {date_of_birth}")
            credentials_file.close()
            credentials_file = open(name, "r")
            credentials = credentials_file.read().split()
            return UserAccount(credentials[0], credentials[1],
                               credentials[2])

    @staticmethod
    def sign_up(acc):
        acc = AccountService.create_account()
        while acc == 0 or acc == 1:
            if acc == 0:
                print("Username already in use, please try another")
                acc = AccountService.create_account()
            elif acc == 1:
                print("Password confirmation failed, please try again")
                acc = AccountService.create_account()
        print("Account successfully created")
        return acc

    @staticmethod
    def login(acc):
        username = input("Enter the username of the account you wish to log into: ")
        if not os.path.isfile(username):
            print("Account does not exist")
            if input("To create an account, press 1. To try to login again, press 2: ") == "1":
                acc = AccountService.sign_up(acc)
                return acc
            else:
                acc = AccountService.login(acc)
                return acc

        if acc:
            if acc.signed_in:
                print("You are already signed in")
                return acc

            if acc.username == username:
                if acc.sign_in(username, input("Enter your password: "),
                               input("Enter your date of birth in the format you entered while signing up: ")):
                    print("Login successful")
                else:
                    print("Username, password or date of birth incorrect")
            else:
                acc = UserAccount(open(username, "r").read().split()[0], open(username, "r").read().split()[1],
                                  open(username, "r").read().split()[2])
                acc = AccountService.login(acc)
        else:
            acc = UserAccount(open(username, "r").read().split()[0], open(username, "r").read().split()[1],
                              open(username, "r").read().split()[2])
            acc = AccountService.login(acc)

        return acc

    @staticmethod
    def logout(acc):
        if acc:
            if acc.signed_in:
                if acc.sign_out():
                    print("Logout successful")
                else:
                    print("Logout failed")
            else:
                print("Not signed into an account")


class UserAccount:
    def __init__(self, username, password, dob):
        self.username = username
        self._password = password
        self._dob = dob
        self.signed_in = False

    def sign_in(self, username, password, dob):
        if self.username == username and self._password == password and self._dob == dob:
            self.signed_in = True
            return True
        else:
            return False

    def sign_out(self):
        self.signed_in = False
        return True


# main program

acc_1 = None
while True:
    user_input = input(
        "Press 1 to sign up, 2 to login with an existing account, 3 to logout an account and 'exit' to exit the "
        "program: ")

    if user_input == "1":
        acc_1 = AccountService.sign_up(acc_1)
    elif user_input == "2":
        acc_1 = AccountService.login(acc_1)
    elif user_input == "3":
        AccountService.logout(acc_1)
    elif user_input != "exit":
        break

print("Program end")
