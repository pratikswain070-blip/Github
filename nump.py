# import numpy

# arr=numpy.array ([1, 2, 3, 4, 5])
# print(arr)


# import numpy as bp

# arr=bp.array ([1, 2, 3, 4, 5])
# print(arr)

# import numpy

# arr=numpy.array ([1, 2, 3, 4, 5,6,7])
# print(arr[1:5])

# import numpy
# arr=numpy.array ([1, 2, 3])
# print(arr.dtype)

# import numpy
# arr=numpy.array(['apple', 'banana', 'cherry'])
# print(arr.dtype)

# import numpy
# arr=numpy.array (['apple', 'banana', 'cherry'])
# print(arr.__len__())

# import numpy
# arr=numpy.array ([1,2,4,5,6,7])
# print(arr.__len__())

# import numpy as nu
# arr=nu.array([1,2,3,4],dtype='i8')
# print(arr.dtype)                

# import numpy as nu
# arr=nu.array(['abnnnnn','245','35'], dtype='U2')
# print(arr.dtype)
# print(arr)

# import numpy as np
# arr=np.array([1.2,2.1,3.5])
# newarr=arr.astype('i')
# print(newarr)
# print(newarr.dtype)


# import numpy as np
# arr=np.array([1.2,2.1,3.5])
# print(arr.dtype)
# print(arr)

# import numpy as np
# arr=np.array([1,0,3,0])
# newarr=arr.astype('bool')
# print(newarr)
# print(newarr.dtype)

# import numpy as np
# arr=np.array([1,2,3,4,5])
# x=arr.copy()
# arr[0]=42
# print(arr)
# print(x)

# import numpy as np
# arr=np.array([1,2,3,4,5])
# x=arr.view()
# arr[0]=42
# print(arr)
# print(x)

# import numpy as np
# arr=np.array([1,2,3,4,5])
# x=arr.view()
# x[0]=31
# print(arr)
# print(x)

# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newarr=arr.reshape(6,2)
# print(newarr)

import numpy as np
a=np.arange(0,9).reshape(3,3)
print(a[1,:]) 