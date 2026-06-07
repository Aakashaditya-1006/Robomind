"""
RoboMind Agent — The brain that converts English to robot actions.
"""

import json
import requests
from typing import Optional


SYSTEM_PROMPT = """You are RoboMind, an AI that converts natural language commands into structured robot actions.

Given a plain English command, respond ONLY with a JSON object like this:
{
  "action": "move" | "rotate" | "pick" | "place" | "navigate" | "stop" | "wait",
  "parameters": {
    "direction": "forward" | "backward" | "left" | "right" (for move/rotate),
    "distance": <number in meters> (for move),
    "angle": <number in degrees> (for rotate),
    "object": "<object name>" (for pick/place),
    "waypoint": "<waypoint name>" (for navigate),
    "duration": <seconds> (for wait)
  },
  "explanation": "<one sentence: what the robot will do>"
}

If the command has multiple steps, return a list of action objects.
Respond ONLY with valid JSON. No extra text."""


class RoboMindAgent:
    """
    The AI brain of RoboMind.
    Converts plain English into structured robot actions using a local LLM.
    """

    def __init__(
        self,
        model: str = "llama3",
        ollama_url: str = "http://localhost:11434",
        verbose: bool = True
    ):
        """
        Initialize the RoboMind agent.

        Args:
            model: The Ollama model to use (default: llama3)
            ollama_url: URL where Ollama is running
            verbose: Print what the robot is doing
        """
        self.model = model
        self.ollama_url = ollama_url
        self.verbose = verbose
        self._check_ollama()

    def _check_ollama(self):
        """Check if Ollama is running and the model is available."""
        try:
            response = requests.get(f"{self.ollama_url}/api/tags", timeout=3)
            if response.status_code == 200:
                models = [m["name"] for m in response.json().get("models", [])]
                if not any(self.model in m for m in models):
                    print(f"⚠️  Model '{self.model}' not found. Run: ollama pull {self.model}")
                else:
                    if self.verbose:
                        print(f"✅ Connected to Ollama. Using model: {self.model}")
        except requests.exceptions.ConnectionError:
            print("❌ Ollama not running! Start it with: ollama serve")
            print("   Then install a model: ollama pull llama3")

    def parse_command(self, command: str) -> list[dict]:
        """
        Convert a plain English command into a list of robot actions.

        Args:
            command: Natural language command (e.g., "move forward 1 meter")

        Returns:
            List of action dictionaries
        """
        if self.verbose:
            print(f"\n🧠 Thinking: '{command}'")

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": command}
            ],
            "stream": False
        }

        try:
            response = requests.post(
                f"{self.ollama_url}/api/chat",
                json=payload,
                timeout=30
            )
            raw = response.json()["message"]["content"].strip()

            # Parse the JSON response
            actions = json.loads(raw)

            # Normalize: always return a list
            if isinstance(actions, dict):
                actions = [actions]

            if self.verbose:
                for action in actions:
                    print(f"📋 Plan: {action.get('explanation', action['action'])}")

            return actions

        except json.JSONDecodeError:
            print(f"⚠️  Could not parse AI response. Raw output: {raw}")
            return []
        except Exception as e:
            print(f"❌ Error communicating with Ollama: {e}")
            return []

    def explain(self, command: str) -> str:
        """
        Explain what the robot would do, without actually doing it.

        Args:
            command: Natural language command

        Returns:
            Human-readable explanation
        """
        actions = self.parse_command(command)
        if not actions:
            return "Could not understand the command."

        explanations = [a.get("explanation", f"Perform: {a['action']}") for a in actions]
        return " → ".join(explanations)
