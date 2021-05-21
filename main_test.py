from main import main


def test_main(monkeypatch):
    monkeypatch.setattr("sys.argv", ['python3', '20', 'c', 'f'])
    assert main() == 68.0
    monkeypatch.setattr("sys.argv", ['python3', '20', 'c', 'c'])
    assert main() == 20.0
    monkeypatch.setattr("sys.argv", ['python3', '20', 'c', 'd'])
    assert main() == "Invalid system enter"
    monkeypatch.setattr("sys.argv", ['python3', '20'])
    assert main() == "Invalid enter"
    monkeypatch.setattr("sys.argv", ['python3', 'a', 'f', 'c'])
    assert main() == "Error"
    monkeypatch.setattr("sys.argv", ['python3', '165', '12', 'c'])
    assert main() == "Invalid system enter"
