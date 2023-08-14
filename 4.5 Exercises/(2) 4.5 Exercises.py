# 2. Ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit,
# the temperature is in. Your program should convert the temperature to the other unit.

while True:
    try:
        temperature = int(input("Enter a temperature: "))
        break
    except ValueError:
        print("Invalid argument.")
while True:
    try:
        type = input("Celsius or Fahrenheit?: ")
        if type.lower() != "celsius" and type.lower() != "fahrenheit":
            print("Invalid argument")
            continue
        else:
            break
    except ValueError:
        print("Invalid argument")

if type.lower() == "celsius":
    output = (temperature * (9/5)) + 32
    print(f"{temperature} {type.capitalize()} in Fahrenheit is: {round(output,2)} F")
elif type.lower() == "fahrenheit":
    output = (temperature - 32) * 5/9
    print(f"{temperature} {type.capitalize()} in Celsius is: {round(output,2)} C")

