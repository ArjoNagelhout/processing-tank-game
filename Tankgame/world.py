class World(object):

    def __init__(self, grid_width, grid_height, cell_size):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.cell_size = cell_size
        
        self.grid = []
    
    def create(self, radius, x, y):
        rect_start_x = x - radius // 2
        rect_start_y = y - radius // 2
        
        for dy in range(radius):
            for dx in range(radius):
                if rect_start_x + dx >= width or rect_start_y + dy >= height \
                    or rect_start_x + dx < 0 or rect_start_y + dy < 0:
                    continue
                self.grid[int((rect_start_y + dy) /  self.cell_size)][int((rect_start_x + dx) / self.cell_size)] = 1
    
    def destroy(self, radius, x, y):
        rect_start_x = x - radius // 2
        rect_start_y = y - radius // 2
        
        for dy in range(radius):
            for dx in range(radius):
                if rect_start_x + dx >= width or rect_start_y + dy >= height \
                    or rect_start_x + dx < 0 or rect_start_y + dy < 0:
                    continue
                self.grid[int((rect_start_y + dy) /  self.cell_size)][int((rect_start_x + dx) / self.cell_size)] = 0
                
    def render(self):
        fill(0)
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x]:
                    rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
    
    def fill_grid(self, _width, _height, a=1, grid=None):
        min_beam_width, max_beam_width = _width // 10, _height // 6
        number_of_beams = int(random(_width // 2, _width))
        
        if grid is None:
            grid = [[0 for _ in range(_width)] for _ in range(_height)]
        
        for _ in range(number_of_beams):
            if int(random(0, 1)) == 0:
                x, y = int(random(0, _width)), int(random(0, _height // 2))
            else:
                x, y = int(random(0, _width // 2)), int(random(0, _height))
        
            beam_size = int(random(min_beam_width, max_beam_width))
            alpha = int(random(45, 90))
            dy = int(random(1, 2))
            dx = int(random(1, 2))
        
            while True:
                if x < 0 or x >= _width or y < 0 or y >= _height:
                    break
            
                if int(random(1, 10)) == 1:
                    break
            
                grid[y][x] = a
            
                x += dx
                y += dy
        
        return grid
        
    def create_grid(self):
        self.grid = self.fill_grid(self.grid_width/self.cell_size, self.grid_height/self.cell_size)
        b = int(random(0, self.grid_width // 2))
        
        for _ in range(b):
            x = int(random(0, self.grid_width/self.cell_size))
            y = int(random(0, self.grid_height/self.cell_size))
            h = int(random(1, self.grid_width/self.cell_size // 3))
            w = int(random(1, self.grid_height/self.cell_size // 3))
            
        
            for hx in range(h):
                s = int(int(random(1, 10) != 1))
                if x + hx >= self.grid_width/self.cell_size:
                    break
            
                for hy in range(h):
                    if y + hy >= self.grid_height/self.cell_size:
                        break
                    self.grid[x + hx][y + hy] = s
        
        self.fill_grid(self.grid_width/self.cell_size, self.grid_height/self.cell_size, 0, self.grid)
