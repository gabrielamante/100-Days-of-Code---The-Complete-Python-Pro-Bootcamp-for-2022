def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def hurdle():
    move()
    jump()

    # HURDLE 1

hurdle_number = 5
while hurdle_number > 0:
    hurdle()
    hurdle_number -= 1
move()
jump()

    # HURDLE 2

while at_goal() == False:
    hurdle()

    # HURDLE 3

while at_goal() == False:
    if front_is_clear() == True:
        move()
    else:
        jump()
    
    # HURDLE 4

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
def hurdle():
    move()
    jump()


while at_goal() == False:
    if wall_in_front():
        jump()
    else:
        move()