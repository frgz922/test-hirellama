# timer.py

import time

class TimerError(Exception):
    """Custom exception trow errors related to Timer class"""

class Timer:
    def __init__(self):
        self._start = None

    def start(self):
        if self._start is not None:
            raise TimerError(f"Timer running. Use .stop() to stop it")

        self._start = time.perf_counter()

    def stop(self):
        if self._start is None:
            raise TimerError(f"Timer not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start
        self._start = None
        print(f"Function ran in: {elapsed_time:0.4f} seconds")