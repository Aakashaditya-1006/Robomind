# Contributing to RoboMind 🤖

First off — **thank you** for wanting to contribute! RoboMind is built by people like you.

This guide will walk you through everything, even if you've never contributed to open source before.

---

## 🌱 First Time Contributing to Open Source?

No worries! Here's what you need to know:

1. **Fork** = Make your own copy of the project
2. **Clone** = Download it to your computer
3. **Branch** = Work on your changes separately
4. **Pull Request (PR)** = Ask us to include your changes

We'll walk you through each step below.

---

## 🚀 Step-by-Step Guide

### 1. Fork the Repository
Click the **Fork** button at the top right of the GitHub page.
This creates your own copy of RoboMind.

### 2. Clone Your Fork
```bash
git clone https://github.com/YOUR_USERNAME/robomind.git
cd robomind
```

### 3. Create a Branch
```bash
# Replace "my-feature" with a short description of your change
git checkout -b my-feature
```

### 4. Make Your Changes
Edit the code, add examples, fix bugs — whatever you're working on!

### 5. Test Your Changes
```bash
pip install -e .
python examples/basic_movement.py
```

### 6. Commit and Push
```bash
git add .
git commit -m "Add: brief description of what you changed"
git push origin my-feature
```

### 7. Open a Pull Request
Go to your fork on GitHub and click **"Compare & pull request"**.
Describe what you changed and why. That's it!

---

## 💡 What Can I Contribute?

### 🟢 Easy (Great for beginners)
- Fix typos in the README or docs
- Add a new example script in `/examples`
- Improve error messages
- Add comments to existing code

### 🟡 Medium
- Add support for a new robot simulator
- Improve the action parser
- Add unit tests
- Create a Jupyter notebook demo

### 🔴 Advanced
- Add ROS 2 integration
- Add vision capabilities (camera input)
- Build a web interface
- Implement multi-robot coordination

Look for issues tagged [`good first issue`](https://github.com/YOUR_USERNAME/robomind/issues?q=is%3Aopen+label%3A%22good+first+issue%22) on GitHub!

---

## 📋 Code Style

- Use Python type hints where possible
- Add a docstring to every function
- Keep lines under 100 characters
- Use descriptive variable names

---

## 🙋 Questions?

Open a [GitHub Discussion](https://github.com/YOUR_USERNAME/robomind/discussions) or join our Discord!

We're friendly, we promise. 😊
