
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from keras.utils import np_utils
np.random.seed(10)


# In[11]:


import keras.backend.tensorflow_backend as KTF #keras中的命令（P56：Using tensorFlow backend.）没有正确运行--疑问1


# In[8]:


from keras.datasets import mnist


# In[10]:


(X_train_image,y_trsin_label),(X_test_image,y_test_label)=mnist.load_data()

