from fileinput import close

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
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


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
    global boy

    running = True
    grass = Grass() # 잔디 생성
    boy = Boy()

def update_world():
    grass.update() # 객체 상태 업데이트
    boy.update()

def render_world():
    clear_canvas()
    grass.draw()
    boy.draw()
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