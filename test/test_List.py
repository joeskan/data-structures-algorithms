import sys
import os

sys.path.append(os.getcwd().split('data-structures')[0] + "data-structures/classes")

from List import List

def main():
    myl = List()
    myl.emplace_back(1)

    myl.emplace_back(2)

    myl.insert(0, 3)
    myl.insert(1, 4)
    myl.emplace_front(5)
    myl.insert(2, 6)
    myl.delete(2)

    read = list(myl)
    assert read == [5, 3, 4, 1, 2]

    assert len(myl) == 5

    assert myl.at(2) == 4
    assert myl.at(4) == 2

    myl.swap(3, 7)
    assert list(myl) == [5, 3, 4, 7, 2]

if __name__ == '__main__':
    main()