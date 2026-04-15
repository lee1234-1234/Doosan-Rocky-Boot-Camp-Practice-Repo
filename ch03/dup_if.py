# 기본 if 문

tscore = 800

print("당신의 토익 점수는")
if tscore >= 900:
    print(tscore, "상위권")
elif tscore >= 700:
    if tscore >= 800:
        print(tscore, "중상위권")
    else:
        print(tscore, "중하위권")
else:
    print(tscore, "하위권")
print("if문 종료")