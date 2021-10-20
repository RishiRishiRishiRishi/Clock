import pygame
from tkinter import *
from tkinter.ttk import *
from time import strftime
import math
import time
import pyttsx3
import datetime
from tkinter import *
root = Tk()
root.title("Clock")
def clock():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices[0].id)
    engine.setProperty('voice', voices[0].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour > 0 and hour < 12:
            speak("Good morning")
        elif hour >= 12 and hour < 18:
            speak("Good afternoon")
        else:
            speak("Good evening")

    if __name__ == "__main__":
        wishMe()

    screen_width = 600
    screen_height = 600

    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Clock')

    def draw_markings():
        d = 100
        d2 = 10
        for i in range(0, 360, 30):
            x1 = screen_width // 2 + d * math.cos(math.radians(i))
            y1 = screen_height // 2 + d * math.sin(math.radians(i))
            x2 = x1 + d2 * math.cos(math.radians(i))
            y2 = y1 + d2 * math.sin(math.radians(i))
            pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2), 5)

    def arc(center, radius, start, end, thickness, color):
        for i in range(start, end):
            x = center[0] + radius * math.cos(math.radians(i - 90))
            y = center[1] + radius * math.sin(math.radians(i - 90))
            pygame.draw.circle(screen, color, (int(x), int(y)), thickness)

    def clock_hand(center, radius, angle, thickness, color):
        x = center[0] + radius * math.cos(math.radians(angle - 90))
        y = center[1] + radius * math.sin(math.radians(angle - 90))
        pygame.draw.line(screen, color, center, (int(x), int(y)), thickness)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        screen.fill((0, 0, 0))
        draw_markings()
        curr_time = time.strftime('%I%M%S', time.localtime(time.time()))
        s = int(curr_time[4]) * 10 + int(curr_time[5])
        m = int(curr_time[2]) * 10 + int(curr_time[3])
        h = int(curr_time[0]) * 10 + int(curr_time[1])
        arc((screen_width // 2, screen_height // 2), 200, 0, s * 6, 11, (0, 255, 0))
        arc((screen_width // 2, screen_height // 2), 180, 0, m * 6, 11, (0, 0, 255))
        arc((screen_width // 2, screen_height // 2), 160, 0, h * 30, 11, (255, 0, 0))
        clock_hand((screen_width // 2, screen_height // 2), 140, s * 6, 5, (0, 255, 0))
        clock_hand((screen_width // 2, screen_height // 2), 120, m * 6, 5, (0, 0, 255))
        clock_hand((screen_width // 2, screen_height // 2), 100, h * 30, 5, (255, 0, 0))
        pygame.display.update()
def digitalclock():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices[0].id)
    engine.setProperty('voice', voices[0].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour > 0 and hour < 12:
            speak("Good morning")
        elif hour >= 12 and hour < 18:
            speak("Good afternoon")
        else:
            speak("Good evening")

    if __name__ == "__main__":
        wishMe()

    root = Tk()
    root.title("DIGITAL CLOCK")

    def time():
        string = strftime("%H:%M:%S %p")
        label.config(text=string)
        label.after(1000, time)

    label = Label(root, font=("ds-digital", 80), background="Black", foreground="cyan")
    label.pack(anchor="center")
    time()

    mainloop()

root.geometry("1450x100")
frame = Frame(root)
frame.pack(anchor="center", fill="x")
button1 = Button(frame, text="Clock", bg="red", fg="black", borderwidth=10, relief=SUNKEN, command=clock)
button1.pack(anchor="center", fill="x")
button2 = Button(frame, text="Digital Clock", bg="red", fg="black", borderwidth=10, relief=SUNKEN, command=digitalclock)
button2.pack(anchor="center", fill="x")
root.mainloop()