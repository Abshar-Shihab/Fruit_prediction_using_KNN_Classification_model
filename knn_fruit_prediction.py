import csv
import numpy as np
import math


def euclidean_distance(row1, row2):
    distance = math.sqrt(sum((row1[i] - row2[i]) ** 2 for i in range(1, len(row1))))
    return distance


def knn_predict(test_row, train_data, k):
    distances = [(train_row, euclidean_distance(test_row, train_row)) for train_row in train_data]

    distances.sort(key=lambda x: x[1])
    neighbors = [distances[i][0] for i in range(k)]

    class_votes = {}
    for neighbor in neighbors:
        label = int(neighbor[0])
        if label in class_votes:
            class_votes[label] += 1
        else:
            class_votes[label] = 1

    prediction = max(class_votes, key=class_votes.get)
    return prediction


with open('fruit_data_with_colours.csv', 'r') as file:
    csvreader = csv.reader(file)
    dataset = []
    for row in csvreader:
        dataset.append(row)

dataset.remove(dataset[0])
dataset = np.array(dataset, dtype=float)

test_samples = dataset[:5]
trainset = dataset[5:]


k = 5
correct_predictions = 0

print("Test Sample Predictions:")
for test_sample in test_samples:
    prediction = knn_predict(test_sample, trainset, k)
    actual_label = int(test_sample[0])
    print(f"Predicted: {prediction}, Actual: {actual_label}")

    if prediction == actual_label:
        correct_predictions += 1

accuracy = (correct_predictions / len(test_samples)) * 100
print(f"\nAccuracy: {accuracy:.2f}%")
