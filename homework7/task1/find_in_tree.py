from typing import Any

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
            "key4": ["RED", "RED", {"jhl": "RED", "ASF": "RED"}]
        }
     },
    "jhl": "RED"
}

list_of_element = []


def find_occurrences(tree: dict, element: Any) -> int:
    for key, value in tree.items():
        if key == element:
            list_of_element.append(key)
        if isinstance(value, dict):
            find_occurrences(value, element)
        elif isinstance(value, list):
            for i in value:
                if isinstance(i, dict):
                    find_occurrences(i, element)
                if i == element:
                    list_of_element.append(i)
        elif isinstance(value, str):
            if value == element:
                list_of_element.append(value)
    return len(list_of_element)
