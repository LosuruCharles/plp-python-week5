import math

def tables_needed(people, seats):
    return math.ceil(people/seats)
    # Return people divided by seats, rounded UP with math.ceil()

def welcome(name):
    return f"Welcome to PLP , {name}!"
    # Return "Welcome to PLP, NAME!" using the name

if __name__ == "__main__":
    print(tables_needed(10, 4))