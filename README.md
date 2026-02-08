# Tic-Tac-Toe (Streamlit)

A simple Tic-Tac-Toe game with a Streamlit UI. Play by clicking the grid or by entering a move number (1-9).

## Requirements

- Python 3.10+

## Setup

```bash
cd /Users/kavin/Documents/New\ project/sample_codex
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run

```bash
streamlit run app.py --server.port 8502 --server.address 127.0.0.1
```

Then open:

- http://127.0.0.1:8502

## How to Play

- Click a square to place your mark, or enter a number 1-9 in the input box.
- The game alternates between X and O.
- Use **Reset** to start a new game.

## Tests

```bash
python -m unittest discover -s tests -p "test_*unittest.py"
python -m pytest -q
```
