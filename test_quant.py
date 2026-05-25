import sys, os
sys.stderr = open(os.devnull, 'w')
os.environ['NO_COLOR'] = '1'
os.environ['OMP_NUM_THREADS'] = '4'
sys.stderr = sys.__stderr__

from PIL import Image
from transparent_background import Remover
import torch

print("Probando modelo comprimido...")
torch.set_num_threads(4)

# Probar con modelo base normal primero
print("Probando modelo base normal...")
remover = Remover(mode='base')
img = Image.open("MODELO.JPG").convert("RGB")
img_small = img.resize((400, 600), Image.LANCZOS)
with torch.no_grad():
    result = remover.process(img_small)
result.save("test_normal.png")
print("Normal: OK")