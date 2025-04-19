

def percentile(data, k):
    sorted_data = sorted(data)
    n = len(sorted_data)
    rank = (k / 100) * (n + 1)

    if rank.is_integer():
        return sorted_data[int(rank) - 1]
    else:
        lower = int(rank) - 1
        upper = lower + 1
        fraction = rank - int(rank)
        return sorted_data[lower] + fraction * (sorted_data[upper] - sorted_data[lower])

data = [3, 7, 8, 5, 12, 14, 21, 13, 18]
print("25th percentile (Q1):", percentile(data, 25))
print("50th percentile (Q2):", percentile(data, 50))
print("75th percentile (Q3):", percentile(data, 75))
