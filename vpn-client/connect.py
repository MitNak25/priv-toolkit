#!/usr/bin/env python3
"""Fetch and display available Proton VPN servers."""

import json
import os
import sys

import requests

API_BASE = "https://api.protonvpn.com/vpn"


def get_token() -> str:
    """Return the API token from the environment without logging it."""
    token = os.environ.get("PROTON_VPN_TOKEN", "").strip()

    if not token:
        print(
            "Set PROTON_VPN_TOKEN before running this command.",
            file=sys.stderr,
        )
        raise SystemExit(1)

    return token


def list_servers(token: str) -> object:
    """Fetch the server list with bounded connection and read timeouts."""
    response = requests.get(
        f"{API_BASE}/servers",
        headers={"Authorization": f"Bearer {token}"},
        timeout=(5, 15),
    )
    response.raise_for_status()
    return response.json()


def main() -> int:
    """Run the command-line client."""
    try:
        servers = list_servers(get_token())
        print(json.dumps(servers, indent=2))

    except requests.RequestException as exc:
        print(f"Unable to fetch Proton VPN servers: {exc}", file=sys.stderr)
        return 2

    except ValueError as exc:
        print(
            f"Received invalid JSON from Proton VPN: {exc}",
            file=sys.stderr,
        )
        return 3

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
