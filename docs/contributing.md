# Contributing to NepaliKit

Thanks for your interest in contributing! There are many ways to do so.

## Ways to Contribute

1. **Report bugs**: Open a GitHub issue
2. **Suggest features**: Open a discussion
3. **Fix bugs**: Submit a PR
4. **Add features**: Submit a PR
5. **Improve docs**: Submit a PR
6. **Write tutorials**: Share your examples

## Development Setup

```bash
git clone https://github.com/prabhashj07/nepalikit
cd nepalikit
uv sync
```

## Run tests

```bash
pytest
pytest --cov=nepalikit
```

## Building the Documentation

The documentation uses [MkDocs](https://www.mkdocs.org/) with the Material theme. To preview it locally:

```bash
# Install mkdocs and theme
uv sync --extra dev

# Serve docs (auto-reload on changes)
uv run mkdocs serve
```

Then open `http://localhost:8000` in your browser.

## Contribute to Documentation

All documentation files reside in the `docs/` folder:

- `docs/usage/*` - Feature usage guides
- `docs/examples/*` - Code examples
- `docs/api/*` - API references (describes functions, parameters, return values)
- `docs/index.md` - Root page

To contribute:

1. Find the appropriate file or create a new one
2. Write in Markdown format
3. Add the page to the `nav` in `mkdocs.yml`
4. Build and verify the docs with `uv run mkdocs build`

## Code Style

- PEP 8 compliant
- Type hints for public functions (where applicable)
- Docstrings in Google style
- tests for new features

## Pull Request process

1. Fork the repository
2. Create a feature branch
3. Make your changes (include tests)
4. Run tests locally: `pytest`
5. Run lint and type checks: `uv run ruff check nepalikit/ && uv run mypy nepalikit/`
6. Build the docs: `uv run mkdocs build`
7. Submit PR with a descriptive summary

## License

MIT, see [LICENSE](../LICENSE).
