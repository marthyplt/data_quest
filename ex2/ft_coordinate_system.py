import math


def get_player_pos() -> tuple[float, ...]:
    first = input("Enter new coordinates as floats in format 'x,y,z': ")
    try:
        if first.count(",") != 2:
            raise SyntaxError("Invalid Syntax!")
        tab: list[str] = first.split(",")
        arr: list[float] = []
        for elem in tab:
            arr.append(float(elem))
        final: tuple[float, ...] = (arr[0], arr[1], arr[2])
        return final
    except SyntaxError as e:
        print(e)
        return get_player_pos()
    except ValueError as e:
        print(f"Error on parameter '{elem}': {e}")
        return get_player_pos()


def get_distance(a: tuple[float, ...], b: tuple[float, ...]) -> float:
    if b is None:
        b = (0, 0, 0)
    return (round(math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2),
            4))


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n\n"
          "Get a first set of coordinates")
    a: tuple[float, ...] = get_player_pos()
    print(f"Got a first tuple: {a}\n"
          f"It includes: X={a[0]}, Y={a[1]}, Z={a[2]}\n"
          f"Distance to center: {get_distance(a, (0, 0, 0))}\n\n"
          "Get a second set of coordinates")
    b: tuple[float, ...] = get_player_pos()
    print(f"Distance between the 2 sets of coordinates: {get_distance(a, b)}")
