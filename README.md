# 🔒 Priv-Toolkit

> A privacy-first Python toolbox for small, security-conscious command-line utilities.

![Python](https://img.shields.io/badge/Python-3.9%2B-3776ab?logo=python&logoColor=fff)
![CI](https://img.shields.io/badge/CI-Ruff%20%2B%20Pytest-4c1)
![License](https://img.shields.io/badge/license-see%20LICENSE-blue)

## 🎯 Project status

This repository currently contains one implemented utility: a Proton VPN server-list client. Additional Drive, Pass, Lumo, and audit integrations are planned but are not implemented or exposed as commands yet.

## ✨ Principles

- Credentials come from environment variables, never hard-coded files.
- Tokens are not printed in normal output or error messages.
- Network requests use bounded connection and read timeouts.
- HTTP failures and invalid JSON return non-zero exit codes.
- Small modules, explicit behavior, and testable code are preferred.

## 🧰 Current functionality

| Path | Purpose |
| --- | --- |
| [`vpn-client/connect.py`](vpn-client/connect.py) | Fetch and print the available Proton VPN servers as formatted JSON. |
| [`tests/test_connect.py`](tests/test_connect.py) | Tests for token handling and request behavior. |
| [`requirements.txt`](requirements.txt) | Runtime dependency constraints. |
| [`.github/workflows/ci.yml`](.github/workflows/ci.yml) | Ruff and Pytest checks. |

## 🚀 Installation

### Requirements

- Python 3.9 or newer
- Internet access
- A valid Proton VPN API token

```bash
git clone https://github.com/MitNak25/priv-toolkit.git
cd priv-toolkit
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## ▶️ Usage

Set the token only in the current shell session:

```bash
export PROTON_VPN_TOKEN="your-token"
python vpn-client/connect.py
```

PowerShell:

```powershell
$env:PROTON_VPN_TOKEN = "your-token"
python vpn-client/connect.py
```

The client calls the Proton VPN server endpoint with bearer authentication and prints the JSON response. It uses a 5-second connection timeout and a 15-second read timeout.

### Exit codes

| Code | Meaning |
| ---: | --- |
| `0` | Request completed successfully. |
| `1` | `PROTON_VPN_TOKEN` is missing. |
| `2` | Network or HTTP request failed. |
| `3` | The API returned invalid JSON. |

## 🧪 Development

Install the development tools and run the checks:

```bash
pip install pytest ruff
ruff check .
pytest -q
```

GitHub Actions runs these checks for pushes and pull requests to `main`.

## 🔐 Security

Do not commit API tokens, `.env` files, shell history containing secrets, or captured API responses containing sensitive data. Confirm the endpoint and authentication method against the Proton API contract before production use. For production deployments, prefer a secret manager and least-privilege credentials.

## 📄 License

See [LICENSE](LICENSE).
