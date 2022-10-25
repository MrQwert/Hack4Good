# RecycleMe!
## Reto: Reciclado Inteligente

## Descripción

RecycleMe! es una aplicación que utiliza dos modelos de Machine Learning para clasificar objetos mediante aprendizaje por transferencia según su material y su correspondiente lugar de desecho.

- Framework Gradio para implementación web
- Modelo base: ResNet50 (weight = "imagnet")
- AWS como hosting web
- Google Colab para entrenamiento en Cloud
- Python como lenguaje principal


## Índice de ContenidosCancel changes
1. [Run](#Run)
2. [Uso](#Uso)
3. [Proyección a Futuro](#Proyección-a-Futuro)
4. [Video Youtube](#Vídeo-Youtube)
5. [Team](#Team)
6. [Referencias](#Referencias)

## Run
### Ejecutar con Docker
```sh
docker run -p 7860:7860 jorgecbufv/recycleme
```
Una vez esté ejecutándose el contenedor, simplemente acceder a su dirección IP a través de un navegador en el puerto 7860.

### A través del código fuente
```sh
pip install -r requirements.txt && python RecicleMe.py
```

## Uso
Fotografíe un objeto para que la aplicación le diga dónde reciclarlo.

## Proyección a Futuro
### ¿Qué nos plantamos a corto plazo?
Mejorar el modelo: El prototipo actual consta de dos modelos convolucionales independientes que clasifican las imágenes. Esto lo hemos hecho así debido a la falta de tiempo para elaborar un dataset etiquetado que contemple los múltiples tipos de residuos con los que se puede encontrar un ciudadano. Nuestra intención es demostrar que las redes convolucionales a día de hoy son herramientas muy sofisticadas que correctamente entrenadas son capaces de identificar con mayor precisión que un humano medio. 

Recogida de datos: La aplicación actualmente guarda un log de consultas realizadas con la que se puede hacer un seguimiento estadístico de uso. Nuestra intención es mejorar el sistema de recogida de información para medir de forma tangible el impacto que supone el uso de la aplicación.

### ¿Qué nos planteamos a medio plazo?
Integración: Tanto en dispositivos, hogares, cubos de basura como centros de reciclaje. Se podrían crear prototipos electrónicos incorporados a las basuras que permitan identificar productos sin necesidad de un dispositivo móvil. Este diseño estará enfocado para instalarlo en centros comerciales, escuelas, cafeterías, empresas y demás lugares públicos y privados.

Geolocalización: Si la aplicación me indica que mi residuo debe depositarse en un punto limpio o espacio en concreto, ¿dónde se encuentra el más cercano? La aplicación mostrará al ciudadano los puntos de reciclaje más cercanos compatibles con sus residuos.

## Vídeo Youtube
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/yrjNGSxmrwg/0.jpg)](https://www.youtube.com/watch?v=yrjNGSxmrwg)

## Team

- Jorge E. Cujó Blasco
- Carlos LLueca
- Marcos Molina
- Julia Quintano
- Diego Valencia 
- Iñigo Vázquez

## Referencias
 - Documentación de Gradio: https://gradio.app/docs
 - Dataset imagnet : https://www.image-net.org/
 - Documentación TensorFlow - ResNet50: https://www.tensorflow.org/api_docs/python/tf/keras/applications/resnet50/ResNet50
 - Documentación de keras: https://keras.io/api/

## Info

Hemos entrenado dos redes, una identifica el objeto y otra el cubo de deshecho. El motivo para hacerlo así es la facilidad de prototipado rápido y la falta de tiempo para elaborar un dataset para entrenar una red capaz de clasificar todo tipo de residuos. 
