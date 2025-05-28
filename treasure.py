print("""
████████╗██████╗ ███████╗███████╗██████╗ ███████╗
╚══██╔══╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝
   ██║   ██████╔╝█████╗  █████╗  ██████╔╝█████╗  
   ██║   ██╔═══╝ ██╔══╝  ██╔══╝  ██╔═══╝ ██╔══╝  
   ██║   ██║     ███████╗███████╗██║     ███████╗
   ╚═╝   ╚═╝     ╚══════╝╚══════╝╚═╝     ╚══════╝
             🏴‍☠️  Treasure Island 🏝️
""")

print("Your mission is to find the hidden treasure.")

choice1 = input("Do you want to go Left or Right? ").strip().lower()
if choice1 == "left":
    choice2 = input("You arrive at a river. Do you Swim or Wait? ").strip().lower()
    if choice2 == "wait":
        choice3 = input("Three doors appear: Red, Blue, and Yellow. Which one do you choose? ").strip().lower()
        if choice3 == "yellow":
            print("🎉 Congratulations! You found the treasure! 🪙")
        elif choice3 == "red":
            print("🔥 The room was full of fire. Game Over.")
        elif choice3 == "blue":
            print("🧊 You were trapped in an icy tomb. Game Over.")
        else:
            print("🚪 That door doesn't exist. Game Over.")
    else:
        print("🐊 You were eaten by crocodiles. Game Over.")
else:
    print("🕳️ You fell into a hole. Game Over.")
