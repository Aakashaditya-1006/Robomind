"""
Example 2: Object Manipulation
================================
This shows how RoboMind handles pick-and-place tasks.
Run this file with: python examples/object_manipulation.py
"""

from robomind import RoboMind

robot = RoboMind(gui=False)

print("=" * 50)
print("Example: Object Manipulation")
print("=" * 50)

# First, explain the plan (without executing it)
print("\n🧠 What will happen if I say 'pick up the red box'?")
explanation = robot.explain("pick up the red box and place it on the table")
print(f"   → {explanation}")

print("\n--- Now actually doing it ---\n")

# Execute the commands
robot.do("move to the red box")
robot.do("pick up the red box")
robot.do("navigate to the table")
robot.do("place the red box on the table")

print("\n✅ Done! Robot status:", robot.status())

robot.shutdown()
