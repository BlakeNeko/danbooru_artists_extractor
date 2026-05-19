# danbooru artists extractor

从 Danbooru 标签数据中提取并清洗画师标签，输出 CSV 文件，用于 AI 图像生成工作流。

## 环境要求

- Python >= 3.12
- [uv](https://docs.astral.sh/uv/)（包管理器）

## 安装

```sh
uv sync
```

下载 [tags.parquet](https://huggingface.co/datasets/itterative/danbooru_wikis_full/blob/main/tags.parquet)

## 使用方法

1. 将 `tags.parquet`放置在项目根目录。
2. 运行脚本：

```sh
uv run python main.py
```

3. 输出文件：`danbooru_tags_artists.csv`

## 输出格式

| 列名       | 说明                           |
| ---------- | ------------------------------ |
| `tag`      | 画师名称（下划线已替换为空格） |
| `category` | 固定为 `1`（画师类别）         |
| `count`    | 使用该标签的作品数量           |
| `alias`    | 预留字段（空）                 |

数据按 `count` 降序排列。

## 配置项

修改 `main.py` 顶部的常量即可调整行为：

| 常量                              | 默认值              | 说明                         |
| --------------------------------- | ------------------- | ---------------------------- |
| `MIN_POST_COUNT`                  | `10`                | 作品数低于此值的画师将被剔除 |
| `BLACKLIST`                       | `['banned_artist']` | 始终排除的标签名称           |
| `USE_SPACE_INSTEAD_OF_UNDERSCORE` | `True`              | 将画师名中的下划线替换为空格 |
