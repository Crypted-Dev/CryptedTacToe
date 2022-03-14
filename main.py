"""
If you're coding this during exams, 
in good consciousness remind yourself to delete this.
"""

import pyglet
import arcade
import time
import views

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
SCREEN_TITLE = "CryptedTacToe!"

def main():
    """
    Main function
    """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.center_window()
    window.set_icon(pyglet.image.load("assets/images/X.png"))
    start_view = views.StartView()
    start_view.setup()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()