import os
import sys
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import subprocess
import time

console = Console()

def print_banner():
    banner = """
████████╗██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███████╗     ██████╗███████╗ ██████╗ 
╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██╔═══██╗██╔════╝    ██╔════╝██╔════╝██╔═══██╗
   ██║   ███████║███████║██╔██╗ ██║██║   ██║███████╗    ██║     █████╗  ██║   ██║
   ██║   ██╔══██║██╔══██║██║╚██╗██║██║   ██║╚════██║    ██║     ██╔══╝  ██║   ██║
   ██║   ██║  ██║██║  ██║██║ ╚████║╚██████╔╝███████║    ╚██████╗███████╗╚██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝     ╚═════╝╚══════╝ ╚═════╝ 
    """
    console.print(Panel(Text(banner, style="bold cyan"), title="[bold yellow]Developer: @thanosceo"))

def install_requirements():
    required_packages = [
        'telethon',
        'pyrogram',
        'rich',
        'pyfiglet',
        'pillow',
        'faker',
        'licensing',
        'requests',
        'configparser',
        'asyncio'
    ]

    console.print("\n[bold yellow]Installing required packages...[/bold yellow]")
    
    for package in required_packages:
        try:
            console.print(f"[cyan]Installing {package}...[/cyan]")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            console.print(f"[green]✓ Successfully installed {package}[/green]")
        except Exception as e:
            console.print(f"[red]✗ Failed to install {package}: {str(e)}[/red]")
        time.sleep(0.5)

def setup_directories():
    directories = ['sessions', 'data']
    
    console.print("\n[bold yellow]Setting up directories...[/bold yellow]")
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            console.print(f"[green]✓ Created directory: {directory}[/green]")
        else:
            console.print(f"[blue]• Directory already exists: {directory}[/blue]")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()
    
    console.print("\n[bold green]Starting installation process...[/bold green]")
    
    install_requirements()
    setup_directories()
    
    console.print("\n[bold green]Installation completed successfully![/bold green]")
    console.print("[yellow]Developer: @thanosceo[/yellow]")
    console.print("[cyan]You can now run the main script.[/cyan]")

if __name__ == "__main__":
    main()