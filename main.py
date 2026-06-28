"""
Smart AI Event Management Assistant

Application Entry Point
"""

from rich.console import Console

from config.settings import (
    APP_NAME,
    APP_VERSION,
    DATABASE_URL,
)

console = Console()


def main() -> None:
    """
    Starts the application.
    """

    console.print()

    console.rule("[bold blue]Smart AI Event Management Assistant")

    console.print(f"[green]Application :[/green] {APP_NAME}")

    console.print(f"[green]Version     :[/green] {APP_VERSION}")

    console.print(f"[green]Database    :[/green] {DATABASE_URL}")

    console.print()

    console.print(
        "[bold green]Project setup completed successfully![/bold green]"
    )


if __name__ == "__main__":
    main()