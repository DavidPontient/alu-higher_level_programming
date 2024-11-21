#!/bin/bash
# Send a GET request with the custom header and display the body of the response
curl -sG "$1" -H "X-School-User-Id: 98"
