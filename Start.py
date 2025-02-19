import Controller
import Setup

def main():
    #Setup.defaultBuild()
    Setup.buildFromPath("DataSets/ARC-IT_ITS/")
    Controller.mainMenu()


if __name__ == "__main__":
    main()