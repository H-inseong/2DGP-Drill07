from fileinput import close
import random

from pico2d import *

# Game object class here
class Grass:
    def __init__(self):
        # 모양없는 납작한 붕어빵의 초기모습결정
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

    def update(self):
        pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame =  random.randint(0, 7)
        self.image = load_image('run_animation.png')
    def update(self):

        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

ball_count = 0
class Ball:
    def __init__(self):
        global ball_count
        self.x, self.y = random.randint(100, 700), 599
        self.dy = ball_count + 5
        self.size = random.randint(0,2)
        if self.size:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')
        ball_count += 1

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if self.size == 0:
            if self.y - self.dy > 60:
              self.y -= self.dy
            else:
                self.y = 60
        else:
            if self.y - self.dy> 50:
              self.y -= self.dy
            else:
                self.y = 50



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global grass
    global team
    global world
    global balls

    running = True
    world = []
    grass = Grass() # 잔디 생성
    world.append(grass)
    team = [Boy() for i in range(10)]
    balls = [Ball() for i in range(20)]
    world += team
    world += balls

def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


open_canvas()
# initialization code
reset_world()
# game main loop code
running = True
while running:
    # game logic
    handle_events()
    update_world()
    render_world()

    delay(0.05)


# finalization code
close_canvas()