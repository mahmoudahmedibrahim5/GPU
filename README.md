<div align="center" >
  
  # GPU
</div>

## Introduction
* This program computes matrix C = (A x B + B x A), where A, B, and C are square matrices of the same large size. 
* We will compare the performance of CPU and GPU at different sizes.
* We will use numpy library to calculate matrices.
* We will use Tensorflow library to use the GPU

</br>

## Test Cases

* Size = 1,000
* Size = 5,000
* Size = 10,000

</br>

## Observation
* We notice that at sizes equal to 5,000 and 10,000 the code using GPU has finished faster than the one using CPU.
* We notice that at a size equal to 1,000 the code using CPU has finished faster than the one using GPU.

</br>

## Conclusion
* We can conclude that GPU performance is much better than CPU performance.
* But at small sizes, CPU may be better as there is a time taken to move the data from CPU to GPU and this time is bigger than the saved time in the calculation itself.

