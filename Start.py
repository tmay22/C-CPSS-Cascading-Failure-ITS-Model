import Controller
import Setup

def main():
    #Setup.defaultBuild()
    Setup.buildFromPath("DataSets/AI_NeoVista/")
    Controller.mainMenu()


if __name__ == "__main__":
    main()