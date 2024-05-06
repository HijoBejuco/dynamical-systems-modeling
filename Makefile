# Run unit tests
#	-v for "verbose" (more detailed output)
#	--cov=src how much of the code is covered, so how many lines
# 	of code have been tested by the unit tests. 
unit_tests: 
	pytest -v tests/test.py --cov=src