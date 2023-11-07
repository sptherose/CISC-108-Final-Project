from dataclasses import dataclass
from designer import *

PLAYER_SPEED = 5
@dataclass
class World:
    player_1: DesignerObject
    player_2: DesignerObject
    jumping_1: False
    jumping_2: False
    player_1_left: False
    player_2_left: False
    player_1_right: False
    player_2_right: False
    player_1_speed: int
    player_2_speed: int

def create_player1() -> DesignerObject:
    player_1 = emoji('🧍')
    grow(player_1, 2)
    player_1.y = get_height() - 40
    player_1.x = 12
    player_1.flip_x = False
    return player_1

def move_right_p1(world: World):
    world.player_1_speed = PLAYER_SPEED
def move_left_p1(world: World):
    world.player_1_speed = -PLAYER_SPEED
def move_player1(world: World, key: str):
    world.player_1.x += world.player_1_speed
    if world.player_1_left:
        move_left_p1(world)
    elif world.player_1_right:
        move_right_p1(world)
    else:
        world.player_1_speed = 0
    if key == "w":
        world.player_1.y += -10
        glide_down(world.player_1, 2)
    if key == "s":
        flashlight1 = emoji("🔦")
        grow(flashlight1, -1 / 2)
        flashlight1.y = world.player_1.y + 5
        flashlight1.x = world.player_1.x + 20
        turn_left(flashlight1, 45)
        light_beam1 = rectangle('yellow', 2, 10, x=flashlight1.x, y=flashlight1.y)
        draw(light_beam1)

def keys_pressed_p1(world: World, key: str):
    if key == "A":
        world.player_1_left = True
    if key == "D":
        world.player_1_right = True

def keys_not_pressed_p1(world: World, key: str):
    if key == "A":
        world.player_1_left = False
    if key == "D":
        world.player_1_right = False

def create_player2() -> DesignerObject:
    player_2 = emoji('🧍')
    grow(player_2, 2)
    player_2.y = get_height() - 40
    player_2.x = 20
    player_2.flip_x = False
    return player_2

def move_right_p2(world: World):
    world.player_2_speed = PLAYER_SPEED
def move_left_p2(world: World):
    world.player_2_speed = -PLAYER_SPEED
def move_player2(world: World, key: str):
    world.player_2.x += world.player_2_speed
    if world.player_2_left:
        move_left_p2(world)
    if world.player_2_right:
        move_right_p2(world)
    if world.player_2_left == False and world.player_2_right == False:
        world.player_2_speed = 0
    if key == "Up":
        world.player_2.y += -10
        #world.player_2.y += 10
    if key == "Down":
        flashlight2 = emoji("🔦")
        grow(flashlight2, -1 / 2)
        flashlight2.y = world.player_2.y + 5
        flashlight2.x = world.player_2.x + 20
        turn_left(flashlight2, 45)
    # light_beam2 = rectangle('yellow', 2, 10)
    # draw(light_beam2)
def keys_pressed_p2(world: World, key: str):
    if key == "Left":
        world.player_2_left = True
    if key == "Right":
        world.player_2_right = True
def keys_not_pressed_p2(world: World, key: str):
    if key == "Left":
        world.player_2_left = False
    if key == "Right":
        world.player_2_right = False
def create_world() -> World:
    return World(create_player1(), create_player2(), False, False, False, False, False, False, 0, 0)


when('starting', create_world)
when('typing', keys_pressed_p1, keys_pressed_p2)
when('done typing', keys_not_pressed_p1, keys_not_pressed_p2)
when('updating', move_player1, move_player2)
start()
