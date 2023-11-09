from dataclasses import dataclass
from designer import *

PLAYER_SPEED = 10

class MovingEmoji(Emoji):
    speed: int
    direction: int
@dataclass
class World:
    player_1: MovingEmoji
    player_2: MovingEmoji
    jumping_1: False
    jumping_2: False
    player_1_left: False
    player_2_left: False
    player_1_right: False
    player_2_right: False
    player_1_speed: int
    player_2_speed: int
    player_1_flashlight : DesignerObject
    player_2_flashlight : DesignerObject
    player_1_flash_on : False
    player_2_flash_on : False

def create_player1() -> MovingEmoji:
    """This creates Player 1 and makes him appear on the bottom left of the screen"""
    player_1 = MovingEmoji('🧍',speed=5,direction=0)
    grow(player_1, 2)
    player_1.y = get_height() - 40
    player_1.x = 12
    player_1.flip_x = False
    return player_1
def create_p1_flashlight() -> DesignerObject:
    """This creates Player 1's flashlight that will appear when the function gets called"""
    player_1_flashlight = emoji("🔦")
    grow(player_1_flashlight, -1 / 2)
    turn_left(player_1_flashlight, 45)
    hide(player_1_flashlight)
    return player_1_flashlight
def move_right_p1(world: World):
    """This function moves Player 1 to the right when it gets called"""
    world.player_1_speed = PLAYER_SPEED
def move_left_p1(world: World):
    """This function moves Player 1 to the left when it gets called"""
    world.player_1_speed = -PLAYER_SPEED
def stop_moving_players(world:World):
    """This function prevents Players 1 and 2 from running off of the screen"""
    if world.player_1.x > get_width():
        world.player_1_speed = 0
    elif world.player_1.x < 0:
        world.player_1_speed = 0
    if world.player_2.x > get_width():
        world.player_2_speed = 0
    elif world.player_2.x < 0:
        world.player_2_speed = 0
def move_player1(world: World, key: str):
    """This function takes in the key being pressed and makes Player 1 move accordingly,
    calling the appropriate helper functions"""
    world.player_1.x += world.player_1_speed
    if world.player_1_left:
        move_left_p1(world)
    if world.player_1_right:
        move_right_p1(world)
    if not world.player_1_left and not world.player_1_right:
        world.player_1_speed = 0
    if key == "W":
        world.player_1.speed += -50
    if world.player_1_flash_on:
        world.player_1_flashlight.y = world.player_1.y + 5
        world.player_1_flashlight.x = world.player_1.x + 20
        show(world.player_1_flashlight)
    if not world.player_1_flash_on:
        hide(world.player_1_flashlight)
       # light_beam1 = rectangle('yellow', 2, 10, x=flashlight1.x, y=flashlight1.y)
       # draw(light_beam1)

def keys_pressed_p1(world: World, key: str):
    """This function checks if the key is still being pressed
    so that Player 1 keeps moving or keeps shining light while the key is being held"""
    if key == "A":
        world.player_1_left = True
    if key == "D":
        world.player_1_right = True
    if key == "S":
        world.player_1_flash_on = True

def keys_not_pressed_p1(world: World, key: str):
    """This function checks if the key has been released
        so that Player 1 stops moving or shining light while the key no longer being held"""
    if key == "A":
        world.player_1_left = False
    if key == "D":
        world.player_1_right = False
    if key == "S":
        world.player_1_flash_on = False

def create_player2() -> MovingEmoji:
    """This creates Player 2 and makes him appear on the bottom left of the screen"""
    player_2 = MovingEmoji('🧍',speed=5,direction=0)
    grow(player_2, 2)
    player_2.y = get_height() - 40
    player_2.x = 20
    player_2.flip_x = False
    return player_2
def create_p2_flashlight() -> DesignerObject:
    """This creates Player 1's flashlight that will appear when the function gets called"""
    player_2_flashlight = emoji("🔦")
    grow(player_2_flashlight, -1 / 2)
    turn_left(player_2_flashlight, 45)
    hide(player_2_flashlight)
    return player_2_flashlight
def move_right_p2(world: World):
    """This function moves Player 2 to the right when it get's called"""
    world.player_2_speed = PLAYER_SPEED
def move_left_p2(world: World):
    """This function moves Player 2 to the left when it get's called"""
    world.player_2_speed = -PLAYER_SPEED
def move_player2(world: World, key: str):
    """This function takes in the key being pressed and makes Player 2 move accordingly,
        calling the appropriate helper functions"""
    world.player_2.x += world.player_2_speed
    if world.player_2_left:
        move_left_p2(world)
    if world.player_2_right:
        move_right_p2(world)
    if not world.player_2_left and not world.player_2_right:
        world.player_2_speed = 0
    if key == "Up":
        world.player_2.speed += -50
    if world.player_2_flash_on:
        world.player_2_flashlight.y = world.player_2.y + 5
        world.player_2_flashlight.x = world.player_2.x + 20
        show(world.player_2_flashlight)
    if not world.player_2_flash_on:
        hide(world.player_2_flashlight)
    # light_beam2 = rectangle('yellow', 2, 10)
    # draw(light_beam2)
def keys_pressed_p2(world: World, key: str):
    """This function checks if the key is still being pressed
       so that Player 2 keeps moving or flashing light while the key is being held"""
    if key == "Left":
        world.player_2_left = True
    if key == "Right":
        world.player_2_right = True
    if key == "Down":
        world.player_2_flash_on = True
def keys_not_pressed_p2(world: World, key: str):
    """This function checks if the key has been released
        so that Player 1 stops moving or flashing light while the key no longer being held"""
    if key == "Left":
        world.player_2_left = False
    if key == "Right":
        world.player_2_right = False
    if key == "Down":
        world.player_2_flash_on = False
def accelerate_player(world:World):
    if world.player_1.y + world.player_1.speed<=  get_height() - 40:
        world.player_1.y += world.player_1.speed
        world.player_1.speed += 10
    if world.player_2.y + world.player_2.speed <= get_height() - 40:
        world.player_2.y += world.player_2.speed
        world.player_2.speed += 10

def create_world() -> World:
    return World(create_player1(), create_player2(), False, False, False, False, False, False, 0, 0, create_p1_flashlight(), create_p2_flashlight(),False,False)


when('starting', create_world)
when('typing', keys_pressed_p1, keys_pressed_p2, move_player1,move_player2)
when('done typing', keys_not_pressed_p1, keys_not_pressed_p2)
when('updating', move_player1, move_player2)
when ('updating',stop_moving_players)
when('updating',accelerate_player)
start()
