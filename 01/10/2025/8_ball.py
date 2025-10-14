import pygame, math, sys

pygame.init()

# ----------------------------
# CONFIG
# ----------------------------
WIDTH, HEIGHT = 1200, 700
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("8-Ball Pool")

# COLORS
GREEN_FELT = (30, 120, 30)
CUSHION_GREEN = (20, 70, 20)
WOOD_BROWN = (139, 69, 19)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# POCKETS (6 positions)
POCKET_RADIUS = 32
POCKETS = [
    (50, 50),  # Top-left
    (WIDTH // 2, 40),  # Top-middle
    (WIDTH - 50, 50),  # Top-right
    (50, HEIGHT - 50),  # Bottom-left
    (WIDTH // 2, HEIGHT - 40),  # Bottom-middle
    (WIDTH - 50, HEIGHT - 50)  # Bottom-right
]

# FIX 1: Removed wrong pockets (top-mid, bottom-mid) → replaced with proper side pockets
POCKETS = [
    (50, 50), (WIDTH - 50, 50),
    (WIDTH // 2, 50), (WIDTH // 2, HEIGHT - 50),
    (50, HEIGHT - 50), (WIDTH - 50, HEIGHT - 50)
]


# ----------------------------
# BALL CLASS
# ----------------------------
class Ball:
    def __init__(self, x, y, color, radius=12, number=None, striped=False):
        self.x, self.y = x, y
        self.vx, self.vy = 0, 0
        self.color = color
        self.radius = radius
        self.number = number
        self.striped = striped
        self.in_play = True

    def update(self):
        # Apply friction
        self.x += self.vx
        self.y += self.vy
        self.vx *= 0.985
        self.vy *= 0.985
        if abs(self.vx) < 0.05: self.vx = 0
        if abs(self.vy) < 0.05: self.vy = 0

        # Bounce off cushions
        if self.x < 60 or self.x > WIDTH - 60:
            self.vx *= -1
        if self.y < 60 or self.y > HEIGHT - 60:
            self.vy *= -1

        # Pocket check
        for px, py in POCKETS:
            if math.hypot(self.x - px, self.y - py) < POCKET_RADIUS:
                self.in_play = False

    def draw(self, surface):
        if not self.in_play: return

        # Ball base
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

        # FIX 4: Add highlight (shiny reflection)
        pygame.draw.circle(surface, WHITE, (int(self.x - 4), int(self.y - 4)), 4)

        # Ball numbers
        if self.number:
            font = pygame.font.SysFont("Arial", 12, bold=True)
            text = font.render(str(self.number), True, BLACK)
            rect = text.get_rect(center=(self.x, self.y))
            surface.blit(text, rect)


# ----------------------------
# CUE CLASS
# ----------------------------
class Cue:
    def __init__(self, cue_ball):
        self.cue_ball = cue_ball
        self.visible = True
        self.power = 0
        self.charging = False

    def handle_input(self, events):
        # Only show if balls are stopped
        if any(abs(b.vx) > 0.1 or abs(b.vy) > 0.1 for b in game.balls):
            self.visible = False
            return
        else:
            self.visible = True

        # Mouse controls
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                self.charging = True
                self.power = 0
            if e.type == pygame.MOUSEBUTTONUP and self.charging:
                self.shoot()
                self.charging = False
                self.power = 0

        if self.charging:
            self.power = min(self.power + 0.5, 20)  # cap power

    def shoot(self):
        # Aim based on mouse position
        mx, my = pygame.mouse.get_pos()
        dx, dy = mx - self.cue_ball.x, my - self.cue_ball.y
        dist = math.hypot(dx, dy)
        if dist == 0: return
        dx, dy = dx / dist, dy / dist

        self.cue_ball.vx -= dx * self.power
        self.cue_ball.vy -= dy * self.power

    def draw(self, surface):
        if not self.visible: return

        mx, my = pygame.mouse.get_pos()
        dx, dy = mx - self.cue_ball.x, my - self.cue_ball.y
        angle = math.atan2(dy, dx)

        # Stick length based on charging
        stick_length = 100 + self.power * 5
        x2 = self.cue_ball.x - math.cos(angle) * stick_length
        y2 = self.cue_ball.y - math.sin(angle) * stick_length

        pygame.draw.line(surface, (200, 150, 100),
                         (self.cue_ball.x, self.cue_ball.y),
                         (x2, y2), 6)


# ----------------------------
# TABLE CLASS
# ----------------------------
class Table:
    def draw(self, surface):
        # Draw felt
        surface.fill(GREEN_FELT)

        # Borders
        pygame.draw.rect(surface, WOOD_BROWN, (0, 0, WIDTH, HEIGHT), border_radius=20)
        pygame.draw.rect(surface, GREEN_FELT, (40, 40, WIDTH - 80, HEIGHT - 80), border_radius=15)

        # Cushions
        pygame.draw.rect(surface, CUSHION_GREEN, (50, 50, WIDTH - 100, HEIGHT - 100), border_radius=10)

        # FIX 3: Draw 6 natural pockets
        for px, py in POCKETS:
            pygame.draw.circle(surface, BLACK, (px, py), POCKET_RADIUS)


# ----------------------------
# GAME CLASS
# ----------------------------
class Game:
    def __init__(self):
        self.table = Table()
        self.balls = []
        self.setup_balls()
        self.cue = Cue(self.balls[0])  # cue ball
        self.running = True

    def setup_balls(self):
        # Cue ball
        self.balls.append(Ball(300, HEIGHT // 2, WHITE))

        # Example rack: just fill with colors
        colors = [(255, 0, 0), (0, 0, 255), (255, 255, 0),
                  (255, 165, 0), (128, 0, 128), (0, 255, 0),
                  (255, 192, 203)]
        x_start, y_start = 800, HEIGHT // 2
        n = 1
        for row in range(5):
            for col in range(row + 1):
                x = x_start + row * 25
                y = y_start - row * 12 + col * 24
                color = colors[(n - 1) % len(colors)]
                self.balls.append(Ball(x, y, color, number=n))
                n += 1

    def update(self, events):
        self.cue.handle_input(events)
        for b in self.balls:
            if b.in_play: b.update()

    def draw(self):
        self.table.draw(screen)
        for b in self.balls: b.draw(screen)
        self.cue.draw(screen)
        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            self.update(events)
            self.draw()
            clock.tick(FPS)


# ----------------------------
# MAIN
# ----------------------------
if __name__ == "__main__":
    game = Game()
    game.run()
