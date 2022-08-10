W_UNI = [int(input()) for i in range(10)]   # W 대학 10명 점수
K_UNI = [int(input()) for i in range(10)]   # K 대학 10명 점수
W_UNI.sort()                                # W 대학 정렬
K_UNI.sort()                                # K 대학 정렬

W_score = W_UNI[7] + W_UNI[8] + W_UNI[9]    # W 대학 상위 3명 점수 합
K_score = K_UNI[7] + K_UNI[8] + K_UNI[9]    # K 대학 상위 3명 점수 합

print(W_score, K_score)                     # W 대학, K 대학 점수 출력