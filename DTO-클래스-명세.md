---
## 일반

### ListResponse
```java
package com.ncookie.imad.domain.common.dto;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.Getter;
import lombok.experimental.SuperBuilder;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Sort;

import java.util.List;


@Data
@SuperBuilder
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class ListResponse<T> {
    private List<T> detailsList;

    private long totalElements;              // 총 데이터 개수
    private long totalPages;                 // 총 페이지 수

    private int pageNumber;                 // 현재 페이지
    private int numberOfElements;           // 현재 페이지의 데이터 개수
    private int sizeOfPage;                 // 한 페이지 당 최대 데이터 개수

    private int sortDirection;              // 0 : 오름차순, 1 : 내림차순
    private String sortProperty;            // 정렬 기준 (createdDate)


    @Getter
    @AllArgsConstructor
    public static class SortVariable {
        private int sortDirection;
        private String sortProperty;
    }

    protected static SortVariable getSortVariable(Page<?> page) {
        int sortDirection = 0;
        String sortProperty = null;
        Sort sort = page.getSort();
        List<Sort.Order> orders = sort.toList();
        for (Sort.Order order : orders) {
            sortDirection = order.getDirection().isAscending() ? 0 : 1;
            sortProperty = order.getProperty();
        }

        return new SortVariable(sortDirection, sortProperty);
    }
}
```

---
## 회원가입 / 로그인

### Gender
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
```java
package com.ncookie.imad.domain.user.dto.request;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import com.ncookie.imad.domain.user.entity.Gender;
import lombok.Getter;

import java.util.Set;

@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
@Getter
public class UserUpdateRequest {
    Gender gender;
    int ageRange;
    int profileImage;
    String nickname;

    Set<Long> preferredTvGenres;
    Set<Long> preferredMovieGenres;
}
```

### ModifyUserPasswordRequest
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
```java
package com.ncookie.imad.domain.user.dto.response;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import com.ncookie.imad.domain.user.entity.AuthProvider;
import com.ncookie.imad.domain.user.entity.Gender;
import com.ncookie.imad.domain.user.entity.Role;
import com.ncookie.imad.domain.user.entity.UserAccount;
import lombok.Builder;
import lombok.Getter;

import java.util.Set;

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

    private Set<Long> preferredTvGenres;
    private Set<Long> preferredMovieGenres;


    public static UserInfoResponse toDTO(UserAccount userAccount) {
        return UserInfoResponse.builder()
                .email(userAccount.getEmail())
                .nickname(userAccount.getNickname())
                .authProvider(userAccount.getAuthProvider())
                .gender(userAccount.getGender())
                .ageRange(userAccount.getAgeRange())
                .profileImage(userAccount.getProfileImage())

                .preferredTvGenres(userAccount.getPreferredTvGenres())
                .preferredMovieGenres(userAccount.getPreferredMovieGenres())

                .role(userAccount.getRole())
                .build();
    }
}
```

### UserInfoDuplicationResponse
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

---
## 작품

### ContentsSearchResponse
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
    private ContentsType tmdbType;                  // TMDB 내부적으로 사용하는 작품 type

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
    private int reviewCnt;                          // 리뷰 개수
    private Float imadScore;                        // IMAD 평점 평균


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
    
    
    // 북마크 여부
    private Long bookmarkId;
    private boolean bookmarkStatus;

    // 리뷰 정보
    private Long reviewId;
    private boolean reviewStatus;


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
```java
package com.ncookie.imad.domain.review.dto.request;

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

    @JsonProperty("is_spoiler")
    private boolean isSpoiler;          // 스포일러 여부
}
```

### AddReviewResponse
```java
package com.ncookie.imad.domain.review.dto.response;

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
```java
package com.ncookie.imad.domain.review.dto.request;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import lombok.Data;


