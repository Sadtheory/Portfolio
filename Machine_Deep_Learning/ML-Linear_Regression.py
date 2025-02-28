import pandas as pd
import matplotlib.pyplot as plt

# Get the Data
# Source: 'https://archive.org/download/ages-and-heights/AgesAndHeights.pkl'
raw_data = pd.read_pickle(r'E:\Tools\tkinter\Portfolie\Portfolio\AgesAndHeights.pkl')

# Data Cleaning
cleaned_data = raw_data[raw_data['Age'] > 0]

# Visualize the Cleaned Data
# Plot histogram for cleaned data
cleaned_data.hist()
plt.figure()  # Separate figure for the scatter plot
ages = cleaned_data['Age']
heights = cleaned_data['Height']
plt.scatter(ages, heights, label='Raw Data')
plt.title('Height vs Age')
plt.xlabel('Age (Years)')
plt.ylabel('Height (Inches)')
plt.legend()
plt.show()  # Display the first plot

# Build the Model and Train it
parameters = {'alpha': None, 'beta': None}

# Function to calculate predictions
def y_hat(age, params):
    alpha = params['alpha']
    beta = params['beta']
    return alpha + beta * age 

# Function to learn parameters (linear regression)
def learn_parameters(data, params):
    x, y = data['Age'], data['Height']
    x_bar, y_bar = x.mean(), y.mean()
    x, y = x.to_numpy(), y.to_numpy()
    beta = sum((x - x_bar) * (y - y_bar)) / sum((x - x_bar) ** 2) 
    alpha = y_bar - beta * x_bar
    params['alpha'] = alpha
    params['beta'] = beta

# Train the model
new_parameters = {'alpha': 0, 'beta': 0}
learn_parameters(cleaned_data, new_parameters)

# Create predictions for a range of ages
spaced_ages = list(range(18))
spaced_trained_predictions = [y_hat(x, new_parameters) for x in spaced_ages]

# Plot the trained predictions
plt.figure()  # New figure for the linear regression plot
plt.scatter(ages, heights, label='Raw Data')
plt.plot(spaced_ages, spaced_trained_predictions, label='Trained Predictions', color='green', lw=3)
plt.title('Height vs Age with Linear Regression')
plt.xlabel('Age (Years)')
plt.ylabel('Height (Inches)')
plt.legend()
plt.show()  # Display the regression plot

# Use the Model - Make a Prediction for a new age
new_age = 5
predicted_height = y_hat(new_age, new_parameters)
print(f"Predicted height for age {new_age}: {predicted_height:.2f} inches")
