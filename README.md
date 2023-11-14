![image](https://img.shields.io/badge/Keras-FF0000?style=for-the-badge&logo=keras&logoColor=white)
![image](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/generation-of-colors-using-bidirectional-long/text-to-image-generation-on-colors)](https://paperswithcode.com/sota/text-to-image-generation-on-colors?p=generation-of-colors-using-bidirectional-long)


**Color Prediction**
--------------------------------------------

This model implements a Bidirectional Long Short Term Memory that uses a custom dataset created by me. The model is trained on this dataset to predict colors based on a user inputted query. The model is trained on a relation between color names and their respecitve RGB values. A function is then called upon utilizing a dataset of english adjectives and a list of primary and secondary colors. Each color in the list is mapped to adjectives present in the dataset and then prompted through the intially trained model. It is then added back to the ```colors.csv``` file and then trained again to predict colors.


**Model Hyperparameters**
------------------------------------

The model has 1.3M trainable parameters. The model is initially trained for 350 epochs on a batch size of 512 and for the Active Learning step a batch size of 1024 and 15 epochs. The first training loop the model achieves 73% training accuracy with 67% validation accuracy and the second training loop after the active learning step it achieves 75% training accuracy with 85% validation accuracy

![model](https://github.com/chungimungi/Color-prediction/assets/90822297/4e559504-46e2-46cb-97d7-cb7592a7fbe4)



**Results**
-------------------------------------------------

Prompt : Red

![image](https://github.com/chungimungi/Color-prediction/assets/90822297/41c44bcd-d4ef-445e-9335-1d9d10669a48)

Prompt : Deep Purple

![image](https://github.com/chungimungi/Color-prediction/assets/90822297/35b44bcb-9de1-4f0f-b519-e034960568d7)

Prompt : Olive Green

![image](https://github.com/chungimungi/Color-prediction/assets/90822297/83f297a3-6af7-40ca-896a-44c38fad8104)

Prompt : Bubblegum Pink

![image](https://github.com/chungimungi/Color-prediction/assets/90822297/91c37526-09c3-4df1-9cd9-74705612a074)

Prompt : Sunset

![image](https://github.com/chungimungi/Color-prediction/assets/90822297/bbc64e49-1649-4164-b91d-b155215b3d37)

**Possible Applications**
-------------------------------------
* Create realistic visual effects in movies and video games.

* Develop new ways to design and manufacture products.

* Improve the accuracy of medical imaging.



**Note: Paper under review to cite pre-print:**

```
@misc{sinha2023generation,
      title={Generation Of Colors using Bidirectional Long Short Term Memory Networks}, 
      author={A. Sinha},
      year={2023},
      eprint={2311.06542},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```
