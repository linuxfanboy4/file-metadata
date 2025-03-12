import os
import sys
import time
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.panel import Panel
from rich.progress import track
from datetime import datetime
import platform
import pytz

def get_file_metadata(file_path):
    file_stats = os.stat(file_path)
    file_info = Path(file_path)
    
    file_metadata = {
        "File Path": str(file_info),
        "File Name": file_info.name,
        "File Extension": file_info.suffix if file_info.suffix else "None",
        "File Size (Bytes)": file_stats.st_size,
        "File Size (KB)": file_stats.st_size / 1024,
        "File Size (MB)": file_stats.st_size / (1024 * 1024),
        "Creation Time": datetime.fromtimestamp(file_stats.st_ctime),
        "Last Access Time": datetime.fromtimestamp(file_stats.st_atime),
        "Last Modified Time": datetime.fromtimestamp(file_stats.st_mtime),
        "File Permissions": oct(file_stats.st_mode & 0o777),
        "Owner": file_stats.st_uid,
        "Group": file_stats.st_gid,
        "File Type": "Directory" if os.path.isdir(file_path) else "File",
        "Is Readable": os.access(file_path, os.R_OK),
        "Is Writable": os.access(file_path, os.W_OK),
        "Is Executable": os.access(file_path, os.X_OK),
        "Operating System": platform.system(),
        "Architecture": platform.architecture()[0],
        "Timezone": pytz.timezone("UTC").localize(datetime.now()).strftime("%Z"),
    }
    
    return file_metadata

def print_metadata(metadata):
    console = Console()
    table = Table(show_header=True, header_style="bold magenta", show_lines=True)
    
    for key, value in metadata.items():
        table.add_row(Text(str(key), style="bold cyan"), Text(str(value), style="bold green"))
    
    console.print(Panel(table, title="Detailed File Metadata", title_align="center", expand=False))

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)
    
    metadata = get_file_metadata(filename)
    print_metadata(metadata)

if __name__ == "__main__":
    main()
