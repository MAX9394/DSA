import os

README = "# Data Structures and Algorithms\n\n"

for folder in sorted(os.listdir()):
    if os.path.isdir(folder) and not folder.startswith('.'):
        README += f"## {folder}\n\n"

        for file in sorted(os.listdir(folder)):
            filepath = f"{folder}/{file}"

            README += (
                f"- [{file}]"
                f"(./{filepath})\n"
            )

        README += "\n"

with open("README.md", "w", encoding="utf-8") as f:
    f.write(README)

print("README updated.")