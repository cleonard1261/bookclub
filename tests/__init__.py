import unittest

class InitializationTest(unittest.TestCase):

	def test_sanity(self):
		"""
        Assert the world is by 2 + 2 = 4
		"""

		self.assertEqual(2+2, 4)

	def test_import(self):
		"""
        test import
		"""
		
		try:
			import octavo
		except ImportError:
			self.fail("Could not import octavo")

	def test_whatever(self):
		"""
		Tests test_whatever
		"""

		self.assertNotEqual("this", "this")