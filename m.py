import vars
from rich import print as rishabh
from rich.prompt import Prompt
from rich.align import Align
from rich.console import Console

# Color scheme - using Rich's named colors
pk = "thistle1"
lg = "green_yellow"
WHITE = "white"

# Create console for centering
console = Console()

def display_menu():
    # ASCII header with proper markup
    header = (
        f"[{pk}]█▀▀ █░░ █▀█ █▄░█ █▀▀ █▀█[/]\n"
        f"[{pk}]█▄▄ █▄▄ █▄█ █░▀█ ██▄ █▀▄[/]\n"
        f"[{lg}]Developer - @mufasapro[/]"
    )
    
    # Print centered header using console
    console.print(header, justify="left")
    rishabh()  # Empty line for spacing

    # Menu items in demo format
    menu_items = [
        ("PhoneNumber", vars.vars["PhoneNumber"]),
        ("ToGroup", vars.vars["ToGroup"]),
        ("EnterStop", vars.vars["EnterStop"]),
        ("Language", vars.vars["Language"]),
        ("Per_account_add", vars.vars["Per_account_add"]),
        ("StartingAccount", vars.vars["StartingAccount"]),
        ("EndAccount", vars.vars["EndAccount"]),
        ("Message_file", vars.vars["Message_file"] or "Empty"),
        ("USERNAME", vars.vars["USERNAME"] or "Empty"),
        ("last_seen", f"{vars.vars['last_seen']} sec")
    ]

    # List format
    for idx, (name, value) in enumerate(menu_items, 1):
        rishabh(
            f"[{lg}]<{idx}>[/] "
            f"[{pk}]{name}:[/] "
            f"[{lg}]{value}[/]"
        )
    
    rishabh(f"\n[{pk}]<0>[/] [{lg}]Back to main menu[/]")

def update_var(index):
    var_map = {
        1: "PhoneNumber",
        2: "ToGroup",
        3: "EnterStop",
        4: "Language",
        5: "Per_account_add",
        6: "StartingAccount",
        7: "EndAccount",
        8: "Message_file",
        9: "USERNAME",
        10: "last_seen"
    }
    
    var_name = var_map[index]
    current = vars.vars[var_name]
    
    # Fixed prompt markup
    prompt_text = f"[{lg}]Enter new {var_name}[/] (current: [{WHITE}]{current}[/])"
    new_val = Prompt.ask(prompt_text, default=str(current))
    
    # Preserve original data types
    if var_name in ["PhoneNumber", "EnterStop", "Per_account_add", 
                   "StartingAccount", "EndAccount", "last_seen"]:
        new_val = int(new_val)
    elif var_name in ["Message_file", "USERNAME"] and new_val == "Empty":
        new_val = ""
    
    vars.vars[var_name] = new_val
    rishabh(f"[{lg}]✓ Updated![/]\n")

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
            f"[{lg}]Select option to change (0-10)[/]",
            choices=[str(i) for i in range(0, 11)],
            show_choices=False
        )
        
        if choice == "0":
            rishabh(f"[{lg}]Exiting...[/]")
            break
            
        update_var(int(choice))
        save_changes()

configchange()