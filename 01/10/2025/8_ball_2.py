import pygame
import math
import random
import sys

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Constants
WIDTH, HEIGHT = 1200, 700
TABLE_WIDTH, TABLE_HEIGHT = 900, 500
TABLE_X, TABLE_Y = 50, 100
BALL_RADIUS = 12
POCKET_RADIUS = 20
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
DARK_GREEN = (20, 100, 20)
BROWN = (139, 69, 19)
YELLOW = (255, 215, 0)
BLUE = (0, 0, 255)
RED = (220, 20, 60)
PURPLE = (128, 0, 128)
ORANGE = (255, 140, 0)
DARK_BLUE = (0, 0, 139)
LIGHT_BLUE = (135, 206, 250)
PINK = (255, 192, 203)
GRAY = (128, 128, 128)

# Ball colors dictionary - maps ball number to color
BALL_COLORS = {
    0: WHITE,  # Cue ball
    1: YELLOW,  # Solids 1-7
    2: BLUE,
    3: RED,
    4: PURPLE,
    5: ORANGE,
    6: (0, 128, 0),
    7: (128, 0, 0),
    8: BLACK,  # 8-ball
    9: YELLOW,  # Stripes 9-15
    10: BLUE,
    11: RED,
    12: PURPLE,
    13: ORANGE,
    14: (0, 128, 0),
    15: (128, 0, 0)
}

