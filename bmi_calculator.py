#   BMI CALCULATOR - Oasis Infobyte Internship
#   Project 2: BMI Calculator


def calculate_bmi(weight, height):
    """Calculate BMI using weight (kg) and height (m)"""
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def classify_bmi(bmi):
    """Classify BMI into health categories"""
    if bmi < 18.5:
        return "Underweight", "  Aap ka weight thoda kam hai. Doctor se consult karein."
    elif 18.5 <= bmi < 24.9:
        return "Normal (Healthy)", "  Mubarak ho! Aap ka weight bilkul normal hai."
    elif 25 <= bmi < 29.9:
        return "Overweight", "  Aap ka weight thoda zyada hai. Exercise aur diet ka khayal rakhein."
    elif 30 <= bmi < 34.9:
        return "Obese (Class 1)", "  Obesity Class 1. Doctor se zaroor milein."
    elif 35 <= bmi < 39.9:
        return "Obese (Class 2)", "  Obesity Class 2. Turant doctor se milein."
    else:
        return "Obese (Class 3)", "  Obesity Class 3 (Severe). Fori tor par doctor se milein!"

def get_valid_float(prompt, min_val, max_val):
    """Get a valid float input from user within range"""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"  Galat value! Please {min_val} aur {max_val} ke beech value daalen.\n")
        except ValueError:
            print("  Sirf numbers enter karein (e.g. 70 ya 1.75)\n")

def display_bmi_chart():
    """Display BMI reference chart"""
    print("\n" + "="*50)
    print("          BMI REFERENCE CHART")
    print("="*50)
    print(f"  {'BMI Range':<20} {'Category'}")
    print("-"*50)
    print(f"  {'< 18.5':<20} Underweight")
    print(f"  {'18.5 - 24.9':<20} Normal (Healthy)")
    print(f"  {'25.0 - 29.9':<20} Overweight")
    print(f"  {'30.0 - 34.9':<20} Obese Class 1")
    print(f"  {'35.0 - 39.9':<20} Obese Class 2")
    print(f"  {'>= 40.0':<20} Obese Class 3")
    print("="*50)

def main():
    print("\n" + "="*50)
    print("     BMI CALCULATOR - Oasis Infobyte")
    print("="*50)
    print("  Body Mass Index (BMI) calculator mein")
    print("  aap ka swagat hai!")
    print("="*50)

    while True:
        print("\n  MENU:")
        print("  1. BMI Calculate karein")
        print("  2. BMI Chart dekhein")
        print("  3. Exit")
        print("-"*30)

        choice = input("Apna choice enter karein (1/2/3): ").strip()

        if choice == "1":
            print("\n  Apni information darj karein:")
            print("-"*30)

            weight = get_valid_float(
                "  ➤  Aap ka weight (kg mein, e.g. 70): ",
                min_val=2, max_val=500
            )

            height_choice = input("\n  ➤  Height kaise daalna chahte hain?\n     1. Meters mein (e.g. 1.75)\n     2. Centimeters mein (e.g. 175)\n     Apna choice (1/2): ").strip()

            if height_choice == "2":
                height_cm = get_valid_float("  ➤  Aap ki height (cm mein, e.g. 175): ", 50, 300)
                height = height_cm / 100
            else:
                height = get_valid_float("  ➤  Aap ki height (meters mein, e.g. 1.75): ", 0.5, 3.0)

            age = get_valid_float("  ➤  Aap ki umar (saal mein): ", 2, 120)

            bmi = calculate_bmi(weight, height)
            category, advice = classify_bmi(bmi)

            # Display results
            print("\n" + "="*50)
            print("       AAPKA BMI RESULT")
            print("="*50)
            print(f"    Umar      : {age} saal")
            print(f"    Weight    : {weight} kg")
            print(f"    Height    : {height:.2f} m ({height*100:.1f} cm)")
            print("-"*50)
            print(f"    BMI Score : {bmi}")
            print(f"    Category  : {category}")
            print("-"*50)
            print(f"    {advice}")
            print("="*50)

        elif choice == "2":
            display_bmi_chart()

        elif choice == "3":
            print("\n  Shukriya! Apna khayal rakhein. Allah Hafiz!\n")
            break

        else:
            print("\n  Galat choice! Sirf 1, 2, ya 3 daalen.")

if __name__ == "__main__":
    main()
