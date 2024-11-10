from flask import request, jsonify
from services.pdf_processor import procesar_pdf_bytes
import uuid
import os

def init_routes(app):
    @app.route('/procesar_pdf', methods=['POST'])
    def procesar_pdf():
        if 'file' not in request.files:
            return jsonify({'error': 'PDF file not found'}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'Empty file name'}), 400
        if file:
            pdf_bytes = file.read()

            pares_paginas = procesar_pdf_bytes(pdf_bytes)

            token_file_name = f'{uuid.uuid4()}.txt'
            token_file_path = os.path.join(app.config['TOKEN_FOLDER'], token_file_name)

            with open(token_file_path, 'w', encoding='utf-8') as f:
                for i, (texto_pag_1, texto_pag_2) in enumerate(pares_paginas):
                    f.write(f"Pair {i + 1}:\n")
                    f.write(f"Page 1:\n{texto_pag_1}\n")
                    f.write(f"--- End of Page 1 ---\n")
                    f.write(f"Page 2:\n{texto_pag_2}\n")
                    f.write(f"--- End of Page 2 ---\n")
                    f.write("\n--- End of Pair ---\n\n")

            return jsonify({'message': 'PDF processed and saved to text file'}), 200
