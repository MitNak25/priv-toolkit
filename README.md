# Priv-Toolkit

A privacy-focused Python toolbox. The currently implemented module is a small Proton VPN API client that reads `PROTON_VPN_TOKEN` from the environment and does not persist credentials.

## Current module

`vpn-client/connect.py` fetches and prints available Proton VPN servers as formatted JSON. The planned Drive, Pass, Lumo, and audit modules are not implemented yet.

## Installation

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

On Windows PowerShell:

```powershell
.venv\\Scripts\\Activate.ps1
```

## Usage

```bash
export PROTON_VPN_TOKEN="your-token"
python vpn-client/connect.py
```

The client uses bounded connection and read timeouts and does not print the token. Confirm the endpoint and authentication method match the Proton API contract you intend to use before production deployment.

## Checks

```bash
pip install pytest ruff
ruff check .
pytest -q
```

Never commit API tokens or `.env` files.
