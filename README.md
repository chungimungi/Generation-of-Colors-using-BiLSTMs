#Color Prediction with RNN
This repository contains code for a color prediction model using a recurrent neural network (RNN) implemented with TensorFlow. The model takes color names as input and predicts the corresponding RGB values.

Dependencies
TensorFlow
NumPy
pandas
matplotlib
Dataset
The model is trained on a dataset of color names and their corresponding RGB values. The dataset is provided in a CSV file named colors.csv.

Model Architecture
The model architecture consists of a bidirectional SimpleRNN layer followed by a fully connected (Dense) layer and an output layer. The SimpleRNN layer processes the input sequences of color names, and the fully connected layers help in capturing the underlying patterns and relationships. The output layer uses the sigmoid activation function to predict the RGB values.

Training
The model is trained using the fit function from TensorFlow. The color names are tokenized and padded to a maximum length of 25 characters using the Tokenizer and sequence.pad_sequences functions. The RGB values are normalized to the range [0, 1]. The training process is configured with the Adam optimizer, mean squared error (MSE) loss function, and accuracy metric. The training history is stored in the history variable.

Prediction
The repository provides a function predict(name) that takes a color name as input and predicts its corresponding RGB values. The function tokenizes and pads the input name, feeds it to the trained model, and scales the predicted RGB values back to the range [0, 255]. The function also displays a color swatch of the predicted RGB values using matplotlib.

Usage
To use this code, make sure you have the required dependencies installed. Prepare your color dataset in a CSV file named colors.csv with columns for color names, red values, green values, and blue values. Then, execute the code to train the model and make color predictions using the predict(name) function.

Please note that this description assumes the presence of the colors.csv dataset file in the same directory as the code file.
