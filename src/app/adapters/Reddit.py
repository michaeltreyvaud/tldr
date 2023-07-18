from typing import Any
import praw

from src.app.adapters.Adapter import Adapter

POST_LIMIT = 5
SUB_REDDIT_NAME = "tifu"
COMPLETION_MODEL = "text-davinci-003"


class Reddit(Adapter):
    name = "reddit"

    def __init__(self, reddit_client: praw.Reddit, openai_client) -> None:
        self.reddit_client = reddit_client
        self.openai_client = openai_client

    def get_posts(self) -> dict[str, Any]:
        results = {}
        for submission in self.reddit_client.subreddit(SUB_REDDIT_NAME).hot(
            limit=POST_LIMIT
        ):
            results[submission.title] = submission.selftext
        return results

    def create_prompt(self, text: str) -> str:
        prompt = f"""Summarize the text delimited
            by triple quotes in less than 2 paragraphs:
            \"\"\"{text}\"\"\".\n\n\n"""
        return prompt

    def get_response_text(self, response: dict[str, Any]) -> str:
        return response["choices"][0]["text"]

    def summarize_posts(self, posts: dict[str, Any]) -> dict[str, Any]:
        responses = {}
        for post in posts:
            try:
                prompt = self.create_prompt(posts[post])
                response = self.openai_client.Completion.create(
                    model=COMPLETION_MODEL, prompt=prompt, max_tokens=2000
                )
                response_text = self.get_response_text(response)
                responses[post] = response_text
            except Exception as e:
                print(str(e))
        return responses

    def summarize(self) -> dict[str, Any]:
        posts = self.get_posts()
        summarized_posts = self.summarize_posts(posts)
        return summarized_posts
