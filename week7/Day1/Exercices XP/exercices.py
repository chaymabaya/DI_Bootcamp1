
#Exercise 2 : Building a Simple Perceptron Decision System
W_temp = 0.6
W_rain = 0.4
bias = 2.0
threshold = 20

def predict_weather(temp, rain):
    weighted_sum = (W_temp * temp) + (W_rain * rain) + bias
    if weighted_sum >= threshold:
        descision = 1 
    else:
        descision = 0
    return weighted_sum, descision

sum, decision = predict_weather(25, 5)
print("Somme pondérée =", sum)
print("Décision =", decision, "(Oui sortir)" if decision == 1 else "(Non rester)")

#Exercise 3 : Building a Simple Neural Network with TensorFlow/Keras

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.utils import to_categorical
import numpy as np
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train.shape
x_test.shape
y_test.shape
x_train = x_train / 255.0
x_test = x_test / 255.0
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)
model.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.2)
test_loss, test_acc = model.evaluate(x_test, y_test)

#Exercise 4 :  Forward Propagation Calculation

x1= 2000
x2= 3
W1= 0.5
W2= 0.7
b= 50000
z = (W1 * x1) + (W2 * x2) + b
print("La valeur de z est :", z)
def relu(value):
    return max(0, value)    

predict = relu(z)
print("La valeur de la prédiction est :", predict)


