class UI(object):
    
    def __init__(self):
        
        self.gamestart = 0
        self.gameplay = 1
        self.gameover = 2
        self.pause = 3
        
        self.state = self.gamestart
        
        self.font_bold = createFont("Roboto/Roboto-Bold.ttf", 60)
        self.font_regular = createFont("Roboto/Roboto-Regular.ttf", 40)
        
    def render(self):
        if self.state == self.gamestart:
            self.draw_background()
            fill(255)
            textAlign(CENTER)
            textFont(self.font_bold)
            textSize(20)
            text("<Press space to start>", width/2, height-40)
                 
            textSize(60)
            
            text("Processing Tank Game", width/2, 100)
            
            textFont(self.font_regular)
            textSize(30)
            textLeading(40)
            text("Game logic by Arjo\nMap generation by Renze", width/2, 150)
            
            textAlign(LEFT)
            textSize(20)
            textLeading(20)
            text("<W> drive forward\n<S> drive backwards\n<A> turn left\n<D> turn right\n<J> aim left\n<L> aim right\n<SPACE> shoot\n<K> build\n<P> pause", width/2-100, 300)
            
            
        elif self.state == self.gameplay:
            textAlign(RIGHT)
            textFont(self.font_bold)
            textSize(20)
            fill(255)
            text("<P> pause", width-40, 40)
            
        elif self.state == self.gameover:
            self.draw_background()
            fill(255)
            textAlign(CENTER)
            textFont(self.font_bold)
            textSize(60)
            text("Game Over", width/2, 100)
            
            textAlign(CENTER)
            textFont(self.font_bold)
            textSize(20)
            text("<Press space to go back to menu>", width/2, height-40)
            
        elif self.state == self.pause:
            self.draw_background()
            fill(255)
            textAlign(CENTER)
            textFont(self.font_bold)
            textSize(60)
            text("Pause", width/2, 100)
            
            fill(255)
            textAlign(CENTER)
            textFont(self.font_bold)
            textSize(20)
            text("<Press space or P to continue>\n<R> Restart", width/2, height-80)
            
            textAlign(LEFT)
            textSize(20)
            textLeading(20)
            text("<W> drive forward\n<S> drive backwards\n<A> turn left\n<D> turn right\n<J> aim left\n<L> aim right\n<SPACE> shoot\n<K> build", width/2-100, 250)
            
    
    def draw_background(self):
        fill(0, 100)
        rect(0, 0, width, height)
