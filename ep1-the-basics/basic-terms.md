# Terms used

**What is a route?**

Consider the URL: http://facebook.com/himanshub16
Here, the domain name is `facebook.com` and the route is `/himanshub16`.

**What data is sent from my browser when I enter the above URL?**
```
GET /himanshub16 HTTP/1.1
Host: http://www.facebook.com
```

**Anatomy of the above request**
_ | What is it? | Purpose 
---|---|---
`GET` | HTTP Method | It tells the server if this is a request to read or write some information. In case of read, we use `GET`. In case of sending data to write, we use `POST`.
`/himanshub16` | Request path | Tells the server what path is requested
HTTP/1.1 | version | The version of HTTP we are using
Host | hostname | The domain name to send request to.

**What happens on the receiving end?**
Some program (a web framework) which has been listening for requests on some address will parse the `request path`, do some operation, and then return a value.
In our case, we have a flask based app, which maps a route to a function. [See example](flask-hello-world.md)