@Data
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class ModifyReviewRequest {
    private String title;               // 리뷰 제목
    private String content;             // 리뷰 본문

    private float score;                 // 리뷰 점수

    @JsonProperty("is_spoiler")
    private boolean isSpoiler;          // 스포일러 여부
}
```

### ReviewDetailsResponse
```java
package com.ncookie.imad.domain.review.dto.response;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import com.ncookie.imad.domain.review.entity.Review;
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

    // 작품 정보
    private Long contentsId;                // 작품 ID
    private String contentsTitle;           // 작품 제목
    private String contentsPosterPath;      // 작품 포스터 이미지 경로
    
    // 유저 정보
    private Long userId;                    // 유저 id
    private String userNickname;            // 닉네임
    private int userProfileImage;           // 프로필 이미지

    // 리뷰 정보
    private String title;                   // 제목
    private String content;                 // 본문

    private float score;                    // 리뷰 점수
    private boolean isSpoiler;              // 스포일러 여부

    private int likeCnt;                    // 좋아요 수
    private int dislikeCnt;                 // 싫어요 수

    private LocalDateTime createdAt;        // 리뷰 작성 날짜
    private LocalDateTime modifiedAt;       // 리뷰 수정 날짜

    private int likeStatus;                 // 1이면 좋아요, -1이면 싫어요, 0이면 아무 상태도 아님

    public static ReviewDetailsResponse toDTO(Review review) {
        return ReviewDetailsResponse.builder()
                .reviewId(review.getReviewId())

                .contentsId(review.getContents().getContentsId())
                .contentsTitle(review.getContents().getTranslatedTitle())
                .contentsPosterPath(review.getContents().getPosterPath())

                .userId(review.getUserAccount().getId())
                .userNickname(review.getUserAccount().getNickname())
                .userProfileImage(review.getUserAccount().getProfileImage())

                .title(review.getTitle())
                .content(review.getContent())

                .score(review.getScore())
                .isSpoiler(review.isSpoiler())

                .likeCnt(review.getLikeCnt())
                .dislikeCnt(review.getDislikeCnt())

                .createdAt(review.getCreatedDate())
                .modifiedAt(review.getModifiedDate())

                .build();
    }
}
```

### ReviewListResponse
```java
package com.ncookie.imad.domain.review.dto.response;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import com.ncookie.imad.domain.common.dto.ListResponse;
import lombok.experimental.SuperBuilder;
import org.springframework.data.domain.Page;

import java.util.List;


@SuperBuilder
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class ReviewListResponse extends ListResponse<ReviewDetailsResponse> {
    public static ReviewListResponse toDTO(Page<?> page, List<ReviewDetailsResponse> reviewList) {
        SortVariable sortVariable = getSortVariable(page);
        return ReviewListResponse.builder()
                .detailsList(reviewList)

                .totalElements(page.getTotalElements())
                .totalPages(page.getTotalPages())

                .pageNumber(page.getNumber())
                .numberOfElements(page.getNumberOfElements())
                .sizeOfPage(page.getSize())

                .sortDirection(sortVariable.getSortDirection())
                .sortProperty(sortVariable.getSortProperty())

                .build();
    }
}
```

---
## 게시글

### AddPostingRequest
```java
package com.ncookie.imad.domain.posting.dto.request;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import lombok.Data;


@Data
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class AddPostingRequest {
    private Long contentsId;            // 작품 ID

    private String title;               // 게시글 제목
    private String content;             // 게시글  본문
    private int category;               // 게시글 카테고리

    @JsonProperty("is_spoiler")
    private boolean isSpoiler;          // 스포일러 여부
}
```

### ModifyPostingRequest 
```java
package com.ncookie.imad.domain.posting.dto.request;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import lombok.Data;


@Data
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class ModifyPostingRequest {
    private String title;               // 게시글 제목
    private String content;             // 게시글 본문
    private int category;

    @JsonProperty("is_spoiler")
    private boolean isSpoiler;          // 스포일러 여부
}
```

### PostingDetailsResponse 
```java
package com.ncookie.imad.domain.posting.dto.response;


import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import com.ncookie.imad.domain.posting.entity.Posting;
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
public class PostingDetailsResponse {
    private Long postingId;                 // 게시글 ID

    // 작품 정보
    private Long contentsId;                // 작품 ID
    private String contentsTitle;           // 작품 제목
    private String contentsPosterPath;      // 작품 포스터 이미지 경로

    // 유저 정보
    private Long userId;                    // 유저 id
    private String userNickname;            // 닉네임
    private int userProfileImage;           // 프로필 이미지

    // 게시글 정보
    private String title;                   // 제목
    private String content;                 // 본문
    private int category;                   // 카테고리

    private boolean isSpoiler;              // 스포일러 여부

    private int viewCnt;                    // 조회수
    private int likeCnt;                    // 좋아요 수
    private int dislikeCnt;                 // 싫어요 수

    private int likeStatus;                 // 1이면 좋아요, -1이면 싫어요, 0이면 아무 상태도 아님

    private LocalDateTime createdAt;        // 리뷰 작성 날짜
    private LocalDateTime modifiedAt;       // 리뷰 수정 날짜

    // 댓글 정보
    private int commentCnt;                                     // 댓글 개수
    private CommentListResponse commentListResponse;            // 댓글 리스트

