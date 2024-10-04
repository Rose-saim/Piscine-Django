# all_in.py
import sys

def find_state_or_capital(query):
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

    elements = [e.strip().lower() for e in query.split(',') if e.strip()]
    if len(elements) == 0:
        return

    for element in elements:
        found = False
        # Check if it's a state
        for state, code in states.items():
            if state.lower() == element:
                print(f"{capital_cities[code]} is the capital of {state}")
                found = True
                break
        # Check if it's a capital
        if not found:
            for code, city in capital_cities.items():
                if city.lower() == element:
                    for state, state_code in states.items():
                        if state_code == code:
                            print(f"{city} is the capital of {state}")
                            found = True
                            break
        # If neither
        if not found:
            print(f"{element} is neither a capital city nor a state")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        find_state_or_capital(sys.argv[1])
