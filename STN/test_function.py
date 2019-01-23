from PIL import Image
import matplotlib.image as g
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf


# im = Image.open('C:/Users/caibo/Desktop/buff.jpg')
# im1 = g.imread('C:/Users/caibo/Desktop/buff.jpg')
# print(im1.shape)
# ima = np.array(im)
# print(ima.shape)
# plt.imshow(ima)
# plt.show()
# im.show()
def _meshgrid(height, width):
    print('begin--meshgrid')
    with tf.variable_scope('_meshgrid'):
        # This should be equivalent to:
        #  x_t, y_t = np.meshgrid(np.linspace(-1, 1, width),
        #                         np.linspace(-1, 1, height))
        #  ones = np.ones(np.prod(x_t.shape))
        #  grid = np.vstack([x_t.flatten(), y_t.flatten(), ones])

        x_t = tf.matmul(tf.ones(shape=tf.stack([height, 1])),
                        tf.transpose(tf.expand_dims(tf.linspace(-1.0, 1.0, width), 1), [1, 0]))
        print('meshgrid_x_t_ok')
        y_t = tf.matmul(tf.expand_dims(tf.linspace(-1.0, 1.0, height), 1),
                        tf.ones(shape=tf.stack([1, width])))
        print('meshgrid_y_t_ok')
        x_t_flat = tf.reshape(x_t, (1, -1))
        y_t_flat = tf.reshape(y_t, (1, -1))
        print('meshgrid_flat_t_ok')
        ones = tf.ones_like(x_t_flat)
        print('meshgrid_ones_ok')
        print(x_t_flat)
        print(y_t_flat)
        print(ones)

        grid = tf.concat([x_t_flat, y_t_flat, ones], 0)
        print('over_meshgrid')
        return grid


def meshgrid(height, width):
    x_t, y_t = np.meshgrid(np.linspace(-1, 1, width),
                           np.linspace(-1, 1, height))
    print(x_t.shape)
    ones = np.ones(np.prod(x_t.shape))
    grid = np.vstack([x_t.flatten(), y_t.flatten(), ones])

    return grid


grid = meshgrid(300, 400)
# test meshgrid
# x = np.arange(-5, 5, 0.1)
# y = np.arange(-5, 5, 0.1)
# xx, yy = np.meshgrid(x, y, sparse=True)
# z = np.sin(xx**2 + yy**2) / (xx**2 + yy**2)
# h = plt.contourf(x,y,z)
# plt.show()
print(grid.shape)