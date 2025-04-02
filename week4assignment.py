def modify_file_content(content):
    """Modify the content (e.g., convert to uppercase)"""
    return content.upper()  # Example: Convert text to uppercase

def main():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r") as file:
            content = file.read()  # Read content from the file
            modified_content = modify_file_content(content)  # Modify content
        
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)  # Write modified content to new file
        
        print(f"🎉 Success! Modified file saved as '{new_filename}'")

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except IOError:
        print("❌ Error: Unable to read the file. Check permissions or file corruption.")

if __name__ == "__main__":
    main()
