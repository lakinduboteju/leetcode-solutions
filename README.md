# Leetcode Solutions

## How to debug

``` bash
$ docker compose build
$ docker compose up -d
$ docker compose down
```

``` bash
$ docker exec -it leetcode bash
```

``` bash
# Run following command and debug using Pythong Debugger in vscode
$ poetry run python -Xfrozen_modules=off -m debugpy --listen 0.0.0.0:5678 --wait-for-client xxxx.py
```

## Contents

1. [88. Merge Sorted Array](src/88_merge_sorted_array.py) |
[Question](https://leetcode.com/problems/merge-sorted-array)
