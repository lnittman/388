#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """

          �a�_,�o[xكJ4��w�\${tMNA�N|�ޣ!��Sb|��fXۈ�%��mҡ�{Ub
?+k%�z�Q��QQ�Z����m� =V��DB2L
e��ї����1�$�i6J�)����yqM���Uah<�t�
"""
from hashlib import sha256
m = sha256(blob).hexdigest()
m = int(m, 16)
if m % 2 == 0:
	print "I come in peace."
else:
	print "Prepare to be destroyed!"
