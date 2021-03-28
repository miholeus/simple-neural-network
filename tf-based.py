# coding: utf-8
import tensorflow as tf
import numpy as np

features = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0], [1, 1, 0], [1, 1, 1]])
labels = np.array([[1, 0, 0, 1, 1]])
labels = labels.reshape(5, 1)

inputs = tf.keras.Input(shape=(3,), name='features')
outputs = tf.keras.layers.Dense(2, activation='relu', name='predictions')(inputs)

model = tf.keras.Model(inputs=inputs, outputs=outputs)
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(features, labels, epochs=5000)

test_features = np.array([[0, 1, 0]])
probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
predictions = probability_model.predict(test_features)
print(predictions)
