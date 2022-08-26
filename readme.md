Start the application:
```
$ gunicorn --bind 0.0.0.0:5000 "app:create_app()"
```

If you lockpick a lock with success and want other people to do the same as you, you could fill the __locks.json__ file.

The application will display some tips about the lock:

* How many pins?

* How many security pins? and position, and shape

* Which method to use to unlock?

* The difficulty

* Some tips

The application is also available on heroku

```
https://sharelocks.herokuapp.com/
```


![](images/screen.png)
