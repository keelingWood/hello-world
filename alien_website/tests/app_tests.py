from nose.tools import *
from tools import assert_response
import sys
from os import path

sys.path.append( path.dirname(path.dirname(path.abspath(__file__))))
#import os, sys, inspect
#
#cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
#if cmd_folder not in sys.path:
#    sys.path.insert(0, cmd_folder)
#
#cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe()))[0],"Directory/Projects/alien_website")))
#if cmd_subfolder not in sys.path:
#    sys.path.insert(0, cmd_subfolder)

from bin.app import app

def test_index():
    # chect that we geta 404 on the / URL
    resp = app.request("/")
    assert_response(resp, status="404")
    
    #test our first GET request to /hello
    resp = app.request("/hello")
    assert_response(resp)
    
    #make sure our default values work for the form
    resp = app.request("/hello", "POST")
    assert_response(resp, contains="Nobody")
    
    #test that we get expected values
    data = {'name': 'Zed', 'greet': 'Hola'}
    resp = app.request("hello",method="Post", data = data)
    assert_response(resp, contains= "Zed")