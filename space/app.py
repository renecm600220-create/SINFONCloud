import gradio as gr
from transparent_background import Remover
from PIL import Image
import numpy as np
import tempfile
import os

print("Cargando InSPyReNet...")
remover = Remover(mode='base')
print("Listo")

def remove_bg(image):
    if image is None:
        return None
    img = Image.fromarray(image).convert("RGB")
    out = remover.process(img, type='rgba')
    tmp = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    out.save(tmp.name, "PNG")
    return tmp.name

demo = gr.Interface(
    fn=remove_bg,
    inputs=gr.Image(type="numpy"),
    outputs=gr.Image(type="filepath", label="Sin fondo (PNG)"),
    title="SINFON Cloud",
    description="Selecciona una foto"
)

demo.launch()