import ipaddress
import json
import sys
import getopt


def check_network(json_file,ip):
	fich_ips = open(json_file,'r')
	Azure_ip = json.loads(fich_ips.read())
	
	check = ip
	result = ['']

	for i in Azure_ip['values']:
		#print(i['name'])
		#print(i['properties']['addressPrefixes'])
		for j in i['properties']['addressPrefixes']:

			if ipaddress.ip_address(check) in ipaddress.ip_network(j):
				result.append('IP: ' + check + ' -> NET: ' + j + ', ID: ' + i['name'] + ', REGION: ' + i['properties']['region'])
				break

	return(result)


def usage():
	print("Command usage:")
	print()
	print("ip_find.py -f <inputfile> -i <ip_address>")

def main():
	inputfile = ""
	ipaddr = ""
	results = ""	
	try:
	    opts, args = getopt.getopt(sys.argv[1:], "hf:i:", ["file=", "ipaddress="])
	except getopt.GetoptError as err:
	    # print help information and exit:
	    print(err)  # will print something like "option -a not recognized"
	    usage()
	    sys.exit(2)
	output = None
	verbose = False
	for o, a in opts:
	    if o in ("-f", "--file"):
	        inputfile = a
	    elif o in ("-h", "--help"):
	        usage()
	        sys.exit()
	    elif o in ("-i", "--ipaddress"):
	        ipaddr = a
	    else:
	        assert False, "unhandled option"
	        exit
	#print("Parametros 1: %s 2: %s" % (inputfile,ipaddr))
	if inputfile != "" and ipaddr != "":
		results=check_network(inputfile,ipaddr)
	else:
		usage()

	if len(results) == 1:
		print("Not found")
	else:
		for i in results:
			print(i)



if __name__== "__main__":
	main()
