import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# ========== PLOT 1: Histogram (X-ray Pixel Intensities) ==========
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)  # 1 row, 3 columns, first plot
data = np.random.randint(0, 256, 1000)  # Simulating X-ray pixel intensities
plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.title("Histogram of X-ray Pixel Intensities")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

# ========== PLOT 2: Scatter Plot (Age vs Disease Probability) ==========
plt.subplot(1, 3, 2)  # Second plot
age = np.random.randint(20, 80, 50)  # Age of patients
disease_prob = np.random.rand(50)  # Probability of disease (0 to 1)
plt.scatter(age, disease_prob, color='red', alpha=0.6)
plt.title("Age vs Disease Probability")
plt.xlabel("Age of Patients")
plt.ylabel("Probability of Disease")
plt.grid(True)

# ========== PLOT 3: Heatmap (Medical Feature Correlations) ==========
plt.subplot(1, 3, 3)  # Third plot
data = pd.DataFrame(np.random.rand(5, 5), columns=["Fever", "Cough", "Fatigue", "X-ray Score", "Diagnosis"])
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap of Medical Features")

plt.tight_layout()  # Adjust spacing
plt.savefig("visualization.png", dpi=300, bbox_inches="tight")
plt.show()
