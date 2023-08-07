def preprocess_good_suffix(pattern, suffix, prefix):
    m = len(pattern)
    for i in range(m):
        suffix[i] = 0
        prefix[i] = False
    for i in range(m - 1):
        j = i
        k = 0
        while j >= 0 and pattern[j] == pattern[m - 1 - k]:
            j -= 1
            k += 1
            suffix[k] = j + 1
        if j == -1:
            prefix[k] = True

def move_by_good_suffix(j, m, suffix, prefix):
    k = m - 1 - j
    if suffix[k] != -1:
        return j - suffix[k] + 1
    for r in range(j + 2, m):
        if prefix[m - r]:
            return r
    return m

def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return []

    # 预处理坏字符规则
    bad_char = {}
    for i in range(m):
        bad_char[pattern[i]] = i

    # 预处理好后缀规则
    suffix = [0] * m
    prefix = [False] * m
    preprocess_good_suffix(pattern, suffix, prefix)
    
    # 开始搜索
    result = []
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            result.append(i)
            # 根据好后缀规则滑动
            if i + m < n:
                shift = m - suffix[1]
            else:
                shift = 1
        else:
            # 根据坏字符规则滑动
            char_shift = j - bad_char.get(text[i + j], -1)
            gs_shift = 0
            if j < m - 1:
                gs_shift = move_by_good_suffix(j, m, suffix, prefix)
            shift = max(1, char_shift, gs_shift)
        i += shift
    return result

# 示例用法
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
result = boyer_moore(text, pattern)
print(result)