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
