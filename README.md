# Fruit_prediction_using_KNN_Classification_model
This repository contains a Python implementation of the K-Nearest Neighbors (KNN) algorithm for predicting the class of fruits based on features such as size, weight, and colour.


---

## Description: Fruit Prediction using K-Nearest Neighbors (KNN)

This repository contains a Python implementation of the K-Nearest Neighbors (KNN) algorithm for predicting the class of fruits based on features such as size, weight, and color. The KNN algorithm is a simple, non-parametric supervised learning method that classifies data points based on the majority class of their nearest neighbors in the feature space.

### Features
- **KNN Classifier:** Implements the core KNN logic, including calculating distances, finding neighbors, and predicting classes.
- **Euclidean Distance Metric:** Measures the similarity between data points.
- **CSV File Support:** Reads fruit data from a CSV file and uses it for training and testing the model.
- **Dynamic K-Value:** Allows selection of the number of nearest neighbors (K) to tune classification performance.

### Dataset
The dataset consists of fruit characteristics:
- **Features:** Mass, width, height, color_score
- **Labels:** Class of fruit (1, 2, 3, 4)

---


## Usage

1. Place your dataset in the same directory as the script and name it `fruit_data_with_colours.csv`.

2. Run the script:
   ```bash
   python knn_fruit_prediction.py
   ```

3. Modify the number of neighbors (K) in the script to observe how it affects the predictions.

---

## Steps in KNN

### Step 1: Distance Calculation
- The Euclidean distance is used to measure similarity between data points:
  \[
  \text{Distance} = \sqrt{\sum_{i=1}^n (x_i - y_i)^2}
  \]

### Step 2: Finding K Nearest Neighbors
- Distances between the test point and all training points are calculated and sorted.
- The K points with the smallest distances are selected as the neighbors.

### Step 3: Predicting the Class
- The most common class among the neighbors is assigned to the test data.

---

## Dataset

The dataset should be in CSV format, with the following structure:

| fruit_label | Mass | Width  | height      | color_score |
|-------------|------|--------|-------------|--------|
|      1      | 192  | 8.4    | 7.3         | 0.55   |
|      2      | 86   | 6.2    | 4.7         | 0.77   |
|    ...      | ...  | ...    | ...         | ...    |

Replace `fruit_data_with_colours.csv` with your own dataset if needed.



## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

---
