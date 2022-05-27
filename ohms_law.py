#!/usr/bin/env python3
# Created by: Hertz
# Created on: May, 27, 2022
# This program asks the user to enter the potential difference in Volts,the
# resistance offered by the wire and calculates the  current passing through


def calculates_current(volts, resistance):

    # calculation of finding the current
    current = volts/resistance
    print("the current is {:,.2f} Amps.".format(current))


def main():
    print("This program finds the current  passing through the material.")

    # ask the user to enter the the pontential difference and the resistance
    user_volts = input("Enter the pontential difference(V):")
    user_resist = input("Enter the resistance of the wire:")

    try:
        # convert string to float.
        user_v = float(user_volts)
        user_r = float(user_resist)

        if user_v > 0 and user_r > 0:
            calculates_current(user_v, user_r)
        else:
            print("Enter positive numbers only...")

    except Exception:
        print("Invalid input , Please enter numbers only")


if __name__ == "__main__":
    main()
