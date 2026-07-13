# Installation

## Quick Install

```bash
pip install nepalikit
```

## Development Install

```bash
# Clone the repository
git clone https://github.com/prabhashj07/nepalikit
cd nepalikit

# Install with uv (recommended)
uv sync

# Or with pip
pip install -e .
```

## Requirements

- Python 3.9 or higher
- Dependencies: `sentencepiece==0.2.0` (installed automatically)

## Verify Installation

```python
import nepalikit
print(nepalikit.__version__)  # e.g. "1.0.3"
```

## Troubleshooting

### Import Error

If you see `ModuleNotFoundError`, try reinstalling:

```bash
pip uninstall nepalikit
pip install nepalikit
```

### Version Mismatch

Check your installed version:

```bash
pip show nepalikit
```

### Permission Issues

On Linux/macOS, use `--user`:

```bash
pip install --user nepalikit
```

### Windows Issues

If you have issues on Windows, try using a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
pip install nepalikit
```
