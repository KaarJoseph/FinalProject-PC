from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
from psycopg2 import sql, Error
import os
import csv
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def connect_db():
    try:
        return psycopg2.connect(
            dbname="Final",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
    except Error as e:
        raise RuntimeError(f"Error al conectar a la base de datos: {e}")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/ejecutar_extraccion', methods=['POST'])
def ejecutar_extraccion():
    try:
        proceso = subprocess.Popen(
            ["python", "main.py"],  # Comando para ejecutar el script
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = proceso.communicate()  # Esperar a que termine

        if proceso.returncode != 0:
            raise RuntimeError(f"Error al ejecutar el script: {stderr}")

        return jsonify({"mensaje": "Extracción completada con éxito"}), 200
    except Exception as e:
        return jsonify({"error": f"Error al ejecutar la extracción: {e}"}), 500


@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": str(e)}), 500

@app.route('/subir_csv', methods=['POST'])
def subir_csv():
    if 'file' not in request.files:
        return jsonify({"error": "No se ha enviado ningún archivo"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "El nombre del archivo está vacío"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "Formato de archivo no permitido, solo se permite CSV"}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    conn = connect_db()
    cursor = conn.cursor()
    query = """
    INSERT INTO public."ComentariosTikTok" (comentario, fecha, id)
    VALUES (%s, %s, %s)
    ON CONFLICT (comentario, fecha) DO NOTHING;
    """

    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            expected_headers = {"comentario", "fecha"}
            if not expected_headers.issubset(reader.fieldnames):
                return jsonify({"error": "El archivo CSV no contiene los encabezados correctos"}), 400

            for row in reader:
                cursor.execute(query, (row["comentario"], row["fecha"], "t"))
        conn.commit()
        os.remove(file_path)  # Eliminar archivo después de procesarlo
        return jsonify({"mensaje": f"Archivo {filename} subido y procesado con éxito"}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": f"Error al procesar el archivo CSV: {e}"}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/obtener_comentarios', methods=['GET'])
def obtener_comentarios():
    conn = connect_db()
    cursor = conn.cursor()

    query = 'SELECT * FROM public."ComentariosTikTok";'
    try:
        cursor.execute(query)
        resultados = cursor.fetchall()
        comentarios = [
            {"comentario": fila[0], "fecha": fila[1], "id": fila[2]} for fila in resultados
        ]
        return jsonify(comentarios), 200
    except Error as e:
        return jsonify({"error": f"Error al consultar los comentarios: {e}"}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    app.run(debug=True)
