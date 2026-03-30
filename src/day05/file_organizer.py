"""
Day 5 - Mini Project: File Organizer
=====================================
Organises files in a directory into sub-folders by type.
Uses: os, pathlib, shutil, datetime — all from the standard library.

Usage:
    python file_organizer.py                  ← prompts for a directory
    python file_organizer.py path/to/folder  ← uses argument directly
    python file_organizer.py --dry-run       ← preview without moving
"""

import os
import sys
import shutil
from pathlib import Path
from datetime import datetime


class FileOrganizer:
    """Organises files in a directory into category sub-folders."""

    FILE_TYPES = {
        "Images":    [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
        "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".md"],
        "Videos":    [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
        "Audio":     [".mp3", ".wav", ".flac", ".aac", ".ogg"],
        "Archives":  [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Code":      [".py", ".js", ".ts", ".html", ".css", ".java", ".cpp", ".c"],
    }

    def __init__(self, target_directory, dry_run=False):
        self.target_dir = Path(target_directory)
        self.dry_run = dry_run
        self.moved = 0
        self.skipped = 0

    # ----------------------------------------------------------
    # Public interface
    # ----------------------------------------------------------

    def organise(self):
        """Scan the target directory and move files into category folders."""
        if not self.target_dir.exists():
            print(f"Directory '{self.target_dir}' does not exist.")
            return

        if self.dry_run:
            print("(DRY RUN — no files will be moved)\n")

        for file_path in self.target_dir.iterdir():
            if file_path.is_file():
                self._move_file(file_path)

        print(f"\nDone!  Moved: {self.moved}  |  Skipped (no match): {self.skipped}")

    def list_files(self):
        """Print all files in the target directory tree."""
        print(f"\nContents of '{self.target_dir}':")
        for item in sorted(self.target_dir.rglob("*")):
            if item.is_file():
                print(f"  {item.relative_to(self.target_dir)}")

    # ----------------------------------------------------------
    # Private helpers
    # ----------------------------------------------------------

    def _get_category(self, extension):
        """Return the category name for a file extension, or None."""
        ext = extension.lower()
        for category, extensions in self.FILE_TYPES.items():
            if ext in extensions:
                return category
        return None

    def _unique_destination(self, folder, filename, extension):
        """Return a destination Path that does not clash with an existing file."""
        destination = folder / filename
        if destination.exists():
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            stem = Path(filename).stem
            destination = folder / f"{stem}_{timestamp}{extension}"
        return destination

    def _move_file(self, file_path):
        """Move a single file to its category folder."""
        category = self._get_category(file_path.suffix)

        if category is None:
            print(f"  [SKIP]  {file_path.name}  (unknown type)")
            self.skipped += 1
            return

        dest_folder = self.target_dir / category
        destination = self._unique_destination(dest_folder, file_path.name, file_path.suffix)

        action = "PREVIEW" if self.dry_run else "MOVE"
        print(f"  [{action}]  {file_path.name}  →  {category}/")

        if not self.dry_run:
            dest_folder.mkdir(parents=True, exist_ok=True)
            shutil.move(str(file_path), str(destination))

        self.moved += 1


# TODO: Add an undo() method that reads a log file and reverses all moves
# TODO: Add a config_from_file() classmethod to load custom FILE_TYPES from JSON
# TODO: Add an --extension flag to let the user add custom mappings at runtime


# ==============================================================
# Entry point
# ==============================================================
if __name__ == "__main__":
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    paths = [a for a in args if not a.startswith("--")]

    if paths:
        directory = paths[0]
    else:
        directory = input("Enter the directory to organise: ").strip()

    organizer = FileOrganizer(directory, dry_run=dry_run)

    print(f"\nTarget directory: {Path(directory).resolve()}")
    if not dry_run:
        print("Files will be MOVED. Press Enter to continue, Ctrl+C to cancel.")
        input()

    organizer.organise()
    organizer.list_files()
