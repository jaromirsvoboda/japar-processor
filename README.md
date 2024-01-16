# Japar Processor

- Python desktop utility fixing some issues we found in the legacy Japar SW.

## To start developing:

- clone the repo
- create virtual environment: `python -m venv .venv `
- activate it: `.\.venv\Scripts\activate`


## To build .exe file:

- `pip install pyinstaller`
- `pyinstaller --onefile your_script.py`
- exe created in the `dist` folder