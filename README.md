# Casino Dice Simulator 🎲

A fun Python dice simulator where you can play with **fair or loaded dice**. Roll a **6** to win **5× your bet**, but beware: if your loaded dice is too lucky, the house may catch it! The game includes **statistical checks** to detect cheating.

## Features
- Choose between **fair or loaded dice**
- Set your **bet amount**
- Simulate multiple rounds
- Detects suspicious loaded dice using **z-score statistical analysis**

## How It Works: Z-Score Detection 📊
The casino uses a **z-score test** to detect if your dice is suspiciously lucky:

- **Z-score** measures how far your results deviate from what's expected with a fair dice.
- A fair dice has a **1/6 probability (~16.67%)** of rolling a 6.
- If you roll too many 6s, the **z-score increases**.
- When the z-score exceeds **1.64** (90% confidence threshold), the house suspects cheating and confiscates your winnings! 💀

**Formula:**  
z = (p̂ - p₀) / √(p₀(1-p₀)/n)

markdown
Copia codice

Where:  
- `p̂` = observed probability of rolling 6  
- `p₀` = expected probability (1/6)  
- `n` = number of simulations  

> Note: The casino needs a **minimum number of simulations** to reliably detect cheating. Too few rolls, and you might slip through undetected! 🎰

## How to Play
1. Run the Python script:  
   ```bash
   python dice_game.py
Choose the dice type:

1 = Fair dice

2 = Loaded dice (set probability of 6)

Enter your bet amount

Enter the number of simulations

See your final balance and if the dice was fair or caught cheating

Requirements
Python 3.x
