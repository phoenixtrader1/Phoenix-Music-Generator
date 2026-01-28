import os, requests, json, base64
from flask import jsonify, request

HF_API_KEY = os.environ.get("HF_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-small"

# Simple session storage (temporary JSON)
SESSION_FILE = "/tmp/sessions.json"

def load_sessions():
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, "r") as f:
            return json.load(f)
    return {}

def save_sessions(data):
    with open(SESSION_FILE, "w") as f:
        json.dump(data, f)

def handler(request):
    try:
        data = request.get_json()
        username = data.get("username", "guest")
        prompt = data.get("prompt")
        if not prompt:
            return jsonify({"error": "Prompt required"}), 400

        headers = {"Authorization": f"Bearer {HF_API_KEY}"}
        resp = requests.post(API_URL, headers=headers, json={"inputs": prompt})

        if resp.status_code != 200:
            return jsonify({"error": "AI generation failed"}), 500

        audio_bytes = resp.content
        audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")

        # Track history
        sessions = load_sessions()
        user_history = sessions.get(username, [])
        user_history.insert(0, {"prompt": prompt, "audio_base64": audio_base64})
        sessions[username] = user_history[:20]  # keep last 20 tracks
        save_sessions(sessions)

        return jsonify({"audio_base64": audio_base64, "history": user_history})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
