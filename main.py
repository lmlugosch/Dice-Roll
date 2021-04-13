# Demonstrate the normal distribution of rolling multiple 6-sided dice
import random
import matplotlib.pyplot as plt


def get_dice():
    while True:
        try:
            num_dice = int(input("Enter number of dice to roll (1 - 10): "))
            if 1 <= num_dice <= 10:
                break
            else:
                print("Number must be between 1 and 10")
        except ValueError:
            print("Invalid entry. Please enter an integer between 1 and 10")
    return num_dice


def get_rolls():
    while True:
        try:
            num_rolls = int(input("Enter number of dice rolls (1 - 1,000,000): "))
            if 1 <= num_rolls <= 1000000:
                break
            else:
                print("Number must be between 1 and 1,000,000")
        except ValueError:
            print("Invalid entry. Please enter an integer between 1 and 1,000,000")
    return num_rolls


def dice_roll(num_dice, num_rolls):
    roll_list = []
    for i in range(num_rolls):
        roll_sum = 0
        for j in range(num_dice):
            roll = random.randint(1, 6)
            roll_sum += roll
        roll_list.append(roll_sum)
    return roll_list


def roll_freq(num_dice, roll_list):
    freq = []
    for i in range(num_dice, num_dice*6+1):
        freq.append(roll_list.count(i))
    return freq


def plot_freq(num_dice, freq):
    print(f'The frequency of each rolled sum was: \n{freq}')
    x_axis = []
    for i in range(num_dice, num_dice*6+1):
        x_axis.append(i)
    y_axis = freq
    fig, ax = plt.subplots()
    plt.bar(x_axis, y_axis, tick_label=x_axis)
    ax.set_title("Dice Roll Frequency Distribution", fontsize=24)
    ax.set_xlabel("Sum of Rolled Dice", fontsize=14)
    ax.set_ylabel("Number of Times Rolled", fontsize=14)
    ax.yaxis.grid(True, linestyle='--', which='major', color='gray', alpha=0.25)
    plt.show()


def main():
    dice = get_dice()
    rolls = get_rolls()
    roll_list = dice_roll(dice, rolls)
    freq = roll_freq(dice, roll_list)
    plot_freq(dice, freq)


main()

