tscore = int(input("당신의 토익 점수를 입력하세요:"))
if tscore >= 900:
    if tscore > 990:
        print("해당점수는 없습니다.")
    else:
        print("당신의 토익 점수는", tscore, "상위권 점수입니다.")
elif tscore >= 600:
    print("당신의 토익 점수는", tscore, "중상위권 점수입니다.")
elif tscore >= 300:
    print("당신의 토익 점수는", tscore, "중위권 점수입니다.")
else:
    print("당신의 토익 점수는", tscore, "하위권 점수입니다.")
print("if 문 종료됨")