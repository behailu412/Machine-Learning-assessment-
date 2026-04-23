import matplotlib.pyplot as plt
import numpy as np

# Generate x values (angles in radians)

x = np.linspace(-2* np.pi, 2 * np.pi, 400) # From -2pi to 2pi with 400 points
# Calculate y values for sine, cosine, and tangent
y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)

# Create a figure and a set of subplots
fig, axes = plt.subplots(3, 1, figsize=(8, 10)) # 3 rows, 1 column

# Plot sine function in the first subplot
axes[0].plot(x, y_sin, label='sin(x)', color='blue')
axes[0].set_title('Sine Function')
axes[0].set_ylabel('sin(x)')
axes[0].grid(True)
axes[0].legend()

# Plot cosine function in the second subplot
axes[1].plot(x, y_cos, label='cos(x)', color='green')
axes[1].set_title('Cosine Function')
axes[1].set_ylabel('cos(x)')
axes[1].grid(True)
axes[1].legend()

# Plot tangent function in the third subplot
# Handle asymptotes for tangent by setting y-limits
axes[2].plot(x, y_tan, label='tan(x)', color='red')
axes[2].set_title('Tangent Function')
axes[2].set_xlabel('Angle (radians)')
axes[2].set_ylabel('tan(x)')
axes[2].set_ylim(-10, 10) # Limit y-axis to avoid extreme values near asymptotes
axes[2].grid(True)
axes[2].legend()

# Adjust layout to prevent overlapping titles/labels
plt.tight_layout()

# Display the plot
plt.show()
