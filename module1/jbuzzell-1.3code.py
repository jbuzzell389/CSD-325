# James Buzzell
# 10/26/2025
# Assignment 1.3 code


def drunk():
    beer_drunk = input("\nAm I drunk? Yes(y) or No(n)\n\n")

    if (beer_drunk == "Yes") or (beer_drunk == "yes") or (beer_drunk == "Y") or (beer_drunk == "y"):
        print("\nI'm going to bed\n")
    elif (beer_drunk == "No") or (beer_drunk == "no") or (beer_drunk == "N") or (beer_drunk == "n"):
        print("\nTime to get to the supermarket to buy more beer.\n")
        num_bottles = int(input("How many bottles of beer are on the wall?\n\n"))
        countdown(num_bottles)
    else:
        print("\nPlease try again")
        drunk()

def countdown(num_bottles):
    if (num_bottles >= 1):
        for i in range(num_bottles, 0, -1):
            print(f"\n{i} bottle(s) of beer on the wall, {i} bottle(s) of beer.")
            print(f"Take one down and pass it around, {i - 1} bottle(s) of beer on the wall.")
        drunk()
    elif (num_bottles == 0):
        print("There aren't any bottles of beer on the wall.")
        drunk()

try:
    num_bottles = int(input("How many bottles of beer are on the wall?\n\n"))
    (countdown(int(num_bottles)))
except ValueError:
    print("\nWhole bottles only. If there aren't any bottles, enter '0'.\n")
    num_bottles = int(input("How many bottles of beer are on the wall?\n\n"))
    countdown(num_bottles)