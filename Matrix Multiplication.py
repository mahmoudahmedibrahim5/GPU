import numpy
import time

SIZE = 5000

if __name__ == "__main__":
    A = numpy.random.rand(SIZE, SIZE)
    B = numpy.random.rand(SIZE, SIZE)
    
    start = time.time()
    C = (A * B + B * A)
    end = time.time()
    print(f"Time = {end - start}")
    