import typing
import random


def consume_event(arr: list[tuple
                            [str, str]]) -> typing.Generator[tuple[str, str],
                                                             None, None]:
    while arr:
        off: tuple[str, str] = random.choice(arr)
        arr.remove(off)
        yield off


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    player: list[str] = ["bob", "alice", "charlie", "dylan"]
    action: list[str] = ["run", "eat", "sleep", "grab", "move", "climb",
                         "swim", "release", "use"]
    while True:
        res: tuple[str, str] = ((random.choice(player),
                                 random.choice(action)))
        yield res


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    for i in range(1000):
        g = next(gen_event())
        print(f"Event {i}: {g[0]} did action {g[1]}")
    print("Built list of 10 events:", end=" ")
    lst: list[tuple[str, str]] = []
    for i in range(10):
        res = next(gen_event())
        lst.append(res)
    print(f"{lst}")
    for res in consume_event(lst):
        print(f"Got event from list: {res}")
        print(f"Remains in list: {lst}")
