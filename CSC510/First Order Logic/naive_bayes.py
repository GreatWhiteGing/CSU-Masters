import numpy as np
import pandas as pd
from collections import defaultdict

# --- 1. Create a Synthetic Dataset (Categorical Features) ---
# Let's imagine a dataset for predicting if a person will buy a product (Yes/No)
# based on their 'Age Group' and 'Income Level'.

data = {
    'Age_Group': ['Youth', 'Middle_Aged', 'Senior', 'Youth', 'Middle_Aged', 'Senior', 'Youth', 'Middle_Aged', 'Senior', 'Youth'],
    'Income_Level': ['Low', 'Medium', 'High', 'Medium', 'Low', 'Medium', 'High', 'Low', 'High', 'Medium'],
    'Buys_Product': ['No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No']
}
df = pd.DataFrame(data)
print("--- Original Dataset ---")
print(df)
print("\n" + "="*50 + "\n")

# Separate features (X) and target (y)
X = df[['Age_Group', 'Income_Level']]
y = df['Buys_Product']

# Get unique classes
classes = y.unique()
print(f"Classes: {classes}")
print("\n" + "="*50 + "\n")

# --- 2. Calculate Prior Probabilities (P(Class)) ---
# This is derived directly from the frequency of each class in the target variable.
prior_probabilities = y.value_counts(normalize=True).to_dict()
print("--- Prior Probabilities P(Class) ---")
print(prior_probabilities)
print("\n" + "="*50 + "\n")

# --- 3. Create Frequency Tables and Likelihood Tables ---
# P(Feature_Value | Class)
# This will be a dictionary of dictionaries to store counts.
# Outer dict: feature name
# Middle dict: class
# Inner dict: feature value -> count

# For likelihood, we'll convert counts to probabilities later.

feature_value_counts = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
class_counts = y.value_counts().to_dict() # Total count for each class

# Populate counts
for index, row in df.iterrows():
    target_class = row['Buys_Product']
    for feature in X.columns:
        feature_value = row[feature]
        feature_value_counts[feature][target_class][feature_value] += 1

print("--- Raw Feature Value Counts (Frequency Table conceptual) ---")
# Let's pretty print it for clarity
for feature, class_dict in feature_value_counts.items():
    print(f"Feature: {feature}")
    for target_class, value_counts in class_dict.items():
        print(f"  Class '{target_class}': {value_counts}")
print("\n" + "="*50 + "\n")


# --- 4. Calculate Likelihood Table with Laplace Correction ---
# P(Feature_Value | Class) = (Count(Feature_Value, Class) + alpha) / (Count(Class) + alpha * Num_Unique_Feature_Values)
# 'alpha' is the smoothing parameter (1 for Laplace smoothing)

alpha = 1 # Laplace smoothing constant

likelihood_tables = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))

for feature, class_dict in feature_value_counts.items():
    unique_feature_values = df[feature].unique()
    num_unique_feature_values = len(unique_feature_values)

    for target_class in classes: # Iterate through all possible classes
        total_class_count = class_counts[target_class]

        for feature_value in unique_feature_values: # Iterate through all possible feature values for this feature
            # Get the count for this specific feature value and class
            # Use .get() with default 0 in case the combination wasn't seen
            count_fv_c = feature_value_counts[feature][target_class].get(feature_value, 0)

            # Apply Laplace correction
            numerator = count_fv_c + alpha
            denominator = total_class_count + (alpha * num_unique_feature_values)

            likelihood_tables[feature][target_class][feature_value] = numerator / denominator

print("--- Likelihood Tables P(Feature_Value | Class) (with Laplace Correction) ---")
for feature, class_dict in likelihood_tables.items():
    print(f"Feature: {feature}")
    for target_class, value_probs in class_dict.items():
        print(f"  Class '{target_class}': {value_probs}")
print("\n" + "="*50 + "\n")


# --- 5. Calculate Posterior Probability for a New Instance ---
# P(Class | Features) = P(Class) * P(Feature1 | Class) * P(Feature2 | Class) * ...
# We need to calculate this for each class and pick the one with the highest probability.

def predict_naive_bayes(new_instance, prior_probs, likelihood_tables, classes):
    posterior_probs = {}
    for target_class in classes:
        # Start with the prior probability of the class
        current_posterior = prior_probs[target_class]

        # Multiply by the likelihood of each feature given the class
        for feature, feature_value in new_instance.items():
            # Get the likelihood from the pre-computed tables
            # This is where Laplace smoothing prevents zero probabilities if a feature_value is unseen
            # We assume our likelihood_tables were built considering all possible unique_feature_values,
            # so directly accessing will work. If an *entire new feature value* appears that wasn't in training,
            # this would still handle it by giving it a corrected probability from the smoothing.

            # Get the number of unique values for this feature from the original training data
            num_unique_feature_values_in_training = len(df[feature].unique())
            default_likelihood_for_unseen = alpha / (class_counts[target_class] + alpha * num_unique_feature_values_in_training)

            likelihood = likelihood_tables[feature][target_class].get(feature_value, default_likelihood_for_unseen)
            current_posterior *= likelihood
        
        posterior_probs[target_class] = current_posterior

    # Normalize posterior probabilities (optional, but good practice for true probabilities)
    total_posterior_sum = sum(posterior_probs.values())
    if total_posterior_sum > 0:
        normalized_posterior_probs = {c: p / total_posterior_sum for c, p in posterior_probs.items()}
    else: # If all probabilities are zero (very rare, but for robustness)
        normalized_posterior_probs = {c: 0.0 for c in classes}

    return normalized_posterior_probs, max(normalized_posterior_probs, key=normalized_posterior_probs.get)


