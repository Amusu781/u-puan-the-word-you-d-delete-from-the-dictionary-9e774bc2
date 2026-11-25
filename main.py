import os
import shutil

WORD = "irregardless"

os.makedirs("/output", exist_ok=True)

# Clear only the contents of /output, never the directory itself.
for name in os.listdir("/output"):
    path = os.path.join("/output", name)
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(WORD)
