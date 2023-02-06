# PreferredItemService

---
## How to run

Using poetry:

```bash
poetry install
poetry shell
python -m preferred_item_service
```

Running tests:
```bash
pytest
```

Using docker:

```bash
docker build -t preferred_item_service .
docker run -dp 8080:8080 preferred_item_service
```