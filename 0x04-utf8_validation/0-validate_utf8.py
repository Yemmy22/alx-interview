#!/usr/bin/python3

"""
A validUTF8 function module
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding
    """
    # Initialize count for continuation bytes
    remaining_bytes = 0

    # Masks for UTF-8 patterns
    FIRST_BYTE_MASKS = [0b11110000, 0b11100000, 0b11000000]
    CONTINUATION_MASK = 0b10000000
    CONTINUATION_PATTERN = 0b10000000

    for byte in data:
        # Check if it’s a continuation byte
        if remaining_bytes > 0:
            if (byte & 0b11000000) != CONTINUATION_PATTERN:
                return False
            remaining_bytes -= 1
        else:
            # Determine the type of UTF-8 character by the number of leading 1s
            if (byte & 0b10000000) == 0:
                remaining_bytes = 0  # ASCII (1-byte)
            elif (byte & FIRST_BYTE_MASKS[2]) == 0b11000000:
                remaining_bytes = 1  # 2-byte character
            elif (byte & FIRST_BYTE_MASKS[1]) == 0b11100000:
                remaining_bytes = 2  # 3-byte character
            elif (byte & FIRST_BYTE_MASKS[0]) == 0b11110000:
                remaining_bytes = 3  # 4-byte character
            else:
                return False  # Invalid starting byte

    return remaining_bytes == 0
