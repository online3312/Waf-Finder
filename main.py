import requests
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.padding import Padding

def check_waf(url):
    console = Console()
    
    try:
        response = requests.get(url)
        
        # WAF detection signatures and information
        waf_signatures = {
            "Cloudflare": {
                "signature": "cloudflare",
                "description": "Cloudflare provides DDoS protection, WAF, and CDN functionality as a leading web security solution."
            },
            "Incapsula": {
                "signature": "incapsula",
                "description": "Incapsula is a web security service from Imperva, offering WAF and DDoS protection features."
            },
            "Sucuri": {
                "signature": "sucuri",
                "description": "Sucuri offers WAF, monitoring, and DDoS protection for website security."
            },
            "Akamai": {
                "signature": "akamai",
                "description": "Akamai provides high-performance CDN along with robust web application security."
            },
            "ModSecurity": {
                "signature": "mod_security",
                "description": "ModSecurity is an open-source web application firewall used across various web servers."
            },
            "F5 Networks": {
                "signature": "f5",
                "description": "F5 Networks offers L7 security, load balancing, and WAF functionalities through its network devices."
            },
            "FortiWeb": {
                "signature": "fortiweb",
                "description": "Fortinet's FortiWeb provides web application firewall and advanced threat protection."
            }
        }
        
        detected_waf = None
        for waf_name, waf_info in waf_signatures.items():
            if waf_info['signature'] in response.headers.get('Server', '').lower() or waf_info['signature'] in response.text.lower():
                detected_waf = waf_name
                waf_description = waf_info['description']
                break

        if detected_waf:
            table = Table(title="WAF Detection Result")
            table.add_column("Attribute", style="cyan", no_wrap=True)
            table.add_column("Details", style="magenta")

            table.add_row("WAF Name", detected_waf)
            table.add_row("Description", waf_description)
            table.add_row("URL", url)

            console.print(Panel(table, title="[bold green]WAF Detected[/bold green]", border_style="green"))
        else:
            text = Text("No WAF detected on the provided URL.", style="bold red")
            console.print(Panel(Padding(text, (1, 2)), title="[bold red]WAF UnDetected[/bold red]", border_style="red"))
    
    except requests.exceptions.RequestException as e:
        text = Text(f"An error occurred: {e}", style="bold red")
        console.print(Panel(Padding(text, (1, 2)), title="[bold red]Error[/bold red]", border_style="red"))

if __name__ == "__main__":
    url = input("Enter the URL: ")
    check_waf(url)
