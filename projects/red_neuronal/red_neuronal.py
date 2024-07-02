# -*- coding: utf-8 -*-
"""red_neuronal.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QrewBDMeoNoA9jqRyepkEHs9lv10VGMH

Imnportar las librerías necesarias para el ejercicio
"""

import tensorflow as tf
import numpy as np

"""Declaramos unos cuantos datos aleatorios para entrenar el modelo"""

celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

"""En la parte comentada se hace una red neuronal con solamente una neurona y una conexión (peor predicción), en la otra parte se declara una red neuronal con 2 capas de 3 neuronas y una salida"""

# capa = tf.keras.layers.Dense(units=1, input_shape=[1])
# modelo = tf.keras.Sequential([capa])

oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
oculta2 = tf.keras.layers.Dense(units=3)
salida = tf.keras.layers.Dense(units=1)
modelo = tf.keras.Sequential([oculta1, oculta2, salida])

"""Se compila el modelo y se le especifica el optimizador Adam con una tasa de aprendizaje de 0.1 (Cuanto mayor este valor la red va a ser más "brusca" y cuanto menor va a ser mas fina)"""

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

"""Se entrena el modelo con 1000 vueltas y se declara verbose a False para que no haya salidas por consola"""

print("Comenzando entrenamiento del modelo...")
historial = modelo.fit(celsius, fahrenheit, epochs=1000, verbose=False)
print("Modelo entrenado")

"""Gracias a matplotlib podemos ver el número de vueltas (# Epoca) y la magnitud de perdida, vemos que deja de aprender casi a las 100 vueltas, con una sola neurona dejaba de aprender por el 500"""

import matplotlib.pyplot as plt
plt.xlabel("# Epoca")
plt.ylabel("Magnitud de perdida")
plt.plot(historial.history["loss"])

"""Imprimimos el valor, en este caso el valor correcto debería de ser 212, pero como los datos de entrenamiento son escasos se queda muy cerca"""

print("Hagamos una prediccion!")
resultado = modelo.predict([100])
print("El resultado es " + str(resultado) + " fahrenheit")

"""Por último podemos ver el peso (conexion entre neuronas) y el sesgo (valor de salida) de cada una de las neuronas, como vemos no tiene mucho sentido pero es el camino más optmizado que ha encontrado la red para llegar a este resultado"""

print("Variables internas del modelo")
# print(capa.get_weights())

print(oculta1.get_weights())
print(oculta2.get_weights())
print(salida.get_weights())