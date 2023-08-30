# imad-server-wiki
> IMAD 위키 페이지 백업용 및 기타 스크립트의 변경 이력을 위한 저장소이다.

## 개요

IMAD 프로젝트의 문서를 작성해서 공유하던 노션의 워크스페이스가 용량(이미지 5MB)이 가득차서 이 저장소로 옮기게 되었다. 추후 회의록을 제외한 대부분의 문서는 여기서 공유될 예정이다.

## DTO 클래스 코드 자동 업데이트 스크립트

- 코드 수정 등의 이유로 DTO 클래스의 코드가 변경되었을 때, 파이썬 스크립트를 실행하여 마크다운 페이지의 내부 코드의 업데이트를 수행할 수 있다. 
- 스크립트 실행 시 별도의 매개변수는 필요하지 않으나, 마크다운 페이지를 수정하거나 내용을 추가할 때 정해진 형식을 지켜야 한다.

- 기본적으로 다음과 같은 형식을 지켜야 한다.
````markdown
### {class_name}

>/{github_file_path}
```java
// code block
```
````

- `class_name`에는 클래스 이름이 들어가고, 앞에 `### `을 꼭 붙어야한다. `###` 뒤에 공백이 들어간다는 것을 명심하자
- `github_file_path`은 github API를 통하여 소스파일의 코드를 가져오기 위한 경로이다.
- 작성 예시는 다음과 같다.
````markdown
### Gender

>/src/main/java/com/ncookie/imad/domain/user/entity/Gender.java
````java
package com.ncookie.imad.domain.user.entity;

import lombok.Getter;
import lombok.RequiredArgsConstructor;

@Getter
@RequiredArgsConstructor
public enum Gender {
    NONE("NONE", "default"),
    MALE("MALE", "남자"),
    FEMALE("FEMALE", "여자");

    private final String key;
    private final String gender;
}
```

### AuthProvider

>/src/main/java/com/ncookie/imad/domain/user/entity/AuthProvider.java
````java
package com.ncookie.imad.domain.user.entity;

import java.util.Arrays;

public enum AuthProvider {
    APPLE("APPLE"),
    GOOGLE("GOOGLE"),
    KAKAO("KAKAO"),
    NAVER("NAVER"),
    IMAD("IMAD");

    private final String authProvider;

    public String getAuthProvider() {
        return authProvider;
    }

    AuthProvider(String authProvider){
        this.authProvider = authProvider;
    }

    public static AuthProvider findByCode(String code){
        return Arrays.stream(AuthProvider.values())
                .filter(provider -> provider.getAuthProvider().equals(code))
                .findFirst()
                .orElse(IMAD);
    }
}
```

// ...
````
