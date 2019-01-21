import unittest
from driver import *
import boto3
from S3TextFromLambdaEvent import *



class TestMethods(unittest.TestCase):

	def test_sample_tess(self):
		# Assert
		self.assertEqual(1, 1)


if __name__ == '__main__':
	unittest.main()		


