import torch

tensor_1d = torch.tensor([1,2,3])
print(tensor_1d)

tensor_2d = torch.tensor([[1,2],[3,4]])
print(tensor_2d)

tensor_zero = torch.zeros(5,5)
print(tensor_zero)

tensor_ones = torch.ones(5,5)
print(tensor_ones)

random_tensor = torch.rand(5,5)
print(random_tensor)