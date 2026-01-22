"""
Slot Machine Game
-----------------
A simple command-line slot machine simulator inspired by the original 1891 gambling machine.

Features:
- Simulates a 3-reel slot machine using random symbols.
- Symbols include: Cherry (🍒), Grapes (🍇), Watermelon (🍉), and Seven (7️⃣).
- The player wins a "Jackpot! 💰" only if three Sevens (7️⃣) appear in a row.
- Includes a game loop allowing the player to play multiple rounds.

Usage:
Run the script and follow the prompts. Type 'Y' to spin again or any other key to exit.
"""
import random
symbols = ['🍒', ' 🍇', '🍉', '7️⃣']
def play():
    #1. Spin the wheel
    results = random.choices(symbols , k=3)

    #2.Display result
    print(f"{results[0]} | {results[1]} | {results[2]}")

    #3.Check if you hit the jackpot :
    if results == ['7️⃣', '7️⃣', '7️⃣']:
        print("Jackpot! 💰")
    else :
        print("Thanks for playing!")



### ==== The main game loop ====
while True :
    play()

    again = input("Play again ? (Y/N) : ").upper()

    if again != 'Y' :
        print("Walking away with your money!! .. Smart Choice!")
        break

