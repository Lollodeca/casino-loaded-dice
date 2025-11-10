import random
import math

print("🎰 Welcome, High Roller, to the Casino of your dreams! 🎲")
print("Here you can try your luck with fair dice or dare with loaded dice… but beware: math never forgives!")
print("Every 6 pays you 5 times your bet… otherwise the house wins. May luck be on your side! 🍀\n")

# Choose dice
while True:
    dice = input("Choose your dice - 1) Fair dice  2) Loaded dice: ")
    if dice in ["1", "2"]:
        break
    else:
        print("❌ Invalid choice. Enter 1 or 2, High Roller!")

# If loaded dice, choose probability of 6
if dice == "2":
    while True:
        try:
            cheat_prob = float(input("Enter the probability of rolling a 6 (1-100%): "))
            if 1 <= cheat_prob <= 100:
                break
            else:
                print("⚠️ Enter a number between 1 and 100.")
        except ValueError:
            print("❌ Invalid number.")

# Choose bet
while True:
    try:
        bet = int(input("💰 Enter your bet: "))
        if bet > 0:
            break
        else:
            print("⚠️ Bet must be positive. Don't mess with the house!")
    except ValueError:
        print("❌ Error: enter a valid integer. The house is watching...")

# Statistical parameters
z_confidence = 1.96
p0 = 1/6
error_margin = 0.10
min_simulations = int((z_confidence * math.sqrt(p0 * (1 - p0)) / error_margin) ** 2)

# Choose number of simulations
while True:
    try:
        nSim = int(input("🎲 How many simulations do you want to play? "))
        if nSim > 0:
            break
        else:
            print("⚠️ You must play at least once! The house won't let you off...")
    except ValueError:
        print("❌ Enter a valid integer, don't try to cheat the casino!")

# Play simulations
balance = 0
k = 0
if dice == "1":
    for i in range(nSim):
        throw = random.randint(1, 6)
        if throw == 6:
            balance += bet * 5
            k += 1
        else:
            balance -= bet
elif dice == "2":
    for i in range(nSim):
        throw = random.randint(1, 100)
        if throw <= cheat_prob:
            balance += bet * 5
            k += 1
        else:
            balance -= bet

# Check winnings
if nSim >= min_simulations:
    n = nSim
    p_hat = k / n
    z_score = (p_hat - p0) / math.sqrt(p0 * (1 - p0) / n)
    
    if z_score > z_confidence:
        print(f"\n⚠️ SUSPICIOUS! Math has caught your loaded dice!")
        print(f"All winnings have been confiscated by the house. 💀")
        print(f"You lost {abs(balance)}€, final balance: 0 🃏")
    else:
        if balance >= 0:
            print(f"\n🎉 The dice seem fair and you won!")
            print(f"Profit: +{balance}€, final balance: {balance} 💰")
        else:
            print(f"\n😢 The dice seem fair, but the house has won.")
            print(f"You lost {abs(balance)}€, final balance: 0 🥀")
else:
    if balance >= 0:
        print(f"\n⚠️ The house can't fully verify, but you made a profit.")
        print(f"Profit: +{balance}€, final balance: {balance} 💰")
    else:
        print(f"\n⚠️ The house can't fully verify, but you lost.")
        print(f"You lost {abs(balance)}€, final balance: 0 🥀")
