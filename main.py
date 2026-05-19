import pandas as pd
import os

# ================= Configuration Area =================
input_file = 'tags.parquet'
output_file = 'danbooru_tags_artists.csv'

# 1. Filter threshold: artists with fewer posts than this will be removed
MIN_POST_COUNT = 10 

# 2. Blacklist: completely exclude these tags
BLACKLIST = ['banned_artist']

# 3. Format conversion: replace underscores with spaces?
USE_SPACE_INSTEAD_OF_UNDERSCORE = True
# ===========================================

if not os.path.exists(input_file):
    print(f"❌ Error: cannot find {input_file}")
    exit()

print("🚀 Reading Parquet file...")
df = pd.read_parquet(input_file)

# Auto-detect column names
cols = df.columns
cat_col = 'category' if 'category' in cols else 'category_id'
name_col = 'name' if 'name' in cols else 'tag'
count_col = 'post_count' if 'post_count' in cols else 'count'

# 1. Filter artists (Category = 1)
print("🎨 Filtering artist tags...")
artists = df[df[cat_col] == 1].copy()
artists = artists.rename(columns={name_col: 'tag', count_col: 'count'})

# Record original count
original_count = len(artists)

# 2. Apply filter logic
print("🧹 Cleaning data...")

artists = artists[artists['count'] >= MIN_POST_COUNT]
artists = artists[~artists['tag'].isin(BLACKLIST)]

# Calculate filter results
filtered_count = len(artists)
print(f"   - Original count: {original_count}")
print(f"   - After cleaning: {filtered_count}")
print(f"   - Removed {original_count - filtered_count} invalid/cold artists")

# 3. Format processing
print("🔨 Formatting text...")

# Force category to 1
artists['category'] = 1

# Handle underscores
if USE_SPACE_INSTEAD_OF_UNDERSCORE:
    print("   - [Convert] Replacing underscores with spaces")
    artists['tag'] = artists['tag'].str.replace('_', ' ')
else:
    print("   - [Keep] Preserving original underscore format")

# Ensure alias column exists
artists['alias'] = ""

# 4. Sort
artists = artists.sort_values(by='count', ascending=False)

# 5. Export
final_df = artists[['tag', 'category', 'count', 'alias']]
final_df.to_csv(output_file, index=False, encoding='utf-8')

print(f"✅ Done! Exported {len(final_df)} artists to {output_file}")