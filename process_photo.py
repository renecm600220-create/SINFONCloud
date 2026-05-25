import sys, os
sys.stderr = open(os.devnull, 'w')
os.environ['NO_COLOR'] = '1'
os.environ['OMP_NUM_THREADS'] = '4'
os.environ['MKL_NUM_THREADS'] = '4'

sys.stderr = sys.__stderr__

from PIL import Image
from transparent_background import Remover
import torch

print("Cargando modelo...")
remover = Remover(mode='base')
torch.set_num_threads(4)

print("Procesando foto...")
img = Image.open("MODELO.JPG").convert("RGB")
w, h = img.size
print(f"Tamano: {w}x{h}")

# Resize for web
max_size = 600
ratio = min(max_size/w, max_size/h)
if ratio < 1:
    new_w = int(w * ratio)
    new_h = int(h * ratio)
    img_resized = img.resize((new_w, new_h), Image.LANCZOS)
else:
    img_resized = img
    new_w, new_h = w, h

print(f"Redimensionado: {new_w}x{new_h}")

# Save "before" (resized)
img_resized.save("docs/before.jpg", quality=85)
print("Antes guardado")

# Remove background
with torch.no_grad():
    result = remover.process(img_resized)

# Save "after"
result.save("docs/after.png")
print("Despues guardado")
print("DONE")