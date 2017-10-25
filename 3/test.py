# -*- coding: utf-8 -*-
# @Time    : 2017/10/20 13:00
# @Author  : lgt
# @Site    : 
# @File    : test.py
# @Software: PyCharm


import tensorflow as tf

sess = tf.InteractiveSession()
x = tf.placeholder(tf.float32, [None, 784])

W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x, W) + b)

