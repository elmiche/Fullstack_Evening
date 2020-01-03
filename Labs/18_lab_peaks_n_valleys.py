# this is lab 18
#Justin gave the okay to skip version 2 an 3


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
indexes = list(range(len(data)))
# print(indices)

def peaks(data,indices):
    peaks = []
    for i in indices:
        if (i - 1) in indices and (i + 1) in indices:
            if data[i] > data[i+1] and data[i]> data[i-1]:
                peaks.append(i)
        else:
            pass
    return peaks
print(peaks(data,indexes))

#the funciton above requires the parameter 'indices' to pull data from a variable defined outside of the funciton.
# the function below doesn't require another parameter because the variable is defined WITHIN the function. 

def valleys(data):
    indexes = range(len(data))               #you can reuse var names in function, indexes is a different var here.
    indexes = list(indexes)
    valleys =[]
    for i in indexes:
        if (i -1) in indexes and (i + 1) in indexes:
            if data[i] < data[i-1] and data[i] < data[i+1]:
                valleys.append(i)
        else:
            pass
    return valleys
print(valleys(data))


def peaks_and_valleys(data, indices):
    list_of_valleys = valleys(data)
    list_of_peaks = peaks(data, indices)
    peaks_plus_valleys = list_of_peaks + list_of_valleys
    return sorted(peaks_plus_valleys)
print(peaks_and_valleys(data, indexes))


