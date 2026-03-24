import tracemalloc
import numpy as np

tracemalloc.start()


snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[ Top 10 ]")

for stat in top_stats[:10]:
    print(stat)
