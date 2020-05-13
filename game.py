import random
comp_points = 0
users_points = 0
while users_points != 3 and comp_points != 3:
    comp_move = random.choice(["stone", "paper", "scissors"])
    users_move = input('What do you choose: stone,paper or scissors? ')
    print(f"Computer's Move: {comp_move}")
    print(f"Your move: {users_move}")
    if users_move != "stone" and users_move != "paper" and users_move != "scissors":
        print("Enter a valid move: stone, paper or scissors :)")
    else:
        if comp_move == "stone":
            if users_move.lower() == "stone":
                print("It's a draw!!")
                print(f"Computers score: {comp_points}")
                print(f"Your score: {users_points}")
            if users_move.lower() == "paper":
                print("You win!!")
                users_points += 1
            if users_move.lower() == "scissors":
                print("Better Luck next time!!")
                comp_points += 1
        if comp_move == "paper":
            if users_move.lower() == "stone":
                print("You lose!!")
                comp_points += 1
            if users_move.lower() == "paper":
                print("Draw!!")
                print(f"Computers score: {comp_points}")
                print(f"Your score: {users_points}")
            if users_move.lower() == "scissors":
                print("Yipeee!!")
                users_points += 1
        if comp_move == "scissors":
            if users_move.lower() == "stone":
                users_points += 1
                print(f"You win!! Just {3-users_points} to the victory :D")
            if users_move.lower() == "paper":
                print("Better Luck next chance!!")
                comp_points += 1
            if users_move.lower() == "scissors":
                print("Draw!!")
                print(f"Computers score: {comp_points}")
                print(f"Your score: {users_points}")
print(f"Computers final score: {comp_points}")
print(f"Your final score: {users_points}")
if users_points == 3:
    print("Winner!! Lets play again :)")
else:
    print("Aww, you lose, lets play again :P")
