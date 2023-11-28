from dataclasses import dataclass
from designer import *

PLAYER_SPEED = 10

@dataclass
class Button:
    background: DesignerObject
    border: DesignerObject
    label: DesignerObject

def make_button(message:str,x:int,y:int) -> Button:
    horizontal_padding = 5
    vertical_padding = 3
    label = text("white",message,20,x,y,layer='top')
    return Button(rectangle("black",label.width + horizontal_padding, label.height + vertical_padding, x, y),
                  rectangle("white",label.width + horizontal_padding, label.height + vertical_padding, x, y,1),
                  label)
class MovingEmoji(Emoji):
    speed: int
    direction: int
@dataclass
class World:
    ground: DesignerObject
    cave_entrance_1: DesignerObject
    platforms_L1: DesignerObject
    beat_L1: False
    cave_entrance_2: DesignerObject
    platforms_L2: DesignerObject
    beat_L2: False
    player_1: MovingEmoji
    player_2: MovingEmoji
    grounded_1: True
    grounded_2: True
    player_1_left: False
    player_2_left: False
    player_1_right: False
    player_2_right: False
    player_1_jump: False
    player_2_jump: False
    player_1_speed: int
    player_2_speed: int
    player_1_flashlight : DesignerObject
    player_2_flashlight : DesignerObject
    player_1_flash_on : False
    player_2_flash_on : False


@dataclass
class TitleScreen:
    header: DesignerObject
    start_button: Button
    quit_button: Button
def create_title_screen() -> TitleScreen:
    return TitleScreen(text("black","Scandere",50),
                       make_button("Begin Game", get_width()/2, (get_height()/2 + 50)),
                       make_button("Quit Game", get_width()/2, (get_height()/2) + 100))
def use_title_buttons(world:TitleScreen):
    if colliding_with_mouse(world.start_button.background):
        change_scene('world')
    if colliding_with_mouse(world.quit_button.background):
        quit()
@dataclass
class BeatLevel1:
    background: DesignerObject
    header: DesignerObject
    go_to_L2_Button: Button
    quit_button: Button
def create_beat_L1_screen() -> BeatLevel1:
    return BeatLevel1(rectangle("gray",get_width(),get_height()),
                       text("white","Good Job! You Beat Level 1!",50),
                       make_button("Begin Level 2", get_width()/2, (get_height()/2 + 50)),
                       make_button("Quit Game", get_width()/2, (get_height()/2) + 100))
def create_ground() -> DesignerObject:
    """ This creates thr ground at bottom of screen"""
    ground = rectangle(color="black",width=get_width()*2,height=40,x=0,y=get_height())
    return ground
def create_cave_entrance_1() -> DesignerObject:
    cave_entrance_1 = circle(color="black",radius=50,x=70,y=70)
    return cave_entrance_1
def create_cave_entrance_2() -> DesignerObject:
    cave_entrance_2 = circle(color="black",radius=50,x=70,y=70)
    return cave_entrance_2
def create_plat_L1() -> [DesignerObject]:
    platforms_L1 = [rectangle(color="black",width=80,height=10,x=500,y=get_height()-80),
                    rectangle(color="black",width=340,height=10,x=300,y=get_height()-160),
                    rectangle(color="black",width=100,height=10,x=370,y=get_height()-260),
                    rectangle(color="black",width=100,height=10,x=420,y=get_height()-330),
                    rectangle(color="black", width=100, height=10, x=350, y=get_height() - 430),
                    rectangle(color="black", width=150, height=10, x=200, y=get_height() - 450),
                    rectangle(color="black", width=200, height=10, x=70, y=120)]
    return platforms_L1
def create_plat_L2() -> [DesignerObject]:
    platforms_L2 = [rectangle(color="black",width=80,height=10,x=500,y=get_height()-80),
                    rectangle(color="black",width=340,height=10,x=300,y=get_height()-160),
                    rectangle(color="black",width=100,height=10,x=370,y=get_height()-260),
                    rectangle(color="black",width=100,height=10,x=420,y=get_height()-330),
                    rectangle(color="black", width=100, height=10, x=350, y=get_height() - 430),
                    rectangle(color="black", width=150, height=10, x=200, y=get_height() - 450),
                    rectangle(color="black", width=200, height=10, x=70, y=120)]
    return platforms_L2
