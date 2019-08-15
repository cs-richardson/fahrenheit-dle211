i = 0
while i != 1:
    try:
        c = float(input("C: "))
        f = 1.8 * c + 32
        print("F:", f)
        i = 1
    except ValueError:
        print("That's not a number.")
