from db_helpers import *

print("Please login: ")
user_alias = input("Alias:   ")
user_password = input("Password:   ")

user = run_query("SELECT * FROM hackers WHERE alias=?",[user_alias])
print(user[0][1])
if user_alias != user[0][1]:
    print("Username doesn't exist, try again")
if user_password != user[0][2]:
        print("Password doesn't match, try again")
# run_query("INSERT INTO hackers(alias,password) VALUES (?,?)", [user[0][1], user[0][2]])

#  Once logged in give 4 options:
print("Welcome "+ user[0][1] +". Please choose an option: ")
# 1. Post new content into exploits
while True:
    print("1: Enter a new exploit")
    print("2: See all your exploits")
    print("3: See all other exploits")
    print("4: Exit the application")
    user_choice = input("Which option?:   ")
    if user_choice == "1":
        print("You chose to enter a new exploit")
    if user_choice == "2":
        print("You chose to see all your exploits")
    if user_choice == "3":
        print("You chose to see everyone else's exploits")
    if user_choice == "4":
        break