def create_player1() -> MovingEmoji:
    """This creates Player 1 and makes him appear on the bottom left of the screen"""
    player_1 = MovingEmoji('🧍',speed=5,direction=0)
    grow(player_1, 2)
    player_1.y = get_height()-40
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
def move_up_p1(world:World):
    world.player_1.speed += -30
def stop_moving_players(world:World):
    """This function prevents Players 1 and 2 from running off of the screen"""
    if world.player_1.x == get_width():
        world.player_1_speed = 0
    elif world.player_1.x == 0:
        world.player_1_speed = 0
    if world.player_2.x == get_width():
        world.player_2_speed = 0
    elif world.player_2.x == 0:
        world.player_2_speed = 0
def move_player1(world: World, key: str):
    """This function takes in the key being pressed and makes Player 1 move accordingly,
    calling the appropriate helper functions"""
    world.player_1.x += world.player_1_speed
    if world.player_1_left and world.player_1.x > 0:
        move_left_p1(world)
    if world.player_1_right and world.player_1.x < get_width():
        move_right_p1(world)
    if not world.player_1_left and not world.player_1_right:
        world.player_1_speed = 0
    if key == "W":
        if world.grounded_1:
            move_up_p1(world)
            world.player_1.y += world.player_1.speed
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
    if key == "W":
        world.player_1_jump = False
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
def move_up_p2(world:World):
    world.player_2.speed += -30
def move_player2(world: World, key: str):
    """This function takes in the key being pressed and makes Player 2 move accordingly,
        calling the appropriate helper functions"""
    world.player_2.x += world.player_2_speed
    if world.player_2_left and world.player_2.x > 0:
        move_left_p2(world)
    if world.player_2_right and world.player_2.x < get_width():
        move_right_p2(world)
    if not world.player_2_left and not world.player_2_right:
        world.player_2_speed = 0
    if key == "Up":
        if world.grounded_2:
            move_up_p2(world)
            world.player_2.y += world.player_2.speed
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
    if key == "Up":
        world.player_2_jump = False
def check_beat_levels(world:World):
    if colliding(world.player_1,world.cave_entrance_1) and colliding(world.player_2,world.cave_entrance_1):
        world.beat_L1 = True
        create_beat_L1_screen()
def check_groundings(world:World):
    if colliding(world.player_1,world.ground):
        world.grounded_1 = True
        world.player_1.y = get_height()-40
        world.player_1.speed = 0
    elif not colliding(world.player_1,world.ground):
        world.grounded_1 = False
        for platform_L1 in world.platforms_L1:
            if colliding(world.player_1,platform_L1):
                world.player_1.y = platform_L1.y-30
                world.grounded_1 = True
    if colliding(world.player_2,world.ground):
        world.grounded_2 = True
        world.player_2.y = get_height()-40
        world.player_2.speed = 0
    elif not colliding(world.player_2,world.ground):
        world.grounded_2 = False
        for platform_L1 in world.platforms_L1:
            if colliding(world.player_2,platform_L1):
                world.player_2.y = platform_L1.y-30
                world.grounded_2 = True
def accelerate_player(world:World):
   if world.grounded_1:
        world.player_1.speed = 0
        world.player_1.y += world.player_1.speed
   elif not world.grounded_1:
        world.player_1.y += world.player_1.speed
        world.player_1.speed += 10
   if world.grounded_2:
       world.player_2.speed = 0
       world.player_2.y += world.player_2.speed
   elif not world.grounded_2:
       world.player_2.y += world.player_2.speed
       world.player_2.speed += 10
def create_world() -> World:
    return World(create_ground(),
                 create_cave_entrance_1(), create_plat_L1(), False,
                 create_cave_entrance_2(), create_plat_L2(), False,
                 create_player1(), create_player2(),
                 True, True, False, False, False, False, False, False, 0, 0,
                 create_p1_flashlight(), create_p2_flashlight(), False, False)


when('starting:title', create_title_screen)
when('clicking:title',use_title_buttons)
when('starting:world', create_world)
when('done typing:world', keys_not_pressed_p1, keys_not_pressed_p2)
when('typing:world', keys_pressed_p1, keys_pressed_p2, move_player1,move_player2)
when('updating:world', move_player1, move_player2)
when ('updating:world',stop_moving_players)
when ('updating:world',check_beat_levels)
when('updating:world', check_groundings)
when('updating:world',accelerate_player)
debug()
