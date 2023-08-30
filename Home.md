> IMAD 프로젝트에 대한 명세, 설계, 조사 자료 등을 정리한 위키이다.

- [브레인 스토밍](./브레인-스토밍)

- [기능 명세서](./기능-명세서)

- [앱 레이아웃](./앱-레이아웃)

- [DB 설계](./DB-설계)

- [API 후보](./API-후보)

- [이메일 및 패스워드 정규식 패턴](./이메일-및-패스워드-정규식-패턴)

- [TMDB API 정리](./TMDB-API-정리)

- [랭킹 산출 기준](./랭킹-산출-기준)

- [REST API 문서]
  - 구글 docs 문서 링크를 첨부하려 했으나 외부에 노출 시 보안 문제가 발생할 수 있다고 판단하여 보류함

- [회원탈퇴](./회원탈퇴)

### UserInfoResponse.java

> src/main/java/com/ncookie/imad/domain/user/dto/response/UserInfoResponse.java
```java
package com.ncookie.imad.domain.user.dto.response;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import com.ncookie.imad.domain.user.entity.AuthProvider;
import com.ncookie.imad.domain.user.entity.Gender;
import com.ncookie.imad.domain.user.entity.Role;
import lombok.Builder;
import lombok.Getter;

@Getter
@Builder
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class UserInfoResponse {
    private String email;
    private String nickname;
    private AuthProvider authProvider;
    private Gender gender;
    private int ageRange;
    private int profileImage;
    private Role role;
}
```

### UserInfoResponseTest1.java

> src/main/java/com/ncookie/imad/domain/user/dto/response/UserInfoResponseTest1.java
```java
package com.ncookie.imad.domain.user.dto.response;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import com.ncookie.imad.domain.user.entity.AuthProvider;
import com.ncookie.imad.domain.user.entity.Gender;
import com.ncookie.imad.domain.user.entity.Role;
import lombok.Builder;
import lombok.Getter;

@Getter
@Builder
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class UserInfoResponseTest1 {
    private String email;
    private String nickname;
    private AuthProvider authProvider;
    private Gender gender;
    private int ageRange;
    private int profileImage;
    private Role role;
}
```

### UserInfoResponseTest2.java

> src/main/java/com/ncookie/imad/domain/user/dto/response/UserInfoResponseTest2.java
```java
package com.ncookie.imad.domain.user.dto.response;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import com.ncookie.imad.domain.user.entity.AuthProvider;
import com.ncookie.imad.domain.user.entity.Gender;
import com.ncookie.imad.domain.user.entity.Role;
import lombok.Builder;
import lombok.Getter;

@Getter
@Builder
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class UserInfoResponseTest2 {
    private String email;
    private String nickname;
    private AuthProvider authProvider;
    private Gender gender;
    private int ageRange;
    private int profileImage;
    private Role role;
}
```