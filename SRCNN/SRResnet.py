import torch
import torch.nn as nn

# 定义残差块
class ResidualBlock(nn.Module):
    def __init__(self, channels):
        super(ResidualBlock, self).__init__()
        self.conv1 = nn.Conv2d(channels, channels, kernel_size=3, stride=1, padding=1)
        self.relu = nn.ReLU(inplace=True)
        self.conv2 = nn.Conv2d(channels, channels, kernel_size=3, stride=1, padding=1)

    def forward(self, x):
        residual = x
        out = self.conv1(x)
        out = self.relu(out)
        out = self.conv2(out)
        out += residual
        return out

# 定义SRResNet模型
class SRResNet(nn.Module):
    def __init__(self, num_residual_blocks=16):
        super(SRResNet, self).__init__()

        # Initial convolutional layer
        self.conv1 = nn.Conv2d(3, 64, kernel_size=9, stride=1, padding=4)
        self.relu1 = nn.ReLU(inplace=True)

        # Residual blocks
        self.residual_blocks = nn.Sequential(*[ResidualBlock(64) for _ in range(num_residual_blocks)])

        # Second convolutional layer
        self.conv2 = nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=1)
        self.bn = nn.BatchNorm2d(64)

        # Upsampling layers
        self.upsample1 = nn.Upsample(scale_factor=2, mode='bilinear', align_corners=True)
        self.conv3 = nn.Conv2d(64, 256, kernel_size=3, stride=1, padding=1)
        self.relu2 = nn.ReLU(inplace=True)

#         self.upsample2 = nn.Upsample(scale_factor=2, mode='nearest')
        self.conv4 = nn.Conv2d(256, 256, kernel_size=3, stride=1, padding=1)
        self.relu3 = nn.ReLU(inplace=True)

        # Final output layer
        self.conv5 = nn.Conv2d(256, 3, kernel_size=9, stride=1, padding=4)

    def forward(self, x):
        x = self.upsample1(x)
        out1 = self.relu1(self.conv1(x))
        out = self.residual_blocks(out1)
        out2 = self.bn(self.conv2(out))
        out = out1 + out2
        out = self.relu3(self.conv3(out))
        # out = self.relu2(self.conv3(self.upsample1(out)))
        out = self.relu3(self.conv4(out))
        # out = self.relu3(self.conv4(self.upsample2(out)))
        out = self.conv5(out)

        return out

# # 创建SRResNet模型
# model = SRResNet(num_residual_blocks=16)

# # 打印模型概要信息
# print(model)