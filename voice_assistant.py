import os
import ssl
import certifi
from dotenv import load_dotenv

import websockets.legacy.client
import websockets.sync.client
import functools

_ssl_context = ssl.create_default_context(cafile=certifi.where())

_original_connect = websockets.sync.client.connect
def _patched_connect(*args, **kwargs):
    kwargs.setdefault("ssl", _ssl_context)
    return _original_connect(*args, **kwargs)
websockets.sync.client.connect = _patched_connect

load_dotenv()

AGENT_ID = os.getenv("AGENT_ID")
API_KEY = os.getenv("API_KEY")

from elevenlabs import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from elevenlabs.conversational_ai.conversation import ConversationInitiationData

# Override currently does not work
user_name = "Khoi"
schedule = "Tutoring at 11:00 AM; Night out at 9:00 PM"
prompt = f"You are a helpful virtual assistant. Your interlocutor has the following schedule: {schedule}."
first_message = f"Hello {user_name}, how can I assist you today?"

conversation_override = {
    "agent": {
        "prompt": {
            "prompt": prompt,
        },
        "first_message": first_message,
    },
}

config = ConversationInitiationData() # PROBLEM: Override does not work even if the system prompt and first message parameters in the override settings of the agent is turned on. The agent still speaks in its default way.
    #conversation_config_override=conversation_override,
    #extra_body={},
    #dynamic_variables={},

client = ElevenLabs(api_key=API_KEY)

def print_agent_response(response):
    print(f"Agent: {response}")

def print_interrupted_response(original, corrected):
    print(f"Agent interrupted, truncated response: {corrected}")

def print_user_transcript(transcript):
    print(f"User: {transcript}")

conversation = Conversation(
    client,
    AGENT_ID,
    config=config,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),
    callback_agent_response=print_agent_response,
    callback_agent_response_correction=print_interrupted_response,
    callback_user_transcript=print_user_transcript,
)

conversation.start_session()