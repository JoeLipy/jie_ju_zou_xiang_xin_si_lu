def choose_direction(options):
    if len(options) == 1:  # Not enough options
        raise ValueError("Need more parameters")
    else:
        files = []
        for i in range(len(options)):
            files = files + [options[i]]
        try:
            option = int(input("1 or 2:"))
        except ValueError:
            return 1
        main = open(__file__.split("\\")[len(__file__.split("\\")) - 1], 'a')
        try:
            main.write(open(files[option - 1]).read())
        except IndexError:
            return 1
        main.close()
    return 0


choose_direction(["1.py", "2.py"])
