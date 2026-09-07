import pytest
from greetlab.cli import main


def test_empty_name(monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["sdt-greet", "--name", "   "]
    )

    with pytest.raises(SystemExit):
        main()