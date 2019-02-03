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


	def test_convert_boto_resource_url_to_client_url__url_with_pluses__pluses_removed(self):
		# Arrange
		input = "https://s3.amazonaws.com/bucket/key+name.txt"
# https://s3.amazonaws.com/code-index/prep-input%5CProjectX%5Cintegration_test_1.txt

		# Act
		result = convert_boto_resource_url_to_client_url(input)

		# Assert
		self.assertEqual(result, input.replace("+", " "))

	def test_convert_boto_resource_url_to_client_url__url_with_pluses__pluses_removed(self):
		# Arrange
		input = "https://s3.amazonaws.com/bucket/%5Cfolder%5Ckey.txt"

		# Act
		result = convert_boto_resource_url_to_client_url(input)

		# Assert
		self.assertEqual(result, input.replace("%5C", "\\"))		

if __name__ == '__main__':
	unittest.main()		


