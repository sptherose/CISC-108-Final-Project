from dataclasses import dataclass
from designer import *
from random import randint
from random import choice

PLAYER_SPEED = 10

@dataclass
class Button:
    background: DesignerObject
    border: DesignerObject
    label: DesignerObject

def make_button(message:str,x:int,y:int) -> Button:
    '''
    This function creates a button with the given text and a border and background and outline
    Args:
        message(str): the text that appears on the button
        x(int): the x position of the button
        y(int): the y position of the button
    Returns:
        Button: the button will have an outline of 5x3 pixels and a black rectangular background with
        text layered above the background at the assigned (x,y) coordinates
    '''
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
class Level1:
    ground: DesignerObject
    cave_entrance_1: DesignerObject
    platforms_L1: DesignerObject
    beat_L1: False
    player_1: MovingEmoji
    player_2: MovingEmoji
    player_1_health: int
    player_2_health:int
    healths: [DesignerObject]
    grounded_1: True
    grounded_2: True
    player_1_left: False
    player_2_left: False
    player_1_right: False
    player_2_right: False
    player_1_direction:str
    player_2_direction:str
    player_1_jump: False
    player_2_jump: False
    player_1_speed: int
    player_2_speed: int
    player_1_flashlight : DesignerObject
    player_2_flashlight : DesignerObject
    player_1_flash_on : False
    player_2_flash_on : False
    bats: [DesignerObject]
@dataclass
class Level2:
    ground: DesignerObject
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
    '''
    This function creates the title screen that will appear when game starts
    Returns:
        TitleScreen: this function sets the background image and then creates a title screen with the name of the game in black at size 50,
        and 2 buttons, one to start the game, and another that lets the player quit the game
    '''
    set_background_image('https://img.freepik.com/free-vector/entrance-cave-mountain-with-empty-space_107791-9092.jpg?w=2000&t=st=1701373813~exp=1701374413~hmac=3e18601fcf8632cc5d4f240c3fc30cbc94ab5cf0478dc8f328c75730dff62528')
    return TitleScreen(text("black","Scandere",50),
                       make_button("Begin Game", get_width()/2, (get_height()/2 + 50)),
                       make_button("Quit Game", get_width()/2, (get_height()/2) + 100))
def use_title_buttons(world:TitleScreen):
    '''
    This function makes the buttons that appear on the title screen clickable and makes the buttons perform the
    appropriate actions
    Args:
        world(TitleScreen): the scene that the game is currently at, which is the title screen
    '''
    if colliding_with_mouse(world.start_button.background):
        change_scene('level1')
    if colliding_with_mouse(world.quit_button.background):
        quit()
@dataclass
class EndScreen:
    header: DesignerObject
    quit_button: Button
def create_end_screen() -> EndScreen:
    '''
    This function creates the eng screen that will appear when the player loses the game
    Returns:
        EndScreen: this function sets the background image and then creates a game over screen with
         one button that lets the player quit the game and text saying the player died
    '''
    set_background_image(
        'https://cdna.artstation.com/p/assets/images/images/026/366/308/large/alicia-magistrello-basic-cave.jpg?1588597279')
    return EndScreen(text("black","You Died :P",50),
                     make_button("Quit Game", get_width()/2, (get_height()/2) + 100))
def use_end_buttons(world:EndScreen):
    '''
        This function makes the button that appears on the end screen clickable and makes the button perform the
        appropriate action
        Args:
            world(EndScreen): the scene that the game is currently at, which is the game over screen
        '''
    if colliding_with_mouse(world.quit_button.background):
        quit()

@dataclass
class BeatLevel1:
    #background: DesignerObject
    header: DesignerObject
    go_to_L2_Button: Button
    quit_button: Button
