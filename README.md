# Priv‑Toolkit

**A privacy‑first toolbox built on Proton services** (VPN, Drive, Pass, Lumo).  
Each sub‑folder contains a small, self‑contained utility that:

* Keeps secrets encrypted locally (AES‑256 via `cryptography`).
* Communicates with Proton APIs over HTTPS with OAuth tokens.
* Leaves **no raw logs** on disk – everything is either in‑memory or stored in an encrypted SQLite DB.

## Table of Contents

- [Modules](#modules)
- [Installation](#installation)
- [Usage examples](#usage-examples)
- [Contributing](#contributing)
- [License](#license)

## Modules

| Folder | Purpose | Quick start |
|--------|---------|------------|
| `vpn-client/` | Auto‑connect to the fastest Proton VPN server, rotate exit nodes, store encrypted stats. | `cd vpn-client && ./connect.py` |
| `secure-share/` | Upload a file to Proton Drive and generate a temporary share link. | `python upload.py myfile.pdf` |
| `pass-manager/` | Generate strong passwords and store them in Proton Pass. | `python gen.py` |
| `lumo-assistant/` | Ask Lumo questions from the terminal – zero‑access encryption, no logs. | `python ask.py "How can I encrypt a zip?"` |
| `audit-suite/` | Scan your machine for common privacy leaks and produce an encrypted markdown report. | `python scan.py` |

## Installation

```bash
# Clone the repo
git clone https://github.com/MitNak25/priv-toolkit.git
cd priv-toolkit

# Set up a virtual environment
python3 -m venv .venv
source .venv/bin/activate   # Windows: .\.venv\Scripts\activate

# Install shared dependencies
pip install -r requirements.txt
