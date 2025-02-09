# 练习 1: 斐波那契数列生成器
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# 练习 2: 无限生成器
def count_up(start):
    while True:
        yield start
        start += 1

# 练习 3: 生成器管道
def double_values(iterable):
    for value in iterable:
        yield value * 2

def filter_even(iterable):
    for value in iterable:
        if value % 2 == 0:
            yield value

def first_n(iterable, n):
    iterator = iter(iterable)
    for _ in range(n):
        yield next(iterator)

# 练习 4: 无限序列的采样
def sample_infinite(sequence, n):
    iterator = iter(sequence)
    for _ in range(n):
        yield next(iterator)

# 练习 5: 日历生成器
def days_of_week():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    while True:
        for day in days:
            yield day

# 练习 6: 压缩生成器
def compress(iterable, selectors):
    iterator = iter(iterable)
    for select in selectors:
        value = next(iterator)
        if select:
            yield value

# 练习 7: 生成器的递归使用
def flatten(iterable):
    for item in iterable:
        if isinstance(item, (list, tuple)):
            yield from flatten(item)
        else:
            yield item

# 练习 8: 无限斐波那契数列
def infinite_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 练习 9: 生成器表达式
gen = (x for x in range(1, 1001) if x % 7 == 0)

# 测试代码
if __name__ == "__main__":
    print("斐波那契数列生成器:")
    print([x for x in fibonacci(10)])

    print("\n无限生成器:")
    gen = count_up(5)
    print([next(gen) for _ in range(10)])

    print("\n生成器管道:")
    numbers = range(1, 21)
    pipeline = first_n(filter_even(double_values(numbers)), 5)
    print(list(pipeline))  # 输出应为 [4, 8, 12, 16, 20]

    print("\n无限序列的采样:")
    gen = sample_infinite(count_up(1), 10)
    print(list(gen))  # 输出应为 [1, 2, 3, ..., 10]

    print("\n日历生成器:")
    gen = days_of_week()
    print([next(gen) for _ in range(10)])  # 输出应为 ['Monday', 'Tuesday', ..., 'Wednesday']

    print("\n压缩生成器:")
    data = 'ABCDEF'
    selectors = [1, 0, 1, 0, 0, 1]
    result = compress(data, selectors)
    print(list(result))  # 输出应为 ['A', 'C', 'F']

    print("\n生成器的递归使用:")
    nested_list = [1, [2, [3, 4]], 5]
    print(list(flatten(nested_list)))  # 输出应为 [1, 2, 3, 4, 5]

    print("\n无限斐波那契数列:")
    gen = infinite_fibonacci()
    print([next(gen) for _ in range(10)])  # 输出应为 [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    print("\n生成器表达式:")
    print([next(gen) for _ in range(5)])  # 输出应为 [7, 14, 21, 28, 35]
