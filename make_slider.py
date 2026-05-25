from PIL import Image
import numpy as np

print("Cargando imagenes...")
before = Image.open("docs/before.jpg").convert("RGB")
after = Image.open("docs/after.png").convert("RGBA")

# Make same size
w = min(before.width, after.width)
h = min(before.height, after.height)
before = before.resize((w, h), Image.LANCZOS)
after = after.resize((w, h), Image.LANCZOS)

# Create checkerboard background
checker = Image.new("RGB", (w, h))
pixels = checker.load()
block = 20
for y in range(h):
    for x in range(w):
        if ((x // block) + (y // block)) % 2 == 0:
            pixels[x, y] = (230, 230, 230)
        else:
            pixels[x, y] = (200, 200, 200)

# Paste after on checkerboard
checker.paste(after, (0, 0), after)

before.save("docs/before.jpg", quality=90)
checker.save("docs/after.jpg", quality=90)
print(f"Tamano: {w}x{h}")
print("DONE")