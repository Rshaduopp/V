import vars
from rich import print as rishabh_print
from rich.prompt import Prompt
from rich.align import Align
from rich.console import Console
import os
pingk="[thistle1]"
lightg="[green_yellow]"

# Create console for centering
console = Console()
os.system("clear")


def display_menu():
    header = (
        f"{pingk}██████╗░██╗░░░░░██╗░░░██╗███████╗[/]\n"
        f"{pingk}██╔══██╗██║░░░░░██║░░░██║╚════██║[/]\n"
        f"{pingk}██████╔╝██║░░░░░╚██╗░██╔╝░░░░██╔╝[/]\n"
        f"{pingk}██╔═══╝░██║░░░░░░╚████╔╝░░░░██╔╝░[/]\n"
        f"{pingk}██║░░░░░███████╗░░╚██╔╝░░░░██╔╝░░[/]\n"
        f"{pingk}╚═╝░░░░░╚══════╝░░░╚═╝░░░░░╚═╝░░░[/]\n"
        f"{lightg}Developer - @thanosceo[/]"
    )
    
    # Print centered header using console
    console.print(header, justify="left")
    rishabh_print()  # Empty line for spacing

    # Menu items in demo format
    menu_items = [
        ("PhoneNumber", vars.vars["PhoneNumber"]),
        ("ToGroup", vars.vars["ToGroup"]),
        ("Per_account_add", vars.vars["Per_account_add"]),
        ("StartingAccount", vars.vars["StartingAccount"]),
        ("EndAccount", vars.vars["EndAccount"])
    ]

    # List format
    for idx, (name, value) in enumerate(menu_items, 1):
        rishabh_print(
            f"{pingk}<{idx}>[/] "
            f"{lightg}{name}:[/] "
            f"{pingk}{value}[/]"
        )
    
    rishabh_print(f"\n{pingk}<0>[/] {lightg}Back to main menu[/]")

def update_var(index):
    var_map = {
        1: "PhoneNumber",
        2: "ToGroup",
        3: "Per_account_add",
        4: "StartingAccount",
        5: "EndAccount"
    }
    
    var_name = var_map[index]
    current = vars.vars[var_name]
    
    # Fixed prompt markup
    prompt_text = f"{lightg}Enter new {var_name}[/] (current: {pingk}{current}[/])"
    new_val = Prompt.ask(prompt_text, default=str(current))
    
    # Preserve original data types
    if var_name in ["PhoneNumber", "Per_account_add", 
                   "StartingAccount", "EndAccount"]:
        new_val = int(new_val)
    elif var_name in ["Message_file", "USERNAME"] and new_val == "Empty":
        new_val = ""
    
    vars.vars[var_name] = new_val
    rishabh_print(f"{lightg}✓ Updated![/]\n")

def save_changes():
    with open("vars.py", "w") as f:
        f.write("vars = {\n")
        for key, value in vars.vars.items():
            if isinstance(value, str):
                f.write(f'    "{key}": "{value}",\n')
            else:
                f.write(f'    "{key}": {value},\n')
        f.write("}\n")

def configchange():
    while True:
        display_menu()
        # Fixed prompt markup
        choice = Prompt.ask(
            f"{lightg}Select option to change (0-10)[/]",
            choices=[str(i) for i in range(0, 11)],
            show_choices=False
        )
        
        if choice == "0":
            rishabh_print(f"{lightg}Exiting...[/]")
            break
            
        update_var(int(choice))
        save_changes()
  
configchange()      