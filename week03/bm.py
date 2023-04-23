#Boyer-Moore
def bm_match(txt: str, pat: str) -> int:
    skip = [None] * 26 # 패턴의 알파벳 종류 26개 

    for pt in range(26): # 스킵 테이블 생성 (skip table은 패턴의 각 문자에서 얼마나 많은 문자를 건너뛸지를 미리 계산하여 이동횟수를 최소화하는 테이블)
        skip[pt] = len(pat) # 각 알파벳 기본값은 패턴의 길이로 설정
    
    for pt in range(len(pat) - 1): # 패턴의 각 문자에 대해 스킵 테이블 값 설정
        skip[ord(pat[pt]) - ord('A')] = len(pat) - pt - 1 # 각 문자에서 끝 문자까지의 길이를 저장
    
    pt = len(pat) - 1 # 패턴 찾기 시작 위치 설정
    while pt < len(txt): # 패턴의 끝부터 비교 시작
        pp = len(pat) - 1
        while txt[pt] == pat[pp]: # 패턴 문자열의 처음까지 일치하는 경우, 패턴 위치 반환
            if pp == 0:
                return pt
            pt -= 1 # 비교 위치 이동
            pp -= 1
        # 스킵 테이블을 참조해 다음 비교로 이동    
        pt += skip[ord(txt[pt]) - ord('A')] if skip[ord(txt[pt]) - ord('A')] > len(pat) - pp \
            else len(pat) - pp
    #패턴 미일치
    return -1

if __name__ == '__main__':
    s1 = input('텍스트를 입력하세요:')
    s2 = input('패턴을 입력하세요:')

    idx = bm_match(s1, s2)

    if idx == -1:
        print('텍스트 안에 패턴이 존재하지 않습니다.')
    else:
        print(f'{idx + 1}번째 문자가 일치합니다.')

#string : EAACCAAC
#pattern : CAAC
