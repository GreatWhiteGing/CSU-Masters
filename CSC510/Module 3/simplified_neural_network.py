import tensorflow as tf
import numpy as np

# Define the network architecture
input_size = 3
hidden_size = 4
output_size = 1

# Create the sequential model
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(input_size,)),
    tf.keras.layers.Dense(hidden_size, activation='sigmoid', name='hidden_layer_1'),
    tf.keras.layers.Dense(output_size, activation='sigmoid', name='output_layer')
])

# Define the optimizer and the loss function
optimizer = tf.keras.optimizers.SGD(learning_rate=0.1)  # Stochastic Gradient Descent
loss_fn = tf.keras.losses.MeanSquaredError()

# Training loop
def train_step(model, inputs, targets):
    with tf.GradientTape() as tape:
        predictions = model(inputs)  # Forward pass
        loss = loss_fn(targets, predictions)  # Calculate the loss

    gradients = tape.gradient(loss, model.trainable_variables)  # Calculate gradients
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))  # Apply gradients to update weights
    return loss

# Training data (example)
X_train = np.array([[0.1, 0.5, 0.9],
                    [0.2, 0.7, 0.3],
                    [0.8, 0.1, 0.6],
                    [0.5, 0.9, 0.2]], dtype=np.float32)
y_train = np.array([[0.2],
                    [0.4],
                    [0.7],
                    [0.9]], dtype=np.float32)

# Number of training epochs
epochs = 1000

# Training the model
print("Training the ANN...")
for epoch in range(epochs):
    epoch_loss = 0.0
    for i in range(X_train.shape[0]):
        input_sample = tf.expand_dims(X_train[i], axis=0)
        target_sample = tf.expand_dims(y_train[i], axis=0)
        loss = train_step(model, input_sample, target_sample)
        epoch_loss += loss.numpy()
    if (epoch + 1) % 100 == 0:
        print(f"Epoch {epoch + 1}, Loss: {epoch_loss / X_train.shape[0]:.4f}")

print("\nTraining complete!")

# Evaluate the trained model on the training data
print("\nEvaluating the trained model on the training data:")
predictions_train = model.predict(X_train)
print("Predictions (Training Data):")
print(predictions_train)
print("True Targets (Training Data):")
print(y_train)

# Function to accept user input and make a prediction
def predict_from_input(model):
    while True:
        try:
            input_str = input(f"\nEnter {input_size} comma-separated numbers for prediction (or type 'quit' to exit): ")
            if input_str.lower() == 'quit':
                break
            input_values = [float(x.strip()) for x in input_str.split(',')]
            if len(input_values) != input_size:
                print(f"Please enter exactly {input_size} numbers.")
                continue
            input_array = np.array([input_values], dtype=np.float32)
            prediction = model.predict(input_array)
            print("Prediction:", prediction[0][0])
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")

# Allow user to input data for prediction
predict_from_input(model)

# You can also inspect the trained weights:
print("\nTrained weights of the model:")
for layer in model.layers:
    print(f"\nTrained weights of layer '{layer.name}':")
    print(layer.get_weights())