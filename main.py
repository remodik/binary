import time
from one import binary_search
from two import randomized_binary_search

data = sorted([i for i in range(100000)])
target = 99999

start_time = time.time()
result_classic = binary_search(data, target)
end_time = time.time()
print(f"Классический бинарный поиск: {result_classic}, время: {end_time - start_time:.6f} секунд")

start_time = time.time()
result_randomized = randomized_binary_search(data, target)
end_time = time.time()
print(f"Модифицированный бинарный поиск: {result_randomized}, время: {end_time - start_time:.6f} секунд")
