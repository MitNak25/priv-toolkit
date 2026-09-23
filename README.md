# Priv-Toolkit

A privacy-focused Python toolbox.

The currently implemented module is a small Proton VPN API client. It reads
`PROTON_VPN_TOKEN` from the environment, requests the available server list,
and prints the response as formatted JSON.

No credentials are written to disk or printed in error messages.

## Current module

| Path | Purpose |
| --- | --- |
| `vpn-client/connect.py` | Fetch and display available Proton VPN servers. |

The previously planned Drive, Pass, Lumo, and audit modules are not implemented
yet and are not advertised as available commands.

## Requirements

- Python 3.9 or newer
- A valid Proton VPN API token
- Internet access

## Installation

```bash
git clone https://github.com/MitNak25/priv-toolkit.git
cd priv-toolkit

python3 -m venv .venv
source .venv/bin/activate
