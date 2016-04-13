import json
import requests

#before requests, should contain geth option [--rpcapi "personal"], default parameters are eth, net, web3
#parameters : password, geth ip address
#return : address
def getNewAddress(password="default", gethIPAddress="http://127.0.0.1:8545"):
	data = {"id": 1, 'jsonrpc': '2.0', 'method': "personal_newAccount", 'params':[password]}
 	response = requests.post(gethIPAddress, data = json.dumps(data))
 	json_result = json.loads(response.text)
 	return json_result
