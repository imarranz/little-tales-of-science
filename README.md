
# 🌟 Little Tales of Science (Pequeñas Historias de la Ciencia) 🌟

## 📚 Descripción del Proyecto

Bienvenidos a **Little Tales of Science** (Pequeñas Historias de la Ciencia), un proyecto que combina la magia de la **Inteligencia Artificial Generativa** y el poder de **Python** para crear mini cómics dedicados a la divulgación científica. Aquí exploramos historias y figuras clave de la ciencia, como Alan Turing, Ronald Fisher, Florence Nightingale y muchos otros, utilizando un formato visualmente atractivo: el **cómic**.

### 🤖 Uso de la Inteligencia Artificial

Cada viñeta es generada a través de un modelo de **IA generativa**, lo que permite crear ilustraciones basadas en descripciones detalladas de personajes y escenarios históricos. Gracias a esto, podemos representar a personajes de manera coherente en un estilo **semirealista** con una paleta de colores en tonos tierra y ocres, dándole un aire clásico y científico a las imágenes.

### 🐍 Automatización con Python

Después de generar las imágenes con IA, utilizo **Python** para automatizar el proceso de creación del cómic. He desarrollado un script que toma las imágenes y los textos de configuración (`config.yaml`) y monta automáticamente el cómic, además de generar un archivo **PDF** con el cómic completo o crear una única imagen con todas las viñetas del cómic.

### ✍️ Tipo de Letra Usada

