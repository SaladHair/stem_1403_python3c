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
# sign_up function
def sign_up():
    name = input("Please enter your desired username: ")
    if os.path.isfile(name):
        return 0  # 0 is error code for username already in use
    pwd = input("Please enter your desired password: ")
    confirm_pwd = input("Please confirm your password: ")
    if pwd != confirm_pwd:
        return 1  # 1 is error code for pwd confirm not matching
    date_of_birth = input("Please enter your date of birth: ")
    return create_account(name, pwd, date_of_birth)


def create_account(username, password, dob):
    if os.path.isfile(username):
        return 0  # double check
    else:
        credentials_file = open(username, "w")
        credentials_file.write(f"{username} {password} {dob}")
        credentials_file.close()
        credentials_file = open(username, "r")
        credentials = credentials_file.read().split()
        return UserAccount(credentials[0], credentials[1],
                           credentials[2])


user_input = input("Press 1 to sign up, 2 to login to an existing account, 3 to logout from an account and 'exit' to "
                   "exit the program: ")

acc_1 = None
while user_input != "exit":
    if user_input == "1":
        acc_1 = sign_up()
        if acc_1 == 0:
            print("Username already in use, please try another")
            sign_up()
        elif acc_1 == 1:
            print("Password confirmation failed, please try again")
            sign_up()
        else:
            print("Account successfully created")
    elif user_input == "2":
        username = input("Enter the username of the account you wish to log into: ")
        if acc_1:
            if acc_1.username == username:
                if acc_1.sign_in(username, input("Enter your password"),
                                 input("Enter your date of birth in the format you entered while signing up")):
                    print("Login successful")
                else:
                    print("Username, password or date of birth incorrect")
            else:
                acc_1 = UserAccount(open(username, "r").read().split()[0], open(username, "r").read().split()[1],
                                    open(username, "r").read().split()[2])
                if acc_1.sign_in(username, input("Enter your password: "),
                                 input("Enter your date of birth in the format you entered while signing up: ")):
                    print("Login successful")
                else:
                    print("Username, password or date of birth incorrect")
        else:
            acc_1 = UserAccount(open(username, "r").read().split()[0], open(username, "r").read().split()[1],
                                open(username, "r").read().split()[2])
            if acc_1.sign_in(username, input("Enter your password: "),
                             input("Enter your date of birth in the format you entered while signing up: ")):
                print("Login successful")
            else:
                print("Username, password or date of birth incorrect")
    elif user_input == "3":
        if acc_1:
            if acc_1.signed_in:
                if acc_1.sign_out():
                    print("Logout successful")
                else:
                    print("Logout failed")
            else:
                print("Not signed into an account")
    user_input = input(
        "Press 1 to sign up, 2 to login to an existing account, 3 to logout from an account and 'exit' to exit the "
        "program: ")


print("Program end")