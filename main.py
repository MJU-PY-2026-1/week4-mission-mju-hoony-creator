# 파일이름 :파프입4주차 미션
#미션 3

bucket_list = []

bucket_list.append(input("맛집 리스트 입력: "))
bucket_list.append(input("맛집 리스트 입력: "))
bucket_list.append(input("맛집 리스트 입력: "))
print(f"리스트: {bucket_list}\n")

vip = input("맛집 리스트 추가: ")
bucket_list.insert(0, vip)
print(f"리스트 : {bucket_list}\n")

visited = input("도장 깨기: ")
bucket_list.remove(visited)
print(f"리스트 : {bucket_list}")

# 작 성 자 :변성훈
#🚀 1. 난이도 및 자기 평가 (0~5점)
#체감 난이도: 2점
#스스로의 만족도: 코드 구조가 단순하고 직관적이어서 익히기가 편했던 것 같다.
#💻 2. 실습 소감 및 교수님께 한마디
#깃허브로 실습해보는건 처음인데 뭐가 뭔지 잘 모르겠지만,, 그래도 재미있어 보인다. 화이팅!!