def create_beat_L1_screen() -> BeatLevel1:
    '''
    This function creates the level 1 completion screen that will appear when the players beat the first level
    Returns:
        BeatLevel1: this function sets the background image and then text stating the players beat level 1,
        and 2 buttons, one to go to the next level, and another that lets the player quit the game
    '''
    set_background_image('https://i.redd.it/kdobli2akyh61.jpg')
    return BeatLevel1(
                       text("white","Good Job! You Beat Level 1!",50),
                       make_button("Begin Level 2", get_width()/2, (get_height()/2 + 50)),
                       make_button("Quit Game", get_width()/2, (get_height()/2) + 100))
def use_beat_L1_buttons(world:BeatLevel1):
    '''
        This function makes the buttons that appear on the level completion screen clickable and makes the buttons
        perform the appropriate actions
        Args:
            world(BeatLevel1): the scene that the game is currently at, which is the level 1 completed screen
        '''
    if colliding_with_mouse(world.go_to_L2_Button.background):
        change_scene('title')
    if colliding_with_mouse(world.quit_button.background):
        quit()
def create_ground() -> DesignerObject:
    """ This creates thr ground at bottom of screen"""
    ground = rectangle(color="black",width=get_width()*2,height=40,x=0,y=get_height())
    return ground
def create_cave_entrance_1() -> DesignerObject:
    cave_entrance_1 = circle(color="black",radius=50,x=70,y=70)
    return cave_entrance_1

def create_bat() -> DesignerObject:
    bat = emoji("bat")
    bat.x = choice([0,get_width()])
    bat.y = randint(0,get_height())
    return bat
def spawn_bats_1(level1:Level1) -> [DesignerObject]:
    good_num_bats = len(level1.bats) < 4
    if good_num_bats and randint(1,125) == 120:
        level1.bats.append(create_bat())
def move_bats_1(level1:Level1):
    for bat in level1.bats:
        target = choice([level1.player_1, level1.player_2])
        #point_towards(bat,target)
        target_x = target.x
        target_y = target.y
        if bat.x > target_x:
            bat.x += -1
        if bat.x < target_x:
            bat.x += 1
        if bat.y > target_y:
            bat.y += -1
        if bat.y < target_y:
            bat.y += 1
def flash_bat_collision_1(level1:Level1):
    scared_bats = []
    for bat in level1.bats:
        if colliding(bat,level1.player_1_flashlight) and level1.player_1_flash_on:
            scared_bats.append(bat)
        if colliding(bat,level1.player_2_flashlight) and level1.player_2_flash_on:
            scared_bats.append(bat)
    level1.bats = destroy_bats(level1.bats,scared_bats)
def player_bat_collision_1(level1:Level1):
    remove_bats = []
    for bat in level1.bats:
        if colliding(bat,level1.player_1):
            level1.player_1_health -= 1
            remove_bats.append(bat)
        if colliding(bat,level1.player_2):
            level1.player_2_health -= 1
            remove_bats.append(bat)
    level1.bats = destroy_bats(level1.bats,remove_bats)
def destroy_bats(scene_bats:[DesignerObject], remove_bats:[DesignerObject]) -> [DesignerObject]:
    keep_bats = []
    for bat in scene_bats:
        if bat in remove_bats:
            destroy(bat)
        else:
            keep_bats.append(bat)
    return keep_bats
def display_health() -> [DesignerObject]:
    healths = [text("white","Player 1 Health: " ,20,(get_width()-100),20),
               text("white","Player 2 Health: ",20,(get_width()-100),40)]
    return healths
def update_health(level1:Level1):
    for health in level1.healths:
        if health == level1.healths[0]:
            health.text = "Player 1 Health:" + str(level1.player_1_health)
        if health == level1.healths[1]:
            health.text = "Player 2 Health:" + str(level1.player_2_health)
def lost_game(level1:Level1):
    if level1.player_1_health == 0 or level1.player_2_health == 0:
        change_scene('endscreen')

def create_cave_entrance_2() -> DesignerObject:
    cave_entrance_2 = circle(color="black",radius=50,x=70,y=70)
    return cave_entrance_2
