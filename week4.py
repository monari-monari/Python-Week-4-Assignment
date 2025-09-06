def read_file(filename):
    """Read a file and return its content."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(f" Successfully read '{filename}'")
            return content
    except FileNotFoundError:
        print(f" Error: File '{filename}' not found!")
        return None
    except PermissionError:
        print(f" Error: Cannot read '{filename}' - permission denied!")
        return None
    except Exception as e:
        print(f" Unexpected error: {e}")
        return None

def process_content(content):
    """Add line numbers to the content."""
    lines = content.split('\n')
    numbered_content = []
    
    for i, line in enumerate(lines, 1):
        numbered_content.append(f"Line {i}: {line}")
    
    return '\n'.join(numbered_content)

def write_file(filename, content):
    """Write content to a new file."""
    try:
        # Create new filename
        name, ext = filename.rsplit('.', 1) if '.' in filename else (filename, '')
        new_filename = f"{name}_processed.{ext}" if ext else f"{name}_processed"
        
        with open(new_filename, 'w', encoding='utf-8') as file:
            file.write(content)
        
        print(f" Successfully wrote to '{new_filename}'")
        return True
    except Exception as e:
        print(f" Error writing file: {e}")
        return False

def main():
    """Main program function."""
    print("=" * 50)
    print(" SIMPLE FILE PROCESSOR")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("1. Process a file")
        print("2. Create sample file")
        print("3. Exit")
        
        choice = input("\nChoose an option (1-3): ").strip()
        
        if choice == '1':
            # Get filename from user
            filename = input("Enter filename to process: ").strip()
            
            if not filename:
                print(" Please enter a valid filename!")
                continue
            
            # Read the file
            content = read_file(filename)
            if content is None:
                continue
            
            # Process the content
            print(f" Processing {len(content.split())} words...")
            modified_content = process_content(content)
            
            # Write the modified content
            if write_file(filename, modified_content):
                print(" File processing completed successfully!")
            
        elif choice == '2':
            # Create a sample file
            sample_content = """Hello! This is a sample file."""
            
            try:
                with open("sample.txt", "w", encoding="utf-8") as file:
                    file.write(sample_content)
                print(" Created 'sample.txt' - you can now process it!")
            except Exception as e:
                print(f" Error creating sample file: {e}")
                
        elif choice == '3':
            print(" Goodbye!")
            break
            
        else:
            print(" Invalid choice! Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
