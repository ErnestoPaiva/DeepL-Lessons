# -*- coding: utf-8 -*-
"""1 Curso ML - Primera Red.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Li9php2lLncfyr3zcWNWuTYUcSg80x0T

#Importaciones

Comencemos con nuestras importaciones. Aquí estamos importando TensorFlow y lo llamamos tf para facilitar su uso.

Luego importamos una biblioteca llamada numpy, que nos ayuda a representar nuestros datos de manera fácil y rápida.

El framework para definir una red neuronal como un conjunto de capas secuenciales se llama keras, por lo que también lo importamos.
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.activations import sigmoid

"""#Proporcionar los datos

A continuación, incluiremos algunos datos. En este caso, estamos tomando 6 xs y 6 ys. Puede ver que la relación entre estos es que y = 2x-1, entonces donde x = -1, y = -3 etc.

Una biblioteca de Python llamada 'Numpy' proporciona muchas estructuras de datos de tipo matriz. Declaramos que queremos usarlos especificando los valores como np.array []
"""

x = np.array([-1.0,  0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
y = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

plt.scatter(x,y)
plt.ylabel('y')
plt.xlabel('x')
plt.grid()

"""#Definir y compilar la red neuronal
A continuación, crearemos la red neuronal más simple posible. Tiene 1 capa, y esa capa tiene 1 neurona, y la forma de entrada es solo 1 valor.
"""

model = tf.keras.Sequential([
                             tf.keras.layers.Dense(units=1, input_shape=[1])
                             ])

from tensorflow.keras.layers import Dense
from tensorflow.keras import Sequential

model = Sequential([Dense(units=1, input_shape=[1])])

model = tf.keras.Sequential()

model.add( Dense(1, input_shape=(1,)) )

"""Ahora compilamos nuestra red neuronal. Cuando lo hacemos, tenemos que especificar 2 funciones, una pérdida y un optimizador.

Si ha visto muchas matemáticas para el aprendizaje automático, aquí es donde se usa generalmente, pero en este caso está muy bien encapsulado en funciones para usted. Pero qué pasa aquí, expliquemos ...

Sabemos que en nuestra función, la relación entre los números es y = 2x-1.

Cuando la computadora está tratando de 'aprender' eso, hace una suposición ... tal vez y = 10x + 10. La función LOSS mide las respuestas adivinadas contra las respuestas correctas conocidas y mide qué tan bien o qué tan mal lo hizo.

Luego usa la función OPTIMIZER para hacer otra conjetura. Según cómo fue la función de pérdida, intentará minimizar la pérdida. En ese punto, tal vez se le ocurra algo como y = 5x + 5, que, aunque sigue siendo bastante malo, está más cerca del resultado correcto (es decir, la pérdida es menor)

Repetirá esto para el número de EPOCHS que verá en breve. Pero primero, así es como le decimos que use 'ERROR AL CUADRADO MEDIO' para la pérdida y 'DESCENSO DE GRADIENTE ESTOCÁSTICO' para el optimizador. 

Con el tiempo, aprenderá las diferentes y apropiadas funciones de optimización y pérdida para diferentes escenarios.
"""

model.compile(optimizer='sgd', loss='mean_squared_error')

"""#Entrenamiento de la red neuronal
El proceso de entrenamiento de la red neuronal, donde "aprende" la relación entre las X y las Y, está en model.fit. Aquí es donde pasará por el bucle del que hablamos anteriormente, haciendo una suposición, midiendo qué tan bueno o malo es (también conocido como la pérdida), usando el optimizador para hacer otra suposición, etc. Lo hará por la cantidad de épocas que usted especifica. Cuando ejecute este código, verá la pérdida en el lado derecho.
"""

model.fit(x, y, epochs=500)

"""Ahora tienemos un modelo que ha sido entrenado para aprender la relación entre X e Y. Puedemos usar el método model.predict para que averigüe la Y para una X. Entonces, por ejemplo, si X = 10 , ¿cuál crees que será Y? Adivine antes de ejecutar este código:"""

x_prueba = np.array([10.0])
print(x_prueba)

y_pred = model.predict(x_prueba)
print(y_pred)

"""Predecir para X = -2, 0, 2 , 4, 8"""

x_prueba = np.array([-2, 0, 2 , 4, 8], dtype=float)
print(x_prueba)

y_pred = model.predict(x_prueba)
print(y_pred)

plt.scatter(x,y)
plt.plot(x_prueba, y_pred)
plt.xlabel('Data input')
plt.ylabel('Predicción')
plt.grid()

"""#Caso no lineal"""

x = np.array([-3,  -2, -1, 0, 1, 2, 3], dtype=float)
y = np.array([0.1,0.2,0.5, 1,0.5,0.2,0.1], dtype=float)

plt.scatter(x,y)
plt.ylabel('y')
plt.xlabel('x')
plt.grid()

model = Sequential([Dense(units=2, activation=sigmoid, input_shape=[1]),
                    Dense(units=2, activation=sigmoid),
                    Dense(units=1) ])
model.summary()

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.1), loss=tf.keras.losses.MeanSquaredError())

model.fit(x, y, epochs=500)

x_prueba = np.array([-3,  -2, -1, 0, 1, 2, 3], dtype=float)
print(x_prueba)

y_pred = model.predict(x_prueba)
y_pred

plt.scatter(x,y)
plt.plot(x_prueba, y_pred)
plt.xlabel('Data input')
plt.ylabel('Predicción')
plt.grid()





