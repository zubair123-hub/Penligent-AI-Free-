"""CLI Commands for Penligent AI"""

import typer
import json
from typing import Optional
from rich.console import Console
from rich.table import Table

app = typer.Typer(help="Penligent AI - Advanced Pentesting Framework")
console = Console()


@app.command()
def version() -> None:
    """Show version information"""
    console.print("[bold cyan]Penligent AI[/bold cyan] v0.1.0")
    console.print("Advanced AI-Powered Pentesting Suite")


@app.command()
def scan(
    target: str = typer.Argument(..., help="Target IP or hostname"),
    scan_type: str = typer.Option("full", help="Scan type: full, quick, aggressive"),
    timeout: int = typer.Option(30, help="Scan timeout in seconds")
) -> None:
    """Start a new pentesting scan"""
    console.print(f"[bold green]Starting {scan_type} scan on {target}[/bold green]")
    console.print(f"Timeout: {timeout}s")
    console.print("[yellow]Scan in progress...[/yellow]")


@app.command()
def analyze(
    scan_id: str = typer.Argument(..., help="Scan ID to analyze"),
    use_ai: bool = typer.Option(True, help="Use AI analysis")
) -> None:
    """Analyze scan results"""
    console.print(f"[bold blue]Analyzing scan {scan_id}[/bold blue]")
    if use_ai:
        console.print("[yellow]Running AI vulnerability analysis...[/yellow]")


@app.command()
def report(
    scan_id: str = typer.Argument(..., help="Scan ID"),
    output_format: str = typer.Option("pdf", help="Output format: pdf, json, html")
) -> None:
    """Generate security report"""
    console.print(f"[bold magenta]Generating {output_format} report for scan {scan_id}[/bold magenta]")


@app.command()
def gui() -> None:
    """Launch GUI interface"""
    console.print("[bold cyan]Launching Penligent AI GUI...[/bold cyan]")
    try:
        from ..gui.app import run_gui
        run_gui()
    except ImportError:
        console.print("[red]Error: GUI dependencies not installed. Install with: pip install PyQt5[/red]")


@app.command()
def config() -> None:
    """Show configuration"""
    console.print("[bold yellow]Current Configuration:[/bold yellow]")
    from ..core.config import Config
    cfg = Config()
    table = Table(title="Configuration")
    table.add_column("Setting", style="cyan")
    table.add_column("Value", style="magenta")
    for key, value in cfg.to_dict().items():
        table.add_row(key, str(value))
    console.print(table)


def main():
    """Main CLI entry point"""
    app()


if __name__ == "__main__":
    main()