    // 스크랩 정보
    private Long scrapId;
    private boolean scrapStatus;


    public static PostingDetailsResponse toDTO(Posting posting, CommentListResponse commentList) {
        return PostingDetailsResponse.builder()
                .postingId(posting.getPostingId())

                .contentsId(posting.getContents().getContentsId())
                .contentsTitle(posting.getContents().getTranslatedTitle())
                .contentsPosterPath(posting.getContents().getPosterPath())

                .userId(posting.getUser().getId())
                .userNickname(posting.getUser().getNickname())
                .userProfileImage(posting.getUser().getProfileImage())

                .title(posting.getTitle())
                .content(posting.getContent())
                .category(posting.getCategory())

                .isSpoiler(posting.isSpoiler())

                .viewCnt(posting.getViewCnt())
                .likeCnt(posting.getLikeCnt())
                .dislikeCnt(posting.getDislikeCnt())

                .createdAt(posting.getCreatedDate())
                .modifiedAt(posting.getModifiedDate())

                .commentListResponse(commentList)

                .build();
    }
}
```

### PostingIdResponse 
```java
package com.ncookie.imad.domain.posting.dto.response;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import lombok.Builder;
import lombok.Data;


@Data
@Builder
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class PostingIdResponse {
    Long postingId;
}
```

### PostingListResponse
```java
package com.ncookie.imad.domain.posting.dto.response;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import com.ncookie.imad.domain.common.dto.ListResponse;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.experimental.SuperBuilder;
import org.springframework.data.domain.Page;

import java.util.List;


@EqualsAndHashCode(callSuper = true)
@Data
@SuperBuilder
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class PostingListResponse extends ListResponse<PostingListElement> {
    private Integer searchType;                 // 검색 기준 (제목+내용, 제목, 내용, 글쓴이 등)

    public static PostingListResponse toDTO(Page<?> page, List<PostingListElement> postingList, Integer searchType) {
        SortVariable sortVariable = getSortVariable(page);
        return PostingListResponse.builder()
                .detailsList(postingList)

                .totalElements(page.getTotalElements())
                .totalPages(page.getTotalPages())

                .pageNumber(page.getNumber())
                .numberOfElements(page.getNumberOfElements())
                .sizeOfPage(page.getSize())

                .sortDirection(sortVariable.getSortDirection())
                .sortProperty(sortVariable.getSortProperty())

                .searchType(searchType)

                .build();
    }
}
```

### PostingListElement
```java
package com.ncookie.imad.domain.posting.dto.response;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import com.ncookie.imad.domain.posting.entity.Posting;
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
public class PostingListElement {
    private Long postingId;                 // 게시글 ID

    // 작품 정보
    private Long contentsId;                // 작품 ID
    private String contentsTitle;           // 작품 제목
    private String contentsPosterPath;      // 작품 포스터 이미지 경로

    // 유저 정보
    private Long userId;                    // 유저 id
    private String userNickname;            // 닉네임
    private int userProfileImage;           // 프로필 이미지

    // 게시글 정보
    private String title;                   // 제목
    private int category;                   // 카테고리

    private boolean isSpoiler;              // 스포일러 여부

    private int viewCnt;                    // 조회수
    private int commentCnt;                 // 댓글수
    
    private int likeCnt;                    // 좋아요 수
    private int dislikeCnt;                 // 싫어요 수

    private int likeStatus;                 // 1이면 좋아요, -1이면 싫어요, 0이면 아무 상태도 아님

    private LocalDateTime createdAt;        // 리뷰 작성 날짜
    private LocalDateTime modifiedAt;       // 리뷰 수정 날짜

    // 스크랩 정보
    private Long scrapId;
    private boolean scrapStatus;


    public static PostingListElement toDTO(Posting posting) {
        return PostingListElement.builder()
                .postingId(posting.getPostingId())

                .contentsId(posting.getContents().getContentsId())
                .contentsTitle(posting.getContents().getTranslatedTitle())
                .contentsPosterPath(posting.getContents().getPosterPath())

                .userId(posting.getUser().getId())
                .userNickname(posting.getUser().getNickname())
                .userProfileImage(posting.getUser().getProfileImage())

                .title(posting.getTitle())
                .category(posting.getCategory())

                .isSpoiler(posting.isSpoiler())

                .viewCnt(posting.getViewCnt())
                .likeCnt(posting.getLikeCnt())
                .dislikeCnt(posting.getDislikeCnt())

                .createdAt(posting.getCreatedDate())
                .modifiedAt(posting.getModifiedDate())

                .build();
    }
}
```

---
## 댓글

### AddCommentRequest
```java
package com.ncookie.imad.domain.posting.dto.request;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import lombok.Data;


