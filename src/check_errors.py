from src.utils import help

def check_args(ac, av):
    if ac == 2 and av[1] == "-h":
        help()
        exit(0)
    if ac != 3 and ac != 2:
        raise Exception("ERROR: The number of arguments must be 3.")