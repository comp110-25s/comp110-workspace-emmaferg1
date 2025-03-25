"""Dictionary functions practice!"""

__author__: str = "730566544"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Inverting keys and values of dictionary."""
    inverted_result = {}
    for key, value in d.items():
        if value in inverted_result:
            raise KeyError
        inverted_result[value] = key
    return inverted_result


def count(items: list[str]) -> dict[str, int]:
    """Counting the number of times a certain value is in list."""
    result = {}
    for item in items:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def favorite_color(name_fav_color: dict[str, str]) -> str:
    """Returning most frequently appeared color."""
    color_frequency = count(list(name_fav_color.values()))
    most_frequent = ""
    max_count = 0
    for color, freq in color_frequency.items():
        if freq > max_count:
            most_frequent = color
            max_count = freq
    return most_frequent


def bin_len(strs: list[str]) -> dict[int, set[str]]:
    """Creating dictionary based on key's length."""
    result_bin = {}
    for item in strs:
        length = len(item)
        if length in result_bin:
            result_bin[length].add(item)
        else:
            result_bin[length] = {item}
    return result_bin
