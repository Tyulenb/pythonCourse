class Raises:
    def __init__(self, err):
        self.err = err
        self.expected = None
    def __enter__(self):
        return self
    def __exit__(self, err_type, val, traceback):
        if err_type == None:
            return False
        if issubclass(err_type, self.err):
            self.expected = val 
            return True
        return False

with Raises(ZeroDivisionError) as Err:
    1/0

print(Err.err)
print(Err.expected)
assert Err.err == ZeroDivisionError 
assert Err.expected == "1"