class Ball:
    """
    Ball class handles individual ball physics, rendering, and state
    """
    def __init__(self, x, y, number):
        """Initialize a ball with position and number"""
        self.x = x
        self.y = y
        self.vx = 0  # Velocity in x direction
        self.vy = 0  # Velocity in y direction
        self.number = number
        self.radius = BALL_RADIUS
        self.active = True  # False when pocketed
        self.mass = 1
        self.friction = 0.98  # Friction coefficient for deceleration
        self.is_stripe = number > 8  # Balls 9-15 are striped
        
    def update(self):
        """Update ball position and apply physics"""
        if not self.active:
            return
            
        # Apply friction to slow down the ball
        self.vx *= self.friction
        self.vy *= self.friction
        
        # Stop completely if moving very slowly
        if abs(self.vx) < 0.05:
            self.vx = 0
        if abs(self.vy) < 0.05:
            self.vy = 0
        
        # Update position based on velocity
        self.x += self.vx
        self.y += self.vy
        
        # Bounce off table edges (cushions) with energy loss
        if self.x - self.radius < TABLE_X + 30:
            self.x = TABLE_X + 30 + self.radius
            self.vx = -self.vx * 0.8  # Reverse direction with 80% energy
        elif self.x + self.radius > TABLE_X + TABLE_WIDTH - 30:
            self.x = TABLE_X + TABLE_WIDTH - 30 - self.radius
            self.vx = -self.vx * 0.8
            
        if self.y - self.radius < TABLE_Y + 30:
            self.y = TABLE_Y + 30 + self.radius
            self.vy = -self.vy * 0.8
        elif self.y + self.radius > TABLE_Y + TABLE_HEIGHT - 30:
            self.y = TABLE_Y + TABLE_HEIGHT - 30 - self.radius
            self.vy = -self.vy * 0.8
    
    def draw(self, screen):
        """Draw the ball with number or stripe pattern"""
        if not self.active:
            return
        
        color = BALL_COLORS.get(self.number, WHITE)
        
        # Draw ball shadow for depth effect
        shadow_surface = pygame.Surface((self.radius * 2 + 6, self.radius * 2 + 6), pygame.SRCALPHA)
        pygame.draw.circle(shadow_surface, (0, 0, 0, 80), 
                         (self.radius + 3, self.radius + 3), self.radius)
        screen.blit(shadow_surface, (int(self.x - self.radius), int(self.y - self.radius)))
        
        # Draw main ball circle
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius)
        
        # Draw stripe pattern for striped balls (9-15)
        if self.is_stripe and self.number != 8:
            # White center circle
            pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius - 4)
            # Colored stripe across middle
            pygame.draw.rect(screen, color, 
                           (int(self.x - self.radius), int(self.y - 3), 
                            self.radius * 2, 6))
        
        # Draw ball number
        if self.number > 0:
            font = pygame.font.Font(None, 16)
            text_color = WHITE if self.number == 8 else BLACK
            text = font.render(str(self.number), True, text_color)
            text_rect = text.get_rect(center=(int(self.x), int(self.y)))
            screen.blit(text, text_rect)
        
        # Draw highlight for 3D effect
        highlight_surface = pygame.Surface((8, 8), pygame.SRCALPHA)
        pygame.draw.circle(highlight_surface, (255, 255, 255, 150), (4, 4), 4)
        screen.blit(highlight_surface, (int(self.x - 4), int(self.y - 4)))
    
    def is_moving(self):
        """Check if ball is currently moving"""
        return abs(self.vx) > 0.05 or abs(self.vy) > 0.05
    
    def distance_to(self, other):
        """Calculate Euclidean distance to another ball"""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class Table:
    """
    Table class handles pool table rendering and pocket positions
    """
    def __init__(self):
        # Define 6 pocket positions: 4 corners + 2 middle
        self.pockets = [
            (TABLE_X + 25, TABLE_Y + 25),  # Top-left corner
            (TABLE_X + TABLE_WIDTH / 2, TABLE_Y + 15),  # Top-middle
            (TABLE_X + TABLE_WIDTH - 25, TABLE_Y + 25),  # Top-right corner
            (TABLE_X + 25, TABLE_Y + TABLE_HEIGHT - 25),  # Bottom-left corner
            (TABLE_X + TABLE_WIDTH / 2, TABLE_Y + TABLE_HEIGHT - 15),  # Bottom-middle
            (TABLE_X + TABLE_WIDTH - 25, TABLE_Y + TABLE_HEIGHT - 25)  # Bottom-right corner
        ]
    
    def draw(self, screen):
        """Draw the complete pool table"""
        # Draw outer wooden border
        pygame.draw.rect(screen, BROWN, 
                        (TABLE_X - 30, TABLE_Y - 30, 
                         TABLE_WIDTH + 60, TABLE_HEIGHT + 60))
        # Draw border accent
        pygame.draw.rect(screen, (101, 67, 33), 
                        (TABLE_X - 25, TABLE_Y - 25, 
                         TABLE_WIDTH + 50, TABLE_HEIGHT + 50), 5)
        
        # Draw green felt playing surface
        pygame.draw.rect(screen, GREEN, 
                        (TABLE_X, TABLE_Y, TABLE_WIDTH, TABLE_HEIGHT))
        
        # Draw table markings
        # Break line (at 1/4 of table)
        pygame.draw.line(screen, WHITE, 
                        (TABLE_X + TABLE_WIDTH * 0.25, TABLE_Y + 20),
                        (TABLE_X + TABLE_WIDTH * 0.25, TABLE_Y + TABLE_HEIGHT - 20), 2)
        
        # Center spot for racking (at 3/4 of table)
        pygame.draw.circle(screen, WHITE, 
                          (int(TABLE_X + TABLE_WIDTH * 0.75), 
                           int(TABLE_Y + TABLE_HEIGHT / 2)), 3)
        
        # Draw all 6 pockets
        for px, py in self.pockets:
            # Black pocket hole
            pygame.draw.circle(screen, BLACK, (int(px), int(py)), POCKET_RADIUS)
            # Gray pocket rim
            pygame.draw.circle(screen, (50, 50, 50), (int(px), int(py)), POCKET_RADIUS, 3)
    
    def check_pocketed(self, ball):
        """Check if a ball has fallen into any pocket"""
        for px, py in self.pockets:
            distance = math.sqrt((ball.x - px)**2 + (ball.y - py)**2)
            if distance < POCKET_RADIUS - 2:
                return True
        return False


