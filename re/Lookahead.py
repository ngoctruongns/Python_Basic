
import re

input_string = "This is [an] example [of] a [string] with [square brackets]."
result = re.findall(r'(?<=\[).*?(?=\])', input_string)
print(result)

result = re.search(r'(?<=\[).*(?=\])', input_string)
print(result.group())

result = re.search(r'(?<=\[).*?(?=\])', input_string)
print(result.group())
