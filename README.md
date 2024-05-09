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
  <div align="left" >
    <img width="50%" height="100%" alt="welcome to my profile!" src="https://github.com/mahmoudahmedibrahim5/GPU/blob/main/Screenshots/CPU_1.png">
  </div>
  </br>
  <div align="left" >
    <img width="50%" height="200%" alt="welcome to my profile!" src="https://github.com/mahmoudahmedibrahim5/GPU/blob/main/Screenshots/GPU_1.png">
  </div>
* Size = 5,000
  <div align="left" >
    <img width="50%" height="100%" alt="welcome to my profile!" src="https://github.com/mahmoudahmedibrahim5/GPU/blob/main/Screenshots/CPU_5.png">
  </div>
  </br>
  <div align="left" >
    <img width="50%" height="200%" alt="welcome to my profile!" src="https://github.com/mahmoudahmedibrahim5/GPU/blob/main/Screenshots/GPU_5.png">
  </div>
* Size = 10,000
  <div align="left" >
    <img width="50%" height="100%" alt="welcome to my profile!" src="https://github.com/mahmoudahmedibrahim5/GPU/blob/main/Screenshots/CPU_10.png">
  </div>
  </br>
  <div align="left" >
    <img width="50%" height="200%" alt="welcome to my profile!" src="https://github.com/mahmoudahmedibrahim5/GPU/blob/main/Screenshots/GPU_10.png">
  </div>

</br>

## Observation
* We notice that at sizes equal to 5,000 and 10,000 the code using GPU has finished faster than the one using CPU.
* We notice that at a size equal to 1,000 the code using CPU has finished faster than the one using GPU.

</br>

## Conclusion
* We can conclude that GPU performance is much better than CPU performance.
* But at small sizes, CPU may be better as there is a time taken to move the data from CPU to GPU and this time is bigger than the saved time in the calculation itself.

