import re
import os

file_path = r"e:\Downloads\meera-radhey saloon\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace images/filename.jpg.jpg with images/filename.webp
# Replace images/filename.jpg with images/filename.webp
content = re.sub(r'images/([^"]+?)\.(jpg\.jpg|jpg|jpeg|png)', r'images/\1.webp', content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Replacement successful.")