# --- Test with a new instance ---
new_instance1 = {'Age_Group': 'Youth', 'Income_Level': 'High'}
posterior_probs1, predicted_class1 = predict_naive_bayes(new_instance1, prior_probabilities, likelihood_tables, classes)
print(f"--- Posterior Probabilities for new instance {new_instance1} ---")
print(f"Probabilities: {posterior_probs1}")
print(f"Predicted Class: {predicted_class1}")
print("\n")

new_instance2 = {'Age_Group': 'Senior', 'Income_Level': 'Low'}
posterior_probs2, predicted_class2 = predict_naive_bayes(new_instance2, prior_probabilities, likelihood_tables, classes)
print(f"--- Posterior Probabilities for new instance {new_instance2} ---")
print(f"Probabilities: {posterior_probs2}")
print(f"Predicted Class: {predicted_class2}")
print("\n")

new_instance3 = {'Age_Group': 'Middle_Aged', 'Income_Level': 'Medium'}
posterior_probs3, predicted_class3 = predict_naive_bayes(new_instance3, prior_probabilities, likelihood_tables, classes)
print(f"--- Posterior Probabilities for new instance {new_instance3} ---")
print(f"Probabilities: {posterior_probs3}")
print(f"Predicted Class: {predicted_class3}")
print("\n")

# Example of an unseen feature value in the test instance (e.g., 'Child' Age_Group)
# This will use the default_likelihood_for_unseen for 'Child'
# If a feature in the new instance has a value not seen *at all* in training for that feature,
# it will be handled by the .get() method with the calculated default_likelihood_for_unseen.
new_instance_unseen_value = {'Age_Group': 'Child', 'Income_Level': 'High'}
posterior_probs_unseen, predicted_class_unseen = predict_naive_bayes(new_instance_unseen_value, prior_probabilities, likelihood_tables, classes)
print(f"--- Posterior Probabilities for new instance with unseen value {new_instance_unseen_value} ---")
print(f"Probabilities: {posterior_probs_unseen}")
print(f"Predicted Class: {predicted_class_unseen}")
print("\n" + "="*50 + "\n")

# --- Comparing with Scikit-learn's Multinomial Naive Bayes (for categorical data) ---
# Scikit-learn's `MultinomialNB` expects numerical features. We need to encode our categorical features.
# One-Hot Encoding is suitable here.

from sklearn.preprocessing import OneHotEncoder
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

print("--- Comparing with Scikit-learn's Multinomial Naive Bayes ---")

# Encode categorical features
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False) # handle_unknown='ignore' for unseen categories in test
X_encoded = encoder.fit_transform(X)
feature_names = encoder.get_feature_names_out(X.columns)
X_encoded_df = pd.DataFrame(X_encoded, columns=feature_names)

print("\nEncoded Features (X_encoded):\n", X_encoded_df)

# Train a Multinomial Naive Bayes model
mnb = MultinomialNB(alpha=1.0) # alpha=1.0 for Laplace smoothing (default)
mnb.fit(X_encoded, y)

# Predict using scikit-learn
# Need to encode the new instance similarly
new_instance1_encoded = encoder.transform(pd.DataFrame([new_instance1]))
skl_pred1 = mnb.predict(new_instance1_encoded)
skl_proba1 = mnb.predict_proba(new_instance1_encoded)

print(f"\nScikit-learn Prediction for {new_instance1}:")
print(f"  Predicted Class: {skl_pred1[0]}")
print(f"  Probabilities (P(Class|Features)): {skl_proba1[0]} (Order: {mnb.classes_})")


new_instance_unseen_value_encoded = encoder.transform(pd.DataFrame([new_instance_unseen_value]))
skl_pred_unseen = mnb.predict(new_instance_unseen_value_encoded)
skl_proba_unseen = mnb.predict_proba(new_instance_unseen_value_encoded)

print(f"\nScikit-learn Prediction for {new_instance_unseen_value}:")
print(f"  Predicted Class: {skl_pred_unseen[0]}")
print(f"  Probabilities (P(Class|Features)): {skl_proba_unseen[0]} (Order: {mnb.classes_})")
print("\n" + "="*50 + "\n")