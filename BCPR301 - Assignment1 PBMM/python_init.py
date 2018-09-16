import controller as cont
import sys


def initiate_controller():
    controller = cont.Controller()
    print("Number of Arguments:", len(sys.argv), "Arguments.")
    print("Arguments", sys.argv)
    controller.cmdloop()


if __name__ == '__main__':
    initiate_controller()