class Cue:
    """
    Cue class handles cue stick aiming, power charging, and shooting
    """
    def __init__(self):
        self.angle = 0  # Angle of cue stick in radians
        self.power = 0  # Current power level
        self.max_power = 30  # Maximum power level
        self.charging = False  # Is power being charged
        self.visible = True  # Should cue be drawn
        
    def update(self, cue_ball, mouse_pos=None):
        """Update cue angle to point away from mouse"""
        if mouse_pos:
            dx = mouse_pos[0] - cue_ball.x
            dy = mouse_pos[1] - cue_ball.y
            self.angle = math.atan2(dy, dx)
    
    def charge_power(self):
        """Increase shooting power while charging"""
        if self.charging and self.power < self.max_power:
            self.power += 0.5
    
    def shoot(self, cue_ball):
        """Apply force to cue ball based on power and angle"""
        if self.power > 0:
            force = self.power / 5  # Scale power to reasonable velocity
            cue_ball.vx = math.cos(self.angle) * force
            cue_ball.vy = math.sin(self.angle) * force
            self.power = 0
            self.charging = False
            return True
        return False
    
    def draw(self, screen, cue_ball):
        """Draw the cue stick and power meter"""
        if not self.visible or not cue_ball.active:
            return
        
        # Calculate cue stick position
        cue_length = 200
        offset = 40 + (self.power * 2)  # Pull back cue based on power
        
        # Start position (behind cue ball)
        start_x = cue_ball.x + math.cos(self.angle) * offset
        start_y = cue_ball.y + math.sin(self.angle) * offset
        # End position (extending away from ball)
        end_x = start_x + math.cos(self.angle) * cue_length
        end_y = start_y + math.sin(self.angle) * cue_length
        
        # Draw wooden cue stick
        pygame.draw.line(screen, (200, 150, 100), 
                        (int(start_x), int(start_y)), 
                        (int(end_x), int(end_y)), 6)
        # Draw white tip
        pygame.draw.line(screen, WHITE, 
                        (int(start_x), int(start_y)), 
                        (int(start_x + math.cos(self.angle) * 30), 
                         int(start_y + math.sin(self.angle) * 30)), 8)
        
        # Draw aiming guideline (dotted line showing direction)
        aim_length = 150
        for i in range(0, int(aim_length), 20):
            seg_x = cue_ball.x - math.cos(self.angle) * i
            seg_y = cue_ball.y - math.sin(self.angle) * i
            # Check if segment is within table bounds
            if (TABLE_X < seg_x < TABLE_X + TABLE_WIDTH and 
                TABLE_Y < seg_y < TABLE_Y + TABLE_HEIGHT):
                pygame.draw.circle(screen, (255, 255, 255, 150), 
                                 (int(seg_x), int(seg_y)), 2)
        
        # Draw power meter when charging
        if self.charging:
            meter_x = WIDTH - 100
            meter_y = 50
            meter_height = 200
            
            # Meter outline
            pygame.draw.rect(screen, GRAY, (meter_x, meter_y, 40, meter_height), 2)
            
            # Filled power bar
            power_height = (self.power / self.max_power) * meter_height
            color = GREEN if self.power < self.max_power * 0.7 else RED
            pygame.draw.rect(screen, color, 
                           (meter_x + 2, meter_y + meter_height - power_height, 
                            36, power_height))
            
            # "POWER" label
            font = pygame.font.Font(None, 24)
            text = font.render("POWER", True, WHITE)
            screen.blit(text, (meter_x - 10, meter_y - 30))


