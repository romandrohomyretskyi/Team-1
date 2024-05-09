
import pygame as pg
import sys
import random



class Snake:
    
    def __init__(self, start_pos, MSIZE,apple):
        self.start_pos = start_pos
        self.snake = [self.start_pos]
        self.direction = 0 
        self.directions = [(1,0),(0, 1),(-1,0), (0,-1)]
        self.MSIZE = MSIZE
        self.alive = True
        self.apple = apple
        
    def update(self):
        new_pos = self.snake[0][0] + self.directions[self.direction][0], self.snake[0][1] + self.directions[self.direction][1]
        if not (0 <= new_pos[0] < self.MSIZE[0] and 0 <= new_pos[1] < self.MSIZE[1]) or new_pos in self.snake:
            self.alive = False
        else:
            self.snake.insert(0, new_pos)
            if new_pos == self.apple.pos:
                self.snake.append(self.snake[-1])    
                self.apple.new()    
            else:
                self.snake.pop()
                
class Apple:
    def __init__(self, MSIZE):
        self.MSIZE = MSIZE
        self.new() 
        
    def new(self):
        self.pos = random.randint(0, self.MSIZE[0]-1), random.randint(0, self.MSIZE[1]-1)

class SnakeGame:
    def __init__(self):
        pg.init()
        self.WSIZE = (720, 480)
        self.screen = pg.display.set_mode(self.WSIZE)
        self.TSIDE = 30
        self.MSIZE = self.WSIZE[0] // self.TSIDE, self.WSIZE[1] // self.TSIDE
        self.clock = pg.time.Clock()
        self.font_score = pg.font.SysFont("Arial", 25)
        self.font_gameover = pg.font.SysFont("Arial", 45)
        self.font_space = pg.font.SysFont("Arial", 18)
        self.apple = Apple(self.MSIZE)
        self.snake = Snake((self.MSIZE[0] // 2, self.MSIZE[1] // 2), self.MSIZE, self.apple)
        self.fps = 10
        
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN:
                if self.snake.alive:
                    if event.key == pg.K_RIGHT and self.snake.direction != 2:
                        self.snake.direction = 0
                    if event.key == pg.K_DOWN and self.snake.direction != 3:
                        self.snake.direction = 1
                    if event.key == pg.K_LEFT and self.snake.direction != 0:
                        self.snake.direction = 2
                    if event.key == pg.K_UP and self.snake.direction != 1:
                        self.snake.direction = 3
                else:
                    if event.key == pg.K_SPACE:
                        self.snake.alive = True
                        self.snake.snake = [self.snake.start_pos]
                        self.apple.new()
                        self.fps = 10

    def run(self):
        self.running = True
        while self.running:
            self.update()
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        for segment in self.snake.snake:
            pg.draw.rect(self.screen, (0, 255, 0), (segment[0]*self.TSIDE, segment[1]*self.TSIDE, self.TSIDE, self.TSIDE))
        pg.draw.rect(self.screen, (255, 0, 0), (self.apple.pos[0]*self.TSIDE, self.apple.pos[1]*self.TSIDE, self.TSIDE, self.TSIDE))

    
    def update(self):
        self.handle_events()
        self.clock.tick(self.fps)
        if self.snake.alive:
            self.snake.update()
        self.draw()
        pg.display.flip()
    
    


        
                
    
