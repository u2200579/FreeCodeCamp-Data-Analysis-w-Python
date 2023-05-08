import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  y = np.array(list)
  x = y.reshape(3, 3)
  return  {
    'mean' : [x.mean(axis=0).tolist(), x.mean(axis=1).tolist(),x.mean()],
    'variance' : [x.var(axis=0).tolist(), x.var(axis=1).tolist(),x.var()],
    'standard deviation': [x.std(axis=0).tolist(), x.std(axis=1).tolist(),x.std()],
    'max': [x.max(axis=0).tolist(), x.max(axis=1).tolist(),x.max()],
    'min' : [x.min(axis=0).tolist(), x.min(axis=1).tolist(),x.min()],
    'sum' : [x.sum(axis=0).tolist(), x.sum(axis=1).tolist(),x.sum()]
  }
