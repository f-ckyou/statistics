import statistics

# median_low & median_high

data1 = [1, 3, 3, 4, 5, 7]
print(f"Low median of {data1}: {statistics.median_low(data1)}")  
print(f"High median of {data1}: {statistics.median_high(data1)}") 

data2 = [1, 2, 3, 4]
print(f"Low median of {data2}: {statistics.median_low(data2)}")  
print(f"High median of {data2}: {statistics.median_high(data2)}")


# multimode

data1 = ['a', 'b', 'c', 'b', 'd', 'b']
print(f"Multimode of {data1}: {statistics.multimode(data1)}") 

data2 = [1, 2, 2, 3, 4, 4, 5]
print(f"Multimode of {data2}: {statistics.multimode(data2)}") 

data3 = []
print(f"Multimode of {data3}: {statistics.multimode(data3)}") 