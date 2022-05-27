import os

os.system("color")

class Ocol:
    def red(tri):
        return '\033[91m'+tri+'\033[0m'

    def green(tri):
        return '\033[92m'+tri+'\033[0m'

    def bleu(tri):
        return '\033[94m'+tri+'\033[0m'

    def purple(tri):
        return '\033[95m'+tri+'\033[0m'

    def cus_col(tri,code=""):
        if not code in range(110):
            print(Ocol.red("\n[You have to pass a code in range 0 - 110]:"))
            Ocol.available_col()
        return f'\033[{code}m'+tri+'\033[0m'

    def available_col():
        for i in range(110):
            print(f'\033[5;{i}m'+"Color code is: "+'\033[0;0m', i)


if __name__ == "__main__":
    Ocol.available_col()