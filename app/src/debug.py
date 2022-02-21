from modules.app import Main

import pygame; pygame.init()

def main():
    app = Main()
    
    while True:
        app.run()

if __name__ == "__main__":
    main()