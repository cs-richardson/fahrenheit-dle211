complete = 0
while complete != 1:
    try:
        celsius = float(input("C: "))
        fahrenheit = 1.8 * celsius + 32
        print("F:", fahrenheit)
        complete = 1
    except ValueError:
        print("That's not a number.")
