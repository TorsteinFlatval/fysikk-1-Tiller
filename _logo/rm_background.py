from rembg import remove
from PIL import Image

inp = Image.open("r1_logo.jpg").convert("RGBA")
out = remove(inp)  # returns a PIL image or bytes depending on version
out.save("logo_nobg.png")
