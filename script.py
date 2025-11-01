# write_to_file.py

# Define the message to write
message = "Hello! This is a simple test output written to test.txt."

# Open (or create) test.txt in write mode
with open("test.txt", "w") as file:
    file.write(message)

print("✅ Output written successfully to test.txt")
