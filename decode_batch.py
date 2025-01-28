import re
import sys
import getopt

idstr="@cls&@set"

# Imports and utility functions
# Build dictionary based on the substitution variable
def build_dict(varname,value):
    res={}
    count=0
    for i in value:
        key=varname + ":~" + str(count) + ",1"
        res[key] = value[count]
        count+=1
    return res

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

# Function for the substition of the characters
def replacement(match, d, group=1):
    for key in d:
        if re.match(key, match.group(group)):
            return d[key]
    return match.group(group)

def decode_file(varname,dic,text):
    result=""
    new = build_dict(varname,dic)
    re_string=r'\%(' + varname + r':\~\d+,1)\%'
    text=re.sub(re_string,lambda x: replacement(x, new),text)
    # Clean the text from non defined variables with non-ascii characters
    var=re.compile(r"\%.*?\%")
    for i in var.findall(text):
        if is_ascii(i)==False:
            text=text.replace(i,"")
        else:
            pass
    return text
# Open file and check is expected type

def check_file(filename):
    FILE = filename
    varname_1=""
    result=""
    dict_values=""

    f = open(FILE, "r")
    head = f.readline()

    if re.findall(idstr,head):
        re_string = idstr + " \"(.*?)=(.*?)\"$"
        array = re.findall(re_string,head)
        varname_1=array[0][0]
        dict_values=array[0][1]
        file_text=f.read()
        text_d=decode_file(varname_1,dict_values,file_text)
        result=text_d
    else:
        result="Not the right file type"

    return result
def usage():
	print("Command usage:")
	print()
	print("decode_bat.py -f <inputfile>")

def main():
	inputfile = ""
	ipaddr = ""
	results = ""
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hf:", ["file="])
	except getopt.GetoptError as err:
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
		else:
			assert False, "unhandled option"
			exit

	if inputfile != "":
		results=check_file(inputfile)
	else:
		usage()

	print(results)

if __name__== "__main__":
	main()
