def add_to_70(n):
    print("long time...")
    return n + 70


def memoized_add_to_70():
    cache = {}

    def closure_function(n):
        nonlocal cache
        if cache.get(n) is None:
            print("long time...")
            cache[n] = n + 80
        return cache[n]

    return closure_function


if __name__ == "__main__":
    # Creating a function object
    memoized = memoized_add_to_70()
    # Runs calculation
    print(memoized(5))
    # Uses cache
    print(memoized(5))
    print(memoized(5))