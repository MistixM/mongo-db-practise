from db import (write_data, 
                update_data, 
                delete_data,
                check_data)

def main():

    # Request registration/login with try block
    try:
        # Ask name, username
        name = input("Hello! Please enter your name to proceed with registration: ")
        username = input("Also we want know your username: ")
        
        # Check if the username already exists in the database
        sub_check = check_data({"username": username})

        if sub_check:

            # Suggest to update or delete the data from the database
            print("Your submission already exists in our database. Do you want to update or delete it?")
            update_choice = input("U/D: ")

            if update_choice.lower() == 'u':
                new_username = input("Please enter your new username: ")

                update_data({"username": username}, {"username": new_username})

                print(f"Your username has changed to {new_username}")

                return
            elif update_choice.lower() == 'd':
                delete_data({'username': username})
                
                print("Your submission has been deleted.")
                return
        
        # Ask age if the user don't have a submission
        age = int(input("Thanks! Now we need to confirm your age: "))

    except Exception as e:
        print(f"There was a problem with your registration. Please try again later!: {e}")
        return
    
    # Check name and write data to the database
    if name.isalpha():
        submission = write_data({"name": name, "username": username, "age": age})
    else:
        print("There was a problem with your registration. Please try again later")
        return

    print(f"Thanks for your submission! Your ID is: {submission['submission_id']}")

    
if __name__ == '__main__':
    main()