"""
test_agent.py - Comprehensive automated test suite for Ariya AI Career Agent.
Validates LinkedIn deep linking, 300-character limits, ReAct reasoning,
and safety boundaries.
"""

import pytest
from tools import (
    LinkedInDeepLinkTool,
    OutreachGeneratorTool,
    ContentDrafterTool,
    PortfolioKnowledgeTool,
    SafetyAuditTool
)
from agent import AriyaCareerAgent
from server import app

@pytest.fixture
def agent():
    return AriyaCareerAgent()

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c

def test_linkedin_deep_link():
    link = LinkedInDeepLinkTool.get_profile_link()
    assert link == "https://www.linkedin.com/in/ryleen-ariyakutty"

def test_linkedin_feed_share_url():
    url = LinkedInDeepLinkTool.get_feed_share_url("Hello World")
    assert "linkedin.com/feed/?shareActive=true&text=" in url

def test_outreach_character_limit():
    names = ["Alice", "Jonathan Christopher Montgomery III", "Dr. Bob", ""]
    companies = ["Google DeepMind", "Amazon Web Services Cyber Operations", "Startup", ""]
    
    for name in names:
        for comp in companies:
            res = OutreachGeneratorTool.generate_connection_note(name, comp, "Engineering Lead")
            assert res["character_count"] <= 300, f"Exceeded 300 chars: {res['character_count']} for {name} at {comp}"
            assert res["within_limit"] is True
            assert "https://www.linkedin.com/in/ryleen-ariyakutty" in res["profile_url"]

def test_inmail_content():
    res = OutreachGeneratorTool.generate_inmail("Sarah", "Meta", "Director of Engineering")
    msg = res["message"]
    assert "Sarah" in msg
    assert "Meta" in msg
    assert "Western Governors University" in msg
    assert "https://ariya-boop.github.io" in msg

def test_content_drafter_topics():
    topics = ["adversarial-ml", "crypto", "phishing", "game", "general"]
    for t in topics:
        res = ContentDrafterTool.draft_technical_post(t)
        assert len(res["post_content"]) > 100
        assert "feed_share_url" in res
        assert "linkedin.com/feed/?shareActive=true" in res["feed_share_url"]

def test_knowledge_base_retrieval():
    res = PortfolioKnowledgeTool.search_knowledge("Tell me about the adversarial ML project")
    assert res["matches_found"] > 0
    proj = [r for r in res["results"] if r.get("id") == "adversarial-ml-lab"][0]
    assert "Gradient Masking" in str(proj["data"]["metrics"])

    res_edu = PortfolioKnowledgeTool.search_knowledge("Where did Ryleen go to school?")
    assert any(r["type"] == "education" for r in res_edu["results"])

def test_safety_audit():
    safe_text = "Software Engineer with an MS in AI Engineering at Western Governors University."
    audit_safe = SafetyAuditTool.audit_text(safe_text)
    assert audit_safe["is_safe"] is True

    unsafe_text = "Here is my private info: rariya2@wgu.edu and my password"
    audit_unsafe = SafetyAuditTool.audit_text(unsafe_text)
    assert audit_unsafe["is_safe"] is False
    assert len(audit_unsafe["violations"]) > 0

def test_agent_react_reasoning(agent):
    # Test link query
    res1 = agent.reason_and_act("Give me Ryleen's LinkedIn link")
    assert res1["tool_used"] == "LinkedInDeepLinkTool"
    assert "https://www.linkedin.com/in/ryleen-ariyakutty" in res1["deep_link"]

    # Test outreach request
    res2 = agent.reason_and_act("Write an outreach note for Google")
    assert res2["tool_used"] == "OutreachGeneratorTool"

    # Test technical post request
    res3 = agent.reason_and_act("Draft a LinkedIn post on zero knowledge encryption")
    assert res3["tool_used"] == "ContentDrafterTool"

    # Test general question
    res4 = agent.reason_and_act("What are Ryleen's skills?")
    assert res4["tool_used"] == "PortfolioKnowledgeTool"

def test_flask_api(client):
    res = client.get("/api/health")
    assert res.status_code == 200
    assert res.json["status"] == "healthy"

    res_chat = client.post("/api/chat", json={"message": "What is the phishing detector accuracy?"})
    assert res_chat.status_code == 200
    assert "98.93%" in res_chat.json["response"]
