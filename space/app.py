import gradio as gr
from transparent_background import Remover
from PIL import Image
import io

print("Cargando modelo InSPyReNet...")
remover = Remover(mode='base')
print("Modelo listo")

def remove_bg(image):
    img = Image.fromarray(image).convert("RGB")
    out = remover.process(img, type="rgba")
    return out

demo = gr.Interface(
    fn=remove_bg,
    inputs=gr.Image(type="numpy"),
    outputs=gr.Image(type="pil"),
    title="SINFON Cloud",
    description="Recorte de fotos con IA"
)

demo.launch()