# Tools
Tools

## ip_find.py 
Check if an IP address belongs to one of the Azure network ranges. Just download the **json** from: https://www.microsoft.com/en-us/download/details.aspx?id=56519
```
ip_find.py -f <inputfile> -i <ip_address>
```
## decode_batch.py 
Decodes obfuscated **.bat** files used by a new malware. These files use a simple character array substitution and empty variables obfuscation. This script extracts the original .bat script.
```
decode_batch.py -f <inputfile>
```
