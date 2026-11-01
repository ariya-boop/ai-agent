"""
agent.py - Autonomous AI Career & Networking Agent for Ryleen Ariyakutty.
Integrates ReAct tool execution with direct deep-linking to LinkedIn.
"""

import sys
import os
import argparse
from typing import Dict, Any, List

from knowledge import PROFILE
from tools import (
    LinkedInDeepLinkTool,
    OutreachGeneratorTool,
    ContentDrafterTool,
    PortfolioKnowledgeTool,
    SafetyAuditTool
)

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.markdown import Markdown
    from rich.table import Table
    console = Console()
except ImportError:
    console = None


class AriyaCareerAgent:
    """
    Autonomous AI Agent representing Ryleen Ariyakutty.
    Understands visitor intent, retrieves factual project metrics,
    drafts LinkedIn connection notes, generates technical LinkedIn posts,
    and constructs direct deep links to LinkedIn.
    """

    def __init__(self):
        self.name = "Ariya AI Agent"
        self.profile = PROFILE
        self.linkedin_url = LinkedInDeepLinkTool.get_profile_link()

    def reason_and_act(self, user_prompt: str) -> Dict[str, Any]:
        """
        Executes an autonomous Observe -> Reason -> Act loop.
        Analyzes the user's intent, chooses the optimal tool,
        and returns structured output with verified facts and LinkedIn deep links.
        """
        p = user_prompt.strip().lower()
        
        # Tool 1: Direct LinkedIn link request
        if any(w in p for w in ["linkedin link", "linkedin profile", "connect with ryleen", "how to contact", "social", "where to reach"]):
            return {
                "intent": "linkedin_profile_query",
                "tool_used": "LinkedInDeepLinkTool",
                "response": (
                    f"You can connect directly with {PROFILE['name']} on LinkedIn:\n\n"
                    f"👉 **[LinkedIn Profile: {PROFILE['name']}]({self.linkedin_url})**\n\n"
                    f"• Professional Email: [{PROFILE['links']['email']}](mailto:{PROFILE['links']['email']})\n"
                    f"• Interactive Portfolio: [{PROFILE['links']['portfolio']}]({PROFILE['links']['portfolio']})\n"
                    f"• GitHub Repositories: [{PROFILE['links']['github']}]({PROFILE['links']['github']})"
                ),
                "deep_link": self.linkedin_url,
                "actions": [{"label": "Open LinkedIn Profile", "url": self.linkedin_url}]
            }

        # Tool 2: LinkedIn Connection / Outreach Generation
        if any(w in p for w in ["outreach", "connection request", "connect note", "reach out", "inmail", "message recruiter"]):
            # Extract basic context or use smart defaults
            company = "your company"
            role = "Engineering Leader"
            if " at " in p:
                parts = p.split(" at ")
                company = parts[-1].split()[0].title()
            
            outreach = OutreachGeneratorTool.generate_connection_note("Hiring Manager", company, role)
            inmail = OutreachGeneratorTool.generate_inmail("Hiring Manager", company, role)
            
            response = (
                f"### 🤝 Tailored LinkedIn Connection Note (Under 300 Characters)\n\n"
                f"```text\n{outreach['note']}\n```\n"
                f"*(Character count: {outreach['character_count']} / 300 allowed)*\n\n"
                f"### 📬 Extended InMail / Email Template\n\n"
                f"```text\n{inmail['message']}\n```\n\n"
                f"👉 **[Connect with Ryleen directly on LinkedIn]({self.linkedin_url})**"
            )
            return {
                "intent": "generate_outreach",
                "tool_used": "OutreachGeneratorTool",
                "response": response,
                "deep_link": self.linkedin_url,
                "actions": [
                    {"label": "Open LinkedIn Profile to Connect", "url": self.linkedin_url}
                ]
            }

        # Tool 3: Draft Technical LinkedIn Post
        if any(w in p for w in ["post", "article", "draft", "share on linkedin", "thought leadership", "publish"]):
            topic = "general"
            if "adversarial" in p or "ml" in p or "pgd" in p:
                topic = "adversarial-ml"
            elif "crypto" in p or "vault" in p or "zero" in p:
                topic = "crypto"
            elif "phishing" in p or "nlp" in p:
                topic = "phishing"
            elif "game" in p or "canvas" in p:
                topic = "game"
                
            draft = ContentDrafterTool.draft_technical_post(topic)
            response = (
                f"### 📝 Generated LinkedIn Technical Post\n\n"
                f"{draft['post_content']}\n\n"
                f"---\n"
                f"🔗 **One-Click Share to LinkedIn:**\n"
                f"[Click here to open LinkedIn and share this post]({draft['feed_share_url']})"
            )
            return {
                "intent": "draft_linkedin_post",
                "tool_used": "ContentDrafterTool",
                "response": response,
                "deep_link": draft["feed_share_url"],
                "actions": [
                    {"label": "One-Click Share to LinkedIn Feed", "url": draft["feed_share_url"]},
                    {"label": "View Ryleen's LinkedIn", "url": self.linkedin_url}
                ]
            }

        # Tool 4: Knowledge Retrieval / Q&A
        kb_results = PortfolioKnowledgeTool.search_knowledge(user_prompt)
        
        # Formulate answer
        lines = []
        lines.append(f"### 🤖 Ariya AI Knowledge Base Result\n")
        
        for item in kb_results["results"]:
            itype = item["type"]
            if itype == "project":
                pdata = item["data"]
                lines.append(f"**Project: {pdata['name']}** ({pdata['category']})")
                lines.append(f"• Summary: {pdata['summary']}")
                lines.append(f"• Repository: [{pdata['repo']}]({pdata['repo']})")
                if "demo" in pdata:
                    lines.append(f"• Live Demo: [{pdata['demo']}]({pdata['demo']})")
                lines.append(f"• Key Metrics:")
                for m in pdata["metrics"]:
                    lines.append(f"  - {m}")
                lines.append("")
            elif itype == "education":
                lines.append(f"**Education & Credentials:**")
                for e in item["data"]:
                    lines.append(f"• **{e['degree']}** — {e['institution']} ({e['period']})")
                    lines.append(f"  Focus: {e['focus']}")
                lines.append("")
            elif itype == "skills":
                lines.append(f"**Core Technical Skills:**")
                for domain, sklist in item["data"].items():
                    lines.append(f"• **{domain.replace('_', ' ').title()}**: {', '.join(sklist)}")
                lines.append("")
            elif itype == "general_overview":
                lines.append(f"**{item['name']}** — {item['title']}")
                lines.append(f"{item['bio']}\n")
                lines.append(f"Explore all {item['projects_count']} projects on the live portfolio: [{PROFILE['links']['portfolio']}]({PROFILE['links']['portfolio']})")
                lines.append("")
                
        lines.append(f"---\n👉 **Direct LinkedIn Connection**: [{self.linkedin_url}]({self.linkedin_url})")
        
        full_text = "\n".join(lines)
        
        # Security Safety Audit check
        audit = SafetyAuditTool.audit_text(full_text)
        if not audit["is_safe"]:
            full_text = "Content contained restricted tokens and was sanitized for safety."
            
        return {
            "intent": "knowledge_retrieval",
            "tool_used": "PortfolioKnowledgeTool",
            "response": full_text,
            "deep_link": self.linkedin_url,
            "actions": [
                {"label": "Connect on LinkedIn", "url": self.linkedin_url},
                {"label": "View Portfolio Site", "url": PROFILE["links"]["portfolio"]}
            ]
        }


