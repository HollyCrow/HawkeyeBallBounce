# Main.py
#
from Bounce import Bounce
from dataLoading import readData


def main():
    bounces = readData()
    print(bounces[0])


if __name__ == "__main__":
    main()
