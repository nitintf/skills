#!/usr/bin/env bash
# Render HTML designs to PNGs so they can be looked at before anyone else does.
#
# Usage: shots.sh <out-dir> <file.html>... [--web]
#   Default viewport is a phone (390x844). --web renders at 1440x900 and 375x812.
#   Each file is shot in light and dark (dark via ?theme=dark, which every studio
#   page honours by setting data-theme="dark" on <html>).
set -euo pipefail

out="$1"; shift
web=0; files=()
for a in "$@"; do
  if [ "$a" = "--web" ]; then web=1; else files+=("$a"); fi
done
[ ${#files[@]} -gt 0 ] || { echo "usage: shots.sh <out-dir> <file.html>... [--web]"; exit 2; }
mkdir -p "$out"

# Chromium for Playwright, installed once.
npx -y playwright install chromium >/dev/null 2>&1 || true

sizes=("390,844")
[ "$web" = 1 ] && sizes=("1440,900" "375,812")

for f in "${files[@]}"; do
  abs="$(cd "$(dirname "$f")" && pwd)/$(basename "$f")"
  name="$(basename "$f" .html)"
  for size in "${sizes[@]}"; do
    for theme in light dark; do
      png="$out/${name}-${size/,/x}-${theme}.png"
      url="file://${abs}"
      [ "$theme" = dark ] && url="${url}?theme=dark"
      npx -y playwright screenshot --full-page --viewport-size="$size" --wait-for-timeout=600 "$url" "$png" >/dev/null
      echo "$png"
    done
  done
done