def run_cli_chat():
    agent = AriyaCareerAgent()
    if console:
        console.print(Panel.fit(
            f"[bold cyan]Ariya AI Career & Networking Agent[/bold cyan]\n"
            f"[green]Directly linked to Ryleen Ariyakutty's LinkedIn[/green]\n"
            f"[dim]Type 'outreach', 'post', 'projects', 'linkedin', or ask any question. Type 'exit' to quit.[/dim]",
            border_style="cyan"
        ))
    else:
        print("=== Ariya AI Career & Networking Agent ===")
        print("Directly linked to Ryleen Ariyakutty's LinkedIn")
        print("Type 'exit' to quit.\n")

    while True:
        try:
            prompt = input("\nYou > ").strip()
            if not prompt:
                continue
            if prompt.lower() in ["exit", "quit", "q"]:
                print("Goodbye!")
                break

            result = agent.reason_and_act(prompt)
            
            if console:
                console.print(Panel(
                    Markdown(result["response"]),
                    title=f"[cyan]Ariya Agent ({result['tool_used']})[/cyan]",
                    subtitle=f"[dim]LinkedIn: {result['deep_link']}[/dim]",
                    border_style="green"
                ))
            else:
                print(f"\n[Ariya Agent ({result['tool_used']})]:\n")
                print(result["response"])
                print(f"\nDirect LinkedIn URL: {result['deep_link']}")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break


def main():
    parser = argparse.ArgumentParser(description="Ariya Career & Research AI Agent")
    subparsers = parser.add_subparsers(dest="command")

    # Command: chat
    subparsers.add_parser("chat", help="Start interactive CLI chat session")

    # Command: outreach
    p_outreach = subparsers.add_parser("outreach", help="Generate targeted LinkedIn connection note")
    p_outreach.add_argument("--name", default="Hiring Manager", help="Recipient name")
    p_outreach.add_argument("--company", default="Engineering Team", help="Company name")
    p_outreach.add_argument("--role", default="Engineering Lead", help="Target role")
    p_outreach.add_argument("--focus", default="ai_security", help="Focus: ai_security, devsecops, or full-stack")

    # Command: post
    p_post = subparsers.add_parser("post", help="Draft a technical LinkedIn post")
    p_post.add_argument("--topic", default="adversarial-ml", help="Topic: adversarial-ml, crypto, phishing, or game")

    # Command: link
    subparsers.add_parser("link", help="Display verified LinkedIn and portfolio links")

    # Command: serve
    p_serve = subparsers.add_parser("serve", help="Launch local web server for the AI Agent")
    p_serve.add_argument("--port", type=int, default=5050, help="Port to bind (default: 5050)")

    args = parser.parse_args()

    agent = AriyaCareerAgent()

    if args.command == "outreach":
        res = OutreachGeneratorTool.generate_connection_note(args.name, args.company, args.role, args.focus)
        print(f"\n=== LinkedIn Connection Note ({res['character_count']}/300 chars) ===")
        print(res["note"])
        print(f"\nDirect LinkedIn Profile: {res['profile_url']}")
    elif args.command == "post":
        res = ContentDrafterTool.draft_technical_post(args.topic)
        print(f"\n=== Technical LinkedIn Post ({res['character_count']} chars) ===")
        print(res["post_content"])
        print(f"\nOne-Click LinkedIn Share URL:\n{res['feed_share_url']}")
    elif args.command == "link":
        print(f"LinkedIn Profile: {agent.linkedin_url}")
        print(f"Portfolio:        {PROFILE['links']['portfolio']}")
        print(f"GitHub:           {PROFILE['links']['github']}")
    elif args.command == "serve":
        from server import app
        print(f"Starting Ariya AI Agent Web Server on http://localhost:{args.port}...")
        app.run(host="127.0.0.1", port=args.port, debug=False)
    else:
        run_cli_chat()


if __name__ == "__main__":
    main()
