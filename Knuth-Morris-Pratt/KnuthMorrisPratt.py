def build_lps(pattern):
    """
    构建最长公共前后缀列表
    """
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(text, pattern):
    """
    使用 KMP 算法在文本中搜索模式
    """
    m = len(pattern)
    n = len(text)

    # 构建最长公共前后缀（lps）列表
    lps = build_lps(pattern)

    i = 0  # 在文本中的索引
    j = 0  # 在模式中的索引
    matches = []

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

            if j == m:
                matches.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches

# 示例用法
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
matches = kmp_search(text, pattern)
print("匹配位置：", matches)