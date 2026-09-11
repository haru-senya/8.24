import pytest
from greetlab.cli import main


def test_normal_name(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["sdt-greet", "--name", "Alice"])

    main()

    captured = capsys.readouterr()

    assert "Hello, Alice!" in captured.out


def test_empty_name(monkeypatch):
    monkeypatch.setattr("sys.argv", ["sdt-greet", "--name", "   "])

    with pytest.raises(SystemExit) as exc:
        main()

    assert exc.value.code == 2
