def add(a, b):
    """Return sum of a and b

    >>> add(1,2)
    3
    """
    return a + b


def mult(a, b):
    """Return product of a and b"""
    return a * b  # no test for this line


def div(a, b):
    """Return a divided by b and Raise exception for b==0"""
    if not b:
        raise ValueError("Cannot divide by zero!")
    return a / b


def filesum(f):
    """Return sum of all numbers in file f"""
    return sum(int(l.strip()) for l in f)


def fileconcat(f):
    """Return concatination of  all numbers in file f"""
    return int("".join(l.strip() for l in f))


def eps(machine):
    """Return numeric tolerance for machine"""
    return 1e-5 if machine == "x86" else 1e-8


def approx_eq(a, b):
    """Return true if a and b are approximately equal"""
    return abs(a - b) < eps("x86")


if __name__ == "__main__":  # pragma: no cover
    print("add:", add(2, 3))
    print("div:", div(4, 2))