class Game:
    """
    Main game class handling game logic, state management, and main loop
    """
    def __init__(self):
        # Initialize pygame display
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("8-Ball Pool")
        self.clock = pygame.time.Clock()
        
        # Initialize game objects
        self.table = Table()
        self.cue = Cue()
        self.balls = []
        
        # Game state variables
        self.current_player = 1  # 1 or 2
        self.player1_type = None  # 'solids' or 'stripes'
        self.player2_type = None
        self.game_state = 'break'  # 'break', 'playing', 'game_over'
        self.ball_in_hand = False  # Can place cue ball after scratch
        self.winner = None
        self.player1_score = 0  # Number of balls pocketed
        self.player2_score = 0
        self.foul = False  # Track if current turn was a foul
        
        # Setup sound effects
        try:
            self.hit_sound = pygame.mixer.Sound(buffer=self.generate_sound(440, 0.05))
            self.pocket_sound = pygame.mixer.Sound(buffer=self.generate_sound(220, 0.2))
        except:
            # If sound generation fails, disable sounds
            self.hit_sound = None
            self.pocket_sound = None
        
        # Initialize ball positions
        self.setup_balls()
    
    def generate_sound(self, frequency, duration):
        """Generate a simple beep sound effect"""
        sample_rate = 22050
        n_samples = int(round(duration * sample_rate))
        buf = []
        for i in range(n_samples):
            # Generate sine wave
            value = int(32767.0 * math.sin(2.0 * math.pi * frequency * i / sample_rate))
            buf.append([value, value])  # Stereo
        return pygame.sndarray.array(buf)
    
    def setup_balls(self):
        """Set up all 16 balls in starting positions"""
        self.balls = []
        
        # Create cue ball at breaking position (1/4 from left)
        cue_ball = Ball(TABLE_X + TABLE_WIDTH * 0.25, TABLE_Y + TABLE_HEIGHT / 2, 0)
        self.balls.append(cue_ball)
        
        # Rack the 15 object balls in triangle formation at 3/4 from left
        start_x = TABLE_X + TABLE_WIDTH * 0.75
        start_y = TABLE_Y + TABLE_HEIGHT / 2
        
        # Ball arrangement in standard 8-ball rack
        # 8-ball must be in center, solids and stripes distributed
        arrangement = [
            [1],                    # Row 1: 1 ball
            [9, 10],                # Row 2: 2 balls
            [2, 8, 11],             # Row 3: 3 balls (8-ball in center)
            [12, 3, 13, 4],         # Row 4: 4 balls
            [14, 5, 15, 6, 7]       # Row 5: 5 balls
        ]
        
        row_spacing = BALL_RADIUS * 2 + 2  # Space between rows
        ball_spacing = BALL_RADIUS * 2 + 1  # Space between balls in a row
        
        # Create balls in triangle formation
        for row_idx, row in enumerate(arrangement):
            y_offset = -(len(row) - 1) * ball_spacing / 2  # Center the row
            for col_idx, ball_num in enumerate(row):
                x = start_x + row_idx * row_spacing
                y = start_y + y_offset + col_idx * ball_spacing
                self.balls.append(Ball(x, y, ball_num))
    
    def handle_collisions(self):
        """Handle elastic collisions between all balls"""
        # Check every pair of balls
        for i, ball1 in enumerate(self.balls):
            if not ball1.active:
                continue
            
            for ball2 in self.balls[i+1:]:
                if not ball2.active:
                    continue
                
                distance = ball1.distance_to(ball2)
                
                # Check if balls are overlapping
                if distance < ball1.radius + ball2.radius:
                    # Play collision sound
                    if self.hit_sound and (ball1.is_moving() or ball2.is_moving()):
                        self.hit_sound.play()
                    
                    # Calculate collision normal vector
                    nx = (ball2.x - ball1.x) / distance
                    ny = (ball2.y - ball1.y) / distance
                    
                    # Calculate relative velocity
                    dvx = ball1.vx - ball2.vx
                    dvy = ball1.vy - ball2.vy
                    
                    # Calculate relative velocity along collision normal
                    dvn = dvx * nx + dvy * ny
                    
                    # Don't resolve if velocities are separating
                    if dvn > 0:
                        continue
                    
                    # Calculate collision impulse (momentum transfer)
                    impulse = 2 * dvn / (ball1.mass + ball2.mass)
                    
                    # Update velocities based on impulse
                    ball1.vx -= impulse * ball2.mass * nx
                    ball1.vy -= impulse * ball2.mass * ny
                    ball2.vx += impulse * ball1.mass * nx
                    ball2.vy += impulse * ball1.mass * ny
                    
                    # Separate overlapping balls to prevent sticking
                    overlap = ball1.radius + ball2.radius - distance
                    ball1.x -= overlap * nx * 0.5
                    ball1.y -= overlap * ny * 0.5
                    ball2.x += overlap * nx * 0.5
                    ball2.y += overlap * ny * 0.5
    
    def check_pocketed_balls(self):
        """Check for any balls that have been pocketed"""
        cue_ball = self.balls[0]
        pocketed = []
        
        for ball in self.balls:
            if ball.active and self.table.check_pocketed(ball):
                ball.active = False
                pocketed.append(ball.number)
                
                # Play pocket sound
                if self.pocket_sound:
                    self.pocket_sound.play()
                
                # Handle cue ball pocketed (scratch)
                if ball.number == 0:
                    self.foul = True
                    self.ball_in_hand = True
                    # Reactivate cue ball for placement
                    ball.active = True
                    ball.x = TABLE_X + TABLE_WIDTH * 0.25
                    ball.y = TABLE_Y + TABLE_HEIGHT / 2
                    ball.vx = ball.vy = 0
                
                # Handle 8-ball pocketed
                elif ball.number == 8:
                    self.check_8ball_pocket()
                
                # Handle regular ball pocketed
                else:
                    self.update_score(ball.number)
        
        return pocketed
    
    def update_score(self, ball_number):
        """Update player scores when a ball is pocketed"""
        is_stripe = ball_number > 8
        
        # Check if correct ball type was pocketed
        if self.current_player == 1:
            if self.player1_type == 'solids' and not is_stripe:
                self.player1_score += 1
            elif self.player1_type == 'stripes' and is_stripe:
                self.player1_score += 1
            else:
                self.foul = True  # Wrong ball type pocketed
        else:
            if self.player2_type == 'solids' and not is_stripe:
                self.player2_score += 1
            elif self.player2_type == 'stripes' and is_stripe:
                self.player2_score += 1
            else:
                self.foul = True
    
    def check_8ball_pocket(self):
        """Check if 8-ball pocket is legal win or loss"""
        # Player wins if they cleared their group first
        if self.current_player == 1:
            if self.player1_score >= 7:
                self.winner = 1
                self.game_state = 'game_over'
            else:
                # Pocketed 8-ball early = loss
                self.winner = 2
                self.game_state = 'game_over'
        else:
            if self.player2_score >= 7:
                self.winner = 2
                self.game_state = 'game_over'
            else:
                self.winner = 1
                self.game_state = 'game_over'
    
    def assign_ball_types(self):
        """Assign solid/stripe to players after first legal pocket"""
        if self.player1_type is not None:
            return  # Already assigned
        
        # Count which type was pocketed
        solids_pocketed = sum(1 for b in self.balls[1:9] if not b.active)
        stripes_pocketed = sum(1 for b in self.balls[9:] if not b.active and b.number != 8)
        
        # Assign based on what was pocketed
        if solids_pocketed > 0 and stripes_pocketed == 0:
            if self.current_player == 1:
                self.player1_type = 'solids'
                self.player2_type = 'stripes'
            else:
                self.player2_type = 'solids'
                self.player1_type = 'stripes'
        elif stripes_pocketed > 0 and solids_pocketed == 0:
            if self.current_player == 1:
                self.player1_type = 'stripes'
                self.player2_type = 'solids'
            else:
                self.player2_type = 'stripes'
                self.player1_type = 'solids'
    
    def all_balls_stopped(self):
        """Check if all balls have stopped moving"""
        return all(not ball.is_moving() for ball in self.balls if ball.active)
    
    def switch_turn(self):
        """Switch to other player's turn"""
        if self.foul:
            # Foul switches turn
            self.current_player = 2 if self.current_player == 1 else 1
            self.foul = False
        # If no foul and ball was pocketed, turn continues (handled in main loop)
    
    def draw_ui(self):
        """Draw all user interface elements"""
        font = pygame.font.Font(None, 36)
        small_font = pygame.font.Font(None, 24)
        
        # Draw dark background for UI areas
        pygame.draw.rect(self.screen, (30, 30, 30), (0, 0, WIDTH, 80))
        pygame.draw.rect(self.screen, (30, 30, 30), 
                        (TABLE_X + TABLE_WIDTH + 40, 0, 
                         WIDTH - TABLE_X - TABLE_WIDTH - 40, HEIGHT))
        
        # Draw title
        title = font.render("8-BALL POOL", True, YELLOW)
        self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 20))
        
        # Draw Player 1 info (left side)
        p1_color = GREEN if self.current_player == 1 else GRAY
        p1_text = font.render(f"Player 1", True, p1_color)
        self.screen.blit(p1_text, (50, 30))
        
        if self.player1_type:
            type_text = small_font.render(f"({self.player1_type})", True, p1_color)
            self.screen.blit(type_text, (50, 60))
        
        score_text = small_font.render(f"Score: {self.player1_score}/7", True, WHITE)
        self.screen.blit(score_text, (200, 45))
        
        # Draw Player 2 info (right side)
        p2_color = GREEN if self.current_player == 2 else GRAY
        p2_text = font.render(f"Player 2", True, p2_color)
        self.screen.blit(p2_text, (WIDTH - 250, 30))
        
        if self.player2_type:
            type_text = small_font.render(f"({self.player2_type})", True, p2_color)
            self.screen.blit(type_text, (WIDTH - 250, 60))
        
        score_text = small_font.render(f"Score: {self.player2_score}/7", True, WHITE)
        self.screen.blit(score_text, (WIDTH - 120, 45))
        
        # Draw game state messages at bottom
        if self.game_state == 'break':
            msg = small_font.render("BREAK SHOT - Click and drag to shoot!", True, YELLOW)
            self.screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT - 40))
        elif self.ball_in_hand:
            msg = small_font.render("BALL IN HAND - Click to place cue ball", True, RED)
            self.screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT - 40))
        
        # Draw control instructions on right side
        instructions = [
            "Mouse: Aim",
            "Click & Hold: Charge power",
            "Release: Shoot",
            "R: Restart"
        ]
        
        y_offset = 150
        for instruction in instructions:
            text = small_font.render(instruction, True, WHITE)
            self.screen.blit(text, (WIDTH - 190, y_offset))
            y_offset += 30
        
        # Draw game over screen with semi-transparent overlay
        if self.game_state == 'game_over':
            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.set_alpha(200)
            overlay.fill(BLACK)
            self.screen.blit(overlay, (0, 0))
            
            winner_text = font.render(f"PLAYER {self.winner} WINS!", True, YELLOW)
            self.screen.blit(winner_text, 
                           (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 2 - 50))
            
            restart_text = small_font.render("Press R to restart", True, WHITE)
            self.screen.blit(restart_text, 
                           (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 20))
    
    def run(self):
        """Main game loop"""
        running = True
        shot_taken = False
        
        while running:
            self.clock.tick(FPS)
            mouse_pos = pygame.mouse.get_pos()
            
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        # Restart game
                        self.__init__()
                        shot_taken = False
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.ball_in_hand:
                        # Place cue ball within table bounds
                        cue_ball = self.balls[0]
                        if (TABLE_X + 30 < mouse_pos[0] < TABLE_X + TABLE_WIDTH - 30 and
                            TABLE_Y + 30 < mouse_pos[1] < TABLE_Y + TABLE_HEIGHT - 30):
                            cue_ball.x = mouse_pos[0]
                            cue_ball.y = mouse_pos[1]
                            self.ball_in_hand = False
                    elif self.all_balls_stopped() and self.game_state != 'game_over':
                        # Start charging shot
                        self.cue.charging = True
                
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.cue.charging and self.all_balls_stopped():
                        # Release shot
                        if self.cue.shoot(self.balls[0]):
                            shot_taken = True
                            self.cue.visible = False
                            if self.game_state == 'break':
                                self.game_state = 'playing'
            
            # Update game state
            if not self.ball_in_hand:
                # Update cue stick
                if self.all_balls_stopped():
                    self.cue.update(self.balls[0], mouse_pos)
                    self.cue.charge_power()
                    self.cue.visible = True
                
                # Update all ball physics
                for ball in self.balls:
                    ball.update()
                
                # Handle ball collisions
                self.handle_collisions()
                
                # Check for pocketed balls
                pocketed = self.check_pocketed_balls()
                
                # Assign ball types after first legal pocket
                if pocketed and self.game_state == 'playing':
                    self.assign_ball_types()
                
                # Check for turn end after all balls stop
                if shot_taken and self.all_balls_stopped():
                    shot_taken = False
                    # Switch turn only if no ball was pocketed or there was a foul
                    if not pocketed or self.foul:
                        self.switch_turn()
                    self.foul = False
            
            # Rendering
            self.screen.fill((40, 40, 40))  # Dark gray background
            self.table.draw(self.screen)
            
            # Draw all balls
            for ball in self.balls:
                ball.draw(self.screen)
            
            # Draw cue stick
            if not self.ball_in_hand and self.game_state != 'game_over':
                self.cue.draw(self.screen, self.balls[0])
            
            # Draw user interface
            self.draw_ui()
            
            # Update display
            pygame.display.flip()
        
        # Cleanup and exit
        pygame.quit()
        sys.exit()


# Entry point - run the game
if __name__ == "__main__":
    game = Game()
    game.run()