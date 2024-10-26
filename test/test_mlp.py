import numpy as np
from pipeline.mlp.mlp import Mlp
from pipeline.useful_functions import initalize_weights_relu 

def create_synthetic_data(num_samples=1000, num_features=784, num_classes=10):
    # Generate random features
    X = np.random.rand(num_samples, num_features)
    # Generate random labels (one-hot encoded)
    y = np.random.randint(num_classes, size=num_samples)
    
    # Convert labels to one-hot encoding
    Y = np.zeros((num_samples, num_classes))
    for i in range(num_samples):
        Y[i, y[i]] = 1
        
    return X, Y, y

def test_mlp_training():
    # Test parameters
    epochs = 10  # Reduced for testing speed
    num_samples = 1000  # Number of synthetic samples
    X, Y, y = create_synthetic_data(num_samples)

    # Create the MLP model
    mlp_classifier = Mlp(size_layers=[784, 100, 10], 
                         act_funct='relu',
                         reg_lambda=0,
                         bias_flag=False)
    
    # Train the model
    for ix in range(epochs):
        mlp_classifier.train(X, Y, 1)

    # Predict
    Y_hat = mlp_classifier.predict(X)
    
    # Calculate loss
    loss = (0.5) * np.square(Y_hat - Y).mean()
    
    # Calculate accuracy
    y_tmp = np.argmax(Y_hat, axis=1)
    acc = np.mean(y_tmp == np.argmax(Y, axis=1))  # Compare predicted and true labels
    
    # Assertions to validate functionality
    assert Y_hat.shape == (X.shape[0], 10), "Output shape mismatch"
    assert loss >= 0, "Loss should be non-negative"
    assert acc >= 0 and acc <= 1, "Accuracy should be between 0 and 1"

    print(f"Test passed: Loss = {loss}, Accuracy = {acc * 100:.2f}%")

if __name__ == "__main__":
    test_mlp_training()
