# Pokémon Binder Organizer

TOTAL_POKEMON = 151
BINDER_CAPACITY = 24
binder = [None] * BINDER_CAPACITY

def map_pokedex_to_slot(num):
    return (num - 1) % BINDER_CAPACITY

def get_position(index):
    page = index // 4 + 1
    row = (index % 4) + 1
    column = (index % 4) + 1
    return page, row, column

def show_menu():
    print("\n=== Pokémon Binder Menu ===")
    print("1. Insert a Pokémon")
    print("2. Clear the binder")
    print("3. Show binder status")
    print("4. Exit")

def insert_card():
    try:
        number = int(input("Enter a Pokédex number (1-151): "))
        if number < 1 or number > TOTAL_POKEMON:
            print(" That number is outside the allowed range.")
            return
        spot = map_pokedex_to_slot(number)
        if binder[spot] is not None:
            print(f" Spot already has Pokédex #{binder[spot]}.")
            return
        binder[spot] = number
        page, row, column = get_position(spot)
        print(f"\nCard added at:")
        print(f"  Page {page} | Row {row} | Column {column}")
        print(f" Pokédex #{number} was placed in the binder.")
    except ValueError:
        print(" Please enter a valid number.")

def clear_binder():
    print("\n WARNING: This will remove all cards from your binder!")
    response = input("Type YES to confirm or anything else to cancel: ").strip().upper()
    if response == "YES":
        for i in range(BINDER_CAPACITY):
            binder[i] = None
        print(" Binder has been reset.")
    else:
        print("Reset canceled.")

def display_binder():
    print("\n Current Binder Content:")
    filled = 0
    for idx, val in enumerate(binder):
        if val is not None:
            page, row, column = get_position(idx)
            print(f"Pokédex #{val} — Page {page}, Row {row}, Column {column}")
            filled += 1
    print(f"\nTotal cards stored: {filled}")
    print(f"Progress: {filled / BINDER_CAPACITY * 100:.1f}% complete")

def main():
    while True:
        show_menu()
        option = input("Pick an option (1-4): ").strip()
        if option == "1":
            insert_card()
        elif option == "2":
            clear_binder()
        elif option == "3":
            display_binder()
        elif option == "4":
            print(" Goodbye! Thanks for organizing your Pokémon cards.")
            break
        else:
            print(" Invalid choice. Try again.")

# Start the app
if __name__ == "__main__":
    main()
