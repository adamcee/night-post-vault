#!/usr/bin/env bash
# Publish this vault as a website with Quartz.
#   .site/build.sh           build into public/
#   .site/build.sh --serve   preview at http://localhost:8080
set -euo pipefail

# Quartz v4.5.2, pinned by commit so a moved tag can't change what runs.
QUARTZ_COMMIT=4923affa7722dfc751f1074348e6dad214fe0c08
SITE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VAULT="$(cd "$SITE/.." && pwd)"
WORK="$SITE/.quartz"

if [ ! -d "$WORK" ]; then
  git init --quiet "$WORK"
  git -C "$WORK" fetch --quiet --depth 1 https://github.com/jackyzha0/quartz.git "$QUARTZ_COMMIT"
  git -C "$WORK" checkout --quiet FETCH_HEAD
fi
if [ "$(git -C "$WORK" rev-parse HEAD)" != "$QUARTZ_COMMIT" ]; then
  echo "Quartz checkout is not at $QUARTZ_COMMIT; delete $WORK and rerun." >&2
  exit 1
fi
cp "$SITE/quartz.config.ts" "$SITE/quartz.layout.ts" "$WORK/"
[ -d "$WORK/node_modules" ] || (cd "$WORK" && npm ci --silent)

# Stage the vault as Quartz content; the README becomes the home page.
rm -rf "$WORK/content"
rsync -a --exclude '.*' --exclude public "$VAULT/" "$WORK/content/"
mv "$WORK/content/README.md" "$WORK/content/index.md"

cd "$WORK"
if [ "${1:-}" = "--serve" ]; then
  npx quartz build --serve -d content
else
  npx quartz build -d content -o "$VAULT/public"
fi
