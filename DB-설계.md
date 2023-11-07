
# DB 설계

### [깃허브 링크](https://github.com/NCookies/imad-server/tree/master/document)

### [DB diagram 링크](https://dbdiagram.io/d/64830cbc722eb77494b0176f)


# 참고자료

### 다대다 관계
- 영화-장르, 유저-선호장르, 영화-배우, 영화-감독 등 다대다[N:M] 관계의 구현에 대한 링크
- https://ict-nroo.tistory.com/127

### CASCADE 조건
- https://victorydntmd.tistory.com/195
- `Contents` 라는 상위클래스를 만들고, movie와 tv 테이블이 이를 상속하게 만들까?
- 만약 JPA에서 이렇게 상속하게 만들고 `Contents`에서만 관계를 정의할 수 있다면 굉장히 편할 것 같음
