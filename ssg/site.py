from pathlib import Path

# Below the import you just wrote, create a class called Site. Next, create a Site class constructor that accepts three arguments self, source, and dest.
# In the constructor, convert source to a Path object. This can be done by passing it to a call to Path(). Save the result to an instance attribute with the same name. Hint: instance attributes are prefixed with self.
# Repeat these steps for dest.
class Site:
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)
        
    def create_dir(self, path):
        """
        Find the root directory
        The first part of the path is self.dest. The second part of the path needs to be relative to self.source.
        So after a / operator call relative_to() on path passing in self.source. Hint:  destination / relative_to().
        """
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True) # Replace directoy is exists
        
    def build(self):
        """
        Make the destination directory
        Recreate all paths if source directory
        """
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
        
        