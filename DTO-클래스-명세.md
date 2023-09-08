### Gender

>/src/main/java/com/ncookie/imad/domain/user/entity/Gender.java
```java
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
```java
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

### ContentsType

>/src/main/java/com/ncookie/imad/domain/contents/entity/ContentsType.java
```java
package com.ncookie.imad.domain.contents.entity;

import lombok.Getter;

// 작품 상세 페이지에서 보여주는 작품 종류의 ENUM 클래스
@Getter
public enum ContentsType {
    MOVIE("MOVIE"),
    TV("TV"),
    ANIMATION("ANIMATION");         // 장르에 "애니메이션"이 포함되어 있으면 TV, MOVIE가 아닌 ANIMATION으로 분류함

    private final String contentsType;

    ContentsType(String contentsType) {
        this.contentsType = contentsType;
    }
}
```

### SignUpRequest

>/src/main/java/com/ncookie/imad/domain/user/dto/request/SignUpRequest.java
```java
package com.ncookie.imad.domain.user.dto.request;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import com.ncookie.imad.domain.user.entity.AuthProvider;
import com.ncookie.imad.domain.user.entity.Gender;
import lombok.Getter;
import lombok.NoArgsConstructor;

@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
@NoArgsConstructor
@Getter
public class SignUpRequest {
    private String email;
    private String password;
    private AuthProvider authProvider;      // 소셜 회원은 별도의 함수를 사용하기 때문에 "IMAD"만 들어옴
}
```

### UserUpdateRequest

>/src/main/java/com/ncookie/imad/domain/user/dto/request/UserUpdateRequest.java
```java
package com.ncookie.imad.domain.user.dto.request;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import com.ncookie.imad.domain.user.entity.Gender;
import lombok.Getter;

@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
@Getter
public class UserUpdateRequest {
    Gender gender;
    int ageRange;
    int profileImage;
    String nickname;
    // TODO: 장르 추가해야함
}
```

### ModifyUserPasswordRequest

>/src/main/java/com/ncookie/imad/domain/user/dto/request/ModifyUserPasswordRequest.java
```java
package com.ncookie.imad.domain.user.dto.request;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class ModifyUserPasswordRequest {
    String oldPassword;
    String newPassword;
}
```

### UserInfoDuplicationRequest

>/src/main/java/com/ncookie/imad/domain/user/dto/request/UserInfoDuplicationRequest.java
```java
package com.ncookie.imad.domain.user.dto.request;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import lombok.Getter;

@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
@Getter
// 이메일 및 닉네임 중복검사 요청에서 사용되는 DTO 클래스
public class UserInfoDuplicationRequest {
    private String info;    // 이메일 또는 닉네임이 중복되는지 확인하기 위해 사용되는 변수
}
```

### UserInfoResponse

>/src/main/java/com/ncookie/imad/domain/user/dto/response/UserInfoResponse.java
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
    
    // 로그인 주체. 서비스 자체 회원 또는 소설 회원 등이 있음
    private AuthProvider authProvider;

    private Gender gender;
    
    // 연령대
    private int ageRange;

    private int profileImage;

    // 유저의 추가정보 입력여부를 구분하기 위한 플래그 변수
    private Role role;
}
```

### UserInfoDuplicationResponse

>/src/main/java/com/ncookie/imad/domain/user/dto/response/UserInfoDuplicationResponse.java
```java
package com.ncookie.imad.domain.user.dto.response;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import lombok.Builder;
import lombok.Getter;

@Getter
@Builder
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class UserInfoDuplicationResponse {
    private boolean validation;     // 중복 검사 결과 플래그. 중복이 아니라면 true, 중복 데이터라면 false 값을 가진다.
}
```

### ContentsSearchResponse

>/src/main/java/com/ncookie/imad/domain/contents/dto/ContentsSearchResponse.java
```java
package com.ncookie.imad.domain.contents.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import lombok.*;

import java.util.List;

@Getter
@NoArgsConstructor
@AllArgsConstructor
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class ContentsSearchResponse {
    private int page;           // 해당 검색결과의 페이지
    private int totalPages;     // 검색 결과 총 페이지 수
    private int totalResults;   // 검색 결과 데이터 총 개수

    @JsonProperty("results")
    private List<ContentsSearchDetails> results;     // 검색결과 상세 데이터
}
```

### ContentsSearchDetails

>/src/main/java/com/ncookie/imad/domain/contents/dto/ContentsSearchDetails.java
```java
package com.ncookie.imad.domain.contents.dto;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import lombok.*;

import java.time.LocalDate;
import java.util.List;

