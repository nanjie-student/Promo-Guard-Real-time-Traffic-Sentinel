import torch
import torch.nn as nn

class PromoGuardModel(nn.Module):
    def __init__(self, input_size=1, hidden_size=64, num_layers=2, nhead=4):
        super(PromoGuardModel, self).__init__()
        self.embedding = nn.Linear(input_size, hidden_size)
        
        # Transformer Encoder 层
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=hidden_size, 
            nhead=nhead, 
            batch_first=True
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        self.fc = nn.Linear(hidden_size, 2) # 二分类：人 or 机器人

    def forward(self, x):
        # x shape: [batch_size, 50] -> [batch_size, 50, 1]
        x = x.unsqueeze(-1) 
        x = self.embedding(x)
        x = self.transformer(x)
        x = x.mean(dim=1) # 聚合特征
        return self.fc(x)