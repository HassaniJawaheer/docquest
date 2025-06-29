import os
import hashlib # For generating hash

class CorpusStateHasher:
    def compute_hash(self, folder_path: str) -> str:
        hash_input = []

        for root, _, files in os.walk(folder_path):
            for name in sorted(files): # Sort files for consistent ordering (for deterministic order)
                path = os.path.join(root, name)
                try:
                    mtime = os.path.getmtime(path) # Get last modified time
                    hash_input.append(f"{name}:{mtime}") # Add file name and mtime
                except FileNotFoundError:
                    continue # Handle deleted files
            combined = "|".join(hash_input).encode("utf-8") # Join metadata and encode as bytes
        return hashlib.md5(combined).hexdigest() # Return MD5 hash as hex string