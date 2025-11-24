import tkinter as tk
from PIL import Image, ImageTk
import pygame


pygame.mixer.init()
pygame.mixer.music.load("sound.mp3")   


root = tk.Tk()
root.title("Tkinter Background Image + Sound")
root.geometry("600x400")


bg_image = Image.open("background.jpg")   
bg_image = bg_image.resize((600, 400))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


def play_sound():
    pygame.mixer.music.play()


btn = tk.Button(root, text="Play Sound", font=("Arial", 16), command=play_sound)
btn.place(x=240, y=170)

root.mainloop()