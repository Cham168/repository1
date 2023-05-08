import json


class JsonParser:
    def __init__(self, json_str):
        self.obj = json.loads(json_str)

    def __enter__(self):
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Rectangle:
    def __init__(self, p1, p2):
        self.left = min(p1.x, p2.x)
        self.right = max(p1.x, p2.x)
        self.top = max(p1.y, p2.y)
        self.bottom = min(p1.y, p2.y)

    def contains(self, point):
        return self.left <= point.x <= self.right and self.bottom <= point.y <= self.top

    def __contains__(self, point):
        return self.contains(point)


if __name__ == '__main__':
    with JsonParser('"hello"') as res:
        assert res == "hello"

    with JsonParser('{"hello": "world", "key": [1,2,3]}') as res:
        assert res == {"hello": "world", "key": [1, 2, 3]}

    start_point = Point(1, 0)
    end_point = Point(7, 3)

    rect = Rectangle(start_point, end_point)
    assert rect.contains(start_point)
    assert not rect.contains(Point(-1, 3))
    assert start_point in rect
    assert Point(-1, 3) not in rect
