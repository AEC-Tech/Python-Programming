import pyttsx3
import time

speaker = pyttsx3.init()
print("~" * 60)
print("*HELLO BOSS*")
speaker.say("hello boss")
speaker.runAndWait()
print("*WELCOME* YOU ARE WITH WORLD'S MOST ADVANCE CONTACT SYSTEM*")
speaker.say("WELCOME         YOU ARE WITH WORLD'S MOST ADVANCE CONTACT SYSTEM")
speaker.runAndWait()
print("*I AM YOUR PERSONAL ASSISTANT*")
speaker.say("I AM YOUR PERSONAL ASSISTANT")
speaker.runAndWait()
print("~" * 60)
want = (input("DO YOU WANT TO HAVE VOICE OR NOT (YES/NO):-"))
contacts = {}
print("BELOW ARE THE OPTIONS YOU CAN DO HERE")
print("~" * 60)
speaker.say("BELOW ARE THE OPTIONS YOU CAN DO HERE")

speaker.runAndWait()
if want.upper() == "YES":
    while True:
        print("ENTER 1:-CREATE A NEW CONTACT")
        speaker.say("ENTER 1  TO CREATE A NEW CONTACT ")
        speaker.runAndWait()
        print("ENTER 2:-MODIFY A CONTACT")
        speaker.say("ENTER 2 TO MODIFY A CONTACT")
        speaker.runAndWait()
        print("ENTER 3:-REMOVE A CONTACT")
        speaker.say("ENTER 3 TO REMOVE A CONTACT")
        speaker.runAndWait()
        print("ENTER 4:-SEARCH A CONTACT")
        speaker.say("ENTER 4 TO SEARCH A CONTACT")
        speaker.runAndWait()
        print("ENTER 5:-EXIT")
        speaker.say("ENTER 5 TO EXIT")
        speaker.runAndWait()

        choice = int(input("ENTER YOUR CHOICE :-"))
        speaker.say("BOSS ENTER YOUR CHOICE ")
        speaker.runAndWait()

        if choice == 1:
            speaker.say("BOSS YOU CHOOSED TO ADD A NEW CONTACT")
            speaker.runAndWait()
            speaker.say("PLEASE PROVIDE THESE DETAILS TO ADD THE CONTACT")
            speaker.runAndWait()
            ph = input("ENTER THE CONTACT NUMBER:-")
            while len(ph) != 10:
                print("BOSS THE NUMBER YOU ENTERED HAS LESS THAN 10 DIGITS")
                speaker.say("BOSS THE NUMBER YOU ENTERED HAS LESS THAN 10 DIGITS")
                speaker.runAndWait()
            speaker.say("ENTER THE CONTACT NUMBER ")
            speaker.runAndWait()
            Fname = input("ENTER FIRST NAME:-")
            speaker.say("ENTER THE FIRST NAME ")
            speaker.runAndWait()
            Lname = input("ENTER LAST NAME:-")
            speaker.say("ENTER THE LAST NAME ")
            speaker.runAndWait()
            address = input("ENTER THE ADDRESS:-")
            speaker.say("ENTER THE ADDRESS")
            speaker.runAndWait()
            city = input("ENTER CITY NAME:-")
            speaker.say("ENTER THE CITY NAME ")
            speaker.runAndWait()
            speaker.say("THAT'S ALL WE NEED THE INFORMATION WE NEED NOW  ")
            speaker.runAndWait()
            speaker.say("PLEASE WAIT THE CONTACT IS BEING ADDED ")
            speaker.runAndWait()
            contacts[ph] = [Fname, Lname, address, city]
            print("THE CONTACT IS ADDED SUCCESSFULLY")
            speaker.say("THE CONTACT ADDED SUCCESSFULLY ")
            speaker.runAndWait()
            print("~" * 60)

        elif choice == 2:
            speaker.say("BOSS you choosed to modify a contact")
            speaker.runAndWait()
            ph = input("ENTER THE PHONE NUMBER TO MODIFY THE DETAILS:-")
            speaker.say("enter the phone number to modify the details  ")
            speaker.runAndWait()
            if ph in contacts:
                print("PRESS 1:-TO CHANGE FIRST NAME")
                speaker.say("press 1 to change first name   ")
                speaker.runAndWait()
                print("PRESS 2:-TO CHANGE LAST NAME")
                speaker.say("press 2 to change last name   ")
                speaker.runAndWait()
                print("PRESS 3:-TO CHANGE ADDRESS")
                speaker.say("press 3 to change the address   ")
                speaker.runAndWait()
                print("PRESS 4:-TO CHANGE CITY NAME")
                speaker.say("press 4 to change city name   ")
                speaker.runAndWait()
                option = int(input("CHOOSE YOUR choice :-"))
                speaker.say("BOSS please enter your choice     ")
                speaker.runAndWait()
                if option == 1:
                    speaker.say("BOSS you choosed to  change the first name     ")
                    speaker.runAndWait()
                    new = input("ENTER 1ST NAME:-")
                    speaker.say("enter the new  first name    ")
                    speaker.runAndWait()
                    contacts[ph][0] = new
                    print("~" * 60)
                elif option == 2:
                    speaker.say("BOSS you choosed to  change the last name     ")
                    speaker.runAndWait()
                    new = input("ENTER LAST NAME:-")
                    speaker.say("enter the new  last  name    ")
                    speaker.runAndWait()
                    contacts[ph][1] = new
                    print("~" * 60)
                elif option == 3:
                    speaker.say("BOSS you choosed to  change the address     ")
                    speaker.runAndWait()
                    new = input("ENTER NEW ADDRESS:-")
                    speaker.say("enter the new  address    ")
                    speaker.runAndWait()
                    contacts[ph][2] = new
                    print("~" * 60)
                elif option == 4:
                    speaker.say("BOSS you choosed to  change the city      ")
                    speaker.runAndWait()
                    new = input("ENTER CITY NAME:-")
                    speaker.say("enter the new  city     ")
                    speaker.runAndWait()
                    contacts[ph][3] = new
                    print("~" * 60)
                else:
                    print("INVALID CHOICE!!!!!!")
                    speaker.say("BOSS your choice is invalid       ")
                    speaker.runAndWait()
        elif choice == 3:
            speaker.say("BOSS you choosed to remove a contact")
            speaker.runAndWait()
            ph = input("ENTER PHONE NUMBER TO BE REMOVE:-")
            speaker.say("enter the phone number that you want to remove  ")
            speaker.runAndWait()
            if ph in contacts:
                contacts[ph] = None
                print("PHONE NUMBER REMOVE SUCCESSFULY")
                speaker.say("boss the phone number removed successfuly")
                speaker.runAndWait()
                print("~" * 60)
            else:
                print("PHONE NUMBER IS NOT IN YOUR DIRECTORY")
                speaker.say("boss the phone number is not present in your directory ")
                speaker.runAndWait()
        elif choice == 4:
            speaker.say("BOSS you choosed to search a contact")
            speaker.runAndWait()
            ph = input("ENTER PHONE NUMBER TO BE SEARCHED:-")
            speaker.say("enter the phone number that you want to search  ")
            speaker.runAndWait()
            if ph in contacts:
                print(contacts[ph])
                print("~" * 60)
            else:
                print("PHONE NUMBER NOT FOUND!!!!")
                speaker.say("boss the phone number not found ")
                speaker.runAndWait()
        elif choice == 5:
            break
    print("~" * 60)
    speaker.say("boss here is your contact list")
    speaker.runAndWait()
    print("HERE IS YOUR CONTACT LIST")
    print(contacts)
    print("~" * 60)
    speaker.say("please rate us out of 5")
    speaker.runAndWait()
    rating = int(input("PLEASE RATE US (OUT OF 5):-"))
    if rating == 1:
        print("REALY SORRY FOR THE INCONVINENCE!!!")
        print("PLEASE SUGGESTS THE UPGRADES TO THE OWNER .....TELEGRAM ID:-@Ni3_Accuracy_Matter_Rank_Not")
        speaker.say("REALY SORRY FOR THE INCONVINENCE")
        speaker.runAndWait()
        speaker.say("PLEASE SUGGESTS THE UPGRADES TO THE OWNER  nitin sharma ")
        speaker.runAndWait()
    elif rating == 2:
        print("I AM SORRY FOR DISAPOINTING YOU")
        print("PLEASE SUGGESTS THE UPGRADES TO THE OWNER .....TELEGRAM ID:-@Ni3_Accuracy_Matter_Rank_Not")
        speaker.say("I AM SORRY FOR DISAPOINTING YOU")
        speaker.runAndWait()
        speaker.say("PLEASE SUGGESTS THE UPGRADES TO THE OWNER  nitin sharma ")
        speaker.runAndWait()
    elif rating == 3:
        print("I HOPE YOU WILL HELP US TO MAKE THIS MORE INTERACTIVE")
        print("PLEASE SUGGESTS THE UPGRADES TO THE OWNER .....TELEGRAM ID:-@Ni3_Accuracy_Matter_Rank_Not")
        speaker.say("I HOPE YOU WILL HELP US TO MAKE THIS MORE INTERACTIVE")
        speaker.runAndWait()
        speaker.say("PLEASE SUGGESTS THE UPGRADES TO THE OWNER  nitin sharma ")
        speaker.runAndWait()
    elif rating == 4:
        print("THANK YOU FOR RATING US ..I AM HAPPY TO HELP YOU")
        print("YOU MAY SUGGEST SOME UPGRADES TO THE OWNER(IF NEEDED) .....TELEGRAM ID:-@Ni3_Accuracy_Matter_Rank_Not")
        speaker.say("THANK YOU FOR RATING US  I AM HAPPY TO HELP YOU")
        speaker.runAndWait()
        speaker.say("PLEASE SUGGESTS THE UPGRADES TO THE OWNER  nitin sharma ")
        speaker.runAndWait()
    elif rating == 5:
        print("THANK YOU SO MUCH FOR RATING US 5 .....HAPPY TO HELP YOU BOSS")
        speaker.say("THANK YOU SO MUCH FOR RATING US 5    HAPPY TO HELP YOU BOSS")
        speaker.runAndWait()
    print("~" * 60)
    print("PLEASE VISIT AGAIN.....I WILL DEFINATELY MAKE YOU FEEL AWESOME")
    speaker.say("PLEASE VISIT AGAIN     I WILL DEFINATELY MAKE YOU FEEL AWESOME")
    speaker.runAndWait()
