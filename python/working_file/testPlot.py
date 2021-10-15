import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

MyArray = np.array([[0,0,0,0,1,0,0,0,0],
                    [0,0,1,1,1,1,1,0,0],
                    [0,0,1,0,1,0,1,0,0],
                    [0,0,1,1,1,1,1,0,0],
                    [0,0,0,1,0,1,0,0,0],
                    [0,0,0,1,0,1,0,0,0]])

print(MyArray)
plt.imshow(MyArray)
plt.show()