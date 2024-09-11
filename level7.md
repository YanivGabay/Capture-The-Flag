

# Level 7

## Introduction


## Instructions
1. Caesar Cipher
2. pip install Pillow
3. caesar = bytes_to_image(flag_bytes)
4. base64


## Steps
first if we go to the endpoint of level 7 we get:
{"error":"Password doesn't match triifk. 2 attempts remaining."}
which means we need to send a password to the server.
we will shift to the left and try all possibilites.
when we found the password we got the classic use start end to get the flag.
the flag was encoded in 64 bytes to we used 64byte to decode it, than send it to pillow to get the image.



## Resources
- [Caesar cipher - Wikipedia](https://en.wikipedia.org/wiki/Caesar_cipher)
```

