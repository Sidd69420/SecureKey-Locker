from rich.table import Table
from rich.console import Console

console = Console()

def table_creator(search_results):
    if search_results == ([]):
        print("No records available.")
    else:
        search_results = [list(x) for x in search_results]

        s_no = 1
        for result in search_results:
            result.insert(0, str(s_no))
            s_no += 1

        table = Table(title = "Available Records", header_style = "bold purple")
        table.add_column("S No.", style = "red")
        table.add_column("Website", style = "green")
        table.add_column("Username", style = "blue")
        table.add_column("Password", style = "cyan")

        for entry in search_results:
            table.add_row(*entry)

        console.print(table)
