from moviepy import *
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os

WIDTH, HEIGHT = 1080, 1920
FPS = 30
DURATION = 15

os.makedirs("output", exist_ok=True)
IMAGE_PATH = "IMG_2598.jpeg"

def get_font(size):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf"
    ]
    for path in paths:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()

def make_scene(title, subtitle, number):
    image = Image.new("RGB", (WIDTH, HEIGHT), (8, 8, 8))
    draw = ImageDraw.Draw(image)

    red = (225, 35, 45)
    white = (255, 255, 255)
    grey = (175, 175, 175)

    draw.rectangle((70, 100, 1010, 112), fill=red)
    draw.text((80, 220), "SECUREHAUS", font=get_font(48), fill=white)
    draw.text((80, 300), "RED FLAG SAFETY NETWORK EU",
              font=get_font(27), fill=red)

    draw.text((80, 680), number, font=get_font(35), fill=red)
    draw.multiline_text((80, 790), title, font=get_font(82),
                        fill=white, spacing=25)
    draw.multiline_text((80, 1120), subtitle, font=get_font(38),
                        fill=grey, spacing=20)

    draw.rectangle((80, 1650, 1000, 1658), fill=red)
    draw.text((80, 1710), "securehausredflag.com",
              font=get_font(35), fill=white)

    return np.array(image)

scenes = [
    ("SAFETY STARTS\nWITH AWARENESS",
     "Recognise the warning signs.\nMake informed decisions.", "01"),
    ("KNOW THE\nRED FLAGS",
     "Stay alert. Check the facts.\nProtect what matters.", "02"),
    ("CHECK BEFORE\nYOU TRUST",
     "Review. Verify. Decide.\nYour safety comes first.", "03"),
    ("STAY INFORMED.\nSTAY SAFE.",
     "Visit our network and learn more.\nsecurehausredflag.com/#/", "04")
]

clips = []

for title, subtitle, number in scenes:
    frame = make_scene(title, subtitle, number)
    clip = ImageClip(frame).with_duration(3.75)
    clips.append(clip)

video = concatenate_videoclips(clips, method="compose")
video = video.with_fps(FPS)

video.write_videofile(
    "output/securehaus_reel.mp4",
    fps=FPS,
    codec="libx264",
    audio=False
)
