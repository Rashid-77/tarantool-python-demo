from db import Store


def main():
    store = Store()
    print('Start to populate tarantool with data')
    store.set('a', 'aaa')
    store.set('b', 'bbb')
    store.set('c', 'ccc')
    store.set('v', 'vvv')

    print('Start to get data from tarantool')
    assert('bbb' == store.get('b'))
    assert('vvv' == store.get('v'))
    assert('ccc' == store.get('c'))
    assert('aaa' == store.get('a'))
    print('all ok')


if __name__ == "__main__":
    main()