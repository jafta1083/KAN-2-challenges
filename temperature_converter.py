# What should program have
# Step 1
#-> create a menu where user is going to choose which convertion they want
# Step 2
#-> create function for each conversion that take one temp value and should return conversion







def main():

    user = input("Enter temperature you want to convert: ")

    temp_convert = user.split()
    if len(temp_convert) != 2:
        print("Error: provide temperature value and it's units!!")


    value =temp_convert[0]
    temperature = temp_convert[1]
    print(value)
    print(temperature)

    print("***Choose what you want to convert your temperature to!***")

    list_temp = ["Celsius to Fahrenheit", "Fahrenheit to Celsius", "Celsius to Kelvin", "Kelvin to Celsius"]

    for i, name_temp in enumerate(list_temp, start=1):
        print(f"{i}.{name_temp}")

    choice = int(input("Enter number of temperature you want to convert to:"))


    if choice == 1:
        final_temp = celsius_to_fahrenheit(value)
        print(f"final temp: {final_temp:.2f} F")

    elif choice == 2:
        final_temp = fahrenheit_to_celsius(value)
        print(f"final temp: {final_temp:.2f}")

    elif choice == 3:
        final_temp = celsius_to_kelvin(value)
        print(f"final temp: {final_temp:.2f}")

    elif choice == 4:
        final_temp = kelvin_to_celsius(value)
        print(f"final temp: {final_temp:.2f}")

    else:
        print("Error: Invalid choice,please choose from (1 - 4)")


def celsius_to_fahrenheit(value):
    value_int = int(value)
    coverted = (value_int * 9/5) + 32
    return coverted

def fahrenheit_to_celsius(value):
    value_int = int(value)
    converted = (value_int- 32) * 5/9
    return converted

def celsius_to_kelvin(value):
    value_int = int(value)
    converted = (value_int + 273.15)
    return converted

def kelvin_to_celsius(value):
    value_int = int(value)
    converted = (value_int - 273.15)
    return converted

if __name__ == "__main__":
    main()
    



        


