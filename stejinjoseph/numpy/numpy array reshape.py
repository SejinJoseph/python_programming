import numpy as np

original_array=np.array([1,2,3,4,5,6])
print(original_array)
print(original_array.shape)

reshaped_array=original_array.reshape(2,3)
print(reshaped_array)
print(reshaped_array.shape)

reahaped_three_d=original_array.reshape(2,1,3)
print(reahaped_three_d)
print(reahaped_three_d.shape)

invalid_reshaped=original_array.reshape(4,2)
print(invalid_reshaped)

auto_reshape=original_array.reshape(2,-1)
print(auto_reshape)
print(auto_reshape.shape)
