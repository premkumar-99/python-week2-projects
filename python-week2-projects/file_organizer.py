"""
File Organizer Script
- Scans a folder and moves files into subfolders by extension
- Handles name collisions
- Supports --dry-run and logging of moved files
"""
import os
import shutil
import argparse
import logging
from collections import defaultdict

LOG_FILE = "file_organizer.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

EXT_MAP = {
    "images": {".png", ".jpg", ".jpeg", ".gif", ".bmp"},
    "documents": {".pdf", ".docx", ".doc", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"},
    "archives": {".zip", ".tar", ".gz", ".rar"},
    "code": {".py", ".js", ".java", ".c", ".cpp", ".html", ".css"},
    "videos": {".mp4", ".mkv", ".mov"},
    "audio": {".mp3", ".wav", ".flac"}
}

def categorize(ext):
    ext = ext.lower()
    for cat, exts in EXT_MAP.items():
        if ext in exts:
            return cat
    return "others"

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def unique_path(dest_dir, filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    target = os.path.join(dest_dir, filename)
    while os.path.exists(target):
        target = os.path.join(dest_dir, f"{base} ({counter}){ext}")
        counter += 1
    return target

def organize(folder, dry_run=False):
    moved = defaultdict(list)
    for entry in os.listdir(folder):
        src = os.path.join(folder, entry)
        if os.path.isdir(src):
            continue
        _, ext = os.path.splitext(entry)
        cat = categorize(ext)
        dest_dir = os.path.join(folder, cat)
        ensure_dir(dest_dir)
        dest_path = unique_path(dest_dir, entry)
        if dry_run:
            logging.info(f"[DRY-RUN] Would move {src} -> {dest_path}")
            moved[cat].append((src, dest_path))
        else:
            shutil.move(src, dest_path)
            logging.info(f"Moved {src} -> {dest_path}")
            moved[cat].append((src, dest_path))
    return moved

def main():
    parser = argparse.ArgumentParser(description="Organize files in a folder by extension")
    parser.add_argument("folder", help="Target folder to organize")
    parser.add_argument("--dry-run", action="store_true", help="Show actions without moving files")
    args = parser.parse_args()
    folder = args.folder
    if not os.path.isdir(folder):
        print("Folder not found.")
        return
    moved = organize(folder, dry_run=args.dry_run)
    for cat, items in moved.items():
        print(f"{cat}: {len(items)} files")
    print("Done. Check", LOG_FILE, "for details.")

if __name__ == '__main__':
    main()
