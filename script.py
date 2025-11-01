import os

repo_dir = os.getcwd()  # current GitHub workspace
file_path = os.path.join(repo_dir, "test.txt")

with open(file_path, "w") as f:
    f.write("Hello from GitHub Actions!\n")

print(f"✅ Output written successfully to {file_path}")
