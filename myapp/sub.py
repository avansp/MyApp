import typer
from loguru import logger


app = typer.Typer(add_completion=False, help="Sub command written in separate py file.")


@app.command()
def show(name: str = typer.Argument(..., help="Name argument.")):
    """
    An example of sub command.
    """
    logger.info(f"Show under sub command is called.")
    logger.debug(f"Argument name = {name}")
    typer.echo(f"Hello {name}!")
