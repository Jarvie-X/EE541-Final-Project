from torch.utils.data import Dataset
from torchvision import transforms
from PIL import Image
import os
from torchvision.transforms.functional import resize

class CustomDataset(Dataset):
    def __init__(self, root_dir, phase, target_size, transform=None):
        self.root_dir = root_dir
        self.phase = phase
        self.target_size = target_size
        self.transform = transform

        self.hr_folder = os.path.join(root_dir, phase, 'HR')
        self.lr_folder = os.path.join(root_dir, phase, 'LR')
        self.srcnn_folder = os.path.join(root_dir, phase, 'SRCNN')
  
        self.hr_images = os.listdir(self.hr_folder)
        self.hr_images.sort()
        self.lr_images = os.listdir(self.lr_folder)
        self.lr_images.sort()

        self.srcnn_images = os.listdir(self.srcnn_folder)
        self.srcnn_images.sort()

    def __len__(self):
        return len(self.hr_images)

    def __getitem__(self, idx):     
        img_name_hr = os.path.join(self.hr_folder, self.hr_images[idx])
        img_name_lr = os.path.join(self.lr_folder, self.lr_images[idx])
        img_name_srcnn = os.path.join(self.srcnn_folder, self.srcnn_images[idx])

        image_hr = Image.open(img_name_hr).convert('RGB')
        image_lr = Image.open(img_name_lr).convert('RGB')
        image_srcnn = Image.open(img_name_srcnn).convert('RGB')
        
        half_size = tuple(x // 2 for x in self.target_size)
        image_hr = resize(image_hr, self.target_size)
        image_lr = resize(image_lr, half_size)

        if self.transform:
            image_hr = self.transform(image_hr)
            image_lr = self.transform(image_lr)
            image_srcnn = self.transform(image_srcnn)

        return image_lr, image_hr, image_srcnn

root_dir = './data'

target_size = (256, 256)

transform = transforms.Compose([
    transforms.ToTensor(),
    # transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

train_dataset = CustomDataset(root_dir=root_dir, phase='train', target_size=target_size, transform=transform)
val_dataset = CustomDataset(root_dir=root_dir, phase='val', target_size=target_size, transform=transform)
test_dataset = CustomDataset(root_dir=root_dir, phase='test', target_size=target_size, transform=transform)