# maths-for-ml
Python powered maths operations used in machine learning.

### Matrix Multiplication in NumPy
In NumPy, you can perform matrix multiplication using np.dot, np.matmul, or the @ operator. 
NumPy follows these rules:

- **1D arrays:** When passing two 1D arrays to np.dot or np.matmul, it performs the dot product and returns a scalar.
- **2D arrays:** For two 2D arrays, NumPy performs regular matrix multiplication.
- **Broadcasting:** NumPy also supports broadcasting for certain matrix operations, which allows for more flexibility, especially with higher-dimensional arrays.

### Linear Transformation 
A linear transformation in an nn-dimensional space can be represented by a matrix AA. Given a vector v⃗v
, the transformation is applied by multiplying AA with v⃗v:
      w⃗=A⋅v⃗
where: 
- v⃗v  is the original vector (e.g., a data point in an ML dataset). 
- AA is the transformation matrix.
- w⃗w is the transformed vector.


#### Note
In case you are unable to download any python package, try following:
- Ensure pip is upto date, python3 -m pip install --upgrade pip
- Disable proxy:
      -     unset http_proxy
      -     unset https_proxy

