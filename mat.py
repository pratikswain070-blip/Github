# import matplotlib 
# print(matplotlib.__version__)

# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([1,8])
# ypoints = np.array([3,10])
# plt.plot(xpoints, ypoints)
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# ypoints = np.array([3,8,1,10,4,23,6])
# plt.plot(ypoints, marker = 'o')
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# ypoints = np.array([3,8,1,10,4,23,6])
# plt.plot(ypoints, linestyle = 'dotted', marker = 'o', color = 'r')
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# x = np.array([80,85,90,95,100,105,110,115])
# y = np.array([240,250,260,270,280,290,300,310])
# plt.plot(x, y)
# plt.title("Sports Match Data")
# plt.xlabel('Average Pulse Rate')
# plt.ylabel('Calorie Burnage')

# plt.grid
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array(["A","B","C","D"])
# y=np.array([3,8,1,10])

# plt.bar(x,y)
# plt.show()


import matplotlib.pyplot as plt
import numpy as np
y=np.array([35,25,25,15])
mylabels=["Apples","Bananas","Cherries","Dates"]
mycolors =["red","yellow","pink","brown"]
plt.pie(y, labels = mylabels,colors=mycolors)
plt.show()
