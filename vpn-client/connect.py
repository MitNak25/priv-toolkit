#!/usr/bin/env python3
"""Fetch and display available Proton VPN servers."""

import json
import os
import sys

import requests

API_BASE = "https://api.protonvpn.com/vpn"


def get_token() -> str:
    token = os.environ.get("PROTON_VPN_TOKEN")
    if not token:
        print("Set PROTON_VPN_TOKEN before running this command.", file=sys.stderr)
        raise SystemExit(1)
    return token


def list_servers(token: str) -> object:
    response = requests.get(
        f"{API_BASE}/servers",
        headers={"Authorization": f"Bearer {token}"},
        timeout=(5, 15),
    )
    response.raise_for_status()
    return response.json()


def main() -> int:
    try:
        print(json.dumps(list_servers(get_token()), indent=2))
    except requests.RequestException as exc:
        print(f"Unable to fetch Proton VPN servers: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
