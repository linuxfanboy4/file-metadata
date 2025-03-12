# File Metadata Inspector

This tool is a comprehensive Python script that extracts and displays detailed metadata about a specified file. With rich terminal output powered by the `rich` library, the script offers a visually appealing and informative analysis of files on your system. It is designed to aid developers, administrators, and enthusiasts who wish to gain detailed insights into their files.

## Features

- **File Metadata Extraction**: Fetches comprehensive metadata such as file size, permissions, timestamps, and more.
- **Human-Readable Output**: Leverages the `rich` library to display metadata in a structured and visually appealing table format.
- **Cross-Platform Compatibility**: Works across Windows, macOS, and Linux.
- **Validation and Error Handling**: Ensures the file exists and provides meaningful error messages for invalid inputs.
- **Timezone Awareness**: Displays timestamps based on the UTC timezone.

### Metadata Details Displayed

- File path, name, extension, and type (file or directory).
- Size in bytes, kilobytes, and megabytes.
- Creation, last access, and last modification timestamps.
- File permissions in octal format.
- File ownership (user and group IDs).
- Operating system and architecture.
- Read, write, and execute permissions.
- Timezone information for timestamps.

## Installation and Usage

### Prerequisites

Before using this script, ensure you have the following:

- Python 3.7 or later installed on your system.
- The `rich` Python package installed (you can install it using `pip install rich`).

### Installation

To get started, download the script using `wget`:

```bash
wget https://raw.githubusercontent.com/linuxfanboy4/file-metadata/refs/heads/main/main.py
```

### Usage

Once downloaded, run the script from the command line as follows:

```bash
python3 main.py <filename>
```

Replace `<filename>` with the path to the file whose metadata you wish to inspect.

### Example

```bash
python3 main.py example.txt
```

This command will output a detailed table with all metadata for the specified file `example.txt`.

## Output

The metadata will be displayed in a rich, formatted table like this:

```
+---------------------+---------------------------------+
| Key                 | Value                           |
+---------------------+---------------------------------+
| File Path           | /path/to/your/file.txt          |
| File Name           | file.txt                        |
| File Extension      | .txt                            |
| File Size (Bytes)   | 1024                            |
| File Size (KB)      | 1.0                             |
| File Size (MB)      | 0.001                           |
| Creation Time       | 2023-04-06 12:00:00             |
| Last Access Time    | 2023-04-06 13:00:00             |
| Last Modified Time  | 2023-04-06 14:00:00             |
| File Permissions    | 0o644                           |
| Owner               | 1000                            |
| Group               | 1000                            |
| File Type           | File                            |
| Is Readable         | True                            |
| Is Writable         | True                            |
| Is Executable       | False                           |
| Operating System    | Linux                           |
| Architecture        | 64-bit                          |
| Timezone            | UTC                             |
+---------------------+---------------------------------+
```

## Code Structure

- **`get_file_metadata(file_path)`**: This function retrieves metadata about the specified file and formats it into a dictionary.
- **`print_metadata(metadata)`**: This function uses the `rich` library to render the metadata as a beautifully formatted table.
- **`main()`**: This is the entry point of the script, responsible for argument parsing, validation, and invoking the metadata functions.

## Error Handling

- If an invalid file path is provided, the script will output an appropriate error message.
- The script ensures that only valid files are processed, and necessary permissions are checked.

## License

This project is licensed under the **MIT License**. For more details, see the `LICENSE` file.

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests for enhancements and bug fixes.
