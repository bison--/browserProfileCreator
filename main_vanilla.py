#!/usr/bin/python3

from src.browserprofilecreator.BrowserProfileCreator import BrowserProfileCreator

def main():
    manager = BrowserProfileCreator()
    manager.create_profile()


if __name__ == "__main__":
    main()
