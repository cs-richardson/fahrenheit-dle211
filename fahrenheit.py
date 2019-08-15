while True:
    try:
        c = float(input("C: "))
        f = 1.8 * c + 32
        print("F:", f)
        import sys
        sys.exit()
    except ValueError:
        print("That's not a number.")
