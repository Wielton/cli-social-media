from db_helpers import *

# Initial greeting
print("Welcome to Hacker's Paradise.")
print("In this program all options are numerically selected.")


initial_user_greeting = input("Are you a 1) New Hacker or 2) Returning Disruptor? -->   ")

# New hacker register
if initial_user_greeting == "1":
    print("You've chosen wisely. We disrupt networks and want your expertise. Please take a few seconds to input your discreet info -->   ")
    new_user_alias = input("Alias -->   ")
    alias_db = ("SELECT alias FROM hackers")
    for hacker in range(alias_db):
        if new_user_alias == hacker:
            print("Alias already exists.")
            break
        else:
            continue
    # Alias has been accepted, now input password
    print("Welcome " + new_user_alias)
    new_user_password = input("Password -->   ")
    print("Thank you.  ")
    # Create the new hacker
    run_query("INSERT INTO hackers(alias,password) VALUES (?,?)",[new_user_alias,new_user_password])
    # Retrieve newly created hacker and set is_active to true
    user = ("SELECT * FROM hackers WHERE alias=?",[new_user_alias])
    current_user_id = user[0][0]
    current_user_alias = user[0][1]
    current_user_password = user[0][2]
    is_active = True
    
# Returning hacker login
elif initial_user_greeting == "2":
    print("Welcome back like-minded friend. Remember: It's our time -->   ")
    user_alias = input("Alias -->   ")
    # Retrieve and save existing hacker info in variables.  Use password for authentication purposes
    user = run_query("SELECT * FROM hackers WHERE alias=?",[user_alias])
    current_user_id = user[0][0]
    current_user_alias = user[0][1]
    current_user_password = user[0][2]
    # Make sure hacker alias exists
    if user_alias != current_user_alias:
        print("Username doesn't exist, try again")
    else:
        print("Welcome "+ current_user_alias + ".")
    user_password = input("Input your password -->   ")
    # Make sure hacker password matches
    if user_password != current_user_password:
        print("Password doesn't match, try again")
        user_password = input("Input your password -->   ")
    else:
        # Hacker is authenticated and set is_active to true
        print("You're ready to hack!")
        is_active = True
else:
    print("Sorry, your request couldn't process. Please choose a valid option.")

# While Loop to control hacker active status
while is_active:
    
    print("Welcome "+ current_user_alias +". Please choose an option: ")
    # 1. Post new content into exploits
    print("1: Enter a new exploit")
    print("2: See all your exploits")
    print("3: See all other exploits")
    print("4: Exit the application")
    user_choice = input("Which option?:   ")
    if user_choice == "1":
        print("You chose to enter a new exploit")
        new_exploit = input("Begin typing:  ")
        run_query("INSERT INTO exploits (content, user_id) VALUES (?,?)",[new_exploit,current_user_id])
    elif user_choice == "2":
        print("You chose to see all your exploits")
        current_user_exploits = run_query("SELECT hackers.alias, exploits.content FROM hackers JOIN exploits ON hackers.id=exploits.user_id WHERE user_id=?",[current_user_id])
        print(current_user_exploits)
    elif user_choice == "3":
        print("You chose to see everyone else's exploits")
        other_users_exploits = run_query("SELECT hackers.alias, exploits.content FROM hackers RIGHT JOIN exploits ON hackers.id=exploits.user_id WHERE user_id!=?",[current_user_id])
        print(other_users_exploits)
    elif user_choice == "4":
        break
    else:
        continue
        