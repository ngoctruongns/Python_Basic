# importing regex
import re

# Regex Lookbehind example
example = re.search(r'(?<=geeks).*',
					'geeksforgeekshello')

print(example.group())
print(example)
print("Pattern found from index",
	example.start(), example.end())
