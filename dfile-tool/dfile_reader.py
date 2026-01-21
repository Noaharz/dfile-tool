def read_dfile(file_path):
    try:
        with open(file_path, "r", encoding="utf-8-sig") as f:
            content = f.read()

        start_marker = "!=!"
        end_marker = "!0!"

        if start_marker in content and end_marker in content:
            start = content.index(start_marker) + len(start_marker)
            end = content.index(end_marker)
            main_content = content[start:end].strip()
        else:
            main_content = content.strip()

        print("\n--- Content of the .dfile ---\n")
        for line in main_content.splitlines():
            line = line.strip()
            if line:
                print(line)

        print("\n--- End ---\n")

    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(f"Error while reading the file: {e}")


if __name__ == "__main__":
    file_path = input("Enter path to the .dfile: ").strip()
    read_dfile(file_path)
