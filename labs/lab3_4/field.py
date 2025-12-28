def field(items, *args):
    assert len(args) > 0

    # Если передан один аргумент
    if len(args) == 1:
        key = args[0]
        for item in items:
            if key in item and item[key] is not None:
                yield item[key]
    # Если передано несколько аргументов
    else:
        for item in items:
            result = {}
            has_valid_field = False
            for key in args:
                if key in item and item[key] is not None:
                    result[key] = item[key]
                    has_valid_field = True

            if has_valid_field:
                yield result


if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
        {'title': None, 'price': 1000, 'color': 'white'},
        {'title': 'Стул', 'price': None, 'color': 'brown'}
    ]

    print("Test 1 - один аргумент:")
    for title in field(goods, 'title'):
        print(title)

    print("\nTest 2 - несколько аргументов:")
    for item in field(goods, 'title', 'price'):
        print(item)
