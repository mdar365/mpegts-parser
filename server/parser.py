#!/usr/bin/env python
import sys

# Parameters to be configured
PACKET_SIZE = 188
PACKET_START_BYTE = 0x47


class ParsingException(Exception):
    pass


def get_bits(byte_val):
    bits = []
    for i in range(8):
        bit = (byte_val >> i) & 1
        bits.append(bit)
    bits.reverse()
    return "".join([str(x) for x in bits])


def find_indices(list_to_check):
    indices = []
    last_index = 0
    for idx, value in enumerate(list_to_check):
        if value == PACKET_START_BYTE and idx % PACKET_SIZE == 0:
            if idx - last_index > PACKET_SIZE:
                raise ParsingException("No sync byte present in packet " +
                                       str(len(indices)) +
                                       ", offset " +
                                       str(last_index + PACKET_SIZE))

            indices.append(idx)
            last_index = idx
    return indices


def parse_data(data):
    indexes_of_packets = find_indices(data)

    list_of_pids = []
    for index in indexes_of_packets:
        second_byte = get_bits(data[index + 1])
        third_byte = get_bits(data[index + 2])
        pid_bits = second_byte[3:] + third_byte[:8]
        pid = (int(pid_bits, 2))
        list_of_pids.append(pid)

    list_of_pids = list(set(list_of_pids)) # Remove Duplicates
    list_of_pids.sort()
    list_of_pids = [hex(pid) for pid in list_of_pids]

    return list_of_pids
