# Contributing to NepaliKit

Thanks for your interest in contributing!

## Ways to Contribute

1. **Report bugs**: Open an issue
2. **Suggest features**: Open a discussion
3. **Fix bugs**: Submit a PR
4. **Add features**: Submit a PR
5. **Improve docs**: Submit a PR
6. **Write tutorials**: Share your examples

## Development Setup

```bash
# Clone
git clone https://github.com/prabhashj07/nepalikit
cd nepalikit

# Install with uv
uv sync

# Run tests
pytest

# Check coverage
pytest --cov=nepalikit
```

## Code Style

- Follow PEP 8
- Use type hints where appropriate
- Write docstrings (Google style)
- Add tests for new features

## Pull Request Process

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add/update tests
5. Run tests locally
6. Submit PR with description

## Testing

```bash
# Run all tests
pytest

# Run specific test file
pytest test/test_stemmer.py

# Run with verbose output
pytest -v
```

## License

MIT License - see [LICENSE](../LICENSE) for details.
