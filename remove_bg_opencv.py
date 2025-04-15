import os
from PIL import Image
from rembg import remove
from rembg.session_factory import new_session
import logging
import cv2
import numpy as np

# Configuration du journal de logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

# Chemins des répertoires
INPUT_FILE = r'C:\\Users\\...\\unnamed.jpg'
OUTPUT_DIR = r'C:\\Users\\...\\results'
MODEL_PATH = r'C:\\Users\\...\\u2net.onnx'

os.makedirs(OUTPUT_DIR, exist_ok=True)

def cropImage(output_dir):
    """
    Traite le découpage de l'image avec un fond supprimé.
    Objectif : Découper l'image autour du visage détecté avec une marge.
    """
    for filename in os.listdir(output_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            file_path = os.path.join(output_dir, filename)
            try:
                logging.info(f"Découpage de l'image : {filename}")
                image = cv2.imread(file_path)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
                faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

                if len(faces) == 0:
                    logging.warning(f"Aucun visage détecté dans l'image : {filename}")
                    continue

                x, y, w, h = faces[0]

                margin_width = 100
                margin_height = 250 
                x1 = max(0, x - margin_width)
                y1 = max(0, y - margin_height)
                x2 = min(image.shape[1], x + w + margin_width)
                y2 = min(image.shape[0], y + h + margin_height)

                cropped_image = image[y1:y2, x1:x2]

                cv2.imwrite(file_path, cropped_image)
                logging.info(f"Découpage terminé pour : {filename}")
            except Exception as e:
                logging.error(f"Erreur lors du découpage de {filename}: {e}")

def process_image(input_file, output_dir, session):
    """
    Traite une seule image pour supprimer l'arrière-plan
    et enregistre le résultat dans le répertoire de sortie.
    """
    if input_file.lower().endswith(('.png', '.jpg', '.jpeg')):
        filename = os.path.basename(input_file)
        output_path = os.path.join(output_dir, f'result_{filename}')
        
        try:
            logging.info(f"Traitement de l'image : {filename}")
            image = Image.open(input_file)
            result = remove(image, session=session)
            if result.mode == 'RGBA':
                result = result.convert('RGB')
            result.save(output_path)
            logging.info(f"Traitement terminé pour : {filename}")
        except Exception as e:
            logging.error(f"Erreur lors du traitement de {filename}: {e}")

def main():
    """
    Point d'entrée principal du script.
    """
    try:
        logging.info("Initialisation de la session avec le modèle U2Net.")
        session = new_session(model_name="u2net", model_path=MODEL_PATH)
        logging.info("Session initialisée avec succès.")
        
        logging.info("Début du traitement de l'image.")
        process_image(INPUT_FILE, OUTPUT_DIR, session)
        
        logging.info("Début du découpage des images.")
        cropImage(OUTPUT_DIR)
    except FileNotFoundError as fnf_error:
        logging.error(f"Fichier ou répertoire introuvable : {fnf_error}")
    except Exception as e:
        logging.error(f"Une erreur inattendue est survenue : {e}")


if __name__ == "__main__":

    main()