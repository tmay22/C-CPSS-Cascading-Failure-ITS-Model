import Controller
import Setup

def main():
    #Setup.defaultBuild()
    Setup.buildFromPath("DataSets/IndustrialDistrict/")
    Controller.mainMenu()


if __name__ == "__main__":
    main()