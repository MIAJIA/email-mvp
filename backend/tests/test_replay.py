"""Replay mode serves every recording through the real HTTP surface, without the model."""
import importlib
import json
import os

from fastapi.testclient import TestClient

from app.stores import REPO


def test_replay_serves_all_recordings(monkeypatch):
    monkeypatch.setenv("REPLAY", "1")
    import app.llm
    monkeypatch.setattr(app.llm, "complete", lambda *_: (_ for _ in ()).throw(AssertionError("model called in replay")))
    import app.main
    main = importlib.reload(app.main)
    client = TestClient(main.app)
    recs = sorted((REPO / "recordings").glob("*.json"))
    assert len(recs) >= 3
    for p in recs:
        rec = json.loads(p.read_text())
        r = client.post("/draft", json=rec["request"])
        assert r.status_code == 200, p.name
        assert r.json() == rec["response"]
    assert client.get("/contacts").status_code == 200
    os.environ.pop("REPLAY", None)
    importlib.reload(app.main)
