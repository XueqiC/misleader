# This part is borrowed from https://github.com/huawei-noah/Data-Efficient-Model-Compression

import torch.nn as nn
import torch


class LeNet5(nn.Module):

    def __init__(self):
        super(LeNet5, self).__init__()

        self.conv1 = nn.Conv2d(1, 6, kernel_size=(5, 5))
        self.relu1 = nn.ReLU()
        self.maxpool1 = nn.MaxPool2d(kernel_size=(2, 2), stride=2)
        self.conv2 = nn.Conv2d(6, 16, kernel_size=(5, 5))
        self.relu2 = nn.ReLU()
        self.maxpool2 = nn.MaxPool2d(kernel_size=(2, 2), stride=2)
        self.conv3 = nn.Conv2d(16, 120, kernel_size=(5, 5))
        self.relu3 = nn.ReLU()
        self.fc1 = nn.Linear(120, 84)
        self.relu4 = nn.ReLU()
        self.fc2 = nn.Linear(84, 10)

    def forward(self, img, out_feature=False):
        output = self.conv1(img)
        output = self.relu1(output)
        output = self.maxpool1(output)
        output = self.conv2(output)
        output = self.relu2(output)
        output = self.maxpool2(output)
        output = self.conv3(output)
        output = self.relu3(output)
        feature = output.view(-1, 120)
        output = self.fc1(feature)
        output = self.relu4(output)
        output = self.fc2(output)
        if out_feature == False:
            return output
        else:
            return output,feature
    

# class LeNet5Half(nn.Module):

#     def __init__(self):
#         super(LeNet5Half, self).__init__()

#         self.conv1 = nn.Conv2d(3, 3, kernel_size=(5, 5))
#         self.relu1 = nn.ReLU()
#         self.maxpool1 = nn.MaxPool2d(kernel_size=(2, 2), stride=2)
#         self.conv2 = nn.Conv2d(3, 8, kernel_size=(5, 5))
#         self.relu2 = nn.ReLU()
#         self.maxpool2 = nn.MaxPool2d(kernel_size=(2, 2), stride=2)
#         self.conv3 = nn.Conv2d(8, 60, kernel_size=(5, 5))
#         self.relu3 = nn.ReLU()
#         self.fc1 = nn.Linear(60, 42)
#         self.relu4 = nn.ReLU()
#         self.fc2 = nn.Linear(42, 10)

#     def forward(self, img, out_feature=False):
#         output = self.conv1(img)
#         output = self.relu1(output)
#         output = self.maxpool1(output)
#         output = self.conv2(output)
#         output = self.relu2(output)
#         output = self.maxpool2(output)
#         output = self.conv3(output)
#         output = self.relu3(output)
#         feature = output.view(-1, 60)
#         output = self.fc1(feature)
#         output = self.relu4(output)
#         output = self.fc2(output)
#         if out_feature == False:
#             return output
#         else:
#             return output,feature

class LeNet5Half(nn.Module):
    def __init__(self):
        super(LeNet5Half, self).__init__()

        self.conv1 = nn.Conv2d(1, 3, kernel_size=5)  # MNIST: 1 input channel
        self.relu1 = nn.ReLU()
        self.maxpool1 = nn.MaxPool2d(kernel_size=2, stride=2)

        self.conv2 = nn.Conv2d(3, 8, kernel_size=5)
        self.relu2 = nn.ReLU()
        self.maxpool2 = nn.MaxPool2d(kernel_size=2, stride=2)

        self.conv3 = nn.Conv2d(8, 60, kernel_size=5)
        self.relu3 = nn.ReLU()

        self.fc1 = nn.Linear(60, 42)
        self.relu4 = nn.ReLU()
        self.fc2 = nn.Linear(42, 10)

    def forward(self, img, out_feature=False):
        output = self.conv1(img)
        output = self.relu1(output)
        output = self.maxpool1(output)

        output = self.conv2(output)
        output = self.relu2(output)
        output = self.maxpool2(output)

        output = self.conv3(output)
        output = self.relu3(output)

        feature = output.view(-1, 60)
        output = self.fc1(feature)
        output = self.relu4(output)
        output = self.fc2(output)

        if out_feature:
            return output, feature
        else:
            return output
        

