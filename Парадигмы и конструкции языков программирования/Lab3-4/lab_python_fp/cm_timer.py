import time
from contextlib import contextmanager

class cm_timer_1:
    import time
    def __enter__(self):
        self.t = time.clock_gettime(0)
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.t = time.clock_gettime(0) - self.t
        print("time:",self.t)

@contextmanager
def cm_timer_2():
    import time
    try:
        t = time.clock_gettime(0)
        yield
    finally:
        t = time.clock_gettime(0) - t
        print("time:",t)

if __name__ == '__main__':
    with cm_timer_1():
        time.sleep(1)

    with cm_timer_2():
        time.sleep(1.2)

