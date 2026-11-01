"""
server.py - Flask Web Server & REST API for Ariya AI Career Agent.
Provides REST endpoints and web interface with direct LinkedIn deep-linking.
"""

from flask import Flask, request, jsonify, render_template
from agent import AriyaCareerAgent
from tools import OutreachGeneratorTool, ContentDrafterTool, LinkedInDeepLinkTool

app = Flask(__name__, template_folder="templates")
agent = AriyaCareerAgent()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat_endpoint():
    data = request.get_json(force=True, silent=True) or {}
    message = data.get("message", "").strip()
    if not message:
        return jsonify({"error": "Empty message"}), 400
    
    result = agent.reason_and_act(message)
    return jsonify(result)

@app.route("/api/outreach", methods=["POST"])
def outreach_endpoint():
    data = request.get_json(force=True, silent=True) or {}
    name = data.get("name", "Hiring Manager")
    company = data.get("company", "Engineering Team")
    role = data.get("role", "Engineering Leader")
    focus = data.get("focus", "ai_security")
    
    note_res = OutreachGeneratorTool.generate_connection_note(name, company, role, focus)
    inmail_res = OutreachGeneratorTool.generate_inmail(name, company, role, focus)
    return jsonify({
        "connection_note": note_res,
        "inmail": inmail_res,
        "linkedin_url": LinkedInDeepLinkTool.get_profile_link()
    })

@app.route("/api/post", methods=["POST"])
def post_endpoint():
    data = request.get_json(force=True, silent=True) or {}
    topic = data.get("topic", "adversarial-ml")
    res = ContentDrafterTool.draft_technical_post(topic)
    return jsonify(res)

@app.route("/api/health", methods=["GET"])
def health_endpoint():
    return jsonify({
        "status": "healthy",
        "agent": agent.name,
        "linkedin_target": LinkedInDeepLinkTool.get_profile_link()
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=False)
