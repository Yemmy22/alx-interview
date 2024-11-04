#!/usr/bin/python3

"""
A validUTF8 function module
"""

'''
def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding
    """
    # Initialize count for continuation bytes
    remaining_bytes = 0

    # Masks and patterns for UTF-8
    FIRST_BYTE_MASKS = [0b11110000, 0b11100000, 0b11000000]
    FIRST_BYTE_PATTERNS = [0b11110000, 0b11100000, 0b11000000]
    CONTINUATION_MASK = 0b11000000
    CONTINUATION_PATTERN = 0b10000000

    for byte in data:
        byte = byte & 0xFF
        if remaining_bytes > 0:
            # Check if byte is a valid continuation byte
            if (byte & CONTINUATION_MASK) != CONTINUATION_PATTERN:
                return False
            remaining_bytes -= 1
        else:
            # Check starting byte for number of following bytes
            if (byte & 0b10000000) == 0:
                remaining_bytes = 0  # ASCII (1-byte)
            elif (byte & FIRST_BYTE_MASKS[2]) == FIRST_BYTE_PATTERNS[2]:
                remaining_bytes = 1  # 2-byte character
            elif (byte & FIRST_BYTE_MASKS[1]) == FIRST_BYTE_PATTERNS[1]:
                remaining_bytes = 2  # 3-byte character
            elif (byte & FIRST_BYTE_MASKS[0]) == FIRST_BYTE_PATTERNS[0]:
                remaining_bytes = 3  # 4-byte character
            else:
                return False  # Invalid starting byte

    return remaining_bytes == 0
'''


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding
    """
    # Initialize count for continuation bytes
    remaining_bytes = 0

    for byte in data:
        # Get only the 8 least significant bits
        byte = byte & 0xFF

        if remaining_bytes == 0:
            # This is a starting byte - determine sequence length
            if byte & 0b10000000 == 0:  # 0xxxxxxx
                remaining_bytes = 0
            elif byte & 0b11100000 == 0b11000000:  # 110xxxxx
                remaining_bytes = 1
            elif byte & 0b11110000 == 0b11100000:  # 1110xxxx
                remaining_bytes = 2
            elif byte & 0b11111000 == 0b11110000:  # 11110xxx
                remaining_bytes = 3
            else:
                return False
        else:
            # This should be a continuation byte (10xxxxxx)
            if byte & 0b11000000 != 0b10000000:
                return False
            remaining_bytes -= 1

    # All sequences should be complete
    return remaining_bytes == 0
