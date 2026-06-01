#   RANDOM PASSWORD GENERATOR - Oasis Infobyte Internship
#   Project 5: Simple Password Generator

import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    """
    Generate a random password based on user preferences.
    
    Args:
        length (int): Password length
        use_letters (bool): Include letters (a-z, A-Z)
        use_numbers (bool): Include numbers (0-9)
        use_symbols (bool): Include symbols (!@#$...)
    
    Returns:
        str: Generated password
    """
    character_pool = ""

    if use_letters:
        character_pool += string.ascii_letters   # a-z aur A-Z
    if use_numbers:
        character_pool += string.digits          # 0-9
    if use_symbols:
        character_pool += string.punctuation     # !@#$%^&*...

    if not character_pool:
        return None

    password = []

    if use_letters:
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.ascii_lowercase))
    if use_numbers:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    remaining = length - len(password)
    for _ in range(remaining):
        password.append(random.choice(character_pool))

    random.shuffle(password)

    return "".join(password)

def check_password_strength(password):
    """Evaluate and return password strength"""
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Capital letters add karein")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Small letters add karein")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Numbers add karein")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Symbols add karein")

    if score <= 3:
        strength = " Kamzor (Weak)"
        color_hint = "❌"
    elif score <= 5:
        strength = " Theek Theek (Medium)"
        color_hint = "⚠️"
    else:
        strength = " Mazboot (Strong)"
        color_hint = "✅"

    return f"{color_hint} {strength}", feedback

def get_yes_no(prompt):
    """Get yes or no answer from user"""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ['y', 'yes', 'ha', 'haan', '1']:
            return True
        elif answer in ['n', 'no', 'nahi', 'na', '0']:
            return False
        else:
            print("   Sirf 'y' (haan) ya 'n' (nahi) daalen!")

def get_valid_int(prompt, min_val, max_val):
    """Get valid integer input within range"""
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"   {min_val} aur {max_val} ke beech number daalen!")
        except ValueError:
            print("    Sirf number daalen!")

def main():
    print("\n" + "="*55)
    print("     RANDOM PASSWORD GENERATOR - Oasis Infobyte")
    print("="*55)
    print("  Apke liye mazboot passwords generate karega!")
    print("="*55)

    while True:
        print("\n  MENU:")
        print("  1. Naya Password Banayein")
        print("  2. Multiple Passwords Banayein")
        print("  3. Exit")
        print("-"*35)

        choice = input("Apna choice (1/2/3): ").strip()

        if choice in ["1", "2"]:

            print("\n  PASSWORD SETTINGS:")
            print("-"*35)

            length = get_valid_int(
                "  ➤  Password kitni lambi chahiye? (4-128): ",
                min_val=4, max_val=128
            )

            print("\n   Kon se characters shamil karein?")
            use_letters = get_yes_no("  ➤  Letters (A-Z, a-z)? (y/n): ")
            use_numbers = get_yes_no("  ➤  Numbers (0-9)? (y/n): ")
            use_symbols = get_yes_no("  ➤  Symbols (!@#$%)? (y/n): ")

            if not (use_letters or use_numbers or use_symbols):
                print("\n    Kam se kam ek option zaroor select karein!")
                continue

            if choice == "2":
                count = get_valid_int("\n  ➤  Kitne passwords chahiye? (1-20): ", 1, 20)
            else:
                count = 1

            print("\n" + "="*55)
            print("          GENERATED PASSWORDS")
            print("="*55)

            for i in range(count):
                password = generate_password(length, use_letters, use_numbers, use_symbols)

                if password:
                    strength, tips = check_password_strength(password)
                    if count > 1:
                        print(f"\n  Password #{i+1}:")
                    print(f"    {password}")
                    print(f"    Mazbooti: {strength}")
                    if tips:
                        print(f"   Tip: {', '.join(tips)}")
                else:
                    print("    Password generate nahi ho saka!")

            print("\n" + "="*55)
            print("    TIPS:")
            print("  • Is password ko kisi safe jagah save karein")
            print("  • Ek password sirf ek account ke liye use karein")
            print("  • Kabhi kisi ko password share mat karein")
            print("="*55)

            again = get_yes_no("\n  Dobara password banana hai? (y/n): ")
            if not again:
                print("\n  Shukriya! Apne accounts ko safe rakhein. Allah Hafiz!\n")
                break

        elif choice == "3":
            print("\n  Shukriya! Apne accounts ko safe rakhein. Allah Hafiz!\n")
            break

        else:
            print("\n  Galat choice! Sirf 1, 2, ya 3 daalen.")

if __name__ == "__main__":
    main()
