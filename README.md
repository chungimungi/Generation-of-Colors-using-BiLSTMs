**Color Prediction**

This repository contains code for a color prediction model using a recurrent neural network (RNN) implemented with TensorFlow. The model takes color names as input and predicts the corresponding RGB values. I have used a RNN model :
1. LSTM


**Dependencies**

TensorFlow
NumPy
pandas
matplotlib
Dataset
The model is trained on a dataset of color names and their corresponding RGB values. The dataset is provided in a CSV file named colors.csv.


**Training**

The model is trained using the fit function from TensorFlow. The color names are tokenized and padded to a maximum length of 25 characters using the Tokenizer and sequence.pad_sequences functions. The RGB values are normalized to the range [0, 1]. The training process is configured with the Adam optimizer, mean squared error (MSE) loss function, and accuracy metric. The training history is stored in the history variable.
