#!/usr/bin/env python3
"""Fetch and display the list of available Proton VPN servers."""

import json
import os
import sys

import requests

API_BASE = "https://api.protonvpn.com/vpn"


def get_token() -> str:
    """Read the API token from the environment."""
    token = os.getenv("PROTON_VPN_TOKEN")
    if not token:
        print("Set PROTON_VPN_TOKEN before running this command.", file=sys.stderr)
        raise SystemExit(1)
    return token


def list_servers(token: str) -> object:
    """Request the available servers with a bounded network timeout."""
    response = requests.get(
        f"{API_BASE}/servers",
        headers={"Authorization": f"Bearer {token}"},
        timeout=15,
    )
    response.raise_for_status()
    return response.json()


def main() -> None:
    try:
        print(json.dumps(list_servers(get_token()), indent=2))
    except requests.RequestException as exc:
        print(f"Unable to fetch Proton VPN servers: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc


if __name__ == "__main__":
    main()
