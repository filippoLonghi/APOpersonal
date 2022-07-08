def PaintBucket(img, col, pos):
        r = pos[0]
        c = pos[1]
        prev_col = img[r][c]
        img[r][c] = col
        for i in range(max(0, r - 1), min(len(img), r + 2)):
            for j in range(max(0, c - 1), min(len(img[0]), c + 2)):
                if img[i][j] == prev_col:
                    PaintBucket(img, col, (i, j))
        return img

img = [[5, 2, 3, 2, 1, 4], [1, 4, 2, 5, 2, 4], [2, 3, 2, 2, 2, 5], [2, 4, 1, 2, 3, 1]]
print(PaintBucket(img,1,(2,4)))