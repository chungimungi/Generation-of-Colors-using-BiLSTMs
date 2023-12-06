import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Bidirectional, LSTM
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing import sequence
import numpy as np
import pandas as pd

if tf.test.is_gpu_available():
    # Force TensorFlow to use the GPU
    config = tf.compat.v1.ConfigProto(device_count={'GPU': 1})
    config.gpu_options.allow_growth = True  # Allow GPU memory growth
    tf.compat.v1.keras.backend.set_session(tf.compat.v1.Session(config=config))
else:
    print("No GPU available, using CPU.")

# Load and preprocess your data
np.random.seed(10)
data = pd.read_csv("colors.csv")
names = data["name"]

maxlen = 100
t = Tokenizer(char_level=True)
t.fit_on_texts(names)
tokenized = t.texts_to_sequences(names)
padded_names = sequence.pad_sequences(tokenized, maxlen=maxlen)

def scale(n):
    return int(n * 255)

normalized_values = np.column_stack([data["red"], data["green"], data["blue"]])
normalized_values = normalized_values / 255.0

# Create and compile your model
model = Sequential()
model.add(Conv1D(256, kernel_size=3, activation='relu', input_shape=(maxlen, 3)))
model.add(Bidirectional(LSTM(256, activation='tanh')))
model.add(Dense(128, activation='tanh'))
model.add(Dense(128, activation='tanh'))
model.add(Dense(64, activation='tanh'))
model.add(Dense(64, activation='tanh'))
model.add(Dense(3, activation='sigmoid'))
model.add(Dropout(0.2))
model.compile(optimizer='adam', loss='mae', metrics=['acc'])

# Train the model with the initial data
history = model.fit(np.repeat(padded_names[:, :, np.newaxis], 3, axis=-1), normalized_values, epochs=350, batch_size=512, validation_split=0.20)

# Function to generate color names by combining adjectives and colors
def generate_color_names():
    with open('adj.txt', 'r') as file:
        adjectives = file.read().splitlines()

    colors = ["Red", "Yellow", "Blue", "Orange", "Green", "Violet"]

    for adjective in adjectives:
        for color in colors:
            yield f"{adjective} {color}"

path = 'colors.csv'

# Function to predict RGB values and update the CSV
def predict_and_update(name):
    global path
    name = name.lower()
    tokenized = t.texts_to_sequences([name])
    padded = sequence.pad_sequences(tokenized, maxlen=maxlen)
    pred = model.predict(np.repeat(padded[:, :, np.newaxis], 3, axis=-1))[0]
    r, g, b = scale(pred[0]), scale(pred[1]), scale(pred[2])
    data.loc[len(data)] = [name, r, g, b]  # Add the new RGB values to the CSV
    path = 'colors.csv'
    data.to_csv(path, index=False)

# Automated loop for generating and updating color names
for color_name in generate_color_names():
    predict_and_update(color_name)

print("\n Task Done \n")

# Retrain the model after adding new data
names = data["name"]
normalized_values = np.column_stack([data["red"], data["green"], data["blue"]])
normalized_values = normalized_values / 255.0
tokenized = t.texts_to_sequences(names)
padded_names = sequence.pad_sequences(tokenized, maxlen=maxlen)

history = model.fit(np.repeat(padded_names[:, :, np.newaxis], 3, axis=-1), normalized_values, epochs=350, batch_size=256, validation_split=0.20)

def plot_rgb(rgb):
    data = [[rgb]]
    plt.figure(figsize=(2, 2))
    plt.imshow(data, interpolation='nearest')
    plt.show()

def predict(name):
    name = name.lower()
    tokenized = t.texts_to_sequences([name])
    padded = sequence.pad_sequences(tokenized, maxlen=maxlen)
    pred = model.predict(np.repeat(padded[:, :, np.newaxis], 3, axis=-1))[0]
    r, g, b = scale(pred[0]), scale(pred[1]), scale(pred[2])
    print(name + ',', 'R,G,B:', r, g, b)
    plot_rgb(pred)

n = input()
predict(n)
