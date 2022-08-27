def choose_direction(options):
    if len(options) == 1:
        raise ValueError("Need more parameters")
    else:
        files = []
        for i in range(len(options)):
            files = files + [options[i]]
        option = int(input())
        main = open(__file__.split("\\")[len(__file__.split("\\")) - 1], 'a')
        main.write(open(files[option - 1]).read())
        main.close()
    return 0


choose_direction(["1.py", "2.py"])
