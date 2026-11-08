>>> import urllib3
>>> resp = urllib3.request("GET", "http://httpbin.org/robots.txt")
>>> resp.status
200
>>> resp.data
b"User-agent: *\nDisallow: /deny\n"
