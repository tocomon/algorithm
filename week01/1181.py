n = int(input())
words = set()  # 중복 제거를 위한 set

# 입력 받기
for i in range(n):
    word = input()
    words.add(word)

# 길이가 짧은 것부터, 길이가 같으면 사전 순으로 정렬
result = sorted(words, key=lambda x: (len(x), x))

# 출력
for word in result:
    print(word)
