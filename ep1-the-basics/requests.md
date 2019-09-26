# HTTP requests

So far, we were using the browser to make requests to our server.

However, a lot of times, we need to make HTTP requests to third-party servers when some event happens.
For example, send a notification when someone sends an email.

In this case, we want to make request from python code to any HTTP server.

For this, we'll be using the `requests` library provided pre-installed in Python. If it doesn't exist, feel free to install it using `pip3 install requests`.

Run the following lines in python shell one by one.

```python
>>> import requests
>>> res = requests.get("http://pokeapi.co/api/v2/pokemon/pikachu")
>>> response = res.json()
>>> # Now, response contains the response of above request in JSON format, which is essentially a Python dictionary.
>>> response["abilities"] 
>>> # Print all abilities one by one
>>> for a in response["abilities"]:
>>>   print(a["ability"]["name"])
```

This is how we make request to any third-party API.

## What you should be doing now?
Pick any URL, and start making requsts from Python shell.