@Builder
@NoArgsConstructor
@AllArgsConstructor
@Getter
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class ContentsSearchDetails {
    private int id;     // TMDB에서 사용하는 id

    // For Movie
    private String title;               // 번역된 제목
    private String original_title;      // 원본 제목
    private LocalDate releaseDate;      // 개봉일

    // For TV shows
    private String name;                // 번역된 제목
    private String original_name;       // 원본 제목
    private LocalDate firstAirDate;     // 첫 방영일

    private List<String> origin_country;    // 원본 국가
    private String original_language;       // 원본 언어

    private boolean adult;                  // 성인여부. 일반적인 19세 등급을 받은 작품이 아니라, 포르노와 같은 성인용 작품이 여기에 해당됨
    private String backdrop_path;           // 배경 포스터
    private String overview;                // 작품 상세설명
    private String poster_path;             // 포스터
    private String media_type;              // 쓰이는 것을 본 적이 없어서 잘 모르겠음
    private List<Integer> genreIds;         // 장르 리스트
    private boolean video;                  // 프리뷰 영상
}
```

### TmdbDetails

>/src/main/java/com/ncookie/imad/domain/tmdb/dto/TmdbDetails.java
```java
package com.ncookie.imad.domain.tmdb.dto;

import com.fasterxml.jackson.annotation.*;
import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import com.ncookie.imad.domain.contents.entity.ContentsType;
import com.ncookie.imad.domain.networks.dto.DetailsNetworks;
import com.ncookie.imad.domain.person.dto.DetailsCredits;
import com.ncookie.imad.domain.season.dto.DetailsSeason;
import lombok.*;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

@Builder
@Data
@NoArgsConstructor
@AllArgsConstructor
@JsonIgnoreProperties(ignoreUnknown = true, allowSetters = true)
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
// 작품 상세 정보를 클라이언트에게 전달해주기 위한 DTO 클래스
public class TmdbDetails {
    private long contentsId;                        // IMAD 자체적으로 사용하는 id
    private long tmdbId;                            // TMDB 내부적으로 사용하는 id

    private String overview;                        // 작품 개요
    private String tagline;                         // 작품의 핵심이 되는 포인트나 제목에 대한 부연설명
    private String posterPath;                      // 포스터
    private String originalLanguage;                // 원어
    private String certification;                   // 영상물 등급

    private String status;                          // 제작 중, 개봉함, 방영함 등의 값을 가짐

    private Set<Integer> genres;                    // 장르 리스트
    private Set<String> productionCountries;        // 제작 국가


    // IMAD Data
    private ContentsType contentsType;


    // Movie Data
    private String title;
    private String originalTitle;

    private String releaseDate;                      // 개봉일
    private int runtime;                             // 상영시간


    // TV Data
    private String name;
    private String originalName;

    private String firstAirDate;                      // 첫화 방영일
    private String lastAirDate;                       // 마지막화 방영일

    private int numberOfEpisodes;                     // 에피소드 개수
    private int numberOfSeasons;                      // 시즌 개수

    private List<DetailsSeason> seasons;              // 시즌 정보
    private List<DetailsNetworks> networks;           // 작품 방영한 방송사 정보


    // Credits
    @JsonProperty("credits")
    private DetailsCredits credits;                    // 출연진(배우, 감독, 작가, 스태프 등 포함) 정보


    @JsonCreator
    public TmdbDetails(
            @JsonProperty("id") int id,
            @JsonProperty("genres") Set<DetailsGenre> genreSet,
            @JsonProperty("production_countries") Set<ProductionCountry> productionCountrySet) {
        this.tmdbId = id;

        this.genres = new HashSet<>();
        genreSet.forEach(genre -> this.genres.add(genre.getId()));

        this.productionCountries = new HashSet<>();
        productionCountrySet.forEach(country -> this.productionCountries.add(country.getIso_3166_1()));
    }
}
```

### DetailsSeason

>/src/main/java/com/ncookie/imad/domain/season/dto/DetailsSeason.java
```java
package com.ncookie.imad.domain.season.dto;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import com.ncookie.imad.domain.season.entity.Season;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDate;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@JsonIgnoreProperties(ignoreUnknown = true)
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
// TV 작품의 시즌 정보를 가지고 있는 DTO 클래스
public class DetailsSeason {
    private long id;

    private String name;
    private LocalDate airDate;
    private int episodeCount;
    private String overview;
    private String posterPath;
    private int seasonNumber;

    @JsonCreator
    public DetailsSeason(@JsonProperty("air_date") String airDateString) {
        if (airDateString == null) {
            this.airDate = null;
        } else {
            this.airDate = LocalDate.parse(airDateString);
        }
    }

    public static DetailsSeason toDTO(Season season) {
        return  DetailsSeason.builder()
                .id(season.getSeasonId())
                .name(season.getSeasonName())
                .airDate(season.getAirDate())
                .episodeCount(season.getEpisodeCount())
                .overview(season.getOverview())
                .posterPath(season.getPosterPath())
                .seasonNumber(season.getSeasonNumber())
                .build();
    }
}
```

### DetailsNetworks

>/src/main/java/com/ncookie/imad/domain/networks/dto/DetailsNetworks.java
```java
package com.ncookie.imad.domain.networks.dto;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import com.ncookie.imad.domain.networks.entity.Networks;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Builder
@Data
@NoArgsConstructor
@AllArgsConstructor
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
// TV 작품을 방영한 방송사의 정보를 가지고 있는 DTO 클래스
public class DetailsNetworks {
    private long id;
    private String logoPath;
    private String name;
    private String originCountry;

