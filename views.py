import arcade
import functions

class StartView(arcade.View):
    """
    Main Application Class
    """
    def __init__(self):
        # Call parent class and set up the window.
        super().__init__()

        # Scene Object
        self.scene = None
        self.board = []
        # Setting the background color
        arcade.set_background_color(arcade.csscolor.DARK_GRAY)

    def setup(self):
        """
        Called on start
        """
        # Initializing scene
        self.scene = arcade.Scene()

    def on_show(self):
        """ Called when switching to this view"""
        pass

    def on_draw(self):
        """
        Rendering the screen
        """
        self.clear()

        title_text = f"CryptedTacToe!"
        arcade.draw_text(title_text, 0, self.window.height / 2, arcade.csscolor.GRAY, 38, width=self.window.width, font_name="The Bold Font", align="center")
        arcade.draw_text("Press any key to continue", 0, self.window.height / 2 - 20, arcade.csscolor.GRAY, 12, width=self.window.width, font_name="The Bold Font", align="center")

    def on_update(self, delta_time):
        """
        Runs every frame
        """
        pass

    def on_key_release(self, symbol: int, modifiers: int):
        self.window.show_view(GameView())
    


class GameOverView(arcade.View):
    """
    Main Application Class
    """
    def __init__(self):
        # Call parent class and set up the window.
        super().__init__()

        # Scene Object
        self.scene = None
        self.board = []
        # Setting the background color
        arcade.set_background_color(arcade.csscolor.DARK_GRAY)

    def setup(self, tie, winner: str):
        """
        Called on start
        """
        # Initializing scene
        self.scene = arcade.Scene()
        self.tie = tie
        self.winner = winner

    def on_show(self):
        """ Called when switching to this view"""
        pass

    def on_draw(self):
        """
        Rendering the screen
        """
        self.clear()

        title_text = "" #LOL
        if self.tie == True:
            title_text = "It's a tie!"
        else:
            title_text = f"{self.winner} wins!"
        arcade.draw_text(title_text, 0, self.window.height / 2, arcade.csscolor.GRAY, 38, width=self.window.width, font_name="The Bold Font", align="center")
        arcade.draw_text("Press any key to play again", 0, self.window.height / 2 - 20, arcade.csscolor.GRAY, 12, width=self.window.width, font_name="The Bold Font", align="center")

    def on_update(self, delta_time):
        """
        Runs every frame
        """
        pass

    def on_key_release(self, symbol: int, modifiers: int):
        self.window.show_view(GameView())





class GameView(arcade.View):
    """
    Main Application Class
    """
    def __init__(self):
        # Call parent class and set up the window.
        super().__init__()

        # Scene Object
        self.scene = None
        self.board = []
        self.sprite_list = None
        self.player = "X"
        self.game_over = False
        arcade.set_background_color(arcade.csscolor.DARK_GRAY)

    def setup(self):
        """
        Called on start
        """
        self.board = [
            "0", "0", "0",
            "0", "0", "0",
            "0", "0", "0"
        ]        
        # Initializing scene
        self.scene = arcade.Scene()
        self.sprite_list = arcade.SpriteList()
        self.boardImage = arcade.Sprite("assets/images/Board.png", 1)
        self.boardImage.center_x = self.window.width / 2
        self.boardImage.center_y = self.window.height / 2
        
        current = 0
        for val in self.board:
            current += 1
            if val == "1":
                x_sprite = arcade.Sprite("assets/images/X.png", 2)
                pos = functions.GetPositionFromNumber(current)
                x_sprite.center_x = pos[0]
                x_sprite.center_y = pos[1]
                self.sprite_list.append(x_sprite)
            elif val == "2":
                y_sprite = arcade.Sprite("assets/images/Y.png", 1)
                pos = functions.GetPositionFromNumber(current)
                y_sprite.center_x = pos[0]
                y_sprite.center_y = pos[1]
                self.sprite_list.append(y_sprite)

    def on_show(self):
        """ Called when switching to this view"""
        self.setup()

    def on_draw(self):
        """
        Rendering the screen
        """
        self.clear()
        
        # Drawing the scene
        self.scene.draw()
        self.boardImage.draw()
        self.sprite_list.draw()

    def update_board(self):
        current = 0
        for val in self.board:
            current += 1
            if val == "1":
                x_sprite = arcade.Sprite("assets/images/X.png", 2)
                pos = functions.GetPositionFromNumber(current)
                x_sprite.center_x = pos[0]
                x_sprite.center_y = pos[1]
                self.sprite_list.append(x_sprite)
            elif val == "2":
                y_sprite = arcade.Sprite("assets/images/Y.png", 2)
                pos = functions.GetPositionFromNumber(current)
                y_sprite.center_x = pos[0]
                y_sprite.center_y = pos[1]
                self.sprite_list.append(y_sprite)

        XWon = functions.CheckXWin(self.board)
        YWon = functions.CheckYWin(self.board)
        end_view = GameOverView()
        if XWon:
            end_view.setup(False, "X")
            self.window.show_view(end_view)
        elif YWon:
            end_view.setup(False, "Y")
            self.window.show_view(end_view)
        else:
            done = functions.CheckBoardFull(self.board)
            if done:
                end_view.setup(True, "X")
                self.window.show_view(end_view)
            else: 
                print("No winner, continuing")

    def on_update(self, delta_time):
        # Runs every frame
        pass
    
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            if not self.game_over:
                number = functions.GetNumberFromPosition((x, y))
                if number is None:
                    print("tis none")
                else:
                    number -= 1
                    if self.board[number] == "0":
                        if self.player == "X":
                            self.board[number] = "1"
                            self.player = "Y"
                        else:
                            self.board[number] = "2"
                            self.player = "X"
                        self.update_board()

    def on_mouse_drag(self, x: float, y: float, dx: float, dy: float, _buttons: int, _modifiers: int):
        pass

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        pass

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        pass

    def on_key_release(self, symbol: int, modifiers: int):
        altPressed = modifiers == 4 or modifiers == 20 or modifiers == 28
        entPressed = symbol == 65293
        if altPressed and entPressed:
            self.window.set_fullscreen(not self.window.fullscreen)