# Message Board

This is a dynamic message board for the [Galactic Unicorn](https://shop.pimoroni.com/products/galactic-unicorn). 

Because of the limitations of memory on the Pico microcontroller, I decided to implement a client/server model where a web server running flask responds to aynchronous API requests with information about the pixels that should be displayed when scrolling.

In a very basic way, the server will generate enough content to return a buffer of pixels to the Galactic Unicorn. The Unicorn will then display these pixels, and scroll the buffer right one column at a time. Although it is not very efficient to set individual pixels on the Unicorn, I have found that it is actually very smooth and the performance is constant, regardless of the content. In other scrolling examples, I have found that the performance will degrade if trying to add large amounts of text because they render the full amount of text for every redraw of the screen. Clearly this server / client mechanism is a massively over-engineered solution to the problem!

## Running

<ol>
<li>Install Flask</li>
<li>Run the server in development mode using <code>flask --app flaskr run --debug --host 0.0.0.0 --port 5050</code> (do <b>not</b> run Flask in development mode on an internet facing connection)</li>
<li>Copy these dependencies to your Galactic Unicorn </li>
<ul>
<li><a href="https://github.com/pimoroni/supercon6/blob/main/005%20Pimoroni%20MicroPython%20Code/common/network_manager.py">NetworkManager.py</a></li>
<li><a href="https://github.com/StevenRuest/async_urequests"> async_urequests.py</a> (at the time of writing, this code does need a small fix for non-standard http ports, which I have submitted a PR for - as of yet, I have not tested against an SSL connection)</li>
<li>You may need to install the ntptime package - the code displays the time while it is waiting for the network, I will probably remove this at some point as it isn't really necessary!</li>
</ul>
<li>Create or add a <code>secrets.py</code> file on your Galactic Unicorn containing these values</li>
<ul>
<li>BASE_URL - the URL where you're running the Flask APIs</li>
<li>WIFI_SSID, WIFI_PASSWORD, COUNTRY - Your wifi details and the ISO code for your country e.g. GB</li>
</ul>
<li>Copy the <code>dynamic_display.py</code> file to your Galactic Unicorn</li>
</ol>

## Configure
You can add fonts and states to the config.py file and of course can change `message_controller.py` to add new modes.

## Next steps
* Run it on the internet - I've only tried it on my local computer so far
* Add more colours - initially I decided just to use some basic colours but will try to add support for more colours depending on memory limitations
* Animated sprites - I want to be able to define multiple values for each pixel which can be rotated so that there is some form of animation
* Improved fonts
  * The fonts aren't great so want to add more fonts and better fonts
  * Anti-aliased fonts?
  * More font effects e.g. shadow
* More than scrolling
  * I'd like to be able to support different modes e.g. vertical scrolling or static display
* The possibilities are endless!

## Testing

There are some limited unit tests which can be run with pytest in the project's root directory.