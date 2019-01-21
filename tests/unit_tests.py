import unittest
from driver import *

class TestMethods(unittest.TestCase):
	def test_parse_command__existing_pattern__command_returned(self):		
		# Arrange
		patterns = patterns = [
				{"command" : "quit" , "re" : "quit|q|e|exit"}, 
				{"command" : "s3_download" , "re" : ".*s3.amazonaws.com.*"},
				{"command" : "help" , "re" : "help|h"}
			]

		# Act
		result = parse_command(patterns, "http://s3.amazonaws.com/fakebucket/key.txt")

		# Assert
		self.assertEqual(result, "s3_download")


	def test_parse_command__missing_pattern__empty_string_returned(self):		
		# Arrange
		patterns = patterns = [
				{"command" : "quit" , "re" : "quit|q|e|exit"}, 
				{"command" : "s3_download" , "re" : ".*s3.amazonaws.com.*"},
				{"command" : "help" , "re" : "help|h"}
			]

		# Act
		result = parse_command(patterns, "there is no pattern for this")

		# Assert
		self.assertEqual(result, "")


if __name__ == '__main__':
	unittest.main()		


