def smith_waterman(seq1, seq2, gap_penalty, match_score, mismatch_score):
    # 创建得分矩阵和回溯矩阵
    m = len(seq1) + 1
    n = len(seq2) + 1
    score_matrix = [[0] * n for _ in range(m)]
    traceback_matrix = [[0] * n for _ in range(m)]

    # 记录得分矩阵中的最大得分和对应的位置
    max_score = 0
    max_i = 0
    max_j = 0

    # 填充得分矩阵和回溯矩阵
    for i in range(1, m):
        for j in range(1, n):
            if seq1[i - 1] == seq2[j - 1]:
                match = score_matrix[i - 1][j - 1] + match_score
            else:
                match = score_matrix[i - 1][j - 1] + mismatch_score
            delete = score_matrix[i - 1][j] + gap_penalty
            insert = score_matrix[i][j - 1] + gap_penalty
            score_matrix[i][j] = max(0, match, delete, insert)

            # 更新最大得分和位置
            if score_matrix[i][j] > max_score:
                max_score = score_matrix[i][j]
                max_i = i
                max_j = j

            # 更新回溯矩阵
            if score_matrix[i][j] == 0:
                traceback_matrix[i][j] = 0
            elif score_matrix[i][j] == delete:
                traceback_matrix[i][j] = 1
            elif score_matrix[i][j] == insert:
                traceback_matrix[i][j] = 2
            else:
                traceback_matrix[i][j] = 3

    # 回溯生成对齐结果
    align1 = ""
    align2 = ""
    i = max_i
    j = max_j

    while i > 0 and j > 0 and score_matrix[i][j] > 0:
        if traceback_matrix[i][j] == 0:
            break
        elif traceback_matrix[i][j] == 1:
            align1 = seq1[i - 1] + align1
            align2 = "-" + align2
            i -= 1
        elif traceback_matrix[i][j] == 2:
            align1 = "-" + align1
            align2 = seq2[j - 1] + align2
            j -= 1
        else:
            align1 = seq1[i - 1] + align1
            align2 = seq2[j - 1] + align2
            i -= 1
            j -= 1

    return align1, align2

# 示例用法
seq1 = "GCATGCU"
seq2 = "GATTACA"
gap_penalty = -1
match_score = 1
mismatch_score = -1

alignment1, alignment2 = smith_waterman(seq1, seq2, gap_penalty, match_score, mismatch_score)
print("Alignment 1:", alignment1)
print("Alignment 2:", alignment2)