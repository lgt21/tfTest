# -*- coding: utf-8 -*-
# @Time    : 2017/10/24 10:47
# @Author  : lgt
# @Site    : 
# @File    : softmax_test.py
# @Software: PyCharm



from tensorflow.examples.tutorials.mnist import input_data
mnist=input_data.read_data_sets('MNIST_data/',one_hot=True)

print(mnist.train.images.shape,mnist.train.labels.shape)
print(mnist.test.images.shape,mnist.test.labels.shape)
print(mnist.validation.images.shape,mnist.validation.labels.shape)
import tensorflow as tf
sess=tf.InteractiveSession()

#x为神经元的输入，比如一个照片28*28，就输入784个点的灰度值进去，并且是0-1之间用小数表示
x=tf.placeholder(tf.float32,[None,784])

#w为神经元的权重
W=tf.Variable(tf.zeros([784,10]))

#b为神经元的偏移值
b=tf.Variable(tf.zeros([10]))
#y为神经元输出，根据x的输入，计算出对应0-9是那个数值
y=tf.nn.softmax(tf.matmul(x,W)+b)
#y_监督数据的输出层
y_=tf.placeholder(tf.float32,[None,10])
#cross_entropy计算误差
cross_entropy=tf.reduce_mean(-tf.reduce_sum(y_*tf.log(y), reduction_indices=[1]))
#梯度下降训练设置
train_step=tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

tf.global_variables_initializer().run()
#训练1000次，每次100个数据，数据抽取采用随机的方式。
for i in range(550):
    #抽取100个图片进行训练
   batch_xs,batch_ys=mnist.train.next_batch(100)
   train_step.run({x:batch_xs,y_:batch_ys})
correct_prediction=tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
#计算训练集通过模型后的识别准确率
accuracy=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
print(accuracy.eval({x:mnist.test.images,y_:mnist.test.labels}))