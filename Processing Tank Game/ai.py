class AI(object):
    def __init__(self, speed):
        self.speed = speed
        self.timer = 20
        
    def move(self, tank):
        tank.key_aim_right = True
        tank.key_drive = True
        tank.key_shoot = True
        
        self.timer -= 1
        
        if self.timer <= 0:
            self.timer = int(random(10, 60))
            
            self.do_random(tank)
    
    def do_random(self, tank):
        a = int(random(5))
        if a == 0:
            tank.key_aim_right = True
            tank.key_aim_left = False
        elif a == 1:
            tank.key_aim_right = False
            tank.key_aim_left = True
        elif a == 2:
            tank.key_turn_right = True
            tank.key_turn_left = False
        elif a == 3:
            tank.key_turn_right = False
            tank.key_turn_left = True
        elif a == 4:
            tank.key_turn_right = False
            tank.key_turn_left = False
