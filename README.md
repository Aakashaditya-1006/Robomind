# 🤖 RoboMind

<div align="center">

**Control any robot using plain English. No code required.**

[![Stars](https://img.shields.io/github/stars/Aakashaditya-1006/robomind?style=for-the-badge&color=FFD700)](https://github.com/Aakashaditya-1006/robomind/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)](https://python.org)
[![Ollama](https://img.shields.io/badge/Powered%20by-Ollama-orange?style=for-the-badge)](https://ollama.com)

[**Demo**](#demo) • [**Quick Start**](#quick-start) • [**Examples**](#examples) • [**Contributing**](#contributing) • [**Discord**](#community)

![RoboMind Demo](demo.gif)

</div>

---

## What is RoboMind?

RoboMind is an open-source bridge between **Large Language Models** and **robot simulators**. You type a command in plain English — RoboMind figures out how to execute it.

```python
from robomind import RoboMind

robot = RoboMind()
robot.do("pick up the red box and place it on the shelf")
```

That's it. No robotics degree required.

---

## Why RoboMind?

| Without RoboMind | With RoboMind |
|---|---|
| Write complex trajectory code | Just describe what you want |
| Learn ROS, Gazebo, MoveIt | Works out of the box |
| Debug joint angles for hours | "Move arm to position A" |
| Requires expert knowledge | Beginner-friendly |

---

## Demo

> 📽️ [Watch the full demo on YouTube](#) | [Try it in your browser (Colab)](#)

<div align="center">
<img src="assets/demo.gif" width="700" alt="RoboMind Demo"/>
</div>

---

## Quick Start

### Step 1: Install Ollama (the local AI brain)
```bash
# On Linux/Mac:
curl -fsSL https://ollama.com/install.sh | sh

# Then pull a model:
ollama pull llama3
```

### Step 2: Install RoboMind
```bash
pip install robomind
```

### Step 3: Run your first robot command
```python
from robomind import RoboMind

# Connect to the simulator
robot = RoboMind(simulator="pybullet")

# Just tell it what to do!
robot.do("move forward 1 meter")
robot.do("turn left 90 degrees")
robot.do("pick up the object in front of you")
```

---

## Examples

### 🦾 Basic Movement
```python
robot.do("move to the center of the room")
robot.do("spin in a circle")
robot.do("go to the charging station")
```

### 📦 Object Manipulation
```python
robot.do("pick up the red box")
robot.do("stack the boxes from largest to smallest")
robot.do("place the object gently on the table")
```

### 🗺️ Navigation
```python
robot.do("navigate to waypoint A while avoiding obstacles")
robot.do("patrol the room perimeter")
robot.do("return to starting position")
```

### 🧠 Complex Reasoning
```python
robot.do("find all blue objects and count them")
robot.do("if the box is heavy, ask for help, otherwise pick it up")
```

---

## Supported Simulators

| Simulator | Status | Notes |
|-----------|--------|-------|
| PyBullet | ✅ Ready | Best for beginners |
| Gazebo | 🚧 In Progress | ROS integration |
| MuJoCo | 🚧 In Progress | Physics simulation |
| Isaac Sim | 📋 Planned | NVIDIA platform |
| Webots | 📋 Planned | Open source sim |

---

## Architecture

```
Your English Command
        ↓
   RoboMind Agent
        ↓
 Local LLM (Ollama)     ← No internet needed!
        ↓
  Action Planner
        ↓
 Robot Simulator (PyBullet / Gazebo / etc.)
        ↓
   Robot Moves! 🤖
```

---

## Installation (Full)

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/robomind.git
cd robomind

# Install dependencies
pip install -r requirements.txt

# Install in dev mode
pip install -e .

# Run a demo
python examples/basic_movement.py
```

---

## Contributing

We love contributions! RoboMind is built by the community.

👉 Read [CONTRIBUTING.md](CONTRIBUTING.md) to get started.

**Easy first issues for beginners:**
- 📝 Improve documentation
- 🧪 Add more example scripts
- 🌐 Add support for a new simulator
- 🐛 Report or fix bugs

Check our [good first issues](https://github.com/Aakashaditya-1006/robomind/issues?q=is%3Aopen+label%3A%22good+first+issue%22) label!

---

## Community

- 💬 [Discord Server](#) — chat with contributors
- 🐦 [Twitter/X](#) — follow for updates
- 📧 [Newsletter](#) — monthly updates

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Aakashaditya-1006/robomind&type=Date)](https://star-history.com/#Aakashaditya-1006/robomind&Date)

---

## License

MIT License — free to use, modify, and distribute. See [LICENSE](LICENSE).

---

<div align="center">
Made with ❤️ by the open-source community

**If RoboMind helped you, please ⭐ star this repo!**
</div>
