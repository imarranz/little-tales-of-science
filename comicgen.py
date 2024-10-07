 
import sys

from PIL import Image, ImageDraw, ImageFont
from PyPDF2 import PdfReader, PdfWriter
from fpdf import FPDF
import os

import yaml

# sys.argv es una lista que contiene los argumentos de línea de comando.
# El primer elemento (índice 0) es el nombre del archivo script.
# Los argumentos adicionales siguen desde el índice 1 en adelante.

if len(sys.argv) > 2:
    if sys.argv[1] == '--personaje':
        personaje = sys.argv[2]
        print(f"¡Has seleccionado el personaje de {personaje} para generar un cómic!")
    else:
        print("Uso incorrecto. Prueba: $python comicgen.py --personaje [personaje]")
        sys.exit(1)
else:
    print("Se esperaba un argumento para el personaje.")
    sys.exit(1)


# Cargar la configuración desde el fichero YAML
with open(f'./{personaje}/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

box_color = tuple(config['BOXCOLOR'])
border_color = tuple(config['BORDERCOLOR'])
n_images = config['NIMAGES']
image_paths = config['IMAGES']
spanish_texts = config['TEXTS']['SPANISH']
english_texts = config['TEXTS']['ENGLISH']


def insert_newlines(text, interval):
    words = text.split()
    current_length = 0
    result = []

    for word in words:
        if current_length + len(word) + 1 > interval:  # +1 para el espacio
            result.append('\n' + word)
            current_length = len(word)
        else:
            if result:
                result.append(' ' + word)
            else:
                result.append(word)
            current_length += len(word) + 1  # +1 para el espacio

    return ''.join(result)

# Función para dibujar un rectángulo redondeado
def draw_rounded_rectangle(draw, position, width, height, radius, fill):

    """Dibuja un rectángulo redondeado."""
    upper_left_point = (position[0], position[1])
    bottom_right_point = (position[0] + width, position[1] + height)

    draw.rectangle([upper_left_point, bottom_right_point], fill = fill)

def combine_images_with_text(images, rows, cols, image_size, title_text, font_path, font_size):

    # Calcular el alto adicional para el texto
    text_height = 150  # Ajusta según sea necesario

    # Tamaño de la imagen total (ancho, alto)
    dst = Image.new('RGB', (cols * image_size[0], rows * image_size[1] + text_height), tuple(config['BORDERCOLOR']))

    # Preparar el dibujo de texto
    draw = ImageDraw.Draw(dst)
    font = ImageFont.truetype(font_path, font_size)

    # Calcular el tamaño del texto usando textbbox
    text_bbox = draw.textbbox((0, 0), title_text, font = font)
    text_width = text_bbox[2] - text_bbox[0]  # Anchura del texto

    # Posición del texto (centrado en la parte superior)
    text_x = 150 #(dst.width - text_width) // 2
    text_y = (text_height - font_size) // 2
    # Dibujar el texto
    draw.text((text_x, text_y), title_text, fill = "white", font=font)

    for i, img_path in enumerate(images):
        # Cargar imagen
        img = Image.open(img_path)
        # Asegurar que la imagen tenga el tamaño adecuado
        img = img.resize(image_size)
        # Calcular la posición de inserción
        x = (i % cols) * image_size[0]
        y = (i // cols) * image_size[1] + text_height  # Ajustar para el texto
        # Pegar la imagen en la posición calculada
        dst.paste(img, (x, y))

    return dst


def combine_images(images, rows, cols, image_size):
    # Tamaño de la imagen total (ancho, alto)
    dst = Image.new('RGB', (cols * image_size[0], rows * image_size[1]))

    for i, img_path in enumerate(images):
        # Cargar imagen
        img = Image.open(img_path)
        # Asegurar que la imagen tenga el tamaño adecuado
        img = img.resize(image_size)
        # Calcular la posición de inserción
        x = (i % cols) * image_size[0]
        y = (i // cols) * image_size[1]
        # Pegar la imagen en la posición calculada
        dst.paste(img, (x, y))

    return dst

def add_custom_border_with_text(image, border_size, border_bottom_size, border_color, text, font_path, font_size):
    """Agrega un borde con un color especificado a una imagen, con un borde inferior personalizado y añade texto en el borde inferior."""

    width, height = image.size

    new_width = width + 2 * border_size
    new_height = height + 2 * border_size + border_bottom_size  # Añade espacio extra para el borde inferior

    # Crear una nueva imagen con el color de fondo y las dimensiones adecuadas
    new_img = Image.new('RGB', (new_width, new_height), border_color)

    # Pegar la imagen original en el centro de la nueva imagen
    new_img.paste(image, (border_size, border_size))

    # Preparar para dibujar en la imagen
    draw = ImageDraw.Draw(new_img)

    # Cargar la fuente
    font = ImageFont.truetype(font_path, font_size)

    # Calcular la posición del texto (abajo a la derecha, encima del borde inferior)

    # Calcular el tamaño del texto usando textbbox
    text_bbox = draw.textbbox((0, 0), text, font = font)
    text_width = text_bbox[2] - text_bbox[0]  # Anchura del texto
    text_height = text_bbox[3] - text_bbox[1]  # Altura del texto

    text_position = (new_width - text_width - 50, height + (border_bottom_size / 2) + (text_height / 2) + 5)

    # Dibujar el texto
    draw.text(text_position, text, font = font, fill = "white")

    return new_img


# Función para añadir texto con caja redondeada
def add_text_with_rounded_box(image_path, text, box_color, language = 'spanish', title = False):
    # Cargar la imagen
    image = Image.open(f"./{personaje}/images/{image_path}")

    width, height = image.size

    # Especificar parámetros
    border_size = 30
    border_bottom_size = 40
    border_color = tuple(config['BORDERCOLOR'])
    text_signature = "@imarranz/little-tales-of-science"
    font_path = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'  # Asegúrate de usar el path correcto a la fuente que desees
    font_size = 36

    # Aplicar la función modificada
    image = add_custom_border_with_text(image = image,
                                        border_size = border_size,
                                        border_bottom_size = border_bottom_size,
                                        border_color = border_color,
                                        text = text_signature,
                                        font_path = font_path,
                                        font_size = font_size)

    draw = ImageDraw.Draw(image)

    # Si title=True, añadir un título en la parte superior de la imagen
    if title:
        title_text = insert_newlines(config['METADATA'][language.upper()]['Title'], 20)  # Obtener el título desde el YAML
        title_font = ImageFont.truetype("LuckiestGuy-Regular.ttf", 75)  # Tamaño de la fuente para el título

        # Calcular posición del título (centrado en la parte superior)
        title_bbox = draw.textbbox((0, 0), title_text, font = title_font)
        title_x = 50 # (width - (title_bbox[2] - title_bbox[0])) // 2
        title_y = 50 # Ajusta según el espacio superior

        # Dibujar el borde negro del texto (desplazado ligeramente en 8 direcciones)
        outline_range = 4  # Ajuste para el grosor del borde
        for offset_x in range(-outline_range, outline_range + 1):
            for offset_y in range(-outline_range, outline_range + 1):
                if offset_x != 0 or offset_y != 0:  # Para evitar sobrescribir el centro con negro
                    draw.text((title_x + offset_x, title_y + offset_y), title_text, font = title_font, fill = "black")

        # Dibujar el texto en blanco encima del borde
        draw.text((title_x, title_y), title_text, font = title_font, fill = "white")

    # Definir la fuente
    # font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
    font = ImageFont.truetype("LuckiestGuy-Regular.ttf", 48)

    # Procesar el texto y agregar la caja redondeada
    text = insert_newlines(text, 35)

    # Calcular el tamaño del texto usando textbbox
    text_bbox = draw.textbbox((0, 0), text, font = font)
    text_width = text_bbox[2] - text_bbox[0]  # Anchura del texto
    text_height = text_bbox[3] - text_bbox[1]  # Altura del texto

    # Definir la altura y anchura total del rectángulo con márgenes
    margin = 12
    rectangle_width = text_width + 2 * margin
    rectangle_height = text_height + 2 * margin

    # Posición inicial del rectángulo
    rectangle_x = 55
    rectangle_y = width - 25 - text_height

    # Dibujar rectángulo redondeado
    draw_rounded_rectangle(draw, (rectangle_x, rectangle_y), rectangle_width, rectangle_height, radius = 10, fill = box_color)

    # Posiciones del texto centrado dentro del rectángulo
    text_x = rectangle_x + margin
    text_y = rectangle_y + margin

    # Dibujar texto centrado
    draw.text((text_x, text_y), text, font = font, fill = (0, 0, 0))

    # Guardar la imagen
    image.save(f"./{personaje}/images/Annotated_{language}_{image_path}")


def create_pdf_from_images(image_paths, output_pdf_path, language = 'spanish'):

    # Asegurarse de que las imágenes estén en modo RGB
    images = [Image.open(f"./{personaje}/images/Annotated_{language}_{img_path}").convert("RGB") for img_path in image_paths]

    # La primera imagen será la primera página del PDF, el resto se añadirán después
    first_image = images[0]

    # Guardar el PDF temporal sin metadatos
    temp_pdf_path = output_pdf_path + "_temp.pdf"

    first_image.save(temp_pdf_path,
                     save_all = True,
                     append_images = images[1:],
                     resolution = 100.0,
                     quality = 100)

    # Leer el PDF temporal
    reader = PdfReader(temp_pdf_path)
    writer = PdfWriter()

    # Copiar todas las páginas al nuevo PDF
    for page in reader.pages:
        writer.add_page(page)

    # Metadatos a añadir
    if language == 'spanish':

        metadata = {
            '/Author': config['METADATA']['SPANISH']['Author'],
            '/Title': config['METADATA']['SPANISH']['Title'],
            '/Subject': config['METADATA']['SPANISH']['Subject'],
            '/Keywords': config['METADATA']['SPANISH']['Keywords'],
            '/Creator': config['METADATA']['SPANISH']['Author']
        }
    if language == 'english':

        metadata = {
            '/Author': config['METADATA']['ENGLISH']['Author'],
            '/Title': config['METADATA']['ENGLISH']['Title'],
            '/Subject': config['METADATA']['ENGLISH']['Subject'],
            '/Keywords': config['METADATA']['ENGLISH']['Keywords'],
            '/Creator': config['METADATA']['SPANISH']['Author']
        }

    # Añadir metadatos al PDF
    writer.add_metadata(metadata)

    # Guardar el PDF final con metadatos
    with open(output_pdf_path, "wb") as f:
        writer.write(f)

    # Eliminar el PDF temporal
    os.remove(temp_pdf_path)

def clean_project():
    """
    Elimina todos los archivos en el directorio especificado que comiencen con 'Annotated'.
    Dejamos el directorio limpio con los ficheros originales
    """

    # Listar todos los archivos en el directorio

    for filename in os.listdir(f'./{personaje}/images/'):
        # Comprobar si el nombre del archivo comienza con 'Annotated'
        if filename.startswith("Annotated"):
            # Construir la ruta completa del archivo
            file_path = os.path.join(f'./{personaje}/images/', filename)
            # Eliminar el archivo
            os.remove(file_path)
            # print(f"Archivo eliminado: {file_path}")


def create_stories(output_pdf_path, endswith = 'spanish'):
    # Directorio raíz con las carpetas que contienen las imágenes
    root_dir = './'  # Cambia esta ruta a la que corresponda

    # Inicializa el objeto PDF
    pdf = None

    # Recorre todas las subcarpetas en el directorio raíz
    for folder in os.listdir(root_dir):
        folder_path = os.path.join(root_dir, folder)

        # Verifica que sea una carpeta
        if os.path.isdir(folder_path):
            # Busca la imagen que sigue el patrón 'comic_XXXXXXXXX_{endswith}.jpg'
            for file in os.listdir(folder_path):
                if file.startswith('comic_') and file.endswith(f'_{endswith}.jpg'):
                    image_path = os.path.join(folder_path, file)

                    # Carga la imagen para obtener sus dimensiones
                    image = Image.open(image_path)
                    width, height = image.size

                    # Convertir píxeles a milímetros para el PDF
                    width_mm = width * 0.264583
                    height_mm = height * 0.264583

                    # Si es la primera imagen, inicializa el PDF con esas dimensiones
                    if pdf is None:
                        pdf = FPDF(unit = "mm", format = (width_mm, height_mm))

                    # Añade una nueva página con el tamaño de la imagen
                    pdf.add_page()

                    # Agrega la imagen a la página
                    pdf.image(image_path, 0, 0, width_mm, height_mm)

    # Guarda el PDF con todas las imágenes
    if pdf is not None:
        pdf.output(output_pdf_path)
        print(f"PDF creado con éxito en: {output_pdf_path}")
    else:
        print("No se encontraron imágenes para crear el PDF.")

# Ejemplo de uso de la función
#create_stories('stories_spanish.pdf', endswith = 'spanish')
#create_stories('stories_english.pdf', endswith = 'english')


for i in range(n_images):
    add_text_with_rounded_box(image_paths[i], spanish_texts[i], box_color, language = 'spanish', title = True if i == 0 else False)
    add_text_with_rounded_box(image_paths[i], english_texts[i], box_color, language = 'english', title = True if i == 0 else False)

create_pdf_from_images(image_paths, f"./{personaje}/{config['METADATA']['ENGLISH']['Subject']}.pdf", language = 'english')
create_pdf_from_images(image_paths, f"./{personaje}/{config['METADATA']['SPANISH']['Subject']}.pdf", language = 'spanish')



# Tamaño de cada imagen (ancho, alto)
#image_size = (700, 700)  # Ajusta este tamaño según tus imágenes
## Lista de rutas a las imágenes
#annotated_image_paths = [f"./{personaje}/images/Annotated_spanish_{img_path}" for img_path in image_paths]
## Combina las imágenes
#combined_image = combine_images(annotated_image_paths, 2, 4, image_size)
## Guarda la imagen combinada
#combined_image.save(f'./{personaje}/comic_{personaje}_spanish.jpg')

## Lista de rutas a las imágenes
#annotated_image_paths = [f"./{personaje}/images/Annotated_english_{img_path}" for img_path in image_paths]
## Combina las imágenes
#combined_image = combine_images(annotated_image_paths, 2, 4, image_size)
## Guarda la imagen combinada
#combined_image.save(f'./{personaje}/comic_{personaje}_english.jpg')

# Creamos el cómic combinado las imágenes en una única figura


# Tamaño de cada imagen (ancho, alto)
image_size = (700, 700)  # Ajusta este tamaño según tus imágenes
# Lista de rutas a las imágenes
annotated_image_paths = [f"./{personaje}/images/Annotated_english_{img_path}" for img_path in image_paths]
# Combina las imágenes con texto
combined_image = combine_images_with_text(annotated_image_paths, 2, 4, image_size,
                                          title_text = f"{personaje}  |  {config['METADATA']['ENGLISH']['Title']}",
                                          font_path = "LuckiestGuy-Regular.ttf",
                                          font_size = 56)
# Guarda la imagen combinada
combined_image.save(f'./{personaje}/comic_{personaje}_english.jpg')


# Lista de rutas a las imágenes
annotated_image_paths = [f"./{personaje}/images/Annotated_spanish_{img_path}" for img_path in image_paths]
# Combina las imágenes con texto
combined_image = combine_images_with_text(annotated_image_paths, 2, 4, image_size,
                                          title_text = f"{personaje}  |  {config['METADATA']['SPANISH']['Title']}",
                                          font_path = "LuckiestGuy-Regular.ttf",
                                          font_size = 56)
# Guarda la imagen combinada
combined_image.save(f'./{personaje}/comic_{personaje}_spanish.jpg')

create_stories('stories_spanish.pdf', endswith = 'spanish')
create_stories('stories_english.pdf', endswith = 'english')


clean_project()
