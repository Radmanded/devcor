import requests from request.auth
import HTTPBasicAuth from dnac_config import DNAC, DNAC_PORT, DNAC_USER, DNAC_PASSWORD, token, device_id

def get_device_int(device_id):
  """
  Building out function to retrieve device interface. Using requests.get
  to make a call to the network device Endpoint
  """
url = "https://sandboxdnac.cisco.com/api/v1/interface"
hdr = {'x-auth-token': token, 'content-type' : 'application/json'}
querystring = {"macAddress": device_id} # Dynamically build the query    params to get device-specific Interface info
resp = requests.get(url, headers=hdr, params=querystring)  # Make the Get    Request
interface_info_json = resp.json()

def print_interface_info(interface_info):


print_interface_info(interface_info_json)


