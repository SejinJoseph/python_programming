import numpy as np

scores_array=np.array([10,20,30,40,50,60,70,80,90,100])
print(scores_array)

slicing_array=scores_array[2:5]
print(slicing_array)

print(slicing_array[:4])
print(slicing_array[:])
print(slicing_array[5:])
print(slicing_array[::2])
print(slicing_array[::3])
print(slicing_array[-3:])