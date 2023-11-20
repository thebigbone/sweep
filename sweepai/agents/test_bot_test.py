import os

from sweepai.agents.test_bot import TestBot
from sweepai.core.entities import Message
from sweepai.utils.github_utils import ClonedRepo

installation_id = os.environ["INSTALLATION_ID"]
cloned_repo = ClonedRepo("sweepai/sweep", installation_id, "main")

additional_messages = [
    Message(
        role="user",
        content="""Repo: sweep: Sweep: AI-powered Junior Developer for small features and bug fixes.
Issue Title: Sweep: write unit tests for name_agent.py
Issue Description: ### Details

_No response_""",
        key="user",
    )
]
file_path = "sweepai/agents/test_bot.py"
request = "Write unit tests for test_bot.py"
changes_made = ""
bot = TestBot()
bot.model = "gpt-4-0613"
bot.write_test(
    additional_messages=additional_messages,
    file_path=file_path,
    request=request,
    changes_made=changes_made,
    cloned_repo=cloned_repo,
)
