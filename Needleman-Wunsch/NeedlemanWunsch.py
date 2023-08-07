def needleman_wunsch(seq1, seq2, gap_penalty, match_score, mismatch_score):
    # 创建得分矩阵
    m = len(seq1) + 1
    n = len(seq2) + 1
    score_matrix = [[0] * n for _ in range(m)]

    # 初始化第一行和第一列
    for i in range(m):
        score_matrix[i][0] = i * gap_penalty
    for j in range(n):
        score_matrix[0][j] = j * gap_penalty

    # 填充得分矩阵
    for i in range(1, m):
        for j in range(1, n):
            if seq1[i - 1] == seq2[j - 1]:
                match = score_matrix[i - 1][j - 1] + match_score
            else:
                match = score_matrix[i - 1][j - 1] + mismatch_score
            delete = score_matrix[i - 1][j] + gap_penalty
            insert = score_matrix[i][j - 1] + gap_penalty
            score_matrix[i][j] = max(match, delete, insert)

    # 回溯生成对齐结果
    align1 = ""
    align2 = ""
    i = m - 1
    j = n - 1
    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            score = match_score
        else:
            score = mismatch_score
        if score_matrix[i][j] == score_matrix[i - 1][j - 1] + score:
            align1 = seq1[i - 1] + align1
            align2 = seq2[j - 1] + align2
            i -= 1
            j -= 1
        elif score_matrix[i][j] == score_matrix[i - 1][j] + gap_penalty:
            align1 = seq1[i - 1] + align1
            align2 = "-" + align2
            i -= 1
        else:
            align1 = "-" + align1
            align2 = seq2[j - 1] + align2
            j -= 1

    while i > 0:
        align1 = seq1[i - 1] + align1
        align2 = "-" + align2
        i -= 1

    while j > 0:
        align1 = "-" + align1
        align2 = seq2[j - 1] + align2
        j -= 1

    return align1, align2

# 示例用法
seq1 = "GCATGCU"
seq2 = "GATTACA"
gap_penalty = -1
match_score = 1
mismatch_score = -1

alignment1, alignment2 = needleman_wunsch(seq1, seq2, gap_penalty, match_score, mismatch_score)
print("Alignment 1:", alignment1)
print("Alignment 2:", alignment2)