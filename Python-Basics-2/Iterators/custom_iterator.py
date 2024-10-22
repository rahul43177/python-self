class PowerTwo:
    def __init__(self, max=0):
        self.max = max
        print(f"[__init__] Initialized with max = {self.max}")
    
    def __iter__(self):
        self.n = 0
        print(f"[__iter__] Iterator initialized, n set to {self.n}")
        return self
    
    def __next__(self):
        print(f"[__next__] Current n = {self.n}, max = {self.max}")
        if self.n <= self.max:
            result = 2 ** self.n
            print(f"[__next__] Calculating 2^{self.n} = {result}")
            self.n += 1
            print(f"[__next__] Incrementing n to {self.n}")
            return result
        else:
            print("[__next__] Reached max, raising StopIteration")
            raise StopIteration

# Let's run it step by step
print("\n=== Creating PowerTwo object ===")
power = PowerTwo(3)

print("\n=== Getting iterator ===")
iterator = iter(power)  # This calls __iter__

print("\n=== First next() call ===")
print("Result:", next(iterator))

print("\n=== Second next() call ===")
print("Result:", next(iterator))

print("\n=== Third next() call ===")
print("Result:", next(iterator))

print("\n=== Fourth next() call ===")
print("Result:", next(iterator))

print("\n=== Fifth next() call ===")
try:
    print("Result:", next(iterator))
except StopIteration:
    print("Caught StopIteration exception")