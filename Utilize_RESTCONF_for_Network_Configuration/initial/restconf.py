import sys, requests, urllib3, json

#CSR1kv1 Credentials
URL  = ''
USER = ''
PASS = ''

# Headers required for RESTCONF
headers = {'Content-Type': 'application/yang-data+json',
           'Accept': 'application/yang-data+json'}

# Disable warnings
urllib3.disable_warnings()

# Main method
def main():
    ###########################################
    # Retrieve Device Configuration in Python #
    ###########################################
    # URL for API calls
    url_ge1 = URL + ''

    # GET call to CSR1kv1, SSL checking turned off

    # Print the returned JSON


    #####################################
    # Update Configuration Using Python #
    #####################################
    # URL for API calls
    url_ge3 = URL + ''

    # New IP address

    # PUT call to CSR1kv1, SSL checking turned off


    # Print the response's status code

if __name__ == '__main__':
    main()