import tensorflow as tf
import numpy as np
import time
import os

SIZE = 5000

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

if __name__ == "__main__":
    # Generate random matrices
    A = np.random.rand(SIZE, SIZE)
    B = np.random.rand(SIZE, SIZE)
    
    # Convert numpy arrays to TensorFlow tensors
    A_tf = tf.convert_to_tensor(A, dtype=tf.float32)
    B_tf = tf.convert_to_tensor(B, dtype=tf.float32)
    
    # Define the TensorFlow computation graph
    @tf.function
    def matrix_operation():
        return tf.math.add(tf.math.multiply(A_tf, B_tf), tf.math.multiply(B_tf, A_tf))
    
    # Run the computation graph on GPU
    with tf.device('/GPU:0'):
        start = time.time()
        C_tf = matrix_operation()
        end = time.time()
    
    # Print the execution time
    print(f"Time = {end - start}")
