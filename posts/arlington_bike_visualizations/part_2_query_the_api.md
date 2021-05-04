Exploring Arlington Bikeometers Part 2 (Query the Bike Arlington API)
================

[Project Introduction]()

# Background

The Official [Bike
Arlington](http://counters.bikearlington.com/data-for-developers/) API
is accessed through [this
URL](http://webservices.commuterpage.com/counters.cfc?wsdl) with
multiple endpoints/methods to get everything from the number of bikers
or pedestrians passing a Bikeometer that day, longitude/latitude of each
Bikeometer, to the weather that day.

# Goal

Query the API and return the number of bikers in a date range.

# Libraries

# Step 1 (Make a request)

We can read
[here](http://counters.bikearlington.com/bike/assets/File/Regional_bikearlington_webservices.pdf)
about the different methods available when making requests to the Bike
Arlington API.

First, let’s get some details on the Bikeometers in the database. There
is a method listed ‘GetAllCounters’ that will return the details of the
bikeometers in the database. I’ll use the ‘requests’ library to make a
‘GET’ request to the base Bike Arlington URL and pass in the
‘GetAllCounters’ method as a parameter.

As I will be using chunks of Python code, I’ll call the R reticulate
package to interface with python from R.

``` python
import requests
# Assign the url of the 
url = 'http://webservices.commuterpage.com/counters.cfc?wsdl'
# Defines the method in a dictionary used to make the request
counter_reqest_methods = {'method': 'GetAllCounters'}
# Save the GetAllCounters request to memory
response = requests.get(url, params=counter_reqest_methods)
response
```

    ## <Response [200]>

Great! Response \[200\] means we got an OK response back. When making a
GET request, a ‘response object’ will be returned. Let’s take a look at
what’s inside our response object. Use the .text method as shown below
to look at the data inside our response object.

``` python
response.text
```

The Bike Arlington API allows for queries of 1 year or less. This
limitation can be managed by making requests in 1 year increments and
adding them to the database or concatenating each 1 year request into a
list then adding the data to the database all at once.
