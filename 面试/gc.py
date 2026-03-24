from venv import logger

import gc
import objgraph

# a = 1
# b = 2
#
# gc.collect()
# objgraph.show_most_common_types(limit=50)
#
import tracemalloc

tracemalloc.start(25)
global snapshot
snapshot = tracemalloc.take_snapshot()
gc.collect()
snapshot1 = tracemalloc.take_snapshot()
top_stats = snapshot1.compare_to(snapshot, 'lineno')
logger.warning("[ Top 20 differences ]")
for stat in top_stats[:20]:
    if stat.size_diff < 0:
        continue
    logger.warning(stat)
snapshot = tracemalloc.take_snapshot()
