from roots import *
import hashlib
import sys

# Read the command line input string.
message = sys.argv[1]

nth_root = 3

# The first part of the signature padding we are to exploit.
sig = "\x00\x01\xFF\x00\x30\x21\x30\x09\x06\x05\x2B\x0E\x03\x02\x1A\x05\x00\x04\x14"

# Generate the SHA-1 payload, append to the signature
sig = sig + hashlib.sha1(message).digest()

# Come up with some garbage bytes to append.
garbage = "\xAA" * 217

# Finalize the signature
sig = sig + garbage
# Cast everything to an integer
sig = bytes_to_integer(sig)

# Get the roots of the signature
roots = integer_nthroot(sig, nth_root)
# Extract the element from the first root tuple
forged_signature = roots[0]

print integer_to_base64(forged_signature)