# Tools
These are tools I developed for myself, code could be messy but most of the time it works. If they are useful or could help someone along the way, all the better.

## decode_batch.py 
Decodes obfuscated **.bat** files used by a new malware. These files use a simple character array substitution and empty variables obfuscation. This script extracts the original .bat script without executing it.
The format of the obfuscated files is something like this:
```
ÿþ&@cls&@set "ÃÃ§¡=3aQBGDRprYNqscPt u7ZdkCWgLFhEjmobiy5I8OnvT1lw6M0X@AVJx9U24zKfHSe"

ÿþ&%ÃÃ§¡:~13,1%%ÃÃ§¡:~43,1%%¶iÃa³%%ÃÃ§¡:~12,1%
%ÃÃ§¡:~49,1%%ÃÃ§¡:~63,1%%ÃÃ§¡:~13,1%%ÃÃ§¡:~27,1%%ÃÃ§¡:~31,1%%ÃÃ§¡:~16,1%%ÃÃ§¡:~31,1%%ÃÃ§¡:~60,1%%ÃÃ§¡:~60,1%
%ÃÃ§¡:~12,1%%ÃÃ§¡:~63,1%%vÃYÃ¥e%%ÃÃ§¡:~15,1%%ÃÃ§¡:~43,1%%ÃÃ§¡:~31,1%%ÃÃ§¡:~13,1%%ÃÃ§¡:~1,1%%ÃÃ§¡:~43,1%
...
```
Usage:
```
decode_batch.py -f <inputfile>
```

## ip_find.py 
Check if an IP address belongs to one of the Azure network ranges. Just download the **json** from: https://www.microsoft.com/en-us/download/details.aspx?id=56519
```
ip_find.py -f <inputfile> -i <ip_address>
```
