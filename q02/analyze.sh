#!/bin/bash

if [ ! -f "$1" ]; then
    echo "Error: file not found: $1" >&2
    exit 1
fi

echo "Top 2 5xx paths:"
awk -F',' 'NR > 1 && $4 >= 500 && $4 < 600 {count[$3]++} END {for (p in count) print count[p], p}' "$1" | sort -k1,1nr -k2,2 | head -2

echo "Average latency_ms:"
awk -F',' 'NR > 1 {sum += $5; count++} END {printf "%.2f\n", sum/count}' "$1"
