
import sys
import os
import json
import re
from S3TextFromLambdaEvent import *	
import subprocess


def read_stdin():
	readline = sys.stdin.readline()
	while readline:
		yield readline
		readline = sys.stdin.readline()

## for line in read_stdin():
##	line = line.split()
##	print(line)



def parse_command(patterns, input):
	for pattern in patterns:
		match_obj = re.match(pattern["re"], input)
		if match_obj is not None:
			return pattern["command"]
	return ""


def do_s3_download(input):
	key = get_key_from_url(input)
	filename = os.environ["TEMP"] + "\\" + key
	filename = filename.replace("/", "_")
#	with open(filename, "w") as file:
#		file.write(file_contents)

	download_s3_file_url(input, filename)
	print("\tDownloaded: " + filename)

	subprocess.call("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe \"" + filename + "\"")

def main():

	patterns = [
			{"command" : "quit" , "re" : "quit|q|e|exit"}, 
			{"command" : "s3_download" , "re" : ".*s3.amazonaws.com.*"},
			{"command" : "help" , "re" : "help|h"}
		]

	while True:
		input_text = input("> ")

		command = parse_command(patterns, input_text)
		if command == "":
			print("Can't find command matching that input.")
		else:	
			print("Command:" + command)
			if command == "quit":
				break
			if command == "help":
				for pattern in patterns:
					print("\t" + pattern["command"] + "\t\t- " + pattern["re"])
			if command == "s3_download":
				file_contents = do_s3_download(input_text)

		print("")

if __name__ == '__main__':
	main()	

