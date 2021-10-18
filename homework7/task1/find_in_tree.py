from typing import Any

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    ("jhl", "URL", "TWITTER"): {
        "abc": {"BLUE", "PULL", "RED", True},
        "jhl": "RED",
        "complex_key": {
            "key1": ("YELLOW", "SWIM", "RED", False, None),
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
            "key4": ["RED", "RED", {"jhl": "RED", "ASF": "RED"}]
        }
     },
    "jhl": "RED"
}

count = 0


def find_occurrences(tree: dict, element: Any) -> int:
    global count
    for key, value in tree.items():
        if isinstance(key, str):
            if key == element:
                count += 1
        else:
            for i in key:
                if i == element:
                    count += 1
        if isinstance(value, dict):
            find_occurrences(value, element)
        elif isinstance(value, str):
            if value == element:
                count += 1
        else:
            for i in value:
                if isinstance(i, dict):
                    find_occurrences(i, element)
                if i == element:
                    count += 1
    return count
