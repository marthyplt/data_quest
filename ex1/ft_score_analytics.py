import sys


def ft_score_analytics() -> list[int]:
    tab: list[int] = []
    for elem in sys.argv[1:]:
        try:
            if int(elem):
                tab.append(int(elem))
        except ValueError:
            print(f"Invalid parameter: '{elem}'")
    return tab


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3\
ft_score_analytics.py <score1> <score2> ...")
    else:
        tab: list[int] = ft_score_analytics()
        print(f"Scores processed: {tab}\n"
              f"Total players: {len(tab)}\n"
              f"Total score: {sum(tab)}\n"
              f"Average score: {sum(tab) / len(tab)}\n"
              f"High score: {max(tab)}\n"
              f"Low score: {min(tab)}\n"
              f"Score range: {max(tab) - min(tab)}")
