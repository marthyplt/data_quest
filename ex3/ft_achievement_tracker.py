import random


def gen_player_achievements() -> set[str]:
    a: list[str] = ["Boss Slayer", "Collector Supreme", "Crafting Genius",
                    "First Steps", "Hidden Path Finder", "Master Explorer",
                    "Sharp Mind", "Speed Runner", "Strategist", "Survivor",
                    "Treasure Hunter", "Untouchable", "Unstoppable",
                    "World Savior", "Dragon Slayer", "Master Collector",
                    "Potion Master", "Puzzle Solver", "Secret Keeper",
                    "Legendary Adventurer"]
    b: set[str] = ((set(random.sample(a, k=random.randint(5, len(a) - 5)))))
    return b


if __name__ == "__main__":
    a: set[str] = gen_player_achievements()
    b: set[str] = gen_player_achievements()
    c: set[str] = gen_player_achievements()
    d: set[str] = gen_player_achievements()
    print("=== Achievement Tracker System ===\n")
    print(f"Player Alice : {a}\n"
          f"Player Bob: {b}\n"
          f"Player Charlie: {c}\n"
          f"Player Dylan: {d}\n\n"
          f"All distinct achievements: {a.union(b, c, d)}\n\n"
          f"Common achievements: {a.intersection(b, c, d)}\n\n"
          f"Only Alice has : {a.difference(b, c, d)}\n"
          f"Only Bob has : {b.difference(a, c, d)}\n"
          f"Only Charlie has : {c.difference(a, b, d)}\n"
          f"Only Dylan has : {d.difference(a, b, c)}")
