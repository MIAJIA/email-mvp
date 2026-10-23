from app.generator import build_catalog, generate, parse, strength_of
from app.schema import ContactNote, DraftRequest, Evidence, Fact, NoteField


def note() -> ContactNote:
    return ContactNote(
        email="w@example.com", display_name="王老师", scenario="zh_formal",
        address_as=NoteField(value="王老师您好", count=3, total=3, evidence=[Evidence(message_id="m1", quote="王老师您好")]),
        honorific=NoteField(value="您", count=3, total=3, evidence=[Evidence(message_id="m1", quote="您")]),
        facts=[Fact(id="rec_letter", text="wrote a recommendation letter", evidence=[Evidence(message_id="m2", quote="推荐信")])],
    )


def test_strength_rule():
    assert strength_of(3, 9, "learned") == "strong"
    assert strength_of(2, 3, "learned") == "weak"
    assert strength_of(3, 20, "learned") == "weak"
    assert strength_of(1, 10, "confirmed") == "strong"


def test_parse_builds_highlights_from_note_not_model():
    cat = build_catalog(note(), None, [])
    raw = 'Subject: 好消息\n\n<hl ref="address_as">王老师您好</hl>，\n\n谢谢<hl ref="honorific">您</hl>的<hl ref="fact:rec_letter">推荐信</hl>。'
    subject, segs, hls, warns = parse(raw, cat)
    assert subject == "好消息"
    assert "".join(s.text for s in segs) == "王老师您好，\n\n谢谢您的推荐信。"
    assert [h.ref.kind for h in hls] == ["address_as", "honorific", "fact"]
    assert hls[0].rationale == 'You addressed 王老师 as "王老师您好" in 3 of 3 emails.'
    assert hls[0].evidence[0].quote == "王老师您好"
    assert warns == []
    ids = {h.id for h in hls}
    assert all(s.highlight_id in ids for s in segs if s.highlight_id)


def test_unknown_ref_degrades_to_plain_segment_with_warning():
    cat = build_catalog(note(), None, [])
    _, segs, hls, warns = parse('Subject: x\n\nHi <hl ref="fact:made_up">we met in Paris</hl>.', cat)
    assert hls == []
    assert all(s.highlight_id is None for s in segs)
    assert "".join(s.text for s in segs) == "Hi we met in Paris."
    assert len(warns) == 1 and "fact:made_up" in warns[0]


def test_rejected_entries_are_not_offered_to_the_model():
    n = note()
    n.honorific.status = "rejected"
    assert "honorific" not in build_catalog(n, None, [])


def test_generate_with_fake_model():
    d = generate(DraftRequest(to="w@example.com", brief="thanks"), note(), None, [],
                 lambda p: 'Subject: s\n\n<hl ref="address_as">王老师您好</hl>')
    assert d.scenario == "zh_formal" and len(d.highlights) == 1


def test_inject_unknown_ref_degrades_second_tag():
    d = generate(DraftRequest(to="w@example.com", brief="x", inject="unknown_ref"), note(), None, [],
                 lambda p: 'Subject: s\n\n<hl ref="address_as">王老师您好</hl>，谢谢<hl ref="honorific">您</hl>')
    assert [h.ref.kind for h in d.highlights] == ["address_as"]
    assert any("fact:injected_unknown" in w for w in d.warnings)
    assert "".join(s.text for s in d.segments) == "王老师您好，谢谢您"
