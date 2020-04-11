class Colors:
    """ ANSI color codes """

    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    YELLOW = "\033[1;33m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"


def print_sucess(text="Sample Text", end="\n"):
    print(Colors.GREEN + Colors.BOLD + text + Colors.END, end=end)


def print_failure(text="Sample Text", end="\n"):
    print(Colors.RED + Colors.BOLD + text + Colors.END, end=end)


def print_information(text="Sample Text", end="\n"):
    print(Colors.BLUE + Colors.BOLD + text + Colors.END, end=end)


def print_warning(text="Sample Text", end="\n"):
    print(Colors.YELLOW + Colors.BOLD + text + Colors.END, end=end)
