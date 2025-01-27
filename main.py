import subprocess
import os
import requests

def enviar_csv_al_servidor(filepath):
    if not os.path.exists(filepath):
        print(f"Error: El archivo {filepath} no existe.")
        return

    url = "http://127.0.0.1:5000/subir_csv"
    try:
        with open(filepath, 'rb') as file:
            files = {'file': file}
            response = requests.post(url, files=files)
            if response.status_code == 200:
                print("Archivo enviado con éxito:", response.json())
            else:
                print(f"Error al enviar el archivo: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error al conectarse al servidor: {e}")

def ejecutar_script():
    try:
        if not os.path.exists("tiktok.py"):
            print("Error: El archivo tiktok.py no existe.")
            return

        proceso = subprocess.Popen(
            ["python", "tiktok.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        while True:
            salida = proceso.stdout.readline()
            error = proceso.stderr.readline()

            if salida:
                print(salida.strip())

            if error:
                print(f"Error: {error.strip()}", flush=True)

            if salida == "" and error == "" and proceso.poll() is not None:
                break

        proceso.wait()
        print(f"El script finalizó con código: {proceso.returncode}")

        if proceso.returncode == 0:
            # Ruta del archivo CSV generado
            csv_filepath = "./uploads/comentarios_tiktok.csv"
            enviar_csv_al_servidor(csv_filepath)
        else:
            print("El script terminó con errores.")

    except subprocess.TimeoutExpired:
        proceso.kill()
        print("El script tardó demasiado y fue terminado.")
    except Exception as e:
        print(f"Error al ejecutar el script: {e}")
    finally:
        if proceso.stdout:
            proceso.stdout.close()
        if proceso.stderr:
            proceso.stderr.close()

if __name__ == "__main__":
    ejecutar_script()
