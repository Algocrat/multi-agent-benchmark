#!/bin/bash
echo "Starting LangGraph benchmark..."

source venv/bin/activate
python run_benchmark.py

echo "Benchmark complete. Output saved in ./outputs"
