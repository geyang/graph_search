from graph_search import PriorityQue

if __name__ == '__main__':
    p = PriorityQue()
    p.push(0, 0)
    p.push(1, 1)
    assert p.pop() == (0, 0)
    p.push(0, 0)
    assert p.pop() == (0, 0)
    p.push(3, 2)
    assert p.pop() == (1, 1)
    p.push(10, 0)
    p.push(5, 0)
    p.push(1, 0)
    p.push(2, 0)
    p.push(6, 0)
    p.push(7, 0)
    assert p.pop() == (1, 0)
    assert p.pop() == (2, 0)
    assert p.pop() == (3, 2)
    assert p.pop() == (5, 0)
    assert p.pop() == (6, 0)
    assert p.pop() == (7, 0)
    exit()
