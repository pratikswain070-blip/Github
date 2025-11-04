import pygame
import sys
import math
import random
pygame.init()

# --- Screen ---
WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Full Cartoon Drinking Animation")

clock = pygame.time.Clock()

# --- Colors ---
SKY = (180, 210, 255)
FLOOR = (100, 60, 40)
SKIN = (255, 224, 189)
BLACK = (0, 0, 0)
GLASS = (240, 240, 255)
WHISKEY = (230, 140, 20)

# --- Sound (optional) ---
try:
    drink_sound = pygame.mixer.Sound("drink.wav")
except:
    drink_sound = None

# Tween function for smooth motion
def ease_in_out(t):
    return t * t * (3 - 2 * t)

class Character:
    def __init__(self, x_start, x_end, y, delay):
        self.x = x_start
        self.x_start = x_start
        self.x_end = x_end
        self.y = y
        self.walk_time = 0
        self.walk_duration = 120
        self.delay = delay
        self.state = "waiting"  # waiting → walking → drinking → walking_out
        self.arm_angle = 0
        self.lifting = True
        self.blink_timer = random.randint(60, 160)
        self.eye_closed = False
        self.drink_cycles = 0

    def update(self):
        # Blink
        self.blink_timer -= 1
        if self.blink_timer <= 0:
            self.eye_closed = True
            if self.blink_timer <= -8:
                self.eye_closed = False
                self.blink_timer = random.randint(80, 200)

        # State machine
        if self.state == "waiting":
            self.delay -= 1
            if self.delay <= 0:
                self.state = "walking"

        elif self.state == "walking":
            self.walk_time += 1
            t = min(1, self.walk_time / self.walk_duration)
            smooth = ease_in_out(t)
            self.x = self.x_start + (self.x_end - self.x_start) * smooth
            if t >= 1:
                self.state = "drinking"

        elif self.state == "drinking":
            self.animate_drink()

        elif self.state == "walking_out":
            self.walk_time += 1
            t = min(1, self.walk_time / self.walk_duration)
            smooth = ease_in_out(t)
            self.x = self.x_end + (self.x_start - self.x_end) * smooth
            if t >= 1:
                self.state = "done"

    def animate_drink(self):
        # Smooth arm up/down
        speed = 0.025
        if self.lifting:
            self.arm_angle += speed
            if self.arm_angle > 1.4:
                self.lifting = False
                if drink_sound:
                    drink_sound.play()
                self.drink_cycles += 1
        else:
            self.arm_angle -= speed
            if self.arm_angle < 0.1:
                self.lifting = True
            if self.drink_cycles >= 3:
                self.state = "walking_out"
                self.walk_time = 0

    def draw(self, surf):
        x = int(self.x)
        y = int(self.y)

        # Head
        pygame.draw.circle(surf, SKIN, (x, y - 110), 35)

        # Eyes
        if self.eye_closed:
            pygame.draw.line(surf, BLACK, (x - 12, y - 115), (x - 2, y - 115), 3)
            pygame.draw.line(surf, BLACK, (x + 2, y - 115), (x + 12, y - 115), 3)
        else:
            pygame.draw.circle(surf, BLACK, (x - 7, y - 115), 4)
            pygame.draw.circle(surf, BLACK, (x + 7, y - 115), 4)

        # Body
        pygame.draw.line(surf, BLACK, (x, y - 75), (x, y + 40), 6)

        # Legs
        pygame.draw.line(surf, BLACK, (x, y + 40), (x - 25, y + 120), 6)
        pygame.draw.line(surf, BLACK, (x, y + 40), (x + 25, y + 120), 6)

        # Static arm
        pygame.draw.line(surf, BLACK, (x, y - 70), (x - 60, y - 20), 6)

        # Animated arm
        arm_len = 85
        end_x = x + arm_len * math.cos(self.arm_angle)
        end_y = (y - 70) - arm_len * math.sin(self.arm_angle)
        pygame.draw.line(surf, BLACK, (x, y - 70), (end_x, end_y), 6)

        # Whiskey glass
        pygame.draw.ellipse(surf, GLASS, (end_x - 12, end_y, 24, 28))
        pygame.draw.rect(surf, BLACK, (end_x - 1, end_y + 27, 2, 12))

        # Liquid level moves slightly when drinking
        liquid_height = 20 - (self.arm_angle * 4)
        pygame.draw.rect(surf, WHISKEY, (end_x - 8, end_y + 10, 16, max(1, liquid_height)))


# --- Background ---
def draw_background(surf):
    surf.fill(SKY)
    pygame.draw.rect(surf, FLOOR, (0, HEIGHT - 140, WIDTH, 140))

    # Simple bar shelves
    pygame.draw.rect(surf, (60, 40, 20), (0, HEIGHT - 180, WIDTH, 20))
    pygame.draw.rect(surf, (80, 55, 30), (0, HEIGHT - 220, WIDTH, 20))

    # Bottles on shelves
    for i in range(12):
        bx = 50 + i * 70
        pygame.draw.rect(surf, (20, 150, 40), (bx, HEIGHT - 235, 18, 40))
        pygame.draw.rect(surf, (150, 20, 20), (bx + 3, HEIGHT - 225, 12, 30))


# --- Create multiple characters ---
characters = [
    Character(-200, 300, HEIGHT - 140, delay=30),
    Character(WIDTH + 200, 600, HEIGHT - 140, delay=90)
]

# --- Main Loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_background(screen)

    for c in characters:
        if c.state != "done":
            c.update()
            c.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