else:
    while True:
        print("ENTER 1:-ADD A NEW CONTACT")
        print("ENTER 2:-MODIFY A CONTACT")
        print("ENTER 3:-REMOVE A CONTACT")
        print("ENTER 4:-SEARCH A CONTACT")
        print("ENTER 5:-EXIT")

        choice = int(input("ENTER YOUR CHOICE :-"))
        if choice == 1:
            ph = input("ENTER THE PHONE NUMBER:-")
            while len(ph) != 10:
                print("BOSS THE NUMBER YOU ENTERED HAS LESS THAN 10 DIGITS")
            Fname = input("ENTER FIRST NAME:-")
            Lname = input("ENTER LAST NAME:-")
            address = input("ENTER THE ADDRESS:-")
            city = input("ENTER CITY NAME:-")
            contacts[ph] = [Fname, Lname, address, city]
            print("Processing ",end=' ')
            for i in range(10):
                print(".",end=' ')
                time.sleep(1)
            print()
            print("THE CONTACT IS ADDED SUCCESSFULLY")
            print("~" * 60)
        elif choice == 2:
            ph = input("ENTER THE PHONE NUMBER TO MODIFY THE DETAILS:-")
            if ph in contacts:
                print("PRESS 1:-TO CHANGE FIRST NAME")
                print("PRESS 2:-TO CHANGE LAST NAME")
                print("PRESS 3:-TO CHANGE ADDRESS")
                print("PRESS 4:-TO CHANGE CITY NAME")
                option = int(input("CHOOSE YOUR OPTION:-"))
                if option == 1:
                    new = input("ENTER 1ST NAME:-")
                    contacts[ph][0] = new
                    print("~" * 60)
                elif option == 2:
                    new = input("ENTER LAST NAME:-")
                    contacts[ph][1] = new
                    print("~" * 60)
                elif option == 3:
                    new = input("ENTER NEW ADDRESS:-")
                    contacts[ph][2] = new
                    print("~" * 60)
                elif option == 4:
                    new = input("ENTER CITY NAME:-")
                    contacts[ph][3] = new
                    print("~" * 60)
                else:
                    print("INVALID CHOICE!!!!!!")
        elif choice == 3:
            ph = input("ENTER PHONE NUMBER TO BE REMOVE:-")
            if ph in contacts:
                contacts[ph] = ""
                print("PHONE NUMBER REMOVE SUCCESSFLY")
                print("~" * 60)
            else:
                print("PHONE NUMBER IS NOT IN THE")
        elif choice == 4:
            ph = input("ENTER PHONE NUMBER TO BE SEARCHED:-")
            if ph in contacts:
                print(contacts[ph])
                print("~" * 60)
            else:
                print("PHONE NUMBER NOT FOUND!!!!")
        elif choice == 5:
            break
    print("~" * 60)
    print("HERE IS YOUR CONTACT LIST")
    print(contacts)
    print("~" * 60)
    rating = int(input("PLEASE RATE US (OUT OF 5):-"))
    if rating == 1:
        print("REALY SORRY FOR THE INCONVINENCE!!!")
        print("PLEASE SUGGESTS THE UPGRADES TO THE OWNER .....TELEGRAM ID:-@Ni3_Accuracy_Matter_Rank_Not")
    elif rating == 2:
        print("I AM SORRY FOR DISAPOINTING YOU")
        print("PLEASE SUGGESTS THE UPGRADES TO THE OWNER .....TELEGRAM ID:-@Ni3_Accuracy_Matter_Rank_Not")
    elif rating == 3:
        print("I HOPE YOU WILL HELP US TO MAKE THIS MORE INTERACTIVE")
        print("PLEASE SUGGESTS THE UPGRADES TO THE OWNER .....TELEGRAM ID:-@Ni3_Accuracy_Matter_Rank_Not")
    elif rating == 4:
        print("THANK YOU FOR RATING US ..I AM HAPPY TO HELP YOU")
        print("YOU MAY SUGGEST SOME UPGRADES TO THE OWNER(IF NEEDED) .....TELEGRAM ID:-@Ni3_Accuracy_Matter_Rank_Not")
    elif rating == 5:
        print("THANK YOU SO MUCH FOR RATING US 5 .....HAPPY TO HELP YOU BOSS")
    print("~" * 60)
    print("PLEASE VISIT AGAIN.....I WILL DEFINATELY MAKE YOU FEEL AWESOME")