import sys


def ft_inventory_system() -> dict[str, int]:
    item: list[str] = []
    inventory: dict[str, int] = {}
    if len(args) == 0:
        print("No item found. Enter inventory as '<item_name>:<quantity>'\n"
              + f"Inventory: {inventory}")
        return inventory
    for elem in args:
        try:
            if elem.count(":") != 1:
                raise SyntaxError("Error - invalid parameter ")
            item = elem.split(":")
            if item[0].isalpha() is False:
                raise SyntaxError("Error - invalid key ")
            if item[0] in inventory:
                raise Exception(f"Redundant item '{item[0]}' - discarding")
            value = int(item[1])
            if value <= 0:
                raise ValueError(f"value {value} is null or negative.")
            inventory[item[0]] = value
        except SyntaxError as e:
            print(f"{e}'{elem}'")
        except ValueError as v:
            print(f"Quantity error for '{item[0]}': {v}")
        except Exception as e:
            print(e)
    return inventory


def min_max_pos(qtty: int, inventory: dict[str, int]) -> str:
    found: str = ""
    for key in inventory:
        if inventory[key] == qtty:
            found = key
            break
    return found


if __name__ == "__main__":
    args: list[str] = sys.argv[1:]
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = ft_inventory_system()
    if inventory:
        print(f"Got inventory : {inventory}")
        print(f"Item list: {list(inventory.keys())}")
        print(f"Total quantity of the {len(inventory)} items: \
{sum(inventory.values())}")
        for i in inventory:
            res = round(inventory[i] / sum(inventory.values()) * 100, 1)
            print(f"Item {i} represents {res}%")
        print(f"Item found abundant: {min_max_pos(max(inventory.values()),
                                                  inventory)} with quantity \
{max(inventory.values())}")
        min_max_pos(min(inventory.values()), inventory)
        print(f"Item least abundant: {min_max_pos(min(inventory.values()),
                                                  inventory)} with quantity \
{min(inventory.values())}")
        inventory.update({"magic_item": 1})
        print(f"Updated inventory: {inventory}")
