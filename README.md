
# Voice Assistant

A local voice assistant powered by [ElevenLabs Conversational AI](https://elevenlabs.io/docs/conversational-ai/overview). Speak to it, and it speaks back using an AI agent you configure on the ElevenLabs dashboard.

## Prerequisites

* Python 3.12+
* An [ElevenLabs](https://elevenlabs.io) account
* A configured ElevenLabs Agent (see setup below)

## Installation

Create and activate a virtual environment:

bash

```bash
python3 -m venv venv
source venv/bin/activate
```

Then install dependencies:

bash

```bash
pip install elevenlabs python-dotenv certifi
```

To deactivate the virtual environment when done:

bash

```bash
deactivate
```

## ElevenLabs Setup

1. Go to **ElevenLabs → Conversational AI → Agents**
2. Click **Start from blank** to create a new agent
3. Set your desired **System prompt** and **First message** in the agent settings
4. Go to the **Security** tab and enable the **System prompt** and **First message** overrides if you want to control them from code
5. Copy your **Agent ID** from the agent page
6. Go to your profile → **API Keys** and create a new key with at minimum:
   * Text to Speech → Access
   * ElevenAgents → Write
   * Voices → Read
   * Models → Access

## Environment Variables

Create a `.env` file in the project root:

```
AGENT_ID=your_agent_id_here
API_KEY=your_api_key_here
```

## Usage

bash

```bash
python3 voice_assistant.py
```

The assistant will start listening immediately. Press **Ctrl+C** to stop.

## Notes

* On macOS, if you encounter SSL certificate errors, run:

bash

```bash
  /Applications/Python\3.12/Install\ Certificates.command
```
