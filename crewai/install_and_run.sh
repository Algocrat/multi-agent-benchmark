#!/bin/bash
echo "Installing dependencies..."
pip install crewai langchain langchainhub duckduckgo-search

echo "Running CrewAI benchmark with Mistral..."
python run_crewai_benchmark.py
