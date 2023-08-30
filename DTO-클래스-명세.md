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

@Getter
public enum ContentsType {
    MOVIE("MOVIE"),
    TV("TV"),
    ANIMATION("ANIMATION");

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
    private AuthProvider authProvider;
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
public class UserInfoDuplicationRequest {
    private String info;
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
    private AuthProvider authProvider;
    private Gender gender;
    private int ageRange;
    private int profileImage;
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
    private boolean validation;
}
```

### SearchResponse

>/src/main/java/com/ncookie/imad/domain/contents/dto/SearchResponse.java
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
public class SearchResponse {
    private int page;
    private int totalPages;
    private int totalResults;

    @JsonProperty("results")
    private List<SearchResult> results;
}
```

### SearchResults

>/src/main/java/com/ncookie/imad/domain/contents/dto/SearchResult.java
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
public class SearchResult {
    private int id;

    // For Movie
    private String title;
    private String original_title;
    private LocalDate releaseDate;

    // For TV shows
    private String name;
    private String original_name;
    private LocalDate firstAirDate;

    private List<String> origin_country;
    private String original_language;

    private boolean adult;
    private String backdrop_path;
    private String overview;
    private String poster_path;
    private String media_type;
    private List<Integer> genreIds;
    private boolean video;
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
public class TmdbDetails {
    private long contentsId;
    private long tmdbId;

    private String overview;
    private String tagline;
    private String posterPath;
    private String originalLanguage;
    private String certification;

    private String status;

    private Set<Integer> genres;
    private Set<String> productionCountries;


    // IMAD Data
    private ContentsType contentsType;


    // Movie Data
    private String title;
    private String originalTitle;

    private String releaseDate;
    private int runtime;


    // TV Data
    private String name;
    private String originalName;

    private String firstAirDate;
    private String lastAirDate;

    private int numberOfEpisodes;
    private int numberOfSeasons;

    private List<DetailsSeason> seasons;
    private List<DetailsNetworks> networks;


    // Credits
    @JsonProperty("credits")
    private DetailsCredits credits;


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

