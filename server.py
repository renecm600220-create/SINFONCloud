import sys
import os
os.environ['NO_COLOR'] = '1'
os.environ['OMP_NUM_THREADS'] = '2'

import io
import torch
from flask import Flask, request, send_file, send_from_directory
from flask_cors import CORS
from PIL import Image

app = Flask(__name__, static_folder='static')
CORS(app)

remover = None

def load_model():
    global remover
    if remover is None:
        from transparent_background import Remover
        remover = Remover(mode='base')
        torch.set_num_threads(2)
    return remover

@app.route('/')
def index():
    return send_from_directory('static', 'mobile.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.route('/health')
def health():
    return 'OK'

@app.route('/remove', methods=['POST'])
def remove_bg():
    try:
        data = request.get_data()
        img = Image.open(io.BytesIO(data)).convert('RGB')
        w, h = img.size
        print(f'Procesando {w}x{h}')
        model = load_model()
        with torch.no_grad():
            result = model.process(img)
        buf = io.BytesIO()
        result.save(buf, format='PNG')
        buf.seek(0)
        return send_file(buf, mimetype='image/png')
    except Exception as e:
        print(f'Error: {e}')
        return str(e), 500

if __name__ == '__main__':
    load_model()
    port = int(os.environ.get('PORT', 8082))
    app.run(host='0.0.0.0', port=port)