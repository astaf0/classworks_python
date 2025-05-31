from rich.console import Console
from rich.table import Table

products = ['Апельсин', 'Банан']

console = Console()

table = Table(title='Products')
table.add_column('Name', justify='center', style='cyan')
for product in products:
    table.add_row(product)

console.print(table)