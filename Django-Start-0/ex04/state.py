# state.py
import sys

def find_state(capital):
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

    state_code = None
    for code, city in capital_cities.items():
        if city.lower() == capital.lower():
            state_code = code
            break

    if state_code:
        for state, code in states.items():
            if code == state_code:
                print(state)
                return
    print("Unknown capital city")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        find_state(sys.argv[1])
