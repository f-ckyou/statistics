

data = [10, 12, 23, 23, 16, 23, 21, 16, 18, 22]

# sample skewness
def sample_skewness(data):
    n = len(data)
    mean = sum(data) / n
    std_dev = (sum((x - mean)**2 for x in data) / (n - 1)) ** 0.5

    skewness = (n / ((n - 1)*(n - 2))) * sum(((x - mean)/std_dev)**3 for x in data)
    return skewness

# kurtosis
def kurtosis(data):
    n = len(data)
    mean = sum(data) / n
    std_dev = (sum((x - mean)**2 for x in data) / (n - 1)) ** 0.5

    numerator = sum(((x - mean)/std_dev)**4 for x in data)
    part1 = (n * (n + 1)) / ((n - 1)*(n - 2)*(n - 3))
    part2 = (3 * (n - 1)**2) / ((n - 2)*(n - 3))

    kurtosis = part1 * numerator - part2
    return kurtosis

print("Skewness: ", sample_skewness(data))
print("Kurtosis: ", kurtosis(data))