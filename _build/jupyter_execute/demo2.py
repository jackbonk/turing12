#!/usr/bin/env python
# coding: utf-8

# # Demo notebook

# We can also create parts of our Jupyter Book based on Jupyter Notebooks.

# Let's simulate data for two conditions and print their first ten rows:

# In[1]:


import numpy as np

cond_1 = np.random.rand(100)
print(f'Condition 1 = {cond_1[:10]}')

cond_2 = cond_1 + (np.random.rand(100))
print(f'Condition 2 = {cond_2[:10]}')


# We can also display in our Jupyter Book more complex datastructures, like pandas dataframes:

# In[2]:


import pandas as pd

df = pd.DataFrame(
    {'condition_1': cond_1, 'condition_2': cond_2}, 
    index=np.arange(100)
)

df[:10]


# And of course, we can display plots as well!

# In[3]:


import matplotlib.pyplot as plt

plt.scatter(cond_1, cond_2, alpha=.6)
plt.xlabel('condition 1')
plt.ylabel('condition 2')
plt.title('Scatterplot')
plt.show()


# In[4]:


import ipywidgets as widgets
widgets.IntSlider()

from IPython.display import display
w = widgets.IntSlider()
display(w)


# In[5]:


a = widgets.FloatText()
b = widgets.FloatSlider()
display(a,b)

mylink = widgets.jslink((a, 'value'), (b, 'value'))


# In[6]:


#slider.close()


# In[7]:


from ipywidgets import Layout, Button, Box

items_layout = Layout( width='auto')     # override the default width of the button to 'auto' to let the button grow

box_layout = Layout(display='flex',
                    flex_flow='column',
                    align_items='stretch',
                    border='solid',
                    width='50%')

words = ['correct', 'horse', 'battery', 'staple']
items = [Button(description=word, layout=items_layout, button_style='danger') for word in words]
box = Box(children=items, layout=box_layout)
box


# In[ ]:




