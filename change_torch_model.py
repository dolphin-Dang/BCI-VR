import torch

old_model_name = ''
new_model_name = ''

state_dict = torch.load(old_model_name, map_location=torch.device('cpu'))	
torch.save(state_dict, new_model_name, _use_new_zipfile_serialization=False)
