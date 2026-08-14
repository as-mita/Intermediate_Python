import numpy as np

# Dataset: exam scores
scores = np.array([65, 72, 81, 90, 76, 88, 95, 69, 84, 78])

# Calculate basic statistics
mean = np.mean(scores)
median = np.median(scores)
standard_deviation = np.std(scores)
minimum = np.min(scores)
maximum = np.max(scores)

# Print results
print("Scores:", scores)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", standard_deviation)
print("Minimum:", minimum)
print("Maximum:", maximum)

# Find students who scored above the average
above_average = scores[scores > mean]

print("Scores above average:", above_average)