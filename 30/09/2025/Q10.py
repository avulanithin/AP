import turtle
import pygame

# Initialize Pygame mixer for sound
pygame.mixer.init()
sound = pygame.mixer.Sound("C:\\Users\\nitin\\Downloads\\beep.wav")  # Load sound

# Set up Turtle screen
screen = turtle.Screen()
screen.title("Sound Effect Example")
screen.setup(width=400, height=300)

# Function to play sound
def play_sound():
    sound.play()

# Bind SPACE key
screen.listen()
screen.onkey(play_sound, "space")

# Keep window open
screen.mainloop()
