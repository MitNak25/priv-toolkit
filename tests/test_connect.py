import importlib.util
from pathlib import Path
from unittest.mock import Mock, patch

MODULE_PATH = Path(__file__).resolve().parents[1] / "vpn-client" / "connect.py"
spec = importlib.util.spec_from_file_location("connect", MODULE_PATH)
assert spec and spec.loader
connect = importlib.util.module_from_spec(spec)
spec.loader.exec_module(connect)


def test_list_servers_uses_timeout_and_authentication():
    response = Mock()
    response.json.return_value = {"servers": []}
    response.raise_for_status.return_value = None

    with patch.object(connect.requests, "get", return_value=response) as get:
        assert connect.list_servers("secret") == {"servers": []}

    get.assert_called_once_with(
        "https://api.protonvpn.com/vpn/servers",
        headers={"Authorization": "Bearer secret"},
        timeout=(5, 15),
    )
