import os

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
MUBERT_API_KEY = os.getenv("MUBERT_API_KEY", "")

# Token Settings
TOKEN_COST_PER_GENERATION = 1

# Web3 / Blockchain Config
WEB3_RPC_URL = os.getenv("WEB3_RPC_URL", "")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS", "")

# Server / App Settings
DEBUG = True
PORT = 5000
