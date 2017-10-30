# -*- coding: utf-8 -*-
# @Time    : 2017/10/20 13:00
# @Author  : lgt
# @Site    : 
# @File    : softmax.py
# @Software: PyCharm

import tensorflow.examples.tutorials.mnist.input_data as input_data
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

mnist = input_data.read_data_sets('..data//MNIST_data/', one_hot=True)

print(mnist.train.images.shape, mnist.train.labels.shape)
print(mnist.test.images.shape, mnist.test.labels.shape)
print(mnist.validation.images.shape, mnist.validation.labels.shape)

trainImg = mnist.train.images
trainLable = mnist.train.labels
testImg = mnist.test.images
testLable = mnist.test.labels

nsample = 5
ranidix = np.random.randint(trainImg.shape[0], size=nsample)

for i in ranidix:
    currImg = np.reshape(trainImg[i, :], (28, 28))
    curLable = np.argmax(trainLable[i, :])
    plt.imshow(currImg, cmap = plt.get_cmap('gray'))
    plt.title("" + str(i) + "th Date, Lable is " + str(curLable))
    plt.show()
    print("" + str(i) + "th Date, Lable is " + str(curLable))
    