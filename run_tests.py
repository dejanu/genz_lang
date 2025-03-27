import unittest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    # Discover tests in the 'tests' directory and include 'test_parser.py'
    suite = loader.discover('.', pattern='test_*.py')
    runner = unittest.TextTestRunner()
    runner.run(suite)