@Data
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class AddCommentRequest {
    private Long postingId;         // 게시글 ID

    private Long parentId;          // 부모 댓글 ID. 답글이 아니라면 null 값이 들어감
    private String content;         // 댓글 내용
}
```

### ModifyCommentRequest 
```java
package com.ncookie.imad.domain.posting.dto.request;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import lombok.Data;


@Data
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class ModifyCommentRequest {
    String content;         // 댓글 내용
}
```

### CommentDetailsResponse 
```java
package com.ncookie.imad.domain.posting.dto.response;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import com.ncookie.imad.domain.posting.entity.Comment;
import com.ncookie.imad.domain.user.entity.UserAccount;
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
public class CommentDetailsResponse {
    private Long commentId;

    // 유저 정보
    private Long userId;                    // 유저 ID
    private String userNickname;            // 닉네임
    private int userProfileImage;           // 프로필 이미지

    // 댓글 정보
    private Long parentId;                  // 댓글 부모 ID. 이 댓글이 최상위라면 null 값이 들어감
    private int childCnt;                   // 답글 개수
    private String content;                 // 댓글 내용
    /**
     * 댓글 삭제 여부
     * 해당 필드가 true이면 이 댓글은 삭제된 데이터이므로 content는 null이고 클라이언트에서 삭제되었음이 표시되어야 함
     * Ex) "이 댓글은 삭제되었습니다."
     */
    private boolean isRemoved;

    private int likeStatus;                 // 1이면 좋아요, -1이면 싫어요, 0이면 아무 상태도 아님

    private int likeCnt;                    // 좋아요 수
    private int dislikeCnt;                 // 싫어요 수

    private LocalDateTime createdAt;        // 댓글 작성 날짜
    private LocalDateTime modifiedAt;       // 댓글 수정 날짜


    public static CommentDetailsResponse toDTO(Comment comment, int likeStatus, int childCnt) {
        UserAccount user = comment.getUserAccount();
        Long parentId = comment.getParent() != null ? comment.getParent().getCommentId() : null;

        return CommentDetailsResponse.builder()
                .commentId(comment.getCommentId())

                .userId(user.getId())
                .userNickname(user.getNickname())
                .userProfileImage(user.getProfileImage())

                .parentId(parentId)
                .childCnt(childCnt)

                .content(comment.getContent())
                .isRemoved(comment.isRemoved())

                .likeStatus(likeStatus)
                .likeCnt(comment.getLikeCnt())
                .dislikeCnt(comment.getDislikeCnt())

                .createdAt(comment.getCreatedDate())
                .modifiedAt(comment.getModifiedDate())

                .build();
    }
}
```

### CommentListResponse
```java
package com.ncookie.imad.domain.posting.dto.response;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import com.ncookie.imad.domain.common.dto.ListResponse;
import lombok.experimental.SuperBuilder;
import org.springframework.data.domain.Page;

import java.util.List;


@SuperBuilder
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class CommentListResponse extends ListResponse<CommentDetailsResponse> {
    public static CommentListResponse toDTO(Page<?> page, List<CommentDetailsResponse> commentList) {
        SortVariable sortVariable = getSortVariable(page);
        return CommentListResponse.builder()
                .detailsList(commentList)

                .totalElements(page.getTotalElements())
                .totalPages(page.getTotalPages())

                .pageNumber(page.getNumber())
                .numberOfElements(page.getNumberOfElements())
                .sizeOfPage(page.getSize())

                .sortDirection(sortVariable.getSortDirection())
                .sortProperty(sortVariable.getSortProperty())

                .build();
    }
}
```

### CommentIdResponse
```java
package com.ncookie.imad.domain.posting.dto.response;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import lombok.Builder;
import lombok.Data;

@Data
@Builder
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class CommentIdResponse {
    Long commentId;         // 댓글 ID
}
```

### CommentListResponse
```java
package com.ncookie.imad.domain.posting.dto.response;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import com.ncookie.imad.domain.common.dto.ListResponse;
import lombok.experimental.SuperBuilder;
import org.springframework.data.domain.Page;

import java.util.List;


