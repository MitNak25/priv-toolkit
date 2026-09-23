import importlib.util
from pathlib import Path
from unittest.mock import Mock, patch

MODULE_PATH = Path(__file__).resolve().parents[1] / "vpn-client" / "connect.py"

spec = importlib.util.spec_from_file_location("connect", MODULE_PATH)
assert spec is not None
assert spec.loader is not None

connect = importlib.util.module_from_spec(spec)
spec.loader.exec_module(connect)


def test_list_servers_uses_timeout_and_authentication():
    response = Mock()
    response.json.return_value = {"servers": []}
    response.raise_for_status.return_value = None

    with patch.object(connect.requests, "get", return_value=response) as get:
        result = connect.list_servers("secret")

    assert result == {"servers": []}

    get.assert_called_once_with(
        "https://api.protonvpn.com/vpn/servers",
        headers={"Authorization": "Bearer secret"},
        timeout=(5, 15),
    )


def test_get_token_reads_environment_variable(monkeypatch):
    monkeypatch.setenv("PROTON_VPN_TOKEN", "secret-token")

    assert connect.get_token() == "secret-token"


def test_get_token_rejects_missing_token(monkeypatch):
    monkeypatch.delenv("PROTON_VPN_TOKEN", raising=False)

    try:
        connect.get_token()
    except SystemExit as exc:
        assert exc.code == 1
    else:
        raise AssertionError("get_token() should exit when the token is missing")


def test_main_returns_error_for_request_failure():
    with patch.object(
        connect,
        "list_servers",
        side_effect=connect.requests.RequestException("network error"),
    ):
        with patch.object(connect, "get_token", return_value="secret"):
            assert connect.main() == 2


def test_main_returns_error_for_invalid_json():
    with patch.object(
        connect,
        "list_servers",
        side_effect=ValueError("invalid JSON"),
    ):
        with patch.object(connect, "get_token", return_value="secret"):
            assert connect.main() == 3
