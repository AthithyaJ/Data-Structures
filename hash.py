import hashlib as h
h_obj = h.md5(b"Hello world")
print(h_obj.hexdigest)

