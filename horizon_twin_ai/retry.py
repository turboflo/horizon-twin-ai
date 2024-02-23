import time
import random
from functools import wraps


def retry(
    delay=1,
    tries=3,
    exceptions=(Exception,),
    exponential_backoff=False,
    max_delay=None,
    exponential_factor=2,
    jitter=False,
):
    """
    Decorator to retry a function if an exception occurs, with enhanced logging, maximum delay, jitter, and customizable exponential factor.
    Parameters:
    - delay: Time to wait between retries.
    - tries: Maximum number of retries.
    - exceptions: Tuple of exceptions to catch.
    - exponential_backoff: If True, will increase the delay after each failed try using the exponential factor.
    - max_delay: Maximum delay limit for exponential backoff. None means no limit.
    - exponential_factor: The factor to multiply the delay by on each retry when exponential backoff is True.
    - jitter: If True, adds random jitter to the delays to help spread out retry attempts.
    Usage:
    @retry(delay=2, tries=5, exceptions=(ValueError, KeyError), max_delay=10, jitter=True)
    def my_function():
        ...
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay

            for attempt in range(0, tries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == tries:
                        raise
                    else:
                        if exponential_backoff:
                            next_delay = (
                                min(current_delay * exponential_factor, max_delay)
                                if max_delay
                                else current_delay * exponential_factor
                            )
                        else:
                            next_delay = current_delay
                        if jitter:
                            next_delay = next_delay / 2 + random.uniform(
                                0, next_delay / 2
                            )
                        time.sleep(next_delay)
                        if exponential_backoff:
                            current_delay = next_delay

        return wrapper

    return decorator
