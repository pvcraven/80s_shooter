import random
import arcade
from arcade.experimental import Shadertoy

from views.space_invaders.enemy_bullet import EnemyBullet
from views.space_invaders.constants import *
from views.space_invaders.enemy_invader import EnemyInvader
from views.menus import instruction_view


class DefenderView(arcade.View):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__()

        # Variables that will hold sprite lists
        self.player_list = None
        self.enemy_list = None
        self.player_bullet_list = None
        self.enemy_bullet_list = None
        self.shield_list = None

        # Textures for the enemy
        self.enemy_textures = None

        # State of the game
        self.game_state = PLAY_GAME

        # Set up the player info
        self.player_sprite = None
        self.score = 0
        self.lives = 3
        self.death_pause = 0

        self.filter_on = True

        # Enemy movement
        self.enemy_change_x = -ENEMY_SPEED

        # Don't show the mouse cursor
        self.window.set_mouse_visible(False)

        # Load sounds. Sounds from kenney.nl
        self.gun_sound = arcade.load_sound(":resources:sounds/hurt5.wav")
        self.hit_sound = arcade.load_sound(":resources:sounds/hit5.wav")
        self.player_explosion = arcade.load_sound(":resources:sounds/explosion1.wav")
        self.game_over = arcade.load_sound(":resources:sounds/gameover4.wav")

        arcade.set_background_color(arcade.color.BLACK)

        self.time = 0
        file_name = "shaders/side_city.glsl"
        file = open(file_name)
        shader_sourcecode = file.read()
        size = self.window.width, self.window.height
        self.shadertoy = Shadertoy(size, shader_sourcecode)

        # arcade.configure_logging()


    def setup(self):
        """
        Set up the game and initialize the variables.
        Call this method if you implement a 'play again' feature.
        """

        self.game_state = PLAY_GAME

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.player_bullet_list = arcade.SpriteList()
        self.enemy_bullet_list = arcade.SpriteList()

        # Set up the player
        self.score = 0

        # Image from kenney.nl
        self.player_sprite = arcade.Sprite("images/player.png",
                                           SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 60
        self.player_sprite.color = PLAYER_COLOR
        self.player_list.append(self.player_sprite)


    def draw(self):
        arcade.start_render()
        self.shadertoy.render(time=self.time)


    def on_draw(self):
        """ Render the screen. """

        # Draw our stuff into the screen
        self.window.use()
        self.window.clear()
        self.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called whenever the mouse moves. """
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called whenever the mouse button is clicked. """
        pass

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.time += delta_time

    def on_key_press(self, symbol: int, modifiers: int):
        if self.game_state == GAME_OVER and symbol == arcade.key.SPACE:
            my_game_view = instruction_view.InstructionView()
            self.window.show_view(my_game_view)
