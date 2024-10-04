# capital_city.py
import sys

def find_capital(state):
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    state_code = states.get(state)
    if state_code:
        print(capital_cities.get(state_code))
    else:
        print("Unknown state")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        find_capital(sys.argv[1])
