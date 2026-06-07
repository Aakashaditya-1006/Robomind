"""
RoboMind Robot Controller — Executes actions in the simulator.
"""

import time
import math
from typing import Optional


class SimulatedRobot:
    """
    A simple robot in PyBullet simulator.
    Executes structured actions produced by the RoboMind Agent.
    """

    def __init__(self, gui: bool = True):
        """
        Initialize the robot in PyBullet.

        Args:
            gui: Show the simulator window (True) or run headless (False)
        """
        self.position = [0.0, 0.0, 0.0]   # x, y, z
        self.rotation = 0.0                 # degrees
        self.holding = None                 # object being held
        self.gui = gui
        self._setup_simulator()

    def _setup_simulator(self):
        """Set up the PyBullet physics simulation."""
        try:
            import pybullet as p
            import pybullet_data

            self.p = p
            mode = p.GUI if self.gui else p.DIRECT
            self.physics_client = p.connect(mode)
            p.setAdditionalSearchPath(pybullet_data.getDataPath())
            p.setGravity(0, 0, -9.81)

            # Load a ground plane
            p.loadURDF("plane.urdf")

            # Load a simple robot (R2D2 as placeholder)
            self.robot_id = p.loadURDF(
                "r2d2.urdf",
                basePosition=[0, 0, 0.5]
            )

            print("✅ PyBullet simulator started!")
            self.use_pybullet = True

        except ImportError:
            print("⚠️  PyBullet not installed. Running in text-only mode.")
            print("   Install it with: pip install pybullet")
            self.use_pybullet = False
            self.p = None

    def execute(self, action: dict) -> bool:
        """
        Execute a single action dictionary.

        Args:
            action: Action dict from RoboMindAgent (e.g., {"action": "move", ...})

        Returns:
            True if successful, False otherwise
        """
        action_type = action.get("action", "").lower()
        params = action.get("parameters", {})

        handlers = {
            "move": self._move,
            "rotate": self._rotate,
            "pick": self._pick,
            "place": self._place,
            "navigate": self._navigate,
            "stop": self._stop,
            "wait": self._wait,
        }

        handler = handlers.get(action_type)
        if handler:
            return handler(params)
        else:
            print(f"❓ Unknown action: {action_type}")
            return False

    def _move(self, params: dict) -> bool:
        direction = params.get("direction", "forward")
        distance = float(params.get("distance", 1.0))

        # Calculate new position based on direction and current rotation
        angle_rad = math.radians(self.rotation)
        dx, dy = 0.0, 0.0

        if direction == "forward":
            dx = distance * math.cos(angle_rad)
            dy = distance * math.sin(angle_rad)
        elif direction == "backward":
            dx = -distance * math.cos(angle_rad)
            dy = -distance * math.sin(angle_rad)
        elif direction == "left":
            dx = -distance * math.sin(angle_rad)
            dy = distance * math.cos(angle_rad)
        elif direction == "right":
            dx = distance * math.sin(angle_rad)
            dy = -distance * math.cos(angle_rad)

        self.position[0] += dx
        self.position[1] += dy

        print(f"🚗 Moved {direction} {distance}m → Position: ({self.position[0]:.2f}, {self.position[1]:.2f})")

        if self.use_pybullet:
            self.p.resetBasePositionAndOrientation(
                self.robot_id,
                self.position,
                self.p.getQuaternionFromEuler([0, 0, math.radians(self.rotation)])
            )
            self._simulate_steps(100)

        return True

    def _rotate(self, params: dict) -> bool:
        angle = float(params.get("angle", 90.0))
        direction = params.get("direction", "left")

        if direction == "right":
            angle = -angle

        self.rotation = (self.rotation + angle) % 360
        print(f"🔄 Rotated {angle}° → Facing: {self.rotation:.1f}°")

        if self.use_pybullet:
            self.p.resetBasePositionAndOrientation(
                self.robot_id,
                self.position,
                self.p.getQuaternionFromEuler([0, 0, math.radians(self.rotation)])
            )
            self._simulate_steps(50)

        return True

    def _pick(self, params: dict) -> bool:
        obj = params.get("object", "unknown object")
        if self.holding:
            print(f"❌ Already holding: {self.holding}")
            return False
        self.holding = obj
        print(f"🤏 Picked up: {obj}")
        return True

    def _place(self, params: dict) -> bool:
        if not self.holding:
            print("❌ Not holding anything!")
            return False
        print(f"📦 Placed: {self.holding}")
        self.holding = None
        return True

    def _navigate(self, params: dict) -> bool:
        waypoint = params.get("waypoint", "unknown")
        print(f"🗺️  Navigating to: {waypoint}")
        time.sleep(1)  # Simulate navigation time
        return True

    def _stop(self, params: dict) -> bool:
        print("🛑 Robot stopped.")
        return True

    def _wait(self, params: dict) -> bool:
        duration = float(params.get("duration", 1.0))
        print(f"⏳ Waiting {duration} seconds...")
        time.sleep(duration)
        return True

    def _simulate_steps(self, steps: int):
        """Run PyBullet physics steps."""
        for _ in range(steps):
            self.p.stepSimulation()
            time.sleep(1.0 / 240.0)

    def get_status(self) -> dict:
        """Return the current robot status."""
        return {
            "position": self.position.copy(),
            "rotation": self.rotation,
            "holding": self.holding
        }

    def disconnect(self):
        """Clean up the simulator."""
        if self.use_pybullet and self.p:
            self.p.disconnect()
            print("🔌 Simulator disconnected.")
