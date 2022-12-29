import unittest


class HashMap:
    def __init__(self, size: int = 100):
        self._size = size
        self._keys = set()
        self._values = [None for _ in range(self._size)]

    def set(self, key, value):
        self._keys.add(key)
        hs = self._hash(key)
        if not self._values[hs]:
            self._values[hs] = value
        return self

    def get(self, key):
        return self._values[self._hash(key)]

    def update(self, key, value):
        hs = self._hash(key)
        if not self._values:
            self.set(key, value)
        else:
            self._values[hs] = value
        return self

    def delete(self, key):
        hs = self._hash(key)
        if self._values[hs] is None:
            raise KeyError(f'Not found key for a value "{key}"')
        del self._values[hs]
        self._keys.remove(key)
        return self

    def length(self):
        return len([key for key in self._keys if key is not None])

    def _hash(self, key: str):
        return hash(key)%self._size

class TestHashMap(unittest.TestCase):
    def test_hash_map(self):
        hash_map = HashMap()
        hash_map.set('hello', 'world')
        assert hash_map.get('hello') == 'world'

        hash_map.update('hello', '')
        assert hash_map.get('hello') == ''
        assert hash_map.length() == 1

        hash_map.delete('hello')
        assert hash_map.length() == 0
