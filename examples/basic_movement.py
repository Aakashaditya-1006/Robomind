"""
Example 1: Basic Robot Movement
================================
This shows the simplest way to use RoboMind.
Run this file with: python examples/basic_movement.py
"""

from robomind import RoboMind

# Start the robot
robot = RoboMind(gui=False)  # gui=False for no window, gui=True to see the simulator

print("=" * 50)
print("Example: Basic Movement")
print("=" * 50)

# Simple movement commands
robot.do("move forward 1 meter")
robot.do("turn left 90 degrees")
robot.do("move forward 2 meters")
robot.do("turn right 45 degrees")

# Check where the robot ended up
print("\n📍 Final status:", robot.status())

# See history of what was done
print("\n📜 Command history:")
for i, entry in enumerate(robot.history_log(), 1):
    print(f"  {i}. '{entry['command']}' → {'✅' if entry['success'] else '❌'}")

robot.shutdown()