El tipo de letra que uso en los cómics es **[Luckiest Guy](https://fonts.google.com/specimen/Luckiest+Guy)**, una fuente que añade un toque amigable e informal a las historias.

## 🔧 Estructura del Repositorio

Este repositorio tiene una estructura clara y organizada para facilitar la creación de cómics científicos:

- **`comicgen.py`**: El script principal de Python que automatiza el montaje de las viñetas y la generación del PDF.
- **`README.md`**: Este archivo de documentación.
- **`LuckiestGuy-Regular.ttf`**: Contiene el tipo de letra **Luckiest Guy** utilizado en los cómics.
- **Estructura de cada carpeta de historia o personaje:**
  - **`config.yaml`**: El archivo de configuración que contiene la descripción de las viñetas y los textos que aparecen en el cómic.
  - **`/images`**: Carpeta que almacena las imágenes generadas por la IA para el cómic.

Estructura general del repositorio:

```
📦 little-tales-of-science
 ┣ 📜 comicgen.py
 ┣ 📜 README.md
 ┣ 📜 LuckiestGuy-Regular.ttf
 ┣ 📂 Ada Lovelace
 ┃ ┣ 📜 config.yaml
 ┃ ┗ 📂 images
 ┃   ┣ 📜 Ada_Lovelace_01.webp
 ┃   ┣ 📜 Ada_Lovelace_02.webp
 ┃   ┣ 📜 ...
 ┣ 📂 Alan Turing
 ┃ ┣ 📜 config.yaml
 ┃ ┗ 📂 images
 ┃   ┣ 📜 Alan_Turing_01.webp
 ┃   ┣ 📜 Alan_Turing_02.webp
 ┃   ┣ 📜 ...
 ┣ 📂 Florence Nightingale
 ┃ ┣ 📜 config.yaml
 ┃ ┗ 📂 images
 ┃   ┣ 📜 Florence_Nightingale_01.webp
 ┃   ┣ 📜 Florence_Nightingale_02.webp
 ┃   ┣ 📜 ...
```

## 🎯 Mi Interés por la Divulgación Científica

El propósito de **Little Tales of Science** es acercar la ciencia a todo tipo de público, sobre todo a niños, a través de una narración visual. Mi interés por la **Divulgación Científica** me llevó a crear este proyecto, con la intención de hacer accesibles conceptos, curiosidades o hechos históricos científicos a través de historias cortas y entretenidas y visualmente atractivas.

Espero que este proyecto despierte la curiosidad y el interés en las matemáticas, la estadística, y la historia de la ciencia, mostrando cómo personajes históricos han contribuido al desarrollo del conocimiento.

## 🚀 Cómo Usar Este Repositorio

### Generar las Viñetas

Las viñetas se generan utilizando IA que se basa en descripciones detalladas y prompts permanentes, los cuales definen el aspecto visual, estilo artístico y contexto histórico de cada personaje o escena. Estos prompts contienen información sobre la vestimenta, expresiones faciales, escenarios y otros elementos relevantes, asegurando la coherencia visual a lo largo de toda la historia. Gracias a estos detalles, la IA puede crear ilustraciones precisas y consistentes, logrando un estilo semirrealista que se adapta a la narrativa y el periodo histórico representado.

### Ejecutar el Script

He desarrollado el script de Python (`comicgen.py`). Puedes usarlo para organizar las imágenes y los textos en el formato de cómic.

```bash
$ python comicgen.py --personaje "Alan Turing"
```

### Generar el PDF

El script también genera automáticamente un archivo PDF con el cómic completo.

---

# 🌟 Project: Little Tales of Science 🌟

## 📚 Project Description

Welcome to **Little Tales of Science**, a project that combines the magic of **generative AI** and the power of **Python** to create mini-comics dedicated to science communication. Here, we explore stories and key figures from science, such as Alan Turing, Ronald Fisher, Florence Nightingale, and many others, using a visually engaging comic format.

### 🤖 Use of Artificial Intelligence

Each comic strip is generated through a **generative AI** model, which allows us to create illustrations based on detailed descriptions of characters and historical settings. This ensures that the characters are consistently depicted in a **semi-realistic** style with an earthy, ochre-toned color palette, giving the images a classic and scientific feel.

### 🐍 Automation with Python

Once the images are generated using AI, I use **Python** to automate the comic creation process. The script takes the images and text from the configuration files and automatically assembles the comic, also generating a **PDF** file with the complete comic.

### ✍️ Font Used

The font used in the comics is **[Luckiest Guy](https://fonts.google.com/specimen/Luckiest+Guy)**, adding a friendly touch to the stories we tell.

## 🔧 Repository Structure

This repository has a clear and organized structure to facilitate the creation of science comics:

- **`comicgen.py`**: The main Python script that automates the assembly of the comic strips and the generation of the PDF.
- **`README.md`**: This documentation file.
- **`/font`**: Contains the **Luckiest Guy** font used in the comics.
- **Structure of each story or character folder:**
  - **`config.yaml`**: The configuration file that contains the descriptions of the comic strips and the text that appears in the comic.
  - **`/images`**: Folder that stores the AI-generated images for the comic.

Repository structure:

```
📦 little-tales-of-science
 ┣ 📜 comicgen.py
 ┣ 📜 README.md
 ┣ 📜 LuckiestGuy-Regular.ttf
 ┣ 📂 Ada Lovelace
 ┃ ┣ 📜 config.yaml
 ┃ ┗ 📂 images
 ┃   ┣ 📜 Ada_Lovelace_01.webp
 ┃   ┣ 📜 Ada_Lovelace_02.webp
 ┃   ┣ 📜 ...
 ┣ 📂 Alan Turing
 ┃ ┣ 📜 config.yaml
 ┃ ┗ 📂 images
 ┃   ┣ 📜 Alan_Turing_01.webp
 ┃   ┣ 📜 Alan_Turing_02.webp
 ┃   ┣ 📜 ...
 ┣ 📂 Florence Nightingale
 ┃ ┣ 📜 config.yaml
 ┃ ┗ 📂 images
 ┃   ┣ 📜 Florence_Nightingale_01.webp
 ┃   ┣ 📜 Florence_Nightingale_02.webp
 ┃   ┣ 📜 ...
```

## 🎯 My Interest in Science Communication

The purpose of **Little Tales of Science** is to bring science closer to all types of audiences through visual storytelling. My passion for **Science Communication** led me to create this project, with the intention of making complex scientific concepts more accessible through entertaining and visually appealing stories.

I hope this project sparks curiosity and interest in mathematics, statistics, and the history of science by showing how historical figures have contributed to the advancement of knowledge.

## 🚀 How to Use This Repository

### Generate the Comic Strips

The illustrations are generated using AI based on detailed descriptions and persistent prompts, which define the visual appearance, artistic style, and historical context of each character or scene. These prompts contain information about clothing, facial expressions, settings, and other relevant elements, ensuring visual consistency throughout the story. Thanks to these details, the AI can create accurate and cohesive illustrations, achieving a semi-realistic style that fits the narrative and the historical period represented.

### Run the Script

Use the Python script (`comicgen.py`) to organize the images and texts into the comic format.

```bash
$ python comicgen.py --personaje "Alan Turing"
```

### Generate the PDF

The script also automatically generates a PDF file with the complete comic.

