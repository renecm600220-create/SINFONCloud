import gradio as gr
from transparent_background import Remover
from PIL import Image
import numpy as np

print("Cargando InSPyReNet...")
remover = Remover(mode='base')
print("Listo")

def remove_bg(image):
    if image is None:
        return None
    img = Image.fromarray(image).convert("RGB")
    out = remover.process(img, type='rgba')
    return out

with gr.Blocks(title="SINFON Cloud") as demo:
    gr.Markdown("# SINFON CLOUD\n### Recorte de fotos con IA - Mismo motor que PC")
    with gr.Row():
        inp = gr.Image(type="numpy", label="Foto")
        out = gr.Image(type="pil", image_mode="RGBA", label="Sin fondo")
    inp.change(fn=remove_bg, inputs=inp, outputs=out)

demo.launch()