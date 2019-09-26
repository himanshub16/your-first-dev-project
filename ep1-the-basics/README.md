# Ep1 - The Basics

Slides > https://docs.google.com/presentation/d/1PdvjY3UAJscqfGXVOueDq2w1Jqkg_AxFE6OIVa6LP24/edit?usp=sharing

As we discussed,
- Server is a program which is listening to incoming messages and sends a response
- Your browser is the one making request to the server when you make one
- We use third-party libraries built by people to avoid doing some heavy lifting. This is exactly same as using `math.h` for `sqrt` instead of implementing an algorithm yourself.


- Communication over a medium (here web) requires a standardized way to pass messages. One of the most common way is [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol), which functions when you use your browser.
- Google Google Google. It'll take time to get super confident. Rome wasn't built in a day.

Head on to these examples, one at a time (in order).
You don't need to understand them in one go, just type and run them one by one and see what happens.


- [Some basic terms](basic-terms.md)

- [Hello World Flask app](flask-hello-world.md)

- [Flask app with multiple routes](flask-multi-routes.md)

- [Render HTML page with Flask](flask-render-html/app.py)

    Visit the folder `flask-render-html` and run `python3 app.py`.

    Then, try the URLs http://localhost:5000, http://localhost:5000/hello, http://localhost:5000/hello/Himanshu

- [HTML form handling](flask-form-handling/app.py)

    Visit the folder `flask-form-handling` and run `python3 app.py`.

    Then, try the URLs http://localhost:5000