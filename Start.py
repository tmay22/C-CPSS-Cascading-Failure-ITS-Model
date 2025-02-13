import Controller
import Setup

def main():
    #Setup.defaultBuild()
    Setup.buildFromPath("DataSets/Tess_SmartCity/")
    Controller.mainMenu()


if __name__ == "__main__":
    main()