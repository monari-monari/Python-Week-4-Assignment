import os
# 1) Ask the user for a file path
try:
    file_path = input("Enter the path to the file to read: ").strip()
except (EOFError, KeyboardInterrupt):
    print("No input provided. Exiting.")
    raise SystemExit(1)

if not file_path:
    print("You must provide a file path.")
    raise SystemExit(1)

# 2) Try to read the file
try:
    with open(file_path, "r", encoding="utf-8-sig") as file_handle:
        original_text = file_handle.read()
except FileNotFoundError:
    print(f"File not found: {file_path}")
    raise SystemExit(1)
except IsADirectoryError:
    print(f"That path is a directory, not a file: {file_path}")
    raise SystemExit(1)
except PermissionError:
    print(f"Permission denied when reading: {file_path}")
    raise SystemExit(1)
except UnicodeDecodeError:
    print("Could not read the file as text (UTF-8). It may be binary.")
    raise SystemExit(1)
except OSError as error:
    print(f"OS error while reading: {error}")
    raise SystemExit(1)

# 3) Modify the content (here: add line numbers)
lines = original_text.splitlines()
numbered_lines = []
for index, line in enumerate(lines, start=1):
    numbered_lines.append(f"{index}: {line}")

modified_text = "\n".join(numbered_lines)
if original_text.endswith("\n"):
    # keep a trailing newline if the original had one
    modified_text += "\n"

# 4) Build the output file name (same folder, add _modified before extension)
folder, base_name = os.path.split(file_path)
name, ext = os.path.splitext(base_name)
if not ext:
    ext = ".txt"  # give a default extension if none
output_name = f"{name}_modified{ext}"
output_path = os.path.join(folder or os.getcwd(), output_name)

# 5) Write the modified content to the new file
try:
    with open(output_path, "w", encoding="utf-8") as file_handle:
        file_handle.write(modified_text)
except PermissionError:
    print(f"Permission denied when writing: {output_path}")
    raise SystemExit(1)
except OSError as error:
    print(f"OS error while writing: {error}")
    raise SystemExit(1)

print(f"Modified file written to: {output_path}")

