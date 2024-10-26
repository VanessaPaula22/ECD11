import pipeline.class.mlp
from pipeline.useful_functions import initalize_weights_relu, load_mnist

def main ():
  # Training with 400 epochs
  epochs = 400
  loss = np.zeros([epochs,1])
  
  
  # ## 1. Own implementation, class MLP
  
  # Load data
  X, Y, labels, y  = load_mnist()
  
  tic = time.time()
  
  # Creating the MLP object initialize the weights
  mlp_classifier = mlp.Mlp(size_layers = [784, 100, 10], 
                           act_funct   = 'relu',
                           reg_lambda  = 0,
                           bias_flag   = False)
  
  for ix in range(epochs):
      mlp_classifier.train(X, Y, 1)
      Y_hat = mlp_classifier.predict(X)
      # loss
      loss[ix] = (0.5)*np.square(Y_hat - Y).mean()
  
  print(str(time.time() - tic) + ' s')
          
  # Ploting loss vs epochs
  plt.figure()
  ix = np.arange(epochs)
  plt.plot(ix, loss)
  
  # Training Accuracy
  Y_hat = mlp_classifier.predict(X)
  y_tmp = np.argmax(Y_hat, axis=1)
  y_hat = labels[y_tmp]
  
  acc = np.mean(1 * (y_hat == y))
  print('Training Accuracy: ' + str(acc*100))
  
  
  # ## 2. numpy implementation
  # In this case Backpropagation is hard coded for 3 layers
  
  # Load data
  X, Y, labels, y = load_mnist()
  tic = time.time()
  
  # size_layers = [784, 100, 10]
  
  # Randomly initialize weights
  w1 = initalize_weights_relu(784, 100)
  w2 = initalize_weights_relu(100, 10)
  
  for ix in range(epochs):
      n_examples = X.shape[0]
      # Forward pass: compute y_hat    
      a1 = X
      z2 = a1.dot(w1)
      a2 = np.maximum(z2, 0)
      z3 = a2.dot(w2)
      a3 = np.maximum(z3, 0)
      Y_hat = a3
      
      # Compute loss
      loss[ix] = (0.5) * np.square(Y_hat - Y).mean()
      # Backprop to compute gradients of w1 and w2 with respect to loss
      d3 = Y_hat - Y
      grad2 = a2.T.dot(d3) / n_examples
      d2_tmp = d3.dot(w2.T)
      d2 = d2_tmp.copy()
      d2[z2 <= 0] = 0 #d2 = d2 * derivate of ReLU function
      grad1 = a1.T.dot(d2) / n_examples
      
      # Update weights
      w1 = w1 - grad1
      w2 = w2 - grad2
  
  print(str(time.time() - tic) + ' s')
      
  # Ploting loss vs epochs
  plt.figure()
  ix = np.arange(epochs)
  plt.plot(ix, loss)
  
  # Training Accuracy
  acc = np.mean(1 * (y_hat == y))
  print('Training Accuracy: ' + str(acc*100))
      
if __name__ == "__main__":
    main()
