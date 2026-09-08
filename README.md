# Emotional Support Bot

A calm, Streamlit-based AI companion designed to offer gentle conversation, emotional validation, and grounding support in stressful moments.

![Python](https://img.shields.io/badge/Python-100%25-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?logo=streamlit)
![OpenAI](https://img.shields.io/badge/AI-OpenRouter%20%2F%20OpenAI-111827)
![License](https://img.shields.io/badge/License-Unlicensed-lightgrey)

> **Important:** This app is an emotional support companion, **not** a replacement for a therapist, counselor, crisis service, or other professional help.

---

## ✨ Overview

**Emotional Support Bot** is a lightweight chat application built with **Python** and **Streamlit**. It connects to an LLM through **OpenRouter** and is tuned to respond with empathy, active listening, and supportive reframing.

It includes:
- A friendly, centered chat interface
- Suggested starter prompts for quick engagement
- A sidebar with mindful grounding exercises
- A session token safety limit to prevent runaway usage
- A gentle system prompt focused on emotional support

---

## 🎯 What this project is for

This project is great for:
- Demonstrating a mental wellness–inspired AI chat UI
- Learning how to build Streamlit apps with conversational memory
- Experimenting with prompt design for compassionate assistant behavior
- Showing how to connect a Python app to an LLM API

---

## 🧠 How it works

The app keeps a conversation history in `st.session_state` and sends user messages to an LLM through the OpenRouter API. A system prompt defines the bot’s tone and safety boundaries.

### Core behavior
- **Empathy first:** responses are gentle and validating
- **Short, readable paragraphs:** easy to skim when stressed
- **No diagnosis:** the bot avoids medical or psychiatric labeling
- **Grounding support:** encourages calming reframes and simple exercises

---

## 🖥️ Features

### User experience
- Clean, centered Streamlit layout
- Warm intro banner and supportive messaging
- Clickable starter prompts to begin chatting quickly
- Human-friendly sidebar with breathing/grounding checkboxes

### Safety and control
- Hidden token budget ceiling to limit demo sessions
- Session restart button when the limit is reached
- Clear disclaimer that the app is not professional care

### Developer-friendly design
- Minimal dependency footprint
- Easy to run locally
- Straightforward API integration with `openai` client

---

## 📸 UI Highlights

- **Chat-style interaction** for natural conversation
- **Suggested prompts** for users who don’t know what to say
- **Mindful resources panel** for grounding and calming
- **Session guardrail** to pause when the token budget is reached

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+ recommended
- A valid **OpenRouter API key**
- `pip` installed

### Installation

```bash
git clone https://github.com/suraj11011/emotional-support-bot.git
cd emotional-support-bot
pip install -r requirements.txt