@SuperBuilder
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class CommentListResponse extends ListResponse<CommentDetailsResponse> {
    public static CommentListResponse toDTO(Page<?> page, List<CommentDetailsResponse> commentList) {
        SortVariable sortVariable = getSortVariable(page);
        return CommentListResponse.builder()
                .detailsList(commentList)

                .totalElements(page.getTotalElements())
                .totalPages(page.getTotalPages())

                .pageNumber(page.getNumber())
                .numberOfElements(page.getNumberOfElements())
                .sizeOfPage(page.getSize())

                .sortDirection(sortVariable.getSortDirection())
                .sortProperty(sortVariable.getSortProperty())

                .build();
    }
}
```

---
## 좋아요 / 싫어요

### LikeStatusRequest
```java
package com.ncookie.imad.domain.like.dto;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import lombok.Data;

@Data
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class LikeStatusRequest {
    int likeStatus;
}
```

---
## 프로필

### BookmarksListResponse
```java
package com.ncookie.imad.domain.profile.dto.response;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import com.ncookie.imad.domain.common.dto.ListResponse;
import com.ncookie.imad.domain.profile.entity.ContentsBookmark;
import lombok.experimental.SuperBuilder;
import org.springframework.data.domain.Page;

import java.util.List;


@SuperBuilder
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class BookmarkListResponse extends ListResponse<BookmarkDetails> {
    public static BookmarkListResponse toDTO(Page<ContentsBookmark> page, List<BookmarkDetails> bookmarkDetailsList) {
        SortVariable sortVariable = getSortVariable(page);
        return BookmarkListResponse.builder()
                .detailsList(bookmarkDetailsList)

                .totalElements(page.getTotalElements())
                .totalPages(page.getTotalPages())

                .pageNumber(page.getNumber())
                .numberOfElements(page.getNumberOfElements())
                .sizeOfPage(page.getSize())

                .sortDirection(sortVariable.getSortDirection())
                .sortProperty(sortVariable.getSortProperty())

                .build();
    }
}
```

### BookmarkDetails
```java
package com.ncookie.imad.domain.profile.dto.response;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import com.ncookie.imad.domain.profile.entity.ContentsBookmark;
import lombok.Builder;
import lombok.Data;

import java.time.LocalDateTime;

@Data
@Builder
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class BookmarkDetails {
    private Long bookmarkId;

    private Long userId;

    private Long contentsId;
    private String contentsTitle;           // 작품 제목
    private String contentsPosterPath;      // 작품 포스터 이미지 경로

    private LocalDateTime createdDate;

    public static BookmarkDetails toDTO(ContentsBookmark bookmark) {
        return BookmarkDetails.builder()
                .bookmarkId(bookmark.getId())
                .userId(bookmark.getUserAccount().getId())

                .contentsId(bookmark.getContents().getContentsId())
                .contentsTitle(bookmark.getContents().getTranslatedTitle())
                .contentsPosterPath(bookmark.getContents().getPosterPath())

                .createdDate(bookmark.getCreatedDate())
                .build();
    }
}
```

### ScrapDetails
```java
package com.ncookie.imad.domain.profile.dto.response;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import com.ncookie.imad.domain.profile.entity.PostingScrap;
import lombok.Builder;
import lombok.Data;

import java.time.LocalDateTime;

@Data
@Builder
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class ScrapDetails {
    private Long scrapId;

    private Long userId;

    private Long postingId;                // 게시글 ID
    private String postingTitle;           // 게시글 제목

    private LocalDateTime createdDate;

    public static ScrapDetails toDTO(PostingScrap scrap) {
        return ScrapDetails.builder()
                .scrapId(scrap.getId())
                .userId(scrap.getUserAccount().getId())

                .postingId(scrap.getPosting().getPostingId())
                .postingTitle(scrap.getPosting().getTitle())

                .createdDate(scrap.getCreatedDate())
                .build();
    }
}
```

### ScrapListResponse
```java
package com.ncookie.imad.domain.profile.dto.response;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import com.ncookie.imad.domain.common.dto.ListResponse;
import com.ncookie.imad.domain.profile.entity.PostingScrap;
import lombok.experimental.SuperBuilder;
import org.springframework.data.domain.Page;


import java.util.List;

@SuperBuilder
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class ScrapListResponse extends ListResponse<ScrapDetails> {
    public static ScrapListResponse toDTO(Page<PostingScrap> page, List<ScrapDetails> scrapDetailsList) {
        ListResponse.SortVariable sortVariable = getSortVariable(page);
        return ScrapListResponse.builder()
                .detailsList(scrapDetailsList)

                .totalElements(page.getTotalElements())
                .totalPages(page.getTotalPages())

                .pageNumber(page.getNumber())
                .numberOfElements(page.getNumberOfElements())
                .sizeOfPage(page.getSize())

                .sortDirection(sortVariable.getSortDirection())
                .sortProperty(sortVariable.getSortProperty())

                .build();
    }
}
```

