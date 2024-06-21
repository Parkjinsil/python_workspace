from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier

# Load the breast cnacer dataset
data = load_breast_cancer()
X, y = data.data, data.target 

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Initialize the CatBoostClassifier
model = CatBoostClassifier(loss_function='Logloss', eval_metric='AUC', random_seed=42)

# Fit the model on the training data
model.fit(X_train, y_train)

# Evaluate the model on the test data
print('Acuuracy : {:.2f}'.format(model.score(X_test, y_test)))

from sklearn.metrics import classification_report

# Predict the class labels of the test data
y_pred = model.predict(X_test)

# Get the classification report
cr = classification_report(y_test, y_pred)
print(cr)

from catboost import Pool
import matplotlib.pyplot as plt
import numpy as np

# Create a Pool dataset
pool = Pool(data=X_train, label=y_train)

# Train the model
model.fit(pool)

feature_importance = model.get_feature_importance(pool)

# Sort the feature importances in descending order
sorted_idx = np.argsort(feature_importance)[::1]
 
# Reorder the feature names and the feature importances
sorted_feature_names = data.feature_names[sorted_idx]
sorted_feature_importance = feature_importance[sorted_idx]

# Plot the feature importances
fig, ax = plt.subplots(figsize=(10,5), constrained_layout=True)
ax.barh(range(len(sorted_feature_importance)), sorted_feature_importance)
ax.set_yticks(range(len(sorted_feature_importance)))
ax.set_yticklabels(sorted_feature_names)
plt.show()


