#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): A list of integers.
    Returns:
        int or None: The peak element if found, or None if the list is empty.
    """
    if not list_of_integers:
        return None
    if all(x == list_of_integers[0] for x in list_of_integers):
        return list_of_integers[0]
    return _find_peak_helper(list_of_integers, 0, len(list_of_integers) - 1)


def _find_peak_helper(lst, start, end):
    """
    Helper function for finding a peak recursively within a specified range.

    Args:
        lst (list): The list of integers.
        start (int): The start index of the range to search.
        end (int): The end index of the range to search.
    Returns:
        int or None: The peak element if found within range,None if not found.
    """
    if start == end:
        return lst[start]
    mid = (start + end) // 2
    if lst[mid] > lst[mid - 1] and lst[mid] > lst[mid + 1]:
        return lst[mid]
    elif lst[mid] < lst[mid + 1]:
        return _find_peak_helper(lst, mid + 1, end)
    else:
        return _find_peak_helper(lst, start, mid - 1)
