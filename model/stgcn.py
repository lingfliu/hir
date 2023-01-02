import torch
import torch.nn as nn
import torch.nn.functional as F
class StGcn(nn.Module):
    def __init__(self):
        super(StGcn, self).__init__()
        self.device = torch.device('cuda:0' if torch.cuda.device_count() >= 1 else 'cpu')
        self.criterion = nn.CrossEntropyLoss
        self.net_size = sum(p.numel() for p in self.parameters())

    def loss(self, input):
        y = self.forward(input)
        l = F.log_softmax()
        return l

    def forward(self, input):
        input_size = input.shape[-1]
        proto = self.flatten(input)
        o = []

        return o, proto

    def summariz(self):
        output = str(self)
        output += '\n'
        output += 'number of param {}'.format(self.net_size)
        return output
