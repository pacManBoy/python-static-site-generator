import typer
from ssg.site import Site

def main(source = "content", dest = "dist"):
    config = dict(source=source, dest=dest)
    site = Site(**config)
    site.build()

if __name__ == "__main__":
    typer.run(main)