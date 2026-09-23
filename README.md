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
```

On Windows PowerShell, activate the virtual environment with:

```powershell
.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Usage

Set the API token as an environment variable:

```bash
export PROTON_VPN_TOKEN="your-token"
```

On Windows PowerShell:

```powershell
$env:PROTON_VPN_TOKEN = "your-token"
```

Run the client:

```bash
python vpn-client/connect.py
```

The client uses:

- a 5-second connection timeout
- a 15-second read timeout
- bearer-token authentication
- non-zero exit codes for missing tokens, request failures, and invalid JSON

Confirm that the endpoint and authentication method match the Proton API
contract you intend to use before production deployment.

## Tests

Install the development tools:

```bash
pip install pytest ruff
```

Run linting:

```bash
ruff check .
```

Run the tests:

```bash
pytest -q
```

## Security

Never commit API tokens or other credentials. Use environment variables or a
secrets manager for local and production deployments.
