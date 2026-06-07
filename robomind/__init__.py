"""
RoboMind — Control robots with plain English.

Example:
    from robomind import RoboMind

    robot = RoboMind()
    robot.do("move forward 1 meter, then turn left")
"""

from robomind.agent import RoboMindAgent
from robomind.robot import SimulatedRobot


class RoboMind:
    """
    The main RoboMind interface.
    Combines the AI agent and robot simulator into one simple class.

    Example:
        robot = RoboMind()
        robot.do("pick up the red box and bring it to the table")
    """

    def __init__(
        self,
        simulator: str = "pybullet",
        model: str = "llama3",
        gui: bool = True,
        verbose: bool = True
    ):
        """
        Initialize RoboMind.

        Args:
            simulator: Which simulator to use ("pybullet" supported now)
            model: Which Ollama model to use ("llama3", "mistral", etc.)
            gui: Show the simulator window
            verbose: Print what the robot is doing
        """
        print("🤖 Starting RoboMind...")
        self.agent = RoboMindAgent(model=model, verbose=verbose)
        self.robot = SimulatedRobot(gui=gui)
        self.verbose = verbose
        self.history = []
        print("✅ RoboMind ready! Type your commands.\n")

    def do(self, command: str) -> bool:
        """
        Execute a natural language command.

        Args:
            command: Plain English instruction (e.g., "move forward 2 meters")

        Returns:
            True if all actions succeeded, False otherwise

        Example:
            robot.do("spin around and then move forward")
        """
        # Parse the command into actions
        actions = self.agent.parse_command(command)

        if not actions:
            print("❌ Could not understand command. Try rephrasing.")
            return False

        # Execute each action
        all_succeeded = True
        for action in actions:
            success = self.robot.execute(action)
            if not success:
                all_succeeded = False

        # Save to history
        self.history.append({
            "command": command,
            "actions": actions,
            "success": all_succeeded,
            "status": self.robot.get_status()
        })

        return all_succeeded

    def explain(self, command: str) -> str:
        """
        Explain what the robot WOULD do, without actually doing it.

        Args:
            command: Natural language command

        Returns:
            Human-readable explanation

        Example:
            print(robot.explain("navigate to the charging station"))
        """
        return self.agent.explain(command)

    def status(self) -> dict:
        """Return the current robot status (position, rotation, held objects)."""
        return self.robot.get_status()

    def history_log(self) -> list:
        """Return the full command history."""
        return self.history

    def stop(self):
        """Emergency stop — halt all robot movement."""
        self.robot.execute({"action": "stop", "parameters": {}})

    def shutdown(self):
        """Clean up and disconnect from the simulator."""
        self.robot.disconnect()
        print("👋 RoboMind shut down.")


__version__ = "0.1.0"
__all__ = ["RoboMind"]
