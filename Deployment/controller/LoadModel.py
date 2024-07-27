import pickle

def LoadModel(file_path: str):
  with open(file_path, 'rb') as f:
    model = pickle.load(f)
    
  return model