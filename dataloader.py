import numpy as np
import torch.utils.data as Data
from PIL import Image
import torch
import tools


class mnist_dataset(Data.Dataset):
    def __init__(self, train=True, dir='', transform=None, target_transform=None, noise_rate=0.5, split_per=0.9, random_seed=1,
                 noise_type='none', num_class=10):

        self.transform = transform
        self.target_transform = target_transform
        self.train = train
        original_images = np.load(dir + '/mnist/train_data.npy')
        original_labels = np.load(dir + '/mnist/train_label.npy')
        self.train_data, self.val_data, self.train_labels, self.val_labels = tools.dataset_split(original_images,
                                                                                                 original_labels,
                                                                                                 noise_rate, split_per,
                                                                                                 random_seed, noise_type, num_class)

        pass

    def __getitem__(self, index):

        if self.train:
            img, label = self.train_data[index], self.train_labels[index]
        else:
            img, label = self.val_data[index], self.val_labels[index]

        img = Image.fromarray(img)

        if self.transform is not None:
            img = self.transform(img)

        if self.target_transform is not None:
            label = self.target_transform(label)


        return img, label

    def __len__(self):

        if self.train:
            return len(self.train_data)

        else:
            return len(self.val_data)


class mnist_test_dataset(Data.Dataset):
    def __init__(self, dir='', transform=None, target_transform=None):

        self.transform = transform
        self.target_transform = target_transform

        self.test_data = np.load(dir + '/mnist/test_data.npy')
        self.test_labels = np.load(dir + '/mnist/test_label.npy')  # 0-9

    def __getitem__(self, index):

        img, label = self.test_data[index], self.test_labels[index]

        img = Image.fromarray(img)

        if self.transform is not None:
            img = self.transform(img)

        if self.target_transform is not None:
            label = self.target_transform(label)

        return img, label

    def __len__(self):
        return len(self.test_data)


class cifar10_dataset(Data.Dataset):
    def __init__(self, train=True, dir='', transform=None, target_transform=None, noise_rate=0.5, split_per=0.9, random_seed=1,
                 noise_type='none', num_class=10):

        self.transform = transform
        self.target_transform = target_transform
        self.train = train

        original_images = np.load(dir + '/cifar10/train_data.npy')
        original_labels = np.load(dir + '/cifar10/train_label.npy')
        self.train_data, self.val_data, self.train_labels, self.val_labels = tools.dataset_split(original_images,
                                                                                                 original_labels,
                                                                                                 noise_rate, split_per,
                                                                                                 random_seed, noise_type, num_class)
        if self.train:
            self.train_data = self.train_data.reshape((-1, 3, 32, 32))
            self.train_data = self.train_data.transpose((0, 2, 3, 1))

        else:
            self.val_data = self.val_data.reshape((-1, 3, 32, 32))
            self.val_data = self.val_data.transpose((0, 2, 3, 1))

    def __getitem__(self, index):

        if self.train:
            img, label = self.train_data[index], self.train_labels[index]

        else:
            img, label = self.val_data[index], self.val_labels[index]

        img = Image.fromarray(img)

        if self.transform is not None:
            img = self.transform(img)

        if self.target_transform is not None:
            label = self.target_transform(label)

        return img, label

    def __len__(self):

        if self.train:
            return len(self.train_data)

        else:
            return len(self.val_data)


class cifar10_test_dataset(Data.Dataset):
    def __init__(self, dir='', transform=None, target_transform=None):
        self.transform = transform
        self.target_transform = target_transform

        self.test_data = np.load(dir + '/cifar10/test_data.npy')
        self.test_labels = np.load(dir + '/cifar10/test_label.npy')
        self.test_data = self.test_data.reshape((10000, 3, 32, 32))
        self.test_data = self.test_data.transpose((0, 2, 3, 1))

    def __getitem__(self, index):

        img, label = self.test_data[index], self.test_labels[index]

        img = Image.fromarray(img)

        if self.transform is not None:
            img = self.transform(img)

        if self.target_transform is not None:
            label = self.target_transform(label)

        return img, label

    def __len__(self):
        return len(self.test_data)
