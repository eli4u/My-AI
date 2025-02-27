import tensorflow as tf 
import numpy as np

model = tf.keras.Sequential([
  tf.keras.layers.Dense(units=1,
input_shape=[1])
[)

model.compile(optimizer='sgd',
loss='mean_squared_error')

x_train = np.array[1, 2, 3, 4, 5],
dtype=float)
y_train = np.array([2, 4, 6, 8, 10],
dtype=flout)

model.fit(x_train, y_train, epochs=500,

print(model.predict([6]))
