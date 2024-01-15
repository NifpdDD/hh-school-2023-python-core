import functools
import time

def log_and_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Executing {func.__name__} at {time.strftime('%Y-%m-%d %H:%M:%S')}...")
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} executed in {elapsed_time:.4f} seconds.")
        return result
    return wrapper
