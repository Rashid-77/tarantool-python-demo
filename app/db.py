import tarantool


class Store:
    space = 'link'
    def __init__(self, url: str = 'tarantool', port: int = 3301):
        self.connection = tarantool.connect(url, port)
        self.link_space = self.connection.space('link')

    def get_space(self, space_name: str):
        return self.connection.space(space_name)

    def get(self, key):
        response = self.connection.select(self.space, key)
        return response.data[0][1]

    def set(self, key, value):
        self.connection.replace(self.space, (key, value))
