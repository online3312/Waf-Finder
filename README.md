# WAF Detection Script

This script allows you to detect the presence of a Web Application Firewall (WAF) on a given URL. The script uses specific signatures to identify well-known WAFs and displays detailed information if a WAF is detected.

## Features

- **WAF Detection**: The script identifies common WAFs such as Cloudflare, Incapsula, Sucuri, Akamai, ModSecurity, F5 Networks, and FortiWeb.
- **Detailed Information**: When a WAF is detected, the script provides the WAF's name and a brief description.
- **Beautiful Output**: The script uses the `rich` library to display information in a visually appealing format, with color-coded panels and tables.
- **Error Handling**: The script handles network errors gracefully and informs the user with a clear message.

## Installation

1. Clone this repository or download the `waf.py` file.
2. Install the required dependencies by running:

```bash
pip install requests rich
