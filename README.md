[简体中文](README_CN.md)

# danbooru artists extractor

Extract and clean Danbooru artist tags into a CSV file for AI image generation workflows.

## Requirements

- Python >= 3.12
- [uv](https://docs.astral.sh/uv/) (package manager)

## Setup

```sh
uv sync
```

Download [tags.parquet](https://huggingface.co/datasets/itterative/danbooru_wikis_full/blob/main/tags.parquet)

## Usage

1. Place `tags.parquet` in the project root.
2. Run the script:

```sh
uv run python main.py
```

3. Output: `danbooru_tags_artists.csv`

## Output Format

| Column     | Description                             |
| ---------- | --------------------------------------- |
| `tag`      | Artist name (underscores → spaces)      |
| `category` | Always `1` (artist)                     |
| `count`    | Number of posts tagged with this artist |
| `alias`    | Reserved (empty)                        |

Rows are sorted by `count` descending.

## Configuration

Edit the constants at the top of `main.py`:

| Constant                          | Default             | Description                            |
| --------------------------------- | ------------------- | -------------------------------------- |
| `MIN_POST_COUNT`                  | `10`                | Drop artists with fewer posts          |
| `BLACKLIST`                       | `['banned_artist']` | Tag names to always exclude            |
| `USE_SPACE_INSTEAD_OF_UNDERSCORE` | `True`              | Replace `_` with space in artist names |
