import random

def play():
    user = input("Rock, Paper or Scissors?")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return f'It is a tie! You both choose {user}'

    if is_win(user, computer):
        return f"You won! You choose {user} and the oppenent choose {computer}"
    return f'You lost! You choose {user} and the oppenent choose {computer}'
def is_win(player, oppenent):
    if (player == 'r' and oppenent == 's') or (player == 's' and oppenent == 'p') or (player == 'p' and oppenent == 'r'):
        return True    

print(play())