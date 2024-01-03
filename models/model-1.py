import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# preparamos los datos
celsius = np.array([-40, 10, 0, 8, 15, 22, 38, 50, 35], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100, 122, 95], dtype=float)

# ponemos las capas (capas densas)
capaEntrada = tf.keras.layers.Dense(units=3, input_shape=[1])
capaOculta = tf.keras.layers.Dense(units=3)
capaSalida = tf.keras.layers.Dense(units=1)

# modelo (tipo secuencial)
modelo = tf.keras.Sequential([capaEntrada, capaOculta, capaSalida])

# optimizamos (minimamente para asegurar aprendizaje)
modelo.compile(optimizer=tf.keras.optimizers.Adam(0.1), loss="mean_squared_error")

# entrenamos el modelo! :)
print("Entrenando...")
historial = modelo.fit(celsius, fahrenheit, epochs=1000, verbose=False)
print("Entrenamiento completado! :)")

# graficamos los resultados para medir aprendizaje
plt.xlabel("Numero de epoca")
plt.ylabel("Magnitud de perdida")
plt.plot(historial.history["loss"])

# Al final, el aprendizaje optimo se logra cuando la perdida es minima
# antes de las 50 epocas. De no ocurrir esto, el modelo no aprende
# adecuadamente y es necesario inspeccionarlo.

# Veamos si el modelo ha aprendido bien...
# debe decir que 37 grados celsius son 96 fahrenheit...

print("Vamos a revisar!")
grados = 37.0
resultado = modelo.predict([grados])
print("Si en celsius estamos a", str(grados) + "°...")
print("... en Fahrenheit estaremos a", str(resultado) + "°, o no?")
