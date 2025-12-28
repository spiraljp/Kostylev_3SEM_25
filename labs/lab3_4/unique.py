class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.seen = set()
        self.ignore_case = kwargs.get('ignore_case', False)
        self.iterator = self._unique_generator()

    def _unique_generator(self):
        for item in self.items:
            # Для строк с учетом регистра
            if isinstance(item, str) and self.ignore_case:
                key = item.lower()
            else:
                key = item

            if key not in self.seen:
                self.seen.add(key)
                yield item

    def __next__(self):
        return next(self.iterator)

    def __iter__(self):
        return self


if __name__ == '__main__':
    print("Test 1 - числа:")
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    for item in Unique(data1):
        print(item, end=' ')
    print()

    print("\nTest 2 - строки без ignore_case:")
    data2 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    for item in Unique(data2):
        print(item, end=' ')
    print()

    print("\nTest 3 - строки с ignore_case=True:")
    for item in Unique(data2, ignore_case=True):
        print(item, end=' ')
    print()
