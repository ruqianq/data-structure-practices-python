from typing import List


def flood_fill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    orig_color = image[sr][sc]

    def dfs(i, j):
        if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]) or image[i][j] != orig_color:
            return
        image[i][j] = newColor
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    if newColor != orig_color:
        dfs(sr, sc)

    return image
