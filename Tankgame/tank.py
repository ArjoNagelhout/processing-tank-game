from bullet import Bullet

class Tank(object):
    def __init__(self, x, y, bullets, ui, is_player):
        self.x = x
        self.y = y
        self.body_rot = 0
        self.gun_rot = 0
        
        self._width = 20
        self._height = 30
        
        self.gun_width = 5
        self.gun_height = 30
        
        self.rot_width = 21
        self.rot_height = 23
        
        self.shoot_delay = 60
        self.shoot_current = 0
        self.can_shoot = True
        self.turn_speed = 2
        self.aim_speed = 2
        self.speed = 1
        self.knockback = 10
        
        self.key_drive = False
        self.key_turn_left = False
        self.key_turn_right = False
        self.key_reverse = False
        self.key_aim_left = False
        self.key_aim_right = False
        self.key_shoot = False
        self.key_build = False
        
        self.bullets = bullets
        
        self.real_x = self.x
        self.real_y = self.y
        self.acceleration = 0.1
        
        self.max_health = 5
        self.health = self.max_health
        self.build_offset = 60
        self.build_size = 20
        self.build_delay = self.shoot_delay + 5
        self.build_display_size = 10
        
        self.health_width = 50
        self.health_height = 5
        self.health_offset = 50
        
        self.max_cooldown = 200
        self.cooldown = 0
        self.can_be_hit = True
        
        self.dead = False
        
        self.is_player = is_player
        
        self.ui = ui
        
    
    def update(self, world):
        if self.dead:
            return
        
        turn_direction = -self.key_turn_left + self.key_turn_right
        turn_change = turn_direction * self.turn_speed
        self.body_rot += turn_change
        self.gun_rot += turn_change
        
        aim_direction = -self.key_aim_left + self.key_aim_right
        self.gun_rot += aim_direction * self.aim_speed
        
        drive_direction = -self.key_reverse + self.key_drive
        
        self.x += drive_direction * self.speed * cos(radians(self.body_rot))
        self.y += drive_direction * self.speed * sin(radians(self.body_rot))
        
        self.shoot_current -= 1
        if self.shoot_current <= 0:
            self.can_shoot = True
        
        if self.can_shoot:
            if self.key_shoot:
                self.shoot()
            elif self.key_build:
                self.build(world)
        
        if self.can_be_hit == False:
            self.cooldown -= 1
        
        if self.cooldown <= 0:
            self.can_be_hit = True
            
        
        self.real_x = lerp(self.real_x, self.x, self.acceleration)
        self.real_y = lerp(self.real_y, self.y, self.acceleration)
        
        if self.y-self.real_y < 0:
            for i in range(int(self._height / world.cell_size)):
                if world.grid[int((self.real_y - self._height/2) / world.cell_size)][int((self.real_x - self._height/2) / world.cell_size) + i]:
                    self.y = int((self.real_y - self._height/2) / world.cell_size) * world.cell_size + world.cell_size + self._height/2
                    continue
            
        if self.y-self.real_y > 0:
            for i in range(int(self._height / world.cell_size)):
                if world.grid[int((self.real_y + self._height/2) / world.cell_size)][int((self.real_x - self._height/2) / world.cell_size) + i]:
                    self.y = int((self.real_y + self._height/2) / world.cell_size) * world.cell_size - self._height/2
                    continue
        
        
        if self.x-self.real_x < 0:
            for i in range(int(self._height / world.cell_size)):
                if world.grid[int((self.real_y - self._height/2) / world.cell_size) + i][int((self.real_x - self._height/2) / world.cell_size)]:
                    self.x = int((self.real_x - self._height/2) / world.cell_size) * world.cell_size + world.cell_size + self._height/2
                    continue
            
        if self.x-self.real_x > 0:
            for i in range(int(self._height / world.cell_size)):
                if world.grid[int((self.real_y - self._height/2) / world.cell_size) + i][int((self.real_x + self._height/2) / world.cell_size)]:
                    self.x = int((self.real_x + self._height/2) / world.cell_size) * world.cell_size - self._height/2
                    continue
                
        if self.x < 0:
            self.x = 0
        
        if self.x > width:
            self.x = width
        
        if self.y < 0:
            self.y = 0
        
        if self.y > height:
            self.y = height
    
    def shoot(self):
        bullet_x = self.real_x + self.gun_height * cos(radians(self.gun_rot))
        bullet_y = self.real_y + self.gun_height * sin(radians(self.gun_rot))
        
        bullet = Bullet(bullet_x, bullet_y, self.gun_rot)
        self.bullets.append(bullet)
        self.can_shoot = False
        self.shoot_current = self.shoot_delay
        
        self.x -=  self.knockback * cos(radians(self.gun_rot))
        self.y -=  self.knockback * sin(radians(self.gun_rot))


    def build(self, world):
        build_x = self.real_x + self.build_offset * cos(radians(self.body_rot))
        build_y = self.real_y + self.build_offset * sin(radians(self.body_rot))
        
        self.can_shoot = False
        self.shoot_current = self.build_delay
        world.create(self.build_size, build_x, build_y)
        
    
    def hit(self):
        if self.can_be_hit:
            self.health -= 1
            self.can_be_hit = False
            self.cooldown = self.max_cooldown
            
            if self.health <= 0:
                self.dead = True
                
                if self.is_player:
                    self.ui.state = self.ui.gameover
    
    
    def render(self, debug):
        
        
        
        
        pushMatrix()
        translate(self.real_x, self.real_y)
        
        
        fill(0)
        rect(0-self.health_width/2, 0-self.health_height/2-self.health_offset, self.health_width, self.health_height)
        
        fill(255, 0, 0)
        rect(0-self.health_width/2, 0-self.health_height/2-self.health_offset, (self.health_width/self.max_health)*self.health, self.health_height)
    
        if debug:
            fill(0, 0, 255)
            rect(0-self._height/2, 0-self._height/2, self._height, self._height)
        
        # Draw body
        
        
        pushMatrix()
        rotate(radians(self.body_rot-90))
        
        # Draw build
        if self.key_build:
            fill(0, 0, 255)
            rect(0-self.build_display_size/2, self.build_offset-self.build_display_size/2, self.build_display_size, self.build_display_size)
        
        
        if not self.can_be_hit or self.dead:
            fill(0)
        else:
            if self.is_player:
                fill(0, 0, 255)
            else:
                fill(255, 0, 0)
        
        rect(0-self._width/2, 0-self._height/2, self._width, self._height)
        
        
        popMatrix()
        
        # Draw gun
        pushMatrix()
        rotate(radians(self.gun_rot-90))
        rect(0-self.rot_width/2, 0-self.rot_height/2, self.rot_width, self.rot_height)
        rect(0-self.gun_width/2, 0, self.gun_width, self.gun_height)
        
        popMatrix()
        
        popMatrix()
