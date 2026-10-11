import random


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    print()
    init: list[str] = ["Alice", "bob", "Charlie", "dylan", "Emma",
                       "Gregory", "john", "kevin", "Liam"]
    print(f"Initial list of players: {init}")
    res: list[str] = [ele.capitalize() for ele in init]
    print(f"New list with all names capitalized: {res}")
    only: list[str] = [ele for ele in init if ele == ele.capitalize()]
    print(f"New list of capitalized names only: {only}")
    print()
    score_dict: dict[str, int] = {ele: random.randint(0, 1000) for ele in res}
    print(f"Score dict: {score_dict}")
    ave = round(sum(score_dict.values()) / len(score_dict), 2)
    print(f"Score average is: {ave}")
    final_dict: dict[str, int] = {ele: x for ele, x in
                                  score_dict.items() if x > ave}
    print(f"High scores: {final_dict}")
