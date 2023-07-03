# README.md

## Introduction
This project aims at training a Named Entity Recognition (NER) model using the SpaCy library. The project involves the following steps:

1. Creating a training dataset
2. Verifying the training dataset
3. Training the NER model
4. Creating a testing dataset
5. Testing the NER model
6. Calculating the testing accuracy

---

## 1. Creating a Training Dataset
The training dataset should be a list of tuples, where each tuple contains a text and its annotations. The text is a string, and the annotations are a dictionary with the key 'entities' and value as a list of tuples. Each tuple in the list represents an entity and contains the start index, end index, and label of the entity.

You need to create the training dataset and save it into the folder `training_data` with files named `data_1m_1.py`, `data_1m_2.py`, etc., each containing a list of tuples named `TRAIN_DATA`.

---

## 2. Verifying the Training Dataset
To verify the correctness of the training dataset, use the `verifyDataset.py` script. This script will load each dataset and output the annotations in a more readable format in a file `verifyDatasetResult.py`.

---

## 3. Training the NER Model
To train the NER model, use the `training.py` script. This script will create a new SpaCy model with a custom NER pipeline. The model is trained using the training data saved in the `training_data` folder with `data_1m_{i+1}.py` files. The trained model is saved in a new directory `models/model_{i+1}`.

---

## 4. Creating a Testing Dataset
The testing dataset should be similar to the training dataset. It should contain the text and annotations of the testing data. You need to create the testing dataset and save it into the folder `testing_data` with files named `data_1m_1.py`, `data_1m_2.py`, etc., each containing a list of tuples named `TEST_DATA`.

---

## 5. Testing the NER Model
To test the NER model, use the `testing.py` script. This script will load the latest trained model and run NER on each text in the testing datasets. The predicted entities are then saved in a JSON format in the `testingResult.py` file.

---

## 6. Calculating the Testing Accuracy
To calculate the testing accuracy, use the `testingAccuracy.py` script. This script will compare the predicted entities with the actual entities in the testing data, and compute the accuracy.

---

## Conclusion
This project provides a complete workflow for training and testing a NER model using SpaCy. By following these steps, you can create your own NER model and evaluate its performance.