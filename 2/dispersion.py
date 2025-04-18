
data = [4, 8, 6, 5, 3, 9, 12]

# Range
# 
range = max(data) - min(data)
print(range)


# Variance
#
mean = sum(data)
squared_diffs = [(x - mean) ** 2 for x in data]

sample_variance = sum(squared_diffs) / (len(data) - 1)

population_variance = sum(squared_diffs) / len(data)

print("Sample Variance:", sample_variance)
print("Polulation Variance:", population_variance)


# Standard Deviation
# 
sample_sd = sample_variance ** 0.5
population_sd = population_variance ** 0.5

print("Sample SD:", sample_sd)
print("Polulation SD:", population_sd)


# IQR
#


# MAD
# 
normal_diff = [(x - mean) for x in data]
mad = sum(normal_diff) / len(data)
print("MAD:", mad)


### 

import statistics as st 
    # module 'statistics' has no attribute 'range'

# Sample Variance
sample_variance = st.variance(data)
print(f"Sample Variance: {sample_variance}")

# Population Variance
population_variance = st.pvariance(data)
print(f"Population Variance: {population_variance}")

# Sample Standard Deviation
sample_std_dev = st.stdev(data)
print(f"Sample Standard Deviation: {sample_std_dev}")

# Population Standard Deviation
population_std_dev = st.pstdev(data)
print(f"Population Standard Deviation: {population_std_dev}")

## BIG DIFFERENCE WTF!!!