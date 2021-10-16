from typing import List
from pathlib import Path
import shutil

class Parser:
    def __init__(self):
        self.extensions = List[str]
    
    def valid_extension(self, extension):
        return extension in self.extensions
    
    def parse(self, path, source, dest):
        self.path = Path(path)
        self.source = Path(source)
        self.dest = Path(dest)
        
        raise NotImplementedError("Should be implemented by derived class.")
    
    def read(self, path):
        with open(path, 'r') as file:
            return file.read()
    
    def write(self, path, dest, content, ext=".html"):
        full_path = self.dest / path.with_suffix(ext).name
        with open(full_path, 'w') as file:
            file.write(content)
    
    def copy(self, path, source, dest):
        shutil.copy2(path, dest / path.relative_to(source))
        

class ResourceParser(Parser):
    self.extensions = List[".jpg", ".png", ".gif", ".css", ".html"]
    
    def parse(self, path, source, dest):
        super().copy(path, source, dest)