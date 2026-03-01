import torch
from model import PromoGuardModel 
from torch.utils.data import Dataset,DataLoader
import json
import numpy as np

class ClickstreamDataset(Dataset):
    def __init__(self, json_file):
        with open(json_file, 'r') as f:
            self.data = json.load(f)


    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]
        
        sequences = torch.tensor(item['intervals'], dtype=torch.float32)

        #labels: 0 for normal, 1 for bot
        label = torch.tensor(item['label'], dtype=torch.long)

        return sequences, label
    
if __name__ == "__main__":

    ensure_venv()

    dataset = ClickstreamDataset("traffic_data.json")
    dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

    for sequences, labels in dataloader:
        print("Batch of sequences shape:", {sequences.shape})
        print("Batch of labels shape:", {labels[:5]})