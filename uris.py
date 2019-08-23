#!/usr/bin/env python
import Queue
import threading
import urllib2
import time

hosts = "http://yahoo.com", "http://google.com", "http://amazon.com",
"http://ibm.com", "http://apple.com"          
queue = Queue.Queue()

