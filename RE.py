import re
text = "Hello, My Name is Takesh my Email is takeshbabudupati123@gamil.com"
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
regex = re.compile(pattern)
matches = regex.findall(text)
for match in matches:
    print("Match found: ", match)

