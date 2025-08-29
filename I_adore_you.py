from rich import print
from time import sleep
import time

def printLyrics():
    lines = [
        ("Cuz you know baby", 0.06, 0.3),
        ("I adore you", 0.06, 0.8),
        ("I adore you", 0.08, 0.8),
        ("Can't ignore you", 0.08, 0.7),
        ("Can't ignore you (ah)", 0.08, 0.7),
        ("Body ody my soul and that", 0.05, 0.6),
        ("I'm outta control I can't", 0.05, 0.6),
        ("I adore you", 0.08, 0.6),
        ("I adore you, I do", 0.1, 1),
        ("Plenty more", 0.05, 0.2),
        ("Plenty more", 0.05, 0.8),
        ("But you're my hope for the night", 0.07, 0.5),
        ("Gimme more control", 0.05, 0.8),
        ("Slow down for the night", 0.05, 0.8),
        ("Lemme know", 0.05, 0.2),
        ("Lemme know", 0.05, 0.2),

    ]









    for text, char_delay, line_delay in lines:
        # Print each character with delay
        for char in text:
            print(char, end="", flush=True)
            sleep(char_delay)
        print()  # New line
        if line_delay > 0:  # Only sleep if delay is specified
            sleep(line_delay)

printLyrics()
