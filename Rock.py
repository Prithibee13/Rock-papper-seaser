#I could not load the given templates in codeskluptor for unknwon reasons in any of browsers in my pc. I gave a massage to discussion fourms about it but nobody give any reply. I use incontigo mode in every browsers but result is same.
# So thats why i use these comment my own
import random #import random module
# first helper function
def Name_to_number(name):
    # Checking String and assgining value for each one
    if name == "rock":
        m = 0 # 0 for rock
    elif name == "spock":
        m = 1 # 1 for Spock
    elif name == "paper":
        m = 2 # 2 for paper
    elif name == "lizard":
        m = 3 # 3 for lizard
    elif name == "scissors":
        m = 4 # 4 for scissors
    #returning the assgining value
    return m

def Number_to_name(number):
    if number == 0:
        s = "rock" # 0 for Rock
    elif number == 1:
        s = "spock" # 1 for spock
    elif number == 2:
        s = "paper" # 2 for papper
    elif number == 3:
        s = "lizard" # 3 for papper
    elif number == 4:
        s = "scissors" # 4 for papper
    else:
        s = "Wrong Name" #if parameter out of 4
    # returning the string
    return s
#Creating main rpsls() function
def rpsls(names):
    print("")
    print("Player Chooses", names) #print the player choice
    k = Name_to_number(names) #call the Name_to_Number function
    computer_number = random.randrange(0,5) #generate Random number
    print("Computer Chooses", Number_to_name(computer_number)) #print the computer choicse by calling Number_to_Name function
    l = computer_number - k #find the Difference between computer choice and player choice
    t = abs(l)
    #implementetion
    if l == 0:
        print("Player and computer tie!")
    elif k == 0:
        if t == 4 or t == 3:
            print("Player wins!")
        else:
            print("Computer wins!")
    elif k == 1:
        if l == -1 or l == 3:
            print("Player wins!")
        else:
            print("Computer wins!")
    elif k == 2:
        if l == -1 or l == -2:
            print("Player wins!")
        else:
            print("Computer wins!")
    elif k == 3 or k == 4:
        if l == -1 or l == -2:
            print("Player wins!")
        else:
            print("Computer wins!")
    print("")

#calling the main rpsls() function for severel time

s = input()
rpsls(s)