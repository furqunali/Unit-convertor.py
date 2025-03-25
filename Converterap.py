print("🌟 Super Simple Converter 🌟")

# Just temperature conversion to keep it simple
print("\n1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Choose (1 or 2): ")

if choice == '1':
    c = float(input("Enter Celsius: "))
    f = (c * 9/5) + 32
    print(f"{c}°C = {f:.1f}°F")
elif choice == '2':
    f = float(input("Enter Fahrenheit: "))
    c = (f - 32) * 5/9
    print(f"{f}°F = {c:.1f}°C")
else:
    print("Oops! Just type 1 or 2 :)")

print("\nYou did it! 🎉")