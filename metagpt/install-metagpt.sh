#!/bin/bash
# install_metagpt.sh

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Clone MetaGPT
git clone https://github.com/geekan/MetaGPT.git
cd MetaGPT

# Install requirements
pip install -r requirements.txt

# Optional: Install extras (e.g. for OpenAI or Ollama backends if needed)
pip install ".[all]"

# Verify installation
echo -e "\n✅ MetaGPT installed. To use: source venv/bin/activate && cd MetaGPT"

