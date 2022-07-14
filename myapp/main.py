import typer
from loguru import logger
import sys
from pathlib import Path
from myapp import sub

# reset previous logger, then add console logging
logger.remove()
logger.add(sys.stderr, level="INFO")

# create the main app
app = typer.Typer(add_completion=False)
app.add_typer(sub.app, name="sub")


@app.command()
def info():
    """
    An example of command in main.
    """
    logger.success("Info command is called.")


@app.callback()
def main(log_file: Path = typer.Option(None,
                                       help="External file to store message logs."),
         debug: bool = typer.Option(False, help="Set log level to debug.")):
    """
    This is a skeleton of MyApp.

    For global options, you must call it before commands or sub-commands.
    """
    if debug:
        logger.remove()
        logger.add(sys.stderr, level="DEBUG")

    if log_file is not None:
        # fix home dir
        log_file = log_file.expanduser()

        typer.echo(f"Log file: {log_file}")
        if log_file.is_file():
            logger.warning(f"Log file exist. Replacing it.")
            log_file.unlink()

        logger.add(log_file, level="DEBUG" if debug else "INFO", rotation=None)


if __name__ == "__main__":
    app()

