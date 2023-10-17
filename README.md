![image](https://img.shields.io/badge/Keras-FF0000?style=for-the-badge&logo=keras&logoColor=white)
![image](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)


**Color Prediction**
--------------------------------------------

This model implements a Bidirectional Long Short Term Memory that uses a custom dataset created by me. The model is trained on this dataset to predict colors based on a user inputted query. The model is trained on a relation between color names and their respecitve RGB values. A function is then called upon utilizing a dataset of english adjectives and a list of primary and secondary colors. Each color in the list is mapped to adjectives present in the dataset and then prompted through the intially trained model. It is then added back to the ```colors.csv``` file and then trained again to predict colors.


**Model Hyperparameters**
------------------------------------

The model has 1.3M trainable parametersl to achieve an accuracy of 72%. The model is initially trained for 350 epochs on a batch size of 512 and for the Active Learning step a batch size of 1024 and 250 epochs. The first training loop the model achieves 73% accuracy and the second training loop after the active learning step it achieves.

![model](https://github.com/chungimungi/Color-prediction/assets/90822297/4e559504-46e2-46cb-97d7-cb7592a7fbe4)



**Results**
-------------------------------------------------

Prompt : Red

![image](https://github.com/chungimungi/Color-prediction/assets/90822297/db4786e9-3df1-47aa-aec0-a0e5c824eea6)

Prompt : Deep Purple

![image](https://github.com/chungimungi/Color-prediction/assets/90822297/f07f8164-c78f-493d-985d-da07a8e531fa)

Prompt : Olive Green

![image](https://github.com/chungimungi/Color-prediction/assets/90822297/8ff6e3e4-6baa-4947-a0f3-99b3f8f1b9d5)

Prompt : Bubblegum Pink

![image](https://github.com/chungimungi/Color-prediction/assets/90822297/c979e3bd-fd76-4526-a366-ac7e55625268)

Prompt : Sunset

![image](https://github.com/chungimungi/Color-prediction/assets/90822297/dce49b90-4014-422b-b5e0-3276b72a4047)

**Possible Applications**
-------------------------------------
* Create realistic visual effects in movies and video games.

* Develop new ways to design and manufacture products.

* Improve the accuracy of medical imaging.



**Note: This model is still under developement and is not final. Still working on improving the accuracy and increasing my datasets size**
