#/usr/bin/python

import os
import socket
import dns.resolver
import urllib2
import json
import urlparse

# pip install dnspython for nslookup

ip = "8.8.8.8"
hostname = "www.google.c"

def check_http(hostname):
    url = "http://" + hostname
    print "please wait connecting to " + hostname
    urldata = urllib2.Request(url)
    try:
    	resp = urllib2.urlopen(urldata)
    except urllib2.HTTPError as e:
    	if e.code == 404:
    		print "http 400 response - something wrong"
                print "running extended tests"
                check_ip_ping(ip)
                check_host_ping(hostname)
                check_nslookup(hostname)
    	else:
    		urllib2.urlopen(urldata)
    		print "1st else"
    except urllib2.URLError as e:
    		print "Not an HTTP-specific error (e.g. connection refused)"
                print "running extended tests"
                check_ip_ping(ip)
                check_host_ping(hostname)
                check_nslookup(hostname)
    else:
    	# 200
    	print "http 200 response - all good"
        print "no need to do anything else"

def check_ip_ping(ip):
    response = os.system("ping -c 4 " + ip)
    # and then check the response...
    if response == 0:
        pingstatus = "Ping Test Successful"
    else:
        pingstatus = "Ping Test Failed"

def check_host_ping(hostname):
    response = os.system("ping -c 4 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = "Ping Test Successful"
        print pingstatus
    else:
        pingstatus = "Ping Test Failed"
        print pingstatus
    return pingstatus

def check_nslookup(hostname):
    try:
        response = dns.resolver.query(hostname, 'A')
        for rdata in response:
            print "The A record of " + rdata.address + " has been found for this host: " + hostname
    except:
        print "Can't resolve the A record of hostname " + hostname

check_http(hostname)
