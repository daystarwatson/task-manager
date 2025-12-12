def greet_user():
    print("welcome! good day, dear passenger.")


def pick_ups():
    nigeria_pick_ups = ["lagos", "rivers",
                        "abia", "abuja", "kano", "enugu", "imo"]
    pick_ups = input("please, enter a pick up location: ").lower()
    if pick_ups not in nigeria_pick_ups:
        print("sorry, we dont operate outside nigria. try again")
        pick_ups = input("please, enter a pick up location: ").lower()

    return pick_ups


def nigeria_drop_offs():
    nigeria_drop_offs = ["ikeja", "port_harcourt",
                         "fct", "calabar", "oron", "asaba"]
    drop_off = input("please, enter your drop off location: ")
    if drop_off not in nigeria_drop_offs:
        print("sorry, drop off location is outside of nigeria. try again")
        drop_off = input("please, enter your drop off location: ")
    return drop_off


def start_ride():
    start_ride = input("should we start the ride? (yes/no/hold on): ").lower()

    if start_ride == "yes":
        print("ride started, driving to your destination now")

    elif start_ride == "no":
        print("ride has not started, waiting for you to start the ride")
        start_ride = input(
            "should we start the ride? (yes/no/hold on): ").lower()

    else:
        start_ride == "hold on"
        print("okay, say go when you want me to go")
        start_ride = input(
            "should we start the ride? (go): ").lower()
    return start_ride


def payments(ride_price):
    print(f"the price for the ride is ${ride_price}")
    amount = int(input("enter the amount for the payment of the ride: $"))
    if amount < ride_price:
        print("amount is insufficient. please enter the right amount")
        amount = int(input("enter the amount for the payment of the ride: $"))

    elif amount == ride_price:
        print("payment successful. exact amount thank you")

    else:
        amount > ride_price
        change = amount - ride_price
        print("payment succesful, your change is:", change)
    return amount


def ask_for_tips():
    tip = input(
        "would you like to give a tip? type 'AMOUNT' or type 'NO': ").lower()

    if tip == "no":
        print("thank you for riding with us")
    else:
        tip = int(tip)
        print("thank you so much for the tip of $", tip)

        print("have a lovely day")


def main_program():

    greet_user()

    pick_ups()

    nigeria_drop_offs()

    start_ride()

    payments(5000)

    ask_for_tips()


main_program()
