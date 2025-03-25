"""Dictionary unit test function."""

__author__: str = "730566544"

import pytest
from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


def test_invert_use():
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_use1():
    assert invert({"e": "f", "g": "h"}) == {"f": "e", "h": "g"}


def test_invert_edge():
    assert invert({"apple": "cat"}) == {"apple": "cat"}


with pytest.raises(KeyError):
    my_dictionary = {"kris": "jordan", "michael": "jordan"}
    invert(my_dictionary)


def test_favorite_color_use():
    assert favorite_color({"Emma": "pink", "Cam": "blue", "Jill": "blue"}) == "blue"


def test_favorite_color_use1():
    assert (
        favorite_color({"Dylan": "blue", "Maya": "orange", "Ella": "orange"})
        == "orange"
    )


def test_favorite_color_edge():
    assert favorite_color({"Emma": "pink", "Sam": "red", "Tessa": "red"}) == "pink"


def test_favorite_color_edge1():
    assert favorite_color({"Emma": "pink", "Cam": "blue", "Jill": "red"}) == "pink"


def test_count_use():
    assert count(["happy", "sad", "silly", "happy", "sad", "sad"]) == {
        "happy": 2,
        "sad": 3,
        "silly": 1,
    }


def test_count_use1():
    assert count(["cherry", "apple", "pear", "apple", "cherry", "cherry"]) == {
        "cherry": 3,
        "apple": 2,
        "pear": 1,
    }


def test_count_edge():
    assert count(["banana", "apple"]) == {"banana": 1}


def test_bin_len_use():
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_use1():
    assert bin_len(["dove", "tree", "smile"]) == {4: {"dove", "tree"}, 5: {"smile"}}


def test_bin_len_edge():
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len_use4():
    assert bin_len([]) == {}


def test_bin_len_use2():
    assert bin_len(["b", "a", "ccc"]) == {1: {"b", "a"}, 3: {"ccc"}}
