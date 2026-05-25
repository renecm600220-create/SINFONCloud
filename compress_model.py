import sys
import os
sys.stderr = open(os.devnull, 'w')
os.environ['NO_COLOR'] = '1'

sys.stderr = sys.__stderr__

print("Cargando modelo...")
import onnx
from onnxruntime.quantization import quantize_dynamic, QuantType

input_path = r"C:\Users\Rene\u2net.onnx"
output_path = r"C:\Users\Rene\u2net_quant.onnx"

print(f"Input: {os.path.getsize(input_path) / 1024 / 1024:.1f} MB")
print("Comprimiendo (quantizando)...")

quantize_dynamic(
    model_input=input_path,
    model_output=output_path,
    weight_type=QuantType.QUInt8
)

size_mb = os.path.getsize(output_path) / 1024 / 1024
print(f"Output: {size_mb:.1f} MB")
print("DONE")