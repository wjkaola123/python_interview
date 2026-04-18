class RecentCounter:

    def __init__(self):
        self._history_calls = []

    def ping(self, t: int) -> int:
        self._history_calls.append(t)

        begin = t - 3000
        end = t
        cnt = 0
        for c in self._history_calls:
            if c >= begin and c <= end:
                cnt += 1

        return cnt
