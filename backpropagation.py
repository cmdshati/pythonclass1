import numpy as np

class NeuralNetwork:
    def __init__(self):
        # Initialize weights
        self.w13 = 0.1
        self.w23 = 0.8
        self.w24 = 0.6
        self.w35 = 0.3
        self.w45 = 0.9
        self.learning_rate = 0.5
        self.target = 0.5
        
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        return x * (1 - x)
    
    def forward_pass(self, x1, x2):
        # Hidden layer calculations
        self.net_H3 = self.w13 * x1 + self.w23 * x2
        self.out_H3 = self.sigmoid(self.net_H3)
        
        self.net_H4 = self.w24 * x2
        self.out_H4 = self.sigmoid(self.net_H4)
        
        # Output layer calculations
        self.net_O5 = self.w35 * self.out_H3 + self.w45 * self.out_H4
        self.prediction = self.sigmoid(self.net_O5)
        
        return self.prediction
    
    def calculate_loss(self):
        # Mean Squared Error (H.S.E - Half Squared Error)
        return 0.5 * (self.target - self.prediction) ** 2
    
    def backward_pass(self, x1, x2):
        # Output layer gradient
        error = self.prediction - self.target
        delta_O5 = error * self.sigmoid_derivative(self.prediction)
        
        # Hidden layer gradients
        delta_H3 = delta_O5 * self.w35 * self.sigmoid_derivative(self.out_H3)
        delta_H4 = delta_O5 * self.w45 * self.sigmoid_derivative(self.out_H4)
        
        # Weight updates
        self.w35 -= self.learning_rate * delta_O5 * self.out_H3
        self.w45 -= self.learning_rate * delta_O5 * self.out_H4
        self.w13 -= self.learning_rate * delta_H3 * x1
        self.w23 -= self.learning_rate * delta_H3 * x2
        self.w24 -= self.learning_rate * delta_H4 * x2
        
        return delta_O5, delta_H3, delta_H4

# Initialize network
nn = NeuralNetwork()
x1, x2 = 0.35, 0.9

print("=== INITIAL STATE ===")
print(f"Weights: w13={nn.w13}, w23={nn.w23}, w24={nn.w24}, w35={nn.w35}, w45={nn.w45}")

# First forward pass
prediction = nn.forward_pass(x1, x2)
initial_loss = nn.calculate_loss()

print(f"\n=== FORWARD PASS ===")
print(f"Input: x1={x1}, x2={x2}")
print(f"Hidden H3: net={nn.net_H3:.3f}, out={nn.out_H3:.3f}")
print(f"Hidden H4: net={nn.net_H4:.3f}, out={nn.out_H4:.3f}")
print(f"Output O5: net={nn.net_O5:.3f}, prediction={prediction:.3f}")
print(f"Target: {nn.target}, Loss: {initial_loss:.6f}")

# Backward pass
delta_O5, delta_H3, delta_H4 = nn.backward_pass(x1, x2)

print(f"\n=== BACKWARD PASS ===")
print(f"Output delta (δ5): {delta_O5:.6f}")
print(f"Hidden delta H3 (δ3): {delta_H3:.6f}")
print(f"Hidden delta H4 (δ4): {delta_H4:.6f}")

print(f"\n=== WEIGHT UPDATES ===")
print(f"Δw35 = -{nn.learning_rate} × {delta_O5:.4f} × {nn.out_H3:.3f} = {nn.learning_rate * delta_O5 * nn.out_H3:.6f}")
print(f"Δw45 = -{nn.learning_rate} × {delta_O5:.4f} × {nn.out_H4:.3f} = {nn.learning_rate * delta_O5 * nn.out_H4:.6f}")
print(f"Δw13 = -{nn.learning_rate} × {delta_H3:.6f} × {x1} = {nn.learning_rate * delta_H3 * x1:.6f}")
print(f"Δw23 = -{nn.learning_rate} × {delta_H3:.6f} × {x2} = {nn.learning_rate * delta_H3 * x2:.6f}")
print(f"Δw24 = -{nn.learning_rate} × {delta_H4:.6f} × {x2} = {nn.learning_rate * delta_H4 * x2:.6f}")

print(f"\n=== UPDATED WEIGHTS ===")
print(f"w13_new = {nn.w13:.6f}")
print(f"w23_new = {nn.w23:.6f}")
print(f"w24_new = {nn.w24:.6f}")
print(f"w35_new = {nn.w35:.6f}")
print(f"w45_new = {nn.w45:.6f}")

# Training until convergence
print(f"\n=== TRAINING UNTIL CONVERGENCE ===")
epoch = 0
losses = [initial_loss]

while True:
    prediction = nn.forward_pass(x1, x2)
    loss = nn.calculate_loss()
    nn.backward_pass(x1, x2)
    losses.append(loss)
    
    if epoch % 100 == 0:
        print(f"Epoch {epoch}: Loss = {loss:.8f}")
    
    if loss < 0.0001 or epoch >= 1000:
        print(f"Epoch {epoch}: Loss = {loss:.8f}")
        break
    
    epoch += 1

print(f"\n=== FINAL RESULTS ===")
print(f"Final prediction: {prediction:.6f}")
print(f"Final loss: {loss:.8f}")
print(f"Total epochs: {epoch}")
print(f"Final weights: w13={nn.w13:.6f}, w23={nn.w23:.6f}, w24={nn.w24:.6f}, w35={nn.w35:.6f}, w45={nn.w45:.6f}")