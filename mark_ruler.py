#!/usr/bin/env python3

""" Divide and Conquer algorithm to mark lines on a ruler of a given set
    of heights
"""
import math


def draw_ruler(ruler, left, right, height):
    """ Function to draw all the marks on our ruler, recursing to draw marks of
    smaller and smaller heights

    Accepts a ruler list to be drawn, a left and right point on the ruler,
    and the height of the initial (middle) mark
    As output, prints the final set of marks vertically

    """
    if height > 0:
        middle_point = math.floor((left + right) / 2)
        ruler[middle_point] = mark_ruler(height)
        draw_ruler(ruler, left, middle_point, height - 1)
        draw_ruler(ruler, middle_point, right, height - 1)


def mark_ruler(height):
    """ Function to draw a specific mark on our ruler

    Accepts the height of the given mark
    Returns the specified mark (a string), so that we can add the mark to our
    ruler

    """
    # Marks are drawn with equals signs, like "======"
    mark = height * "="
    return mark


if __name__ == "__main__":
    # Define our ruler variables
    left = 0
    right = 64
    height = 6

    # Then, define a list to store the marks on our ruler. Positions on the ruler will be the indices of the list,
    # and we'll store our marks of a given height as values. Initialize the list with a given size, with empty strings
    ruler = ["" for el in range(right - left)]

    draw_ruler(ruler, left, right, height)

    # Now that our marks have been made, format our ruler appropriately
    print("\n".join(ruler))
