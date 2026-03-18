import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)
import os

# Ensuring that the dataset file is always consistently loaded


# For using from Kaggle

# import kagglehub
# file_path = kagglehub.dataset_download(
#     "miadul/covid-19-patient-symptoms-and-diagnosis-dataset"
# )

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "covid19_patient_symptoms_diagnosis.csv")

df = pd.read_csv(file_path)


# Examining the dataset structure and contents

print("Dataset Shape:", df.shape, "\n")
print("Dataset Info:\n", df.info(), "\n")
print("First few rows of the dataset:\n", df.head(), "\n")


# Preprocessing the dataset

df.drop(
    columns=["patient_id", "gender", "comorbidity"], inplace=True
)  # Dropping categorical features
df.dropna(inplace=True)  # Removing rows with missing values
# Data imputation could also work but that is beyond the scope of this assignment
# Additionally, the features do not have a proper method to be imputed as neither
# mean nor median would be appropriate for binary features

# Loading the basic values

x = df.drop(columns=["covid_result"])
y = df["covid_result"]


# Splitting the dataset; 20% for testing

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

scaler = (
    StandardScaler()
)  # Scaling helps to standardize the features (especially for KNN)
x_train = pd.DataFrame(scaler.fit_transform(x_train), columns=x_train.columns)
x_test = pd.DataFrame(scaler.transform(x_test), columns=x_test.columns)

# Initializing the models using Hyperparameters

dt_classifier = DecisionTreeClassifier(
    criterion="gini", max_depth=7, random_state=42
)  # Using Gini Impurity; Max depth of 7 to prevent overfitting; Random state for reproducibility

nb_classifier = GaussianNB(
    var_smoothing=1e-9
)  # Variable smoothing to handle zero probabilities

knn_classifier = KNeighborsClassifier(
    n_neighbors=7, weights="uniform"
)  # Using 7 neighbors for KNN; Uniform weights


# Training the models

dt_classifier.fit(x_train, y_train)
nb_classifier.fit(x_train, y_train)
knn_classifier.fit(x_train, y_train)


# Evaluating the models


def evaluate_model(
    model, x_test, y_test
):  # Function for DRY coding to evaluate each model
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    print(f"Model: {model.__class__.__name__}")
    print(f"Accuracy: {accuracy}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"F1-Score: {f1}")
    print(f"Confusion Matrix:\n{cm}\n")

    return {"accuracy": accuracy, "precision": precision, "recall": recall, "f1": f1}


dt_metrics = evaluate_model(dt_classifier, x_test, y_test)
nb_metrics = evaluate_model(nb_classifier, x_test, y_test)
knn_metrics = evaluate_model(knn_classifier, x_test, y_test)

comparison = pd.DataFrame(
    [dt_metrics, nb_metrics, knn_metrics],
    index=["Decision Tree", "Naive Bayes", "K-Nearest Neighbors"],
)

print("Comparision of Models:\n", comparison)


# Visualizing the results

# Bar plot

comparison.plot(kind="bar", figsize=(8, 5))
plt.title("Model Performance Comparison")
plt.ylabel("Score")
plt.ylim(0, 1)
plt.xticks(rotation=0)
plt.legend(loc="lower right")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
# plt.savefig(os.path.join(script_dir, "comparison.png"))

# Heatmap for confusion matrices

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

models = [
    ("Decision Tree", dt_classifier),
    ("Naive Bayes", nb_classifier),
    ("KNN", knn_classifier),
]

for ax, (name, model) in zip(axes, models):
    y_pred = model.predict(x_test)
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=["Negative", "Positive"],
        yticklabels=["Negative", "Positive"],
        ax=ax,
        cbar=True,
    )
    ax.set_title(f"{name}")
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")

plt.tight_layout()
# plt.savefig(os.path.join(script_dir, "confusion_matrices.png"))
plt.show()
