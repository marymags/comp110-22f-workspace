# diagramming example code


def foo(a: int, b: int, c: int) -> int:
    if(a < b):
        return c + b
    elif(b < a):
        return c + a
    else:
        return c


def bar(a: int, b: int, c: int) -> int:
    if(c < a):
        return c + b
    else: 
        return b




def main() -> None:
        a: int = 2
        b: int = 3
        c: int = 1
        c = foo(b, c, a)
        b = bar(a, c, a)
        print(a)
        print(b)
        print(c)


if __name__ == '__main__':
    main()


# second practice code (lists)


def foo(a: list[int], b: list[int]) -> None:
    i: int = 0
    while i < len(a):
        a[i] = b[i] + 2
        b.append(a[i])
        i += 1
    b = a

def main() -> None:
    a: list[int] = [0, 1, 2]
    b: list[int] = [3, 4, 1]
    foo(a, b)
    print(a)
    print(b)


if __name__ == '__main__':
    main()


# third example

def main() -> None:
    """Entry point of program."""
    strings: list[str] = ["hey", "o", "eh", "e"]
    word: str = make_word(strings)
    print(word)


def make_word(root: list[str]) -> str:
    """A nonsensical function that makes a 'word'."""
    word: str = ""
    i: int = 0
    while i < len(root):
        if i % 2 == 0:
            word += root[i]
        else:
            if len(word) < 5:
                word += root[i]
            else:
                return word
        i += 1
    return word


if __name__ == '__main__':
    main()

    