    public static DetailsNetworks toDTO(Networks networks) {
        return DetailsNetworks.builder()
                .id(networks.getNetworksId())
                .logoPath(networks.getLogoPath())
                .name(networks.getNetworksName())
                .originCountry(networks.getOriginCountry())
                .build();
    }
}
```

### DetailsPerson

>/src/main/java/com/ncookie/imad/domain/person/dto/DetailsPerson.java
```java
package com.ncookie.imad.domain.person.dto;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import com.ncookie.imad.domain.person.entity.CreditType;
import com.ncookie.imad.domain.user.entity.Gender;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.Objects;


@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@JsonIgnoreProperties(ignoreUnknown = true)
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
// 배우, 감독, 작가, 스태프 등의 정보를 가지고 있는 DTO 클래스
public class DetailsPerson {
    // person id. 인물 자체에 대한 id
    private long id;

    // credit id. 작품과 인물 간의 연결점인 credit의 id
    private String creditId;

    private String name;
    private Gender gender;
    private String profilePath;

    private String character;

    private String knownForDepartment;
    private String department;
    private String job;

    // 많은 직책을 맡을수록 작품의 대표인물, 네임드가 될 확률이 높을 것이라고 판단했다.
    // 클라이언트 화면에서 작품정보의 상단에 표시되는 인물을 구분하기 위해서 이 변수를 만들었다.
    // crew 데이터의 리스트에서 중복될수록 카운트를 +1 한다.
    private int importanceOrder;

    // 해당 인물이 cast(배우)인지, crew(감독, 작가, PD 등)인지 구분하기 위한 변수
    private CreditType creditType;

    @JsonCreator
    public DetailsPerson(@JsonProperty("gender") int gender) {
        if (gender == 1) {
            this.gender = Gender.FEMALE;
        } else if (gender == 2) {
            this.gender = Gender.MALE;
        } else {
            this.gender = Gender.NONE;
        }
    }

    @Override
    public boolean equals(Object object) {
        if (this == object) return true;
        if (!(object instanceof DetailsPerson person)) return false;
        return id == person.id;
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
    }
}
```

---

## 리뷰

### AddReviewRequest

>/src/main/java/com/ncookie/imad/domain/review/dto/AddReviewRequest.java
```java
package com.ncookie.imad.domain.review.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import lombok.Data;

@Data
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class AddReviewRequest {
    private Long contentsId;            // 작품 id
    
    private String title;               // 리뷰 제목
    private String content;             // 리뷰 본문
    
    private float score;                 // 리뷰 점수
    private boolean isSpoiler;          // 스포일러 여부
}
```

### AddReviewResponse

>/src/main/java/com/ncookie/imad/domain/review/dto/AddReviewResponse.java
```java
package com.ncookie.imad.domain.review.dto;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;


@Builder
@Data
@NoArgsConstructor
@AllArgsConstructor
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class AddReviewResponse {
    private Long reviewId;
}
```

### ModifyReviewRequest

>/src/main/java/com/ncookie/imad/domain/review/dto/ModifyReviewRequest.java
```java
package com.ncookie.imad.domain.review.dto;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import lombok.Data;


@Data
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class ModifyReviewRequest {
    private String title;               // 리뷰 제목
    private String content;             // 리뷰 본문

    private float score;                 // 리뷰 점수
    private boolean isSpoiler;          // 스포일러 여부
}
```

### ReviewDetailsResponse

>/src/main/java/com/ncookie/imad/domain/review/dto/ReviewDetailsResponse.java
```java
package com.ncookie.imad.domain.review.dto;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

@Builder
@NoArgsConstructor
@AllArgsConstructor
@Data
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class ReviewDetailsResponse {
    private Long reviewId;                  // 리뷰 ID
    private Long contentsId;                // 작품 ID
    
    // TODO: 클라이언트와 논의하여 필요한 작품 추가 정보 등에 대해 정해야함 (제목, 포스터, 개봉연도 등)

    private String title;                   // 제목
    private String content;                 // 본문

    private float score;                    // 리뷰 점수
    private boolean isSpoiler;              // 스포일러 여부

    private int likeCnt;                    // 좋아요 수
    private int dislikeCnt;                 // 싫어요 수

    private LocalDateTime createdAt;        // 리뷰 작성 날짜
    private LocalDateTime modifiedAt;       // 리뷰 수정 날짜

    private int likeStatus;                 // 1이면 좋아요, -1이면 싫어요, 0이면 아무 상태도 아님
}
```

### ReviewLikeStatusRequest

>/src/main/java/com/ncookie/imad/domain/review/dto/ReviewLikeStatusRequest.java
```java
package com.ncookie.imad.domain.review.dto;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import lombok.Data;

@Data
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class ReviewLikeStatusRequest {
    int likeStatus;
}
```

