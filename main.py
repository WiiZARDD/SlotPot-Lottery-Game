import time
import random
import os
import pickle
from colorama import Fore, Back, Style

class Player:
    def __init__(self):
        self.tokens = 50

    def win_tokens(self, win):
        self.tokens += win

    def lose_tokens(self, lose):
        if lose > self.tokens:
            return "You don't have enough tokens!"
        else:
            self.tokens -= lose

class SlotMachine:
    wheels = ["🍒", "🍋", "🍊", "🍇", "🔔", "💰", "7️⃣", "💲"]  # Added wild slot

    def draw_machine(self, slot1, slot2, slot3, slot4):  # Increased reel size
        print('{:^45}'.format('-----------------'))
        print('{:^45}'.format('|   |   |   |   |'))
        print('{:^45}'.format('| {} | {} | {} | {} |'.format(slot1, slot2, slot3, slot4)))
        print('{:^45}'.format('|   |   |   |   |'))
        print('{:^45}'.format('-----------------'))

    def spin_machine(self):
        for _ in range(10):
            slot1 = random.choice(self.wheels)
            slot2 = random.choice(self.wheels)
            slot3 = random.choice(self.wheels)
            slot4 = random.choice(self.wheels)  # Increased reel size
            os.system('cls' if os.name == 'nt' else 'clear')
            print()
            self.draw_machine(slot1, slot2, slot3, slot4)
            print(Fore.CYAN + '{:^45}'.format('Spinning...'))
            time.sleep(0.1)
        return [slot1, slot2, slot3, slot4]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def save_game(player):
    with open('save.dat', 'wb') as f:
        pickle.dump(player, f)

def load_game():
    try:
        with open('save.dat', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return Player()

def evaluate_spin(spin, player):
  if len(set(spin)) == 1:  # All slots are of the same type
    if spin[0] == "💰":
      player.win_tokens(100)
      print(Fore.GREEN + '{:^45}'.format('JACKPOT! You win 100 tokens!'))
    elif spin[0] == "7️⃣":
      player.win_tokens(70)
      print(Fore.GREEN + '{:^45}'.format('LUCKY 7! You win 70 tokens!'))
    elif spin[0] == "🔔":
      player.win_tokens(50)
      print(Fore.GREEN + '{:^45}'.format('THREE BELLS! You win 50 tokens!'))
    elif spin[0] == "🍇":
      player.win_tokens(30)
      print(Fore.GREEN + '{:^45}'.format('FULL GRAPES! You win 30 tokens!'))
    elif spin[0] == "🍊":
      player.win_tokens(20)
      print(Fore.GREEN + '{:^45}'.format('ORANGE CRAZE! You win 20 tokens!'))
    elif spin[0] == "🍋":
      player.win_tokens(10)
      print(Fore.GREEN + '{:^45}'.format('LEMON SURPRISE! You win 10 tokens!'))
    elif spin[0] == "🍒":
      player.win_tokens(5)
      print(Fore.GREEN + '{:^45}'.format('CHERRY BONUS! You win 5 tokens!'))
    elif spin[0] == "💲":
      player.win_tokens(200)
      print(Fore.GREEN + '{:^45}'.format('WILD JACKPOT! You win 200 tokens!'))
  else:
    player.lose_tokens(1)
    print(Fore.RED + '{:^45}'.format('No match. You lose 1 token.'))

def print_guide():
    print('{:^45}'.format('Guide to Winning!'))
    print('{:^45}'.format('~~~~~~~~~~~~~~~~'))
    print('{:^45}'.format('4 x 💰 : JACKPOT! You win 100 tokens!'))
    print('{:^45}'.format('4 x 7️⃣ : LUCKY 7! You win 70 tokens!'))
    print('{:^45}'.format('4 x 🔔 : THREE BELLS! You win 50 tokens!'))
    print('{:^45}'.format('4 x 🍇 : FULL GRAPES! You win 30 tokens!'))
    print('{:^45}'.format('4 x 🍊 : ORANGE CRAZE! You win 20 tokens!'))
    print('{:^45}'.format('4 x 🍋 : LEMON SURPRISE! You win 10 tokens!'))
    print('{:^45}'.format('4 x 🍒 : CHERRY BONUS! You win 5 tokens!'))
    print('{:^45}'.format('4 x 💲 : WILD JACKPOT! You win 200 tokens!'))
    print("-------------------------")
    input("{:^45}".format("Press enter to go back."))

def main():
    player = load_game()
    slot_machine = SlotMachine()
    
    while True:  
        clear()
        print('{:^45}'.format('Welcome to SlotPot!'))
        print('{:^45}'.format('You currently have {} tokens.'.format(str(player.tokens))))
        print('{:^45}'.format('Press enter to spin, type Q to quit or G for Guide.'))
        x = input()
        if x.lower() == 'q':
            save_game(player)
            break
        elif x.lower() == 'g':
            print_guide()
            continue
        elif player.tokens < 1:
            print(Fore.RED + '{:^45}'.format('You do not have enough tokens to play.'))
            break
        spin = slot_machine.spin_machine()
        print()
        evaluate_spin(spin, player)
        time.sleep(2)

if __name__ == "__main__":
    main()