import torch
import torch.nn as nn

class LeNet5Fifth(nn.Module):
    def __init__(self):
        super(LeNet5Fifth, self).__init__()

        self.conv1 = nn.Conv2d(1, 4, kernel_size=5)      # 1 input channel → 4
        self.relu1 = nn.ReLU()
        self.maxpool1 = nn.MaxPool2d(2, 2)

        self.conv2 = nn.Conv2d(4, 10, kernel_size=5)     # 4 → 10
        self.relu2 = nn.ReLU()
        self.maxpool2 = nn.MaxPool2d(2, 2)

        self.conv3 = nn.Conv2d(10, 30, kernel_size=5)    # 10 → 30
        self.relu3 = nn.ReLU()

        self.fc1 = nn.Linear(30, 30)                     # flatten from conv3
        self.relu4 = nn.ReLU()
        self.fc2 = nn.Linear(30, 10)

    def forward(self, img, out_feature=False):
        output = self.conv1(img)
        output = self.relu1(output)
        output = self.maxpool1(output)

        output = self.conv2(output)
        output = self.relu2(output)
        output = self.maxpool2(output)

        output = self.conv3(output)
        output = self.relu3(output)

        feature = output.view(-1, 30)  # flattened from conv3 output: [batch_size, 30]
        output = self.fc1(feature)
        output = self.relu4(output)
        output = self.fc2(output)

        return (output, feature) if out_feature else output



# class LeNet5Fifth(nn.Module):

#     def __init__(self):
#         super(LeNet5Fifth, self).__init__()

#         self.conv1 = nn.Conv2d(3, 4, kernel_size=(5, 5))
#         self.relu1 = nn.ReLU()
#         self.maxpool1 = nn.MaxPool2d(kernel_size=(2, 2), stride=2)
#         self.conv2 = nn.Conv2d(4, 10, kernel_size=(5, 5))
#         self.relu2 = nn.ReLU()
#         self.maxpool2 = nn.MaxPool2d(kernel_size=(2, 2), stride=2)
#         self.fc1 = nn.Linear(5*5*10, 40)
#         self.relu4 = nn.ReLU()
#         self.fc2 = nn.Linear(40, 10)

#     def forward(self, img, out_feature=False):
#         output = self.conv1(img)
#         output = self.relu1(output)
#         output = self.maxpool1(output)
#         output = self.conv2(output)
#         output = self.relu2(output)
#         output = self.maxpool2(output)

#         feature = output.view(-1, 5*5*10)
#         output = self.fc1(feature)
#         output = self.relu4(output)
#         output = self.fc2(output)
        
#         return output 


class Encoder(nn.Module):

    def __init__(self):
        super(Encoder, self).__init__()

        self.conv1 = nn.Conv2d(3, 4, kernel_size=(5, 5))
        self.relu1 = nn.ReLU()
        self.maxpool1 = nn.MaxPool2d(kernel_size=(2, 2), stride=2)
        self.conv2 = nn.Conv2d(4, 10, kernel_size=(5, 5))
        self.relu2 = nn.ReLU()
        self.maxpool2 = nn.MaxPool2d(kernel_size=(2, 2), stride=2)
        self.fc1 = nn.Linear(5*5*10, 1)

    def forward(self, img, out_feature=False):
        output = self.conv1(img)
        output = self.relu1(output)
        output = self.maxpool1(output)
        output = self.conv2(output)
        output = self.relu2(output)
        output = self.maxpool2(output)

        feature = output.view(-1, 5*5*10)
        output = self.fc1(feature)

        return output 