def create_plat_L1() -> [DesignerObject]:
    platforms_L1 = [rectangle(color="black",width=80,height=10,x=515,y=get_height()-80),
                    rectangle(color="black",width=340,height=10,x=290,y=get_height()-170),
                    rectangle(color="black",width=100,height=10,x=300,y=get_height()-250),
                    rectangle(color="black",width=50,height=10,x=400,y=get_height()-320),
                    rectangle(color="black", width=100, height=10, x=370, y=get_height() - 430),
                    rectangle(color="black", width=150, height=10, x=200, y=get_height() - 450),
                    rectangle(color="black", width=200, height=10, x=70, y=120)]
    return platforms_L1
def create_plat_L2() -> [DesignerObject]:
    platforms_L2 = [rectangle(color="black",width=80,height=10,x=500,y=get_height()-80),
                    rectangle(color="black",width=340,height=10,x=300,y=get_height()-160),
                    rectangle(color="black",width=100,height=10,x=370,y=get_height()-275),
                    rectangle(color="black",width=100,height=10,x=550,y=get_height()-330),
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
    player_1_flashlight.flip_x = False
    hide(player_1_flashlight)
    return player_1_flashlight
def move_right_p1(world: Level1):
    """This function moves Player 1 to the right when it gets called"""
    world.player_1_speed = PLAYER_SPEED
    world.player_1_direction = "right"
def move_left_p1(world: Level1):
    """This function moves Player 1 to the left when it gets called"""
    world.player_1_speed = -PLAYER_SPEED
    world.player_1_direction = "left"
def move_up_p1(world:Level1):
    world.player_1.speed += -30
def stop_moving_players(world:Level1):
    """This function prevents Players 1 and 2 from running off of the screen"""
    if world.player_1.x > get_width():
        world.player_1.x = get_width()
    if world.player_1.x < 0:
        world.player_1.x = 0
    if world.player_2.x > get_width():
        world.player_2.x = get_width()
    if world.player_2.x < 0:
        world.player_2.x = 0
def move_player1(world: Level1, key: str):
    """This function takes in the key being pressed and makes Player 1 move accordingly,
    calling the appropriate helper functions"""
    world.player_1.x += world.player_1_speed
    if world.player_1_left:
        move_left_p1(world)
    if world.player_1_right:
        move_right_p1(world)
    if not world.player_1_left and not world.player_1_right:
        world.player_1_speed = 0
    if world.player_1_jump:
        if world.grounded_1:
            move_up_p1(world)
            world.player_1.y += world.player_1.speed
    if world.player_1_flash_on:
        if world.player_1_direction == "right":
            world.player_1_flashlight.y = world.player_1.y + 5
            world.player_1_flashlight.x = world.player_1.x + 20
            #world.player_1_flashlight.flip_x = False
        if world.player_1_direction == "left":
            world.player_1_flashlight.y = world.player_1.y + 5
            world.player_1_flashlight.x = world.player_1.x - 20
            #world.player_1_flashlight.flip_x = True
        show(world.player_1_flashlight)
    if not world.player_1_flash_on:
        hide(world.player_1_flashlight)
def keys_pressed_p1(world: Level1, key: str):
    """This function checks if the key is still being pressed
    so that Player 1 keeps moving or keeps shining light while the key is being held"""
    if key == "A":
        world.player_1_left = True
    if key == "D":
        world.player_1_right = True
    if key == "S":
        world.player_1_flash_on = True
    if key == "W":
        world.player_1_jump = True
def keys_not_pressed_p1(world: Level1, key: str):
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
    #player_2.flip_x = False
    return player_2
def create_p2_flashlight() -> DesignerObject:
    """This creates Player 1's flashlight that will appear when the function gets called"""
    player_2_flashlight = emoji("🔦")
    grow(player_2_flashlight, -1 / 2)
    turn_left(player_2_flashlight, 45)
    hide(player_2_flashlight)
    return player_2_flashlight
def move_right_p2(world: Level1):
    """This function moves Player 2 to the right when it gets called"""
    world.player_2_speed = PLAYER_SPEED
    world.player_2_direction = "right"
def move_left_p2(world: Level1):
    """This function moves Player 2 to the left when it get's called"""
    world.player_2_speed = -PLAYER_SPEED
    world.player_2_direction = "left"
def move_up_p2(world:Level1):
    world.player_2.speed += -30
def move_player2(world: Level1, key: str):
    """This function takes in the key being pressed and makes Player 2 move accordingly,
        calling the appropriate helper functions"""
    world.player_2.x += world.player_2_speed
    if world.player_2_left and world.player_2.x > 0:
        move_left_p2(world)
    if world.player_2_right and world.player_2.x < get_width():
        move_right_p2(world)
    if not world.player_2_left and not world.player_2_right:
        world.player_2_speed = 0
    if world.player_2_jump:
        if world.grounded_2:
            move_up_p2(world)
            world.player_2.y += world.player_2.speed
    if world.player_2_flash_on:
        if world.player_2_direction == "right":
            world.player_2_flashlight.y = world.player_2.y + 5
            world.player_2_flashlight.x = world.player_2.x + 20
        if world.player_2_direction == "left":
            world.player_2_flashlight.y = world.player_2.y + 5
            world.player_2_flashlight.x = world.player_2.x - 20
        show(world.player_2_flashlight)
    if not world.player_2_flash_on:
        hide(world.player_2_flashlight)
    # light_beam2 = rectangle('yellow', 2, 10)
    # draw(light_beam2)
def keys_pressed_p2(world: Level1, key: str):
    """This function checks if the key is still being pressed
       so that Player 2 keeps moving or flashing light while the key is being held"""
    if key == "Left":
        world.player_2_left = True
    if key == "Right":
        world.player_2_right = True
    if key == "Down":
        world.player_2_flash_on = True
    if key == "Up":
        world.player_2_jump = True
def keys_not_pressed_p2(world: Level1, key: str):
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
def check_beat_levels(world:Level1):
    if colliding(world.player_1,world.cave_entrance_1) and colliding(world.player_2,world.cave_entrance_1):
        world.beat_L1 = True
        change_scene('beatL1')
def collision(player:MovingEmoji, platform:DesignerObject) -> bool:
    feet = player.y - player.height//2
    top = platform.y + platform.height//2
    return feet == top

def check_groundings(world:Level1):
    if colliding(world.player_1,world.ground):
        world.grounded_1 = True
        world.player_1.y = get_height()-40
        world.player_1.speed = 0
    elif not colliding(world.player_1,world.ground):
        world.grounded_1 = False
        for platform_L1 in world.platforms_L1:
            if colliding(world.player_1,platform_L1):
            #if collision(world.player_1, platform_L1) and colliding(world.player_1, platform_L1):
                world.player_1.y = platform_L1.y - 30
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
def accelerate_player(world:Level1):
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
def create_level1() -> Level1:
    set_background_image(
        'https://cdna.artstation.com/p/assets/images/images/026/366/308/large/alicia-magistrello-basic-cave.jpg?1588597279')
    return Level1(create_ground(),
                  create_cave_entrance_1(), create_plat_L1(), False,
                  create_player1(), create_player2(), 3,3,display_health(),
                  True, True, False, False, False, False, "right","right",False, False, 0, 0,
                  create_p1_flashlight(), create_p2_flashlight(), False, False,
                  [])


when('starting:title', create_title_screen)
when('clicking:title',use_title_buttons)
when('starting:level1', create_level1)
when('typing:level1', keys_pressed_p1, keys_pressed_p2)
when('done typing:level1', keys_not_pressed_p1, keys_not_pressed_p2)
when('updating:level1', move_player1, move_player2)
when('updating:level1',stop_moving_players)
when('updating:level1',check_beat_levels)
when('updating:level1', check_groundings)
when('updating:level1',accelerate_player)
when('updating:level1', spawn_bats_1, move_bats_1, move_bats_1, flash_bat_collision_1,player_bat_collision_1)
when('updating:level1',update_health, lost_game)
when('starting:endscreen',create_end_screen)
when('clicking:endscreen',use_end_buttons)
when('starting:beatL1',create_beat_L1_screen)
when('clicking:beatL1',use_beat_L1_buttons)
debug()
