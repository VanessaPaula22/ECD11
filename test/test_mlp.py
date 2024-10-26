import numpy as np
from pipeline.mlp.mlp import Mlp
from pipeline.useful_functions import initalize_weights_relu, load_mnist

def test_mlp_training():
    # Test parameters
    epochs = 10  # Reduced for testing speed
    X, Y, labels, y = load_mnist()
    
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
    y_hat = labels[y_tmp]
    acc = np.mean(1 * (y_hat == y))
    
    # Assertions to validate functionality
    assert Y_hat.shape == (X.shape[0], 10), "Output shape mismatch"
    assert loss >= 0, "Loss should be non-negative"
    assert acc >= 0 and acc <= 1, "Accuracy should be between 0 and 1"

    print(f"Test passed: Loss = {loss}, Accuracy = {acc * 100:.2f}%")

if __name__ == "__main__":
    test_mlp_training()
