**Using GRU** 
*All the models used adam as an optimizer and mse as loss function over the metrics acc*

*At 1000 epochs and batch rate of 128 0.25 validation split activation='softmax'*

Model overtrained giving false outputs for the time it trained for even though a accuracy of 91% was achieved. Model was unable to provide differemt shades if blue, light blue dark blue and blue all outputted the same color


*At 400 epochs and batch rate of 128 0.25 validation split activation='softmax'*

Model overtrained giving false outputs for the time it trained for even though a accuracy of 87% was achieved. Model was unable to provide differemt shades if blue, light blue dark blue and blue all outputted the same color


*At 400 epochs and batch rate of 128 0.25 validation split activation='softmax'*

Model overtrained giving false outputs for the time it trained for even though a accuracy of 87% was achieved. Model was unable to provide differemt shades if blue, light blue dark blue and blue all outputted the same color


*At 40 epochs and batch rate of 64 0.25 validation split activation='softmax'*

Model overtrained giving false outputs for the time it trained for even though a accuracy of 68%. The model was able to distinguish between light blue and blue but light blue was very inaccurate


*At 40 epochs and batch rate of 64 0.2 validation split activation='softmax'*

Model overtrained giving false outputs for the time it trained for even though a accuracy of 68%. The model was able to distinguish between light blue and blue but light blue was very inaccurate


*At 100 epochs and batch rate of 64 0.2 validation split activation='sigmoid'*

Model could be trained better giving acceptable outputs for shades of blue with clear distrinction between blue, dark blue and sky blue even though accuracy was at 71% the best results were received so far
