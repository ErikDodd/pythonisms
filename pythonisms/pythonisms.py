def count_up(n):
    while n < 100:
        yield n
        n + 5

count = count_up(100)
print(next(count))
print(next(count))
print(next(count))


def count_down(n):
    while n > 0:
        yield n
        n - 5

class Car:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __len__(self):
        return "The Length of One Car"

    def __repr__(self):
        return "This is a class of objects called cars. Different types of cars."

    def __add__(self, other):
        return Car(self.name + other.name)

car_1 = Car("BMW")
car_2 = Car("Mercedes Benz")
print(car_1 + " " + car_2)
class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return "This is a node. It has a value and it has a next attribute"


class Queue:

    def __init__(self, collection=None):
        self.front = None
        self.rear = None
        self.items = []
        if collection:
            for item in reversed(collection):
                self.insert(item)


    def is_empty(self):
        return len(self.items) == 0



    def enqueue(self, item):
        self.items.append(item)


    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop(0)


    def __str__(self):
        out = ""
        current = self.front

        while current:
            out += f"[ {current.value} ] -> "
            current = current.next

        return out + "None"


    def __iter__(self):
        def value_generator():
            current = self.head

            while current:
                yield current.value
                current = current.next

        return value_generator()


    def __eq__(self, other):
        return list(self) == list(other)




if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    result = [item for item in q]
    print(result)
