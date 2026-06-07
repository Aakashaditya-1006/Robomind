"""
Example 3: Interactive Mode
============================
Type commands to the robot in real-time!
Run this file with: python examples/interactive.py
"""

from robomind import RoboMind

print("=" * 50)
print("🤖 RoboMind Interactive Mode")
print("=" * 50)
print("Type a command in plain English and watch your robot execute it.")
print("Type 'quit' to exit, 'status' to see robot position.\n")

robot = RoboMind(gui=True)  # gui=True shows the simulator window

while True:
    try:
        command = input("\n💬 Your command: ").strip()

        if not command:
            continue
        elif command.lower() == "quit":
            print("👋 Goodbye!")
            break
        elif command.lower() == "status":
            print("📍 Robot status:", robot.status())
        elif command.lower() == "history":
            print("📜 History:")
            for i, entry in enumerate(robot.history_log(), 1):
                print(f"  {i}. {entry['command']}")
        elif command.lower().startswith("explain "):
            explanation = robot.explain(command[8:])
            print(f"🧠 Explanation: {explanation}")
        else:
            robot.do(command)

    except KeyboardInterrupt:
        print("\n\n🛑 Emergency stop!")
        robot.stop()
        break

robot.shutdown()
