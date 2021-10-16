import typer
from ssg.site import Site

def main(source = "Content", dest = "dist"):
    config = dict(source=source, dest=dest)
    site = Site(**config)
    site.build()

typer.run(main)