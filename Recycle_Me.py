import numpy as np
import gradio as gr
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing import image


# Modelos
objectTypeModel = keras.models.load_model("modelos/ultimoModeloTipos")
categoryModel = keras.models.load_model("modelos/ultimoModeloCategorias16")

# Creacion de etiquetas para los modelos
objectTypeLabels = ["Alimentos", "Botellas", "Bricks", "Cartón", "Envases", "Latas",
                   "Papel", "Pilas", "Ropa", "Vidrio"]
categoryLabels = ["Amarillo", "Azul", "Gris", "Marrón", "Punto limpio", "Verde"]

# Funcion para convertir una imagen desde su filepath a una matriz
def scan_picture(path_to_picture, picture_size):
    img = tf.io.read_file(path_to_picture)
    img = tf.image.decode_image(img)
    img = tf.image.resize(img, size=picture_size)
    img = img/255.
    return img

# Funcion para que los modelos realicen predicciones del tipo de objeto sobre la imagen dada
def make_prediction_type(model_, path_to_picture):
    picture = scan_picture(path_to_picture, [512, 384])
    return model_.predict(tf.expand_dims(picture, axis=0))


# Funcion para que los modelos realicen predicciones del contenedor al que pertenece sobre la imagen dada
def make_prediction_category(model_, path_to_picture):
    picture = scan_picture(path_to_picture, [224, 224])  # 512,384
    return model_.predict(tf.expand_dims(picture, axis=0)) # AQUI

# nueva funcion para mostrar el texto de informacion del cubo de basura                                         !
def mostrar_texto(results):
    contenedor = max(results,key=results.get)
    
    if contenedor == categoryLabels[0]: # Amarillo
        return "Dentro del contenedor amarillo, debemos depositar: botellas y envases de plástico, envases metálicos y bricks"
    elif contenedor == categoryLabels[1]: # Azul
        return "En el contenedor azul pueden ir envases de alimentación, calzado, productos congelados, papel para envolver, papel de uso diario…"
    elif contenedor == categoryLabels[2]: # Gris
        return "El contenedor gris es para todos aquellos residuos que no se reciclan, pero tampoco pueden usarse para hacer compost. Esta fracción de residuos que no pueden ser reutilizados se depositan en los vertederos o rellenos sanitarios."
    elif contenedor == categoryLabels[3]: # Marron
        return "Lo que debe depositarse en el contenedor marrón es: restos de alimentos como pieles de frutas, espinas de pescado, plantas, cascaras de huevo o posos; o servilletas y papel de cocina usados."
    elif contenedor == categoryLabels[4]: # Punto limpio
        return "Los puntos limpios son esos impresionantes lugares donde podemos encontrar una infinidad de tipos de residuos. Se recogen y almacenan temporalmente de forma separada porque podrían ser grandes o peligrosos si se arrojasen en los contenedores convencionales."
    else: #Verde
        return "En el contenedor verde debemos depositar botellas de vidrio (vino, cava…), frascos de vidrio (como perfumes o colonias) o tarros de alimentos (mermeladas, conservas, etc.)."

    
# Funcion para clasificar el tipo de objeto
def classify_type(img_filepath):
    predictions = make_prediction_type(objectTypeModel, img_filepath)
    results = {objectTypeLabels[i]: float(predictions[0][i]) for i in range (len(objectTypeLabels))}
    return results

# Funcion para clasificar la categoria a la que pertenece
def classify_category(img_filepath):
    predictions = make_prediction_category(categoryModel, img_filepath)
    results = {categoryLabels[i]: float(predictions[0][i]) for i in range (len(categoryLabels))}
    texto = mostrar_texto(results)
    return results, texto 

# funcion clasificar que reune ambas funciones                                                                     !
def classify_general(img_filepath):
    res1 = classify_type(img_filepath)
    res2,res3 = classify_category(img_filepath)
    return res1,res2,res3

# Funcion para limpiar los outputs
def limpiar(placeholder):
    return None, None, None, None

# Funcion que añade una imagen de los ejemplos
def addPhoto(img):
    return img

# Interfaz                                                                            !
with gr.Blocks() as demo:
    gr.Markdown('**¿Qué residuo quieres reciclar?**')
    
    with gr.Row():
        with gr.Column():
            with gr.Row():
                imagen = gr.Image(type='filepath')
            with gr.Row():
                btn1 = gr.Button("Enviar")
                btn2 = gr.Button("Limpiar")
        with gr.Column():
            with gr.Row():
                tipo = gr.Label(num_top_classes = 3)
                categoria = gr.Label(num_top_classes = 3)
            with gr.Row():
                texto = gr.Textbox(label = "Información sobre este contenedor")
    with gr.Row():
        with gr.Column():
            gr.Examples(
            examples = ["img/cola.jpg"],
            inputs = [imagen],
            outputs= [imagen],
            fn = addPhoto,
            cache_examples=True
            )
            
    btn1.click(classify_general, inputs=[imagen], outputs=[tipo, categoria, texto])
    btn2.click(limpiar, inputs=[imagen], outputs=[imagen, tipo, categoria, texto])


demo.launch(share=True, server_name="0.0.0.0", max_threads=100)
