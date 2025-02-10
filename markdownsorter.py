import os
import platform
import tkinter as tk
from tkinter import filedialog

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return f"Error reading {file_path}: {e}"

def split_by_headers(content):
    sections = {}
    current_header = None
    for line in content.splitlines():
        if line.startswith("# "):
            current_header = line.strip()
            sections[current_header] = []
        elif line.startswith("* ") and current_header:
            sections[current_header].append(line.strip())
    
    return sections

def sort_sections(sections):
    return {header: sorted(lines) for header, lines in sorted(sections.items())}

def save_sorted_copy(original_path, sorted_sections):
    copy_path = original_path + ".sorted_copy"
    with open(copy_path, 'w', encoding='utf-8') as file:
        for header, lines in sorted_sections.items():
            file.write(f"{header}\n")
            for line in lines:
                file.write(f"{line}\n")
            file.write("\n")  
    
    system_name = platform.system()
    if system_name == "Windows":
        os.system(f"notepad {copy_path}")
    elif system_name == "Darwin":  # macOS
        os.system(f"open -e {copy_path}")
    elif system_name == "Linux":
        os.system(f"xdg-open {copy_path}")

def read_cpt_and_spec_files():
    root = tk.Tk()
    root.withdraw()  
    file_paths = filedialog.askopenfilenames(title="Select md files", filetypes=[("md files", "*.cpt *.spec *.md")])
    
    for file_path in file_paths:
        content = read_file(file_path)
        sections = split_by_headers(content)
        sorted_sections = sort_sections(sections)
        save_sorted_copy(file_path, sorted_sections)

if __name__ == "__main__":
    read_cpt_and_spec_files()
