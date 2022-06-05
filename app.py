from db_helpers import *

print("Please login: ")
while True:
    user_alias = input("Alias:   ")
    user_password = input("Password:   ")
    user = run_query("SELECT * FROM hackers WHERE alias=?",[user_alias])
    print(user[0][1])
    current_user_id = user[0][0]
    current_user_alias = user[0][1]
    current_user_password = user[0][2]
    if user_alias != current_user_alias:
        print("Username doesn't exist, try again")
        break
    if user_password != current_user_password:
        print("Password doesn't match, try again")
        break
    # run_query("INSERT INTO hackers(alias,password) VALUES (?,?)", [user[0][1], user[0][2]])

    #  Once logged in give 4 options:
    print("Welcome "+ current_user_alias +". Please choose an option: ")
    # 1. Post new content into exploits
    while True:
        print("1: Enter a new exploit")
        print("2: See all your exploits")
        print("3: See all other exploits")
        print("4: Exit the application")
        user_choice = input("Which option?:   ")
        if user_choice == "1":
            print("You chose to enter a new exploit")
            new_exploit = input("Begin typing:  ")
            run_query("INSERT INTO exploits (content) VALUES (?) WHERE user_id=?",([new_exploit,current_user_id]))
        elif user_choice == "2":
            print("You chose to see all your exploits")
            current_user_exploits = run_query("SELECT * FROM exploits WHERE user_id=?",[current_user_id])
            print(current_user_exploits)
        elif user_choice == "3":
            print("You chose to see everyone else's exploits")
            other_users_exploits = run_query("SELECT content FROM exploits WHERE user_id!=?",[current_user_id])
            print(other_users_exploits)
        elif user_choice == "4":
            break
        else:
            continue
        