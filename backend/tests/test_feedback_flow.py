"""Keep a weak fact, regenerate, and the same fact comes back strong (status overlay is read)."""
from fastapi.testclient import TestClient

import app.main as main
from app.schema import ContactNote, Evidence, Fact
from app.stores import MarkdownContactStore

MODEL_OUT = 'Subject: s\n\n王老师：\n\n祝您和<hl ref="fact:f2">李阿姨</hl>身体健康。'


def test_keep_then_regenerate_is_strong(tmp_path, monkeypatch):
    note = ContactNote(email="w@example.com", display_name="王建华", scenario="zh_formal",
                       facts=[Fact(id="f2", text="他的妻子是李阿姨", evidence=[Evidence(message_id="m1", quote="李阿姨")])])
    d = tmp_path / "contacts"
    d.mkdir()
    (d / "w@example.com.md").write_text("---\n" + note.model_dump_json(exclude={"body"}) + "\n---\n")
    monkeypatch.setattr(main, "contacts", MarkdownContactStore(d, tmp_path / "status.json"))
    monkeypatch.setattr(main.llm, "complete", lambda *_: MODEL_OUT)
    monkeypatch.setattr(main, "RECORD", False)
    client = TestClient(main.app)
    req = {"mode": "compose", "to": "w@example.com", "brief": "x"}

    first = client.post("/draft", json=req).json()
    h = first["highlights"][0]
    assert h["ref"] == {"kind": "fact", "id": "f2"} and h["strength"] == "weak"

    fb = client.post("/feedback", json={"draft_id": first["draft_id"], "highlight_id": h["id"], "action": "accept"})
    assert fb.json()["status"] == "confirmed"

    second = client.post("/draft", json=req).json()
    assert second["highlights"][0]["strength"] == "strong"
