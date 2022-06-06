#!/usr/bin/env python3
import os, sys, array

EDID_LEN = (128, 256)

def getlen(edidhdr):
    if edidhdr[18] <= 0 or edidhdr[18] > len(EDID_LEN):
        sys.exit('ERROR: Unknown EDID version %d' % edidhdr[18])

    return EDID_LEN[edidhdr[18] - 1]

def checksum(edid):
    return (0 - (sum(edid[:-1]) % 256)) % 256

def main():
    edid = array.array('B', os.read(sys.stdin.fileno(), 256)).tolist()
    edid_len = getlen(edid)
    edid_n = edid[edid_len - 2]
    nbytes = edid_len + (edid_len * edid_n)

    if len(edid) != nbytes:
        sys.exit('ERROR: Input must be %d bytes' % nbytes)

    for b in range(edid_n + 1):
        x = (b + 1) * edid_len
        actsum = edid[x - 1]
        calsum = checksum(edid[x - edid_len:x])

        if actsum != calsum:
            sys.exit('You need to fix checksum on offset 0x%02x\n'
                    '0x%02x is BAD, should be 0x%02x' % (x - 1, actsum, calsum))

    sys.exit('Checksums are correct!')

if __name__ == '__main__':
    main()
