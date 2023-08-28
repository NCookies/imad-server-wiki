> 블로그 링크 : https://velog.io/@ncookie/IMDB-TMDB-API-%EC%82%AC%EC%9A%A9%EB%B2%95-%EC%A0%95%EB%A6%AC

# TMDB API란

```
Welcome to version 3 of The Movie Database (TMDB) API. This is where you will find the definitive list of currently available methods for our movie, tv, actor and image API.
```

The Movie Database (TMDB) API v3는 영화, TV 프로그램, 배우, 그리고 이미지 API 등에 대한 메소드들을 제공하고 있다. 사이트를 조금 살펴봤는데, 영화, 드라마, 다큐, 애니메이션 등 특정 장르에 국한되지 않고 대부분의 영상물 정보를 찾아볼 수 있는 것으로 보인다. 그리고 해외 서비스인 것 치고 한글화(로컬라이징) 부분에서 적극적이어서 이 API를 선택하게 되었다.

[Getting Started](https://developer.themoviedb.org/docs)

# API 키 발급받기

API 키를 등록하기 위해서는 TMDB에 회원가입 후 계정 설정 페이지에서 API 키를 발급받자. API를 적용할 어플리케이션의 정보와 주소, 연락처 등을 써야하지만 따로 검수 없이 바로 발급되니, 간단하게 적어두어도 괜찮을 것 같다. 다만 추후 API를 영리 목적으로 사용할 예정이라면 TMDB 측에 검수를 받아야하므로 그 때 가서 자세하게 작성해야 하지 않나 싶다.

기본적으로 오픈 API이지만,  상업적으로 사용하게 될 경우 사이트 측과 상의하여 비용을 지불해야 한다. [API 이용약관](https://www.themoviedb.org/settings/api/new?type=developer)에서 살펴볼 수 있듯이, 광고를 포함하여 상업용 목적의 서비스 개발은 별도로 TMDB 사에 문의하여 API 이용에 대해 문의해야 한다. 

**`Your site is a "destination" site that uses TMDB content to drive traffic and generate revenue.`**  

해당 API를 사용하여 사이트에 트래픽을 “유도”한다는 점에서 서비스에 광고를 붙여서 수익을 얻는 것도 상업적 목적으로 분류되는 것 같다.

```
A. RULES AND RESTRICTIONS
If the primary purpose of your application is to derive revenue, it is considered a commercial application. TMDB reserves the right to make these evaluations at the time that you apply for the license. TMDB may also monitor your site or application over time to ensure continued compliance with the appropriate type of API key.

If you're in doubt about whether your application is commercial, here are a few common examples of commercial use that may provide you some guidance:

Users are charged a fee for your product or a 3rd party's product or service or a 3rd party's service that includes some sort of integration using the TMDB APIs.
You sell services using TMDb's APIs to bring users' TMDB content into your service.
Your site is a "destination" site that uses TMDB content to drive traffic and generate revenue.
Your site generates revenue by charging users for access to content related to TMDB content such as movies, television shows and music.
```

# API 속도 제한

과거에는 10초 당 요청 수 40으로 제한하는 등의 조건이 있었지만, 비활성화 되었다가 최근에는 초당 50개 근처에서 제한을 두고 있는 것 같다. 다만 이는 사이트 측의 사정에 따라 언제든지 변경될 수 있다. 만약 응답 코드로 429를 받았다면 허용 제한 넘은 것이므로, API 요청 수를 줄이는 방법을 고려하거나 사이트 측에 문의하여 유료로 이용하는 방법도 있다.

# API 사용법

## Append To Response

`append to response`는 최상위 네임스페이스에 추가 요청을 추가하는 쉽고 효율적인 방법이다. 영화, TV 쇼, TV 시즌, TV 에피소드 및 인물 상세 메소드 모두 `append_to_response`라는 쿼리 메소드 파라미터를 지원한다.

예를 들어, 어떤 영화의 상세 정보와 영상을 원한다고 해보자. 보통 아래와 같이 두 개의 요청을 날릴 것이다.

```html
https://api.themoviedb.org/3/movie/157336?api_key=88365cf6bdc6c46015bf85c731dfab8f
https://api.themoviedb.org/3/movie/157336/videos?api_key=88365cf6bdc6c46015bf85c731dfab8f
```

그러나 `append_to_response`를 사용하면 단일 요청으로 처리할 수 있다.

```html
https://api.themoviedb.org/3/movie/157336?api_key=88365cf6bdc6c46015bf85c731dfab8f&append_to_response=videos,images
```

여러 개의 요청의 값들을 콤마로 구분하여 사용할 수도 있다.

```html
https://api.themoviedb.org/3/movie/157336?api_key=88365cf6bdc6c46015bf85c731dfab8f&append_to_response=videos,images
```

## Finding Data

TMDB에서 영화, 티비쇼, 그리고 인물들에 대해 검색하기 위해서는 3가지 방법이 있다.

### /search

텍스트 기반의 검색으로, 가장 일반적인 방법이다. 요청 시 query string와 함께 보내면 TMDB 측에서 가장 근접한 검색 결과를 제공해준다. 텍스트 검색은 원본, 번역, 대체 이름과 제목 모두 가능하다. 

### /discover

등급, 인증 또는 출시 날짜와 같은 정의 가능한 값이나 필터를 기반으로 영화 및 TV 프로그램을 검색할 때 사용한다. 

### /find

TMDB 내부에 저장되어 있는 작품 또는 인물 등의 ID 값을 알고 있을 때 사용한다. 

## Languages

TMDB는 가능한 한 현지화(로컬라이징)를 하려고 노력하지만, 배우와 배역(캐릭터) 이름은 여기에서 제외된다. 추후 지원 예정이라고는 하지만 당장은 기대하기 어렵기 때문에 애플리케이션에서 별도의 조치를 취해야 할 것으로 보인다. 이를 위해 DB에 is_translated 칼럼을 추가할 예정이다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3cda5212-a6d0-4198-a95f-e198c70f0847/Untitled.png)

## Images

작품과 인물 관련 이미지의 URL을 만들기 위해서는 `base_url`, `file_size`, `file_path` 이렇게 3가지의 데이터가 필요하다. base_url과 file_size는 /configuration AIP를 통해서 정보를 받아올 수 있고, file_path는 API에 request를 날렸을 때 응답 데이터에 담겨 있는 정보를 사용하면 된다.

위의 링크에서 받아올 수 있는 데이터는 다음과 같다. 여기서 우리가 쓸 것은 iamges에 있는 size 데이터들이다. 이렇게 3가지에 데이터를 적절히 조합해서 사용하면 우리가 원하는 이미지 파일을 불러올 수 있다.

### 예시

```swift
http://image.tmdb.org/t/p/original/noelOhwX1oaNSvU9NLKhPrHTFI3.jpg
```

## Configuration

[Configuration](https://api.themoviedb.org/3/configuration)

```json
{
  "images": {
    "base_url": "http://image.tmdb.org/t/p/",
    "secure_base_url": "https://image.tmdb.org/t/p/",
    "backdrop_sizes": [
      "w300",
      "w780",
      "w1280",
      "original"
    ],
    "logo_sizes": [
      "w45",
      "w92",
      "w154",
      "w185",
      "w300",
      "w500",
      "original"
    ],
    "poster_sizes": [
      "w92",
      "w154",
      "w185",
      "w342",
      "w500",
      "w780",
      "original"
    ],
    "profile_sizes": [
      "w45",
      "w185",
      "h632",
      "original"
    ],
    "still_sizes": [
      "w92",
      "w185",
      "w300",
      "original"
    ]
  },
  "change_keys": [
    "adult",
    "air_date",
    "also_known_as",
    "alternative_titles",
    "biography",
    "birthday",
    "budget",
    "cast",
    "certifications",
    "character_names",
    "created_by",
    "crew",
    "deathday",
    "episode",
    "episode_number",
    "episode_run_time",
    "freebase_id",
    "freebase_mid",
    "general",
    "genres",
    "guest_stars",
    "homepage",
    "images",
    "imdb_id",
    "languages",
    "name",
    "network",
    "origin_country",
    "original_name",
    "original_title",
    "overview",
    "parts",
    "place_of_birth",
    "plot_keywords",
    "production_code",
    "production_companies",
    "production_countries",
    "releases",
    "revenue",
    "runtime",
    "season",
    "season_number",
    "season_regular",
    "spoken_languages",
    "status",
    "tagline",
    "title",
    "translations",
    "tvdb_id",
    "tvrage_id",
    "type",
    "video",
    "videos"
  ]
}
```

## Genre

- 장르는 TV와 Movie 두 분류에 따라 다른 장르리스트를 보유

### swift 사용예시

```swift
import Foundation

let headers = [
  "accept": "application/json",
  "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxZWE4ZGQzY2FlYTU3MDFjNjBlYTIxYWY5N2U4YzUyZiIsInN1YiI6IjY0Nzg2OWZiMDc2Y2U4MDBhODIyMGUzMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.9IrLgOQhOGZx-Nrru5X_8aKkvEP3V3JV8a3Yz3rYyGg"
]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.themoviedb.org/3/genre/movie/list?language=ko")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

### movie

```json
{
  "genres": [
    {
      "id": 28,
      "name": "액션"
    },
    {
      "id": 12,
      "name": "모험"
    },
    {
      "id": 16,
      "name": "애니메이션"
    },
    {
      "id": 35,
      "name": "코미디"
    },
    {
      "id": 80,
      "name": "범죄"
    },
    {
      "id": 99,
      "name": "다큐멘터리"
    },
    {
      "id": 18,
      "name": "드라마"
    },
    {
      "id": 10751,
      "name": "가족"
    },
    {
      "id": 14,
      "name": "판타지"
    },
    {
      "id": 36,
      "name": "역사"
    },
    {
      "id": 27,
      "name": "공포"
    },
    {
      "id": 10402,
      "name": "음악"
    },
    {
      "id": 9648,
      "name": "미스터리"
    },
    {
      "id": 10749,
      "name": "로맨스"
    },
    {
      "id": 878,
      "name": "SF"
    },
    {
      "id": 10770,
      "name": "TV 영화"
    },
    {
      "id": 53,
      "name": "스릴러"
    },
    {
      "id": 10752,
      "name": "전쟁"
    },
    {
      "id": 37,
      "name": "서부"
    }
  ]
}
```

### tv

```json
{
  "genres": [
    {
      "id": 10759,
      "name": "Action & Adventure"
    },
    {
      "id": 16,
      "name": "애니메이션"
    },
    {
      "id": 35,
      "name": "코미디"
    },
    {
      "id": 80,
      "name": "범죄"
    },
    {
      "id": 99,
      "name": "다큐멘터리"
    },
    {
      "id": 18,
      "name": "드라마"
    },
    {
      "id": 10751,
      "name": "가족"
    },
    {
      "id": 10762,
      "name": "Kids"
    },
    {
      "id": 9648,
      "name": "미스터리"
    },
    {
      "id": 10763,
      "name": "News"
    },
    {
      "id": 10764,
      "name": "Reality"
    },
    {
      "id": 10765,
      "name": "Sci-Fi & Fantasy"
    },
    {
      "id": 10766,
      "name": "Soap"
    },
    {
      "id": 10767,
      "name": "Talk"
    },
    {
      "id": 10768,
      "name": "War & Politics"
    },
    {
      "id": 37,
      "name": "서부"
    }
  ]
}
```

## Countries

[Countries](https://developer.themoviedb.org/reference/configuration-countries)

TMDB에서 사용하는 국가명 약어와 한글이름 데이터

### 데이터
    
```json
[
    {
    "iso_3166_1": "AD",
    "english_name": "Andorra",
    "native_name": "안도라"
    },
    {
    "iso_3166_1": "AE",
    "english_name": "United Arab Emirates",
    "native_name": "아랍에미리트 연합"
    },
    {
    "iso_3166_1": "AF",
    "english_name": "Afghanistan",
    "native_name": "아프가니스탄"
    },
    {
    "iso_3166_1": "AG",
    "english_name": "Antigua and Barbuda",
    "native_name": "앤티가 바부다"
    },
    {
    "iso_3166_1": "AI",
    "english_name": "Anguilla",
    "native_name": "안길라"
    },
    {
    "iso_3166_1": "AL",
    "english_name": "Albania",
    "native_name": "알바니아"
    },
    {
    "iso_3166_1": "AM",
    "english_name": "Armenia",
    "native_name": "아르메니아"
    },
    {
    "iso_3166_1": "AN",
    "english_name": "Netherlands Antilles",
    "native_name": "네덜란드령 안틸레스"
    },
    {
    "iso_3166_1": "AO",
    "english_name": "Angola",
    "native_name": "앙골라"
    },
    {
    "iso_3166_1": "AQ",
    "english_name": "Antarctica",
    "native_name": "남극 대륙"
    },
    {
    "iso_3166_1": "AR",
    "english_name": "Argentina",
    "native_name": "아르헨티나"
    },
    {
    "iso_3166_1": "AS",
    "english_name": "American Samoa",
    "native_name": "아메리칸 사모아"
    },
    {
    "iso_3166_1": "AT",
    "english_name": "Austria",
    "native_name": "오스트리아"
    },
    {
    "iso_3166_1": "AU",
    "english_name": "Australia",
    "native_name": "호주"
    },
    {
    "iso_3166_1": "AW",
    "english_name": "Aruba",
    "native_name": "아루바"
    },
    {
    "iso_3166_1": "AZ",
    "english_name": "Azerbaijan",
    "native_name": "아제르바이잔"
    },
    {
    "iso_3166_1": "BA",
    "english_name": "Bosnia and Herzegovina",
    "native_name": "보스니아 헤르체고비나"
    },
    {
    "iso_3166_1": "BB",
    "english_name": "Barbados",
    "native_name": "바베이도스"
    },
    {
    "iso_3166_1": "BD",
    "english_name": "Bangladesh",
    "native_name": "방글라데시"
    },
    {
    "iso_3166_1": "BE",
    "english_name": "Belgium",
    "native_name": "벨기에"
    },
    {
    "iso_3166_1": "BF",
    "english_name": "Burkina Faso",
    "native_name": "부르키나파소"
    },
    {
    "iso_3166_1": "BG",
    "english_name": "Bulgaria",
    "native_name": "불가리아"
    },
    {
    "iso_3166_1": "BH",
    "english_name": "Bahrain",
    "native_name": "바레인"
    },
    {
    "iso_3166_1": "BI",
    "english_name": "Burundi",
    "native_name": "부룬디"
    },
    {
    "iso_3166_1": "BJ",
    "english_name": "Benin",
    "native_name": "베냉"
    },
    {
    "iso_3166_1": "BM",
    "english_name": "Bermuda",
    "native_name": "버뮤다"
    },
    {
    "iso_3166_1": "BN",
    "english_name": "Brunei Darussalam",
    "native_name": "브루나이"
    },
    {
    "iso_3166_1": "BO",
    "english_name": "Bolivia",
    "native_name": "볼리비아"
    },
    {
    "iso_3166_1": "BR",
    "english_name": "Brazil",
    "native_name": "브라질"
    },
    {
    "iso_3166_1": "BS",
    "english_name": "Bahamas",
    "native_name": "바하마"
    },
    {
    "iso_3166_1": "BT",
    "english_name": "Bhutan",
    "native_name": "부탄"
    },
    {
    "iso_3166_1": "BU",
    "english_name": "Burma",
    "native_name": "Burma"
    },
    {
    "iso_3166_1": "BV",
    "english_name": "Bouvet Island",
    "native_name": "부베"
    },
    {
    "iso_3166_1": "BW",
    "english_name": "Botswana",
    "native_name": "보츠와나"
    },
    {
    "iso_3166_1": "BY",
    "english_name": "Belarus",
    "native_name": "벨라루스"
    },
    {
    "iso_3166_1": "BZ",
    "english_name": "Belize",
    "native_name": "벨리즈"
    },
    {
    "iso_3166_1": "CA",
    "english_name": "Canada",
    "native_name": "캐나다"
    },
    {
    "iso_3166_1": "CC",
    "english_name": "Cocos  Islands",
    "native_name": "코코스제도"
    },
    {
    "iso_3166_1": "CD",
    "english_name": "Congo",
    "native_name": "콩고-킨샤사"
    },
    {
    "iso_3166_1": "CF",
    "english_name": "Central African Republic",
    "native_name": "중앙 아프리카 공화국"
    },
    {
    "iso_3166_1": "CG",
    "english_name": "Congo",
    "native_name": "콩고"
    },
    {
    "iso_3166_1": "CH",
    "english_name": "Switzerland",
    "native_name": "스위스"
    },
    {
    "iso_3166_1": "CI",
    "english_name": "Cote D'Ivoire",
    "native_name": "코트디부아르"
    },
    {
    "iso_3166_1": "CK",
    "english_name": "Cook Islands",
    "native_name": "쿡제도"
    },
    {
    "iso_3166_1": "CL",
    "english_name": "Chile",
    "native_name": "칠레"
    },
    {
    "iso_3166_1": "CM",
    "english_name": "Cameroon",
    "native_name": "카메룬"
    },
    {
    "iso_3166_1": "CN",
    "english_name": "China",
    "native_name": "중국"
    },
    {
    "iso_3166_1": "CO",
    "english_name": "Colombia",
    "native_name": "콜롬비아"
    },
    {
    "iso_3166_1": "CR",
    "english_name": "Costa Rica",
    "native_name": "코스타리카"
    },
    {
    "iso_3166_1": "CS",
    "english_name": "Serbia and Montenegro",
    "native_name": "Serbia and Montenegro"
    },
    {
    "iso_3166_1": "CU",
    "english_name": "Cuba",
    "native_name": "쿠바"
    },
    {
    "iso_3166_1": "CV",
    "english_name": "Cape Verde",
    "native_name": "까뽀베르데"
    },
    {
    "iso_3166_1": "CX",
    "english_name": "Christmas Island",
    "native_name": "크리스마스섬"
    },
    {
    "iso_3166_1": "CY",
    "english_name": "Cyprus",
    "native_name": "사이프러스"
    },
    {
    "iso_3166_1": "CZ",
    "english_name": "Czech Republic",
    "native_name": "체코"
    },
    {
    "iso_3166_1": "DE",
    "english_name": "Germany",
    "native_name": "독일"
    },
    {
    "iso_3166_1": "DJ",
    "english_name": "Djibouti",
    "native_name": "지부티"
    },
    {
    "iso_3166_1": "DK",
    "english_name": "Denmark",
    "native_name": "덴마크"
    },
    {
    "iso_3166_1": "DM",
    "english_name": "Dominica",
    "native_name": "도미니카"
    },
    {
    "iso_3166_1": "DO",
    "english_name": "Dominican Republic",
    "native_name": "도미니카 공화국"
    },
    {
    "iso_3166_1": "DZ",
    "english_name": "Algeria",
    "native_name": "알제리"
    },
    {
    "iso_3166_1": "EC",
    "english_name": "Ecuador",
    "native_name": "에콰도르"
    },
    {
    "iso_3166_1": "EE",
    "english_name": "Estonia",
    "native_name": "에스토니아"
    },
    {
    "iso_3166_1": "EG",
    "english_name": "Egypt",
    "native_name": "이집트"
    },
    {
    "iso_3166_1": "EH",
    "english_name": "Western Sahara",
    "native_name": "서사하라"
    },
    {
    "iso_3166_1": "ER",
    "english_name": "Eritrea",
    "native_name": "에리트리아"
    },
    {
    "iso_3166_1": "ES",
    "english_name": "Spain",
    "native_name": "스페인"
    },
    {
    "iso_3166_1": "ET",
    "english_name": "Ethiopia",
    "native_name": "이디오피아"
    },
    {
    "iso_3166_1": "FI",
    "english_name": "Finland",
    "native_name": "핀란드"
    },
    {
    "iso_3166_1": "FJ",
    "english_name": "Fiji",
    "native_name": "피지"
    },
    {
    "iso_3166_1": "FK",
    "english_name": "Falkland Islands",
    "native_name": "포클랜드 제도"
    },
    {
    "iso_3166_1": "FM",
    "english_name": "Micronesia",
    "native_name": "미크로네시아"
    },
    {
    "iso_3166_1": "FO",
    "english_name": "Faeroe Islands",
    "native_name": "페로제도"
    },
    {
    "iso_3166_1": "FR",
    "english_name": "France",
    "native_name": "프랑스"
    },
    {
    "iso_3166_1": "GA",
    "english_name": "Gabon",
    "native_name": "가봉"
    },
    {
    "iso_3166_1": "GB",
    "english_name": "United Kingdom",
    "native_name": "영국"
    },
    {
    "iso_3166_1": "GD",
    "english_name": "Grenada",
    "native_name": "그레나다"
    },
    {
    "iso_3166_1": "GE",
    "english_name": "Georgia",
    "native_name": "조지아"
    },
    {
    "iso_3166_1": "GF",
    "english_name": "French Guiana",
    "native_name": "프랑스령 기아나"
    },
    {
    "iso_3166_1": "GH",
    "english_name": "Ghana",
    "native_name": "가나"
    },
    {
    "iso_3166_1": "GI",
    "english_name": "Gibraltar",
    "native_name": "지브롤터"
    },
    {
    "iso_3166_1": "GL",
    "english_name": "Greenland",
    "native_name": "그린란드"
    },
    {
    "iso_3166_1": "GM",
    "english_name": "Gambia",
    "native_name": "감비아"
    },
    {
    "iso_3166_1": "GN",
    "english_name": "Guinea",
    "native_name": "기니"
    },
    {
    "iso_3166_1": "GP",
    "english_name": "Guadaloupe",
    "native_name": "과들루프"
    },
    {
    "iso_3166_1": "GQ",
    "english_name": "Equatorial Guinea",
    "native_name": "적도 기니"
    },
    {
    "iso_3166_1": "GR",
    "english_name": "Greece",
    "native_name": "그리스"
    },
    {
    "iso_3166_1": "GS",
    "english_name": "South Georgia and the South Sandwich Islands",
    "native_name": "사우스조지아 사우스샌드위치 제도"
    },
    {
    "iso_3166_1": "GT",
    "english_name": "Guatemala",
    "native_name": "과테말라"
    },
    {
    "iso_3166_1": "GU",
    "english_name": "Guam",
    "native_name": "괌"
    },
    {
    "iso_3166_1": "GW",
    "english_name": "Guinea-Bissau",
    "native_name": "기네비쏘"
    },
    {
    "iso_3166_1": "GY",
    "english_name": "Guyana",
    "native_name": "가이아나"
    },
    {
    "iso_3166_1": "HK",
    "english_name": "Hong Kong",
    "native_name": "홍콩, 중국 특별행정구"
    },
    {
    "iso_3166_1": "HM",
    "english_name": "Heard and McDonald Islands",
    "native_name": "허드섬-맥도널드제도"
    },
    {
    "iso_3166_1": "HN",
    "english_name": "Honduras",
    "native_name": "온두라스"
    },
    {
    "iso_3166_1": "HR",
    "english_name": "Croatia",
    "native_name": "크로아티아"
    },
    {
    "iso_3166_1": "HT",
    "english_name": "Haiti",
    "native_name": "아이티"
    },
    {
    "iso_3166_1": "HU",
    "english_name": "Hungary",
    "native_name": "헝가리"
    },
    {
    "iso_3166_1": "ID",
    "english_name": "Indonesia",
    "native_name": "인도네시아"
    },
    {
    "iso_3166_1": "IE",
    "english_name": "Ireland",
    "native_name": "아일랜드"
    },
    {
    "iso_3166_1": "IL",
    "english_name": "Israel",
    "native_name": "이스라엘"
    },
    {
    "iso_3166_1": "IN",
    "english_name": "India",
    "native_name": "인도"
    },
    {
    "iso_3166_1": "IO",
    "english_name": "British Indian Ocean Territory",
    "native_name": "영국령인도양식민지"
    },
    {
    "iso_3166_1": "IQ",
    "english_name": "Iraq",
    "native_name": "이라크"
    },
    {
    "iso_3166_1": "IR",
    "english_name": "Iran",
    "native_name": "이란"
    },
    {
    "iso_3166_1": "IS",
    "english_name": "Iceland",
    "native_name": "아이슬란드"
    },
    {
    "iso_3166_1": "IT",
    "english_name": "Italy",
    "native_name": "이탈리아"
    },
    {
    "iso_3166_1": "JM",
    "english_name": "Jamaica",
    "native_name": "자메이카"
    },
    {
    "iso_3166_1": "JO",
    "english_name": "Jordan",
    "native_name": "요르단"
    },
    {
    "iso_3166_1": "JP",
    "english_name": "Japan",
    "native_name": "일본"
    },
    {
    "iso_3166_1": "KE",
    "english_name": "Kenya",
    "native_name": "케냐"
    },
    {
    "iso_3166_1": "KG",
    "english_name": "Kyrgyz Republic",
    "native_name": "키르기스스탄"
    },
    {
    "iso_3166_1": "KH",
    "english_name": "Cambodia",
    "native_name": "캄보디아"
    },
    {
    "iso_3166_1": "KI",
    "english_name": "Kiribati",
    "native_name": "키리바시"
    },
    {
    "iso_3166_1": "KM",
    "english_name": "Comoros",
    "native_name": "코모로스"
    },
    {
    "iso_3166_1": "KN",
    "english_name": "St. Kitts and Nevis",
    "native_name": "세인트 키츠 네비스"
    },
    {
    "iso_3166_1": "KP",
    "english_name": "North Korea",
    "native_name": "조선 민주주의 인민 공화국"
    },
    {
    "iso_3166_1": "KR",
    "english_name": "South Korea",
    "native_name": "대한민국"
    },
    {
    "iso_3166_1": "KW",
    "english_name": "Kuwait",
    "native_name": "쿠웨이트"
    },
    {
    "iso_3166_1": "KY",
    "english_name": "Cayman Islands",
    "native_name": "케이맨제도"
    },
    {
    "iso_3166_1": "KZ",
    "english_name": "Kazakhstan",
    "native_name": "카자흐스탄"
    },
    {
    "iso_3166_1": "LA",
    "english_name": "Lao People's Democratic Republic",
    "native_name": "라오스"
    },
    {
    "iso_3166_1": "LB",
    "english_name": "Lebanon",
    "native_name": "레바논"
    },
    {
    "iso_3166_1": "LC",
    "english_name": "St. Lucia",
    "native_name": "세인트루시아"
    },
    {
    "iso_3166_1": "LI",
    "english_name": "Liechtenstein",
    "native_name": "리히텐슈타인"
    },
    {
    "iso_3166_1": "LK",
    "english_name": "Sri Lanka",
    "native_name": "스리랑카"
    },
    {
    "iso_3166_1": "LR",
    "english_name": "Liberia",
    "native_name": "라이베리아"
    },
    {
    "iso_3166_1": "LS",
    "english_name": "Lesotho",
    "native_name": "레소토"
    },
    {
    "iso_3166_1": "LT",
    "english_name": "Lithuania",
    "native_name": "리투아니아"
    },
    {
    "iso_3166_1": "LU",
    "english_name": "Luxembourg",
    "native_name": "룩셈부르크"
    },
    {
    "iso_3166_1": "LV",
    "english_name": "Latvia",
    "native_name": "라트비아"
    },
    {
    "iso_3166_1": "LY",
    "english_name": "Libyan Arab Jamahiriya",
    "native_name": "리비아"
    },
    {
    "iso_3166_1": "MA",
    "english_name": "Morocco",
    "native_name": "모로코"
    },
    {
    "iso_3166_1": "MC",
    "english_name": "Monaco",
    "native_name": "모나코"
    },
    {
    "iso_3166_1": "MD",
    "english_name": "Moldova",
    "native_name": "몰도바"
    },
    {
    "iso_3166_1": "ME",
    "english_name": "Montenegro",
    "native_name": "몬테네그로"
    },
    {
    "iso_3166_1": "MG",
    "english_name": "Madagascar",
    "native_name": "마다가스카르"
    },
    {
    "iso_3166_1": "MH",
    "english_name": "Marshall Islands",
    "native_name": "마샬 군도"
    },
    {
    "iso_3166_1": "MK",
    "english_name": "Macedonia",
    "native_name": "마케도니아"
    },
    {
    "iso_3166_1": "ML",
    "english_name": "Mali",
    "native_name": "말리"
    },
    {
    "iso_3166_1": "MM",
    "english_name": "Myanmar",
    "native_name": "미얀마"
    },
    {
    "iso_3166_1": "MN",
    "english_name": "Mongolia",
    "native_name": "몽골"
    },
    {
    "iso_3166_1": "MO",
    "english_name": "Macao",
    "native_name": "마카오, 중국 특별행정구"
    },
    {
    "iso_3166_1": "MP",
    "english_name": "Northern Mariana Islands",
    "native_name": "북마리아나제도"
    },
    {
    "iso_3166_1": "MQ",
    "english_name": "Martinique",
    "native_name": "말티니크"
    },
    {
    "iso_3166_1": "MR",
    "english_name": "Mauritania",
    "native_name": "모리타니"
    },
    {
    "iso_3166_1": "MS",
    "english_name": "Montserrat",
    "native_name": "몬트세라트"
    },
    {
    "iso_3166_1": "MT",
    "english_name": "Malta",
    "native_name": "몰타"
    },
    {
    "iso_3166_1": "MU",
    "english_name": "Mauritius",
    "native_name": "모리셔스"
    },
    {
    "iso_3166_1": "MV",
    "english_name": "Maldives",
    "native_name": "몰디브"
    },
    {
    "iso_3166_1": "MW",
    "english_name": "Malawi",
    "native_name": "말라위"
    },
    {
    "iso_3166_1": "MX",
    "english_name": "Mexico",
    "native_name": "멕시코"
    },
    {
    "iso_3166_1": "MY",
    "english_name": "Malaysia",
    "native_name": "말레이시아"
    },
    {
    "iso_3166_1": "MZ",
    "english_name": "Mozambique",
    "native_name": "모잠비크"
    },
    {
    "iso_3166_1": "NA",
    "english_name": "Namibia",
    "native_name": "나미비아"
    },
    {
    "iso_3166_1": "NC",
    "english_name": "New Caledonia",
    "native_name": "뉴 칼레도니아"
    },
    {
    "iso_3166_1": "NE",
    "english_name": "Niger",
    "native_name": "니제르"
    },
    {
    "iso_3166_1": "NF",
    "english_name": "Norfolk Island",
    "native_name": "노퍽섬"
    },
    {
    "iso_3166_1": "NG",
    "english_name": "Nigeria",
    "native_name": "나이지리아"
    },
    {
    "iso_3166_1": "NI",
    "english_name": "Nicaragua",
    "native_name": "니카라과"
    },
    {
    "iso_3166_1": "NL",
    "english_name": "Netherlands",
    "native_name": "네덜란드"
    },
    {
    "iso_3166_1": "NO",
    "english_name": "Norway",
    "native_name": "노르웨이"
    },
    {
    "iso_3166_1": "NP",
    "english_name": "Nepal",
    "native_name": "네팔"
    },
    {
    "iso_3166_1": "NR",
    "english_name": "Nauru",
    "native_name": "나우루"
    },
    {
    "iso_3166_1": "NU",
    "english_name": "Niue",
    "native_name": "니우에"
    },
    {
    "iso_3166_1": "NZ",
    "english_name": "New Zealand",
    "native_name": "뉴질랜드"
    },
    {
    "iso_3166_1": "OM",
    "english_name": "Oman",
    "native_name": "오만"
    },
    {
    "iso_3166_1": "PA",
    "english_name": "Panama",
    "native_name": "파나마"
    },
    {
    "iso_3166_1": "PE",
    "english_name": "Peru",
    "native_name": "페루"
    },
    {
    "iso_3166_1": "PF",
    "english_name": "French Polynesia",
    "native_name": "프랑스령 폴리네시아"
    },
    {
    "iso_3166_1": "PG",
    "english_name": "Papua New Guinea",
    "native_name": "파푸아뉴기니"
    },
    {
    "iso_3166_1": "PH",
    "english_name": "Philippines",
    "native_name": "필리핀"
    },
    {
    "iso_3166_1": "PK",
    "english_name": "Pakistan",
    "native_name": "파키스탄"
    },
    {
    "iso_3166_1": "PL",
    "english_name": "Poland",
    "native_name": "폴란드"
    },
    {
    "iso_3166_1": "PM",
    "english_name": "St. Pierre and Miquelon",
    "native_name": "생피에르 미클롱"
    },
    {
    "iso_3166_1": "PN",
    "english_name": "Pitcairn Island",
    "native_name": "핏케언 섬"
    },
    {
    "iso_3166_1": "PR",
    "english_name": "Puerto Rico",
    "native_name": "푸에르토리코"
    },
    {
    "iso_3166_1": "PS",
    "english_name": "Palestinian Territory",
    "native_name": "팔레스타인 지구"
    },
    {
    "iso_3166_1": "PT",
    "english_name": "Portugal",
    "native_name": "포르투갈"
    },
    {
    "iso_3166_1": "PW",
    "english_name": "Palau",
    "native_name": "팔라우"
    },
    {
    "iso_3166_1": "PY",
    "english_name": "Paraguay",
    "native_name": "파라과이"
    },
    {
    "iso_3166_1": "QA",
    "english_name": "Qatar",
    "native_name": "카타르"
    },
    {
    "iso_3166_1": "RE",
    "english_name": "Reunion",
    "native_name": "리유니온"
    },
    {
    "iso_3166_1": "RO",
    "english_name": "Romania",
    "native_name": "루마니아"
    },
    {
    "iso_3166_1": "RS",
    "english_name": "Serbia",
    "native_name": "세르비아"
    },
    {
    "iso_3166_1": "RU",
    "english_name": "Russia",
    "native_name": "러시아"
    },
    {
    "iso_3166_1": "RW",
    "english_name": "Rwanda",
    "native_name": "르완다"
    },
    {
    "iso_3166_1": "SA",
    "english_name": "Saudi Arabia",
    "native_name": "사우디아라비아"
    },
    {
    "iso_3166_1": "SB",
    "english_name": "Solomon Islands",
    "native_name": "솔로몬 제도"
    },
    {
    "iso_3166_1": "SC",
    "english_name": "Seychelles",
    "native_name": "쉐이쉘"
    },
    {
    "iso_3166_1": "SD",
    "english_name": "Sudan",
    "native_name": "수단"
    },
    {
    "iso_3166_1": "SE",
    "english_name": "Sweden",
    "native_name": "스웨덴"
    },
    {
    "iso_3166_1": "SG",
    "english_name": "Singapore",
    "native_name": "싱가포르"
    },
    {
    "iso_3166_1": "SH",
    "english_name": "St. Helena",
    "native_name": "세인트헬레나"
    },
    {
    "iso_3166_1": "SI",
    "english_name": "Slovenia",
    "native_name": "슬로베니아"
    },
    {
    "iso_3166_1": "SJ",
    "english_name": "Svalbard & Jan Mayen Islands",
    "native_name": "스발바르제도-얀마웬섬"
    },
    {
    "iso_3166_1": "SK",
    "english_name": "Slovakia",
    "native_name": "슬로바키아"
    },
    {
    "iso_3166_1": "SL",
    "english_name": "Sierra Leone",
    "native_name": "시에라리온"
    },
    {
    "iso_3166_1": "SM",
    "english_name": "San Marino",
    "native_name": "산마리노"
    },
    {
    "iso_3166_1": "SN",
    "english_name": "Senegal",
    "native_name": "세네갈"
    },
    {
    "iso_3166_1": "SO",
    "english_name": "Somalia",
    "native_name": "소말리아"
    },
    {
    "iso_3166_1": "SR",
    "english_name": "Suriname",
    "native_name": "수리남"
    },
    {
    "iso_3166_1": "SS",
    "english_name": "South Sudan",
    "native_name": "남수단"
    },
    {
    "iso_3166_1": "ST",
    "english_name": "Sao Tome and Principe",
    "native_name": "상투메 프린시페"
    },
    {
    "iso_3166_1": "SU",
    "english_name": "Soviet Union",
    "native_name": "Soviet Union"
    },
    {
    "iso_3166_1": "SV",
    "english_name": "El Salvador",
    "native_name": "엘살바도르"
    },
    {
    "iso_3166_1": "SY",
    "english_name": "Syrian Arab Republic",
    "native_name": "시리아"
    },
    {
    "iso_3166_1": "SZ",
    "english_name": "Swaziland",
    "native_name": "스와질랜드"
    },
    {
    "iso_3166_1": "TC",
    "english_name": "Turks and Caicos Islands",
    "native_name": "터크스케이커스제도"
    },
    {
    "iso_3166_1": "TD",
    "english_name": "Chad",
    "native_name": "차드"
    },
    {
    "iso_3166_1": "TF",
    "english_name": "French Southern Territories",
    "native_name": "프랑스 남부 지방"
    },
    {
    "iso_3166_1": "TG",
    "english_name": "Togo",
    "native_name": "토고"
    },
    {
    "iso_3166_1": "TH",
    "english_name": "Thailand",
    "native_name": "태국"
    },
    {
    "iso_3166_1": "TJ",
    "english_name": "Tajikistan",
    "native_name": "타지키스탄"
    },
    {
    "iso_3166_1": "TK",
    "english_name": "Tokelau",
    "native_name": "토켈라우"
    },
    {
    "iso_3166_1": "TL",
    "english_name": "Timor-Leste",
    "native_name": "동티모르"
    },
    {
    "iso_3166_1": "TM",
    "english_name": "Turkmenistan",
    "native_name": "투르크메니스탄"
    },
    {
    "iso_3166_1": "TN",
    "english_name": "Tunisia",
    "native_name": "튀니지"
    },
    {
    "iso_3166_1": "TO",
    "english_name": "Tonga",
    "native_name": "통가"
    },
    {
    "iso_3166_1": "TP",
    "english_name": "East Timor",
    "native_name": "East Timor"
    },
    {
    "iso_3166_1": "TR",
    "english_name": "Turkey",
    "native_name": "터키"
    },
    {
    "iso_3166_1": "TT",
    "english_name": "Trinidad and Tobago",
    "native_name": "트리니다드 토바고"
    },
    {
    "iso_3166_1": "TV",
    "english_name": "Tuvalu",
    "native_name": "투발루"
    },
    {
    "iso_3166_1": "TW",
    "english_name": "Taiwan",
    "native_name": "대만"
    },
    {
    "iso_3166_1": "TZ",
    "english_name": "Tanzania",
    "native_name": "탄자니아"
    },
    {
    "iso_3166_1": "UA",
    "english_name": "Ukraine",
    "native_name": "우크라이나"
    },
    {
    "iso_3166_1": "UG",
    "english_name": "Uganda",
    "native_name": "우간다"
    },
    {
    "iso_3166_1": "UM",
    "english_name": "United States Minor Outlying Islands",
    "native_name": "미국령 해외 제도"
    },
    {
    "iso_3166_1": "US",
    "english_name": "United States of America",
    "native_name": "미국"
    },
    {
    "iso_3166_1": "UY",
    "english_name": "Uruguay",
    "native_name": "우루과이"
    },
    {
    "iso_3166_1": "UZ",
    "english_name": "Uzbekistan",
    "native_name": "우즈베키스탄"
    },
    {
    "iso_3166_1": "VA",
    "english_name": "Holy See",
    "native_name": "바티칸"
    },
    {
    "iso_3166_1": "VC",
    "english_name": "St. Vincent and the Grenadines",
    "native_name": "세인트빈센트그레나딘"
    },
    {
    "iso_3166_1": "VE",
    "english_name": "Venezuela",
    "native_name": "베네수엘라"
    },
    {
    "iso_3166_1": "VG",
    "english_name": "British Virgin Islands",
    "native_name": "영국령 버진 아일랜드"
    },
    {
    "iso_3166_1": "VI",
    "english_name": "US Virgin Islands",
    "native_name": "미국령 버진 아일랜드"
    },
    {
    "iso_3166_1": "VN",
    "english_name": "Vietnam",
    "native_name": "베트남"
    },
    {
    "iso_3166_1": "VU",
    "english_name": "Vanuatu",
    "native_name": "바누아투"
    },
    {
    "iso_3166_1": "WF",
    "english_name": "Wallis and Futuna Islands",
    "native_name": "왈리스-푸투나 제도"
    },
    {
    "iso_3166_1": "WS",
    "english_name": "Samoa",
    "native_name": "사모아"
    },
    {
    "iso_3166_1": "XC",
    "english_name": "Czechoslovakia",
    "native_name": "Czechoslovakia"
    },
    {
    "iso_3166_1": "XG",
    "english_name": "East Germany",
    "native_name": "East Germany"
    },
    {
    "iso_3166_1": "XI",
    "english_name": "Northern Ireland",
    "native_name": "Northern Ireland"
    },
    {
    "iso_3166_1": "XK",
    "english_name": "Kosovo",
    "native_name": "코소보"
    },
    {
    "iso_3166_1": "YE",
    "english_name": "Yemen",
    "native_name": "예멘"
    },
    {
    "iso_3166_1": "YT",
    "english_name": "Mayotte",
    "native_name": "마요티"
    },
    {
    "iso_3166_1": "YU",
    "english_name": "Yugoslavia",
    "native_name": "Yugoslavia"
    },
    {
    "iso_3166_1": "ZA",
    "english_name": "South Africa",
    "native_name": "남아프리카"
    },
    {
    "iso_3166_1": "ZM",
    "english_name": "Zambia",
    "native_name": "잠비아"
    },
    {
    "iso_3166_1": "ZR",
    "english_name": "Zaire",
    "native_name": "Zaire"
    },
    {
    "iso_3166_1": "ZW",
    "english_name": "Zimbabwe",
    "native_name": "짐바브웨"
    }
]
```
    

## Certifications

국가별 시청 등급을 확인할 수 있으며 MOVIE와 TV 두 개의 종류가 있다.

### [영화 시청등급](https://developer.themoviedb.org/reference/certification-movie-list)

```json
"KR": [
  {
    "certification": "All",
    "meaning": "Film suitable for all ages.",
    "order": 0
  },
  {
    "certification": "12",
    "meaning": "Film intended for audiences 12 and over. Underage audiences accompanied by a parent or guardian are allowed.",
    "order": 1
  },
  {
    "certification": "15",
    "meaning": "Film intended for audiences 15 and over. Underage audiences accompanied by a parent or guardian are allowed.",
    "order": 2
  },
  {
    "certification": "18",
    "meaning": "No one under 18 is allowed to watch this film.",
    "order": 3
  },
  {
    "certification": "Restricted Screening",
    "meaning": "Film needs a certain restriction in screening or advertisement as it is considered a highly bad influence to universal human dignity, social value, good customs or national emotion due to excessive expression of nudity, violence, social behavior, etc. (technically not an age restriction but films with this rating may only be screened at \\"adults only\\" theatres, with the age of majority set at 19).",
    "order": 4
  }
]

```

### [TV 시청등급](https://developer.themoviedb.org/reference/certifications-tv-list)

```json
"KR": [
  {
    "certification": "Exempt",
    "meaning": "This rating is only for knowledge based game shows; lifestyle shows; documentary shows; news; current topic discussion shows; education/culture shows; sports that excludes MMA or other violent sports; and other programs that Korea Communications Standards Commission recognizes.",
    "order": 1
  },
  {
    "certification": "ALL",
    "meaning": "This rating is for programming that is appropriate for all ages. This program usually involves programs designed for children or families.",
    "order": 2
  },
  {
    "certification": "7",
    "meaning": "This rating is for programming that may contain material inappropriate for children younger than 7, and parental discretion should be used. Some cartoon programming not deemed strictly as ",
    "order": 3
  },
  {
    "certification": "12",
    "meaning": "This rating is for programs that may deemed inappropriate for those younger than 12, and parental discretion should be used. Usually used for animations that have stronger themes or violence then those designed for children, or for reality shows that have mild violence, themes, or language.",
    "order": 4
  },
  {
    "certification": "15",
    "meaning": "This rating is for programs that contain material that may be inappropriate for children under 15, and that parental discretion should be used. Examples include most dramas, and talk shows on OTA (over-the-air) TV (KBS, MBC, SBS), and many American TV shows/dramas on Cable TV channels like OCN and OnStyle. The programs that have this rating may include moderate or strong adult themes, language, sexual inference, and violence. As with the TV-MA rating in North America, this rating is commonly applied to live events where the occurrence of inappropriate dialogue is unpredictable. Since 2007, this rating is the most used rating for TV.",
    "order": 5
  },
  {
    "certification": "19",
    "meaning": "This rating is for programs that are intended for adults only. 19-rated programming cannot air during the hours of 7:00AM to 9:00AM, and 1:00PM to 10:00PM. Programmes that receive this rating will almost certainly have adult themes, sexual situations, frequent use of strong language and disturbing scenes of violence.",
    "order": 6
  }
]

```

---

## 상세정보(details)

- status : tv, movie 모두 공통적으로 가지고 있는 필드로, tv의 경우 `Ended`, movie는 `Released`의 값을 가진다. 그 외의 값이 있을 수는 있겠지만 아직 실제 데이터는 확인 못함

---

# API 사용 예시

## Movie 데이터

[Details](https://developer.themoviedb.org/reference/movie-details)

### API REQUEST 예시 <<인생은 아름다워>>

```graphql
curl --request GET \
     --url 'https://api.themoviedb.org/3/movie/637?append_to_response=credits&language=ko-kr' \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4ODM2NWNmNmJkYzZjNDYwMTViZjg1YzczMWRmYWI4ZiIsInN1YiI6IjY0NTRlZmFhZDQ4Y2VlMDEzNmRhMWM1MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QZC-wgg4ipi9UgxmLjrTzUtrW6C8S5u_pINevgwr97k' \
     --header 'accept: application/json'
```

### 실제 수신 데이터(MOVIE)

```json
{
    "adult": false,
    "backdrop_path": "/gavyCu1UaTaTNPsVaGXT6pe5u24.jpg",
    "belongs_to_collection": null,
    "budget": 20000000,
    "genres": [
    {
        "id": 35,
        "name": "코미디"
    },
    {
        "id": 18,
        "name": "드라마"
    }
    ],
    "homepage": "",
    "id": 637,
    "imdb_id": "tt0118799",
    "original_language": "it",
    "original_title": "La vita è bella",
    "overview": "로마에 갓 상경한 시골 총각 귀도는 운명처럼 만난 여인 도라에게 첫눈에 반한다. 넘치는 재치와 유머로 약혼자가 있던 그녀를 사로잡은 귀도는 가정을 꾸리며 분신과도 같은 아들 조수아를 얻는다. 조수아의 다섯 살 생일, 갑작스레 들이닥친 군인들은 귀도와 조수아를 수용소 행 기차에 실어버리고, 소식을 들은 도라 역시 기차에 따라 오른다. 귀도는 아들을 달래기 위해 무자비한 수용소 생활을 단체게임이라 속이고 1,000점을 따는 우승자에게는 진짜 탱크가 주어진다고 말한다. 하루하루가 지나 어느덧 전쟁이 끝났다는 말을 들은 귀도는 조수아를 창고에 숨겨둔 채 아내를 찾아 나서는데...",
    "popularity": 42.514,
    "poster_path": "/yjOqQsQHdsEZfAosZERqHiwjaty.jpg",
    "production_companies": [
    {
        "id": 370,
        "logo_path": null,
        "name": "Melampo Cinematografica",
        "origin_country": "IT"
    }
    ],
    "production_countries": [
    {
        "iso_3166_1": "IT",
        "name": "Italy"
    }
    ],
    "release_date": "1997-12-20",
    "revenue": 230098753,
    "runtime": 116,
    "spoken_languages": [
    {
        "english_name": "English",
        "iso_639_1": "en",
        "name": "English"
    },
    {
        "english_name": "Italian",
        "iso_639_1": "it",
        "name": "Italiano"
    },
    {
        "english_name": "German",
        "iso_639_1": "de",
        "name": "Deutsch"
    },
    {
        "english_name": "Czech",
        "iso_639_1": "cs",
        "name": "Český"
    }
    ],
    "status": "Released",
    "tagline": "깐느가 그랑프리를 헌사한 이탈리아 영화천재의 걸작",
    "title": "인생은 아름다워",
    "video": false,
    "vote_average": 8.455,
    "vote_count": 11932,
    "credits": {
    "cast": [
        {
        "adult": false,
        "gender": 2,
        "id": 4818,
        "known_for_department": "Acting",
        "name": "Roberto Benigni",
        "original_name": "Roberto Benigni",
        "popularity": 13.683,
        "profile_path": "/noelOhwX1oaNSvU9NLKhPrHTFI3.jpg",
        "cast_id": 8,
        "character": "Guido Orefice",
        "credit_id": "52fe4262c3a36847f801a125",
        "order": 0
        },
        {
        "adult": false,
        "gender": 1,
        "id": 9235,
        "known_for_department": "Acting",
        "name": "Nicoletta Braschi",
        "original_name": "Nicoletta Braschi",
        "popularity": 4.931,
        "profile_path": "/i1BYJhg2V6PZEkCaMyYNLRqutmM.jpg",
        "cast_id": 7,
        "character": "Dora",
        "credit_id": "52fe4262c3a36847f801a121",
        "order": 1
        },
        {
        "adult": false,
        "gender": 2,
        "id": 9236,
        "known_for_department": "Acting",
        "name": "Giorgio Cantarini",
        "original_name": "Giorgio Cantarini",
        "popularity": 7.385,
        "profile_path": "/hzb7CRUnOitz31kQbgUqJpIPcLO.jpg",
        "cast_id": 9,
        "character": "Giosué Orefice",
        "credit_id": "52fe4262c3a36847f801a129",
        "order": 2
        },
        {
        "adult": false,
        "gender": 2,
        "id": 9237,
        "known_for_department": "Acting",
        "name": "Giustino Durano",
        "original_name": "Giustino Durano",
        "popularity": 2.852,
        "profile_path": "/o302wA8DHLHDLhTXOF5wEi3C99G.jpg",
        "cast_id": 10,
        "character": "Eliseo Orefice",
        "credit_id": "52fe4262c3a36847f801a12d",
        "order": 3
        },
        {
        "adult": false,
        "gender": 2,
        "id": 9239,
        "known_for_department": "Acting",
        "name": "Sergio Bini Bustric",
        "original_name": "Sergio Bini Bustric",
        "popularity": 3.103,
        "profile_path": "/crnlLn1SxP2LqbsXNr8CQrvaiNc.jpg",
        "cast_id": 12,
        "character": "Ferruccio",
        "credit_id": "52fe4262c3a36847f801a135",
        "order": 4
        },
        {
        "adult": false,
        "gender": 1,
        "id": 9240,
        "known_for_department": "Acting",
        "name": "Lidia Alfonsi",
        "original_name": "Lidia Alfonsi",
        "popularity": 1.525,
        "profile_path": "/iR5CcEPuHaEeWSxVCHuf48IEw9C.jpg",
        "cast_id": 13,
        "character": "Signora Guicciardini",
        "credit_id": "52fe4262c3a36847f801a139",
        "order": 5
        },
        {
        "adult": false,
        "gender": 1,
        "id": 9242,
        "known_for_department": "Acting",
        "name": "Giuliana Lojodice",
        "original_name": "Giuliana Lojodice",
        "popularity": 1.96,
        "profile_path": "/cACsY8JyWaR3WeX7w1D09YssXbq.jpg",
        "cast_id": 17,
        "character": "Direttrice",
        "credit_id": "52fe4262c3a36847f801a149",
        "order": 6
        },
        {
        "adult": false,
        "gender": 2,
        "id": 9238,
        "known_for_department": "Acting",
        "name": "Amerigo Fontani",
        "original_name": "Amerigo Fontani",
        "popularity": 2.116,
        "profile_path": "/uRQn3gGNPGQzG6XNli1b1TiEu6G.jpg",
        "cast_id": 11,
        "character": "Rodolfo",
        "credit_id": "52fe4262c3a36847f801a131",
        "order": 7
        },
        {
        "adult": false,
        "gender": 2,
        "id": 9241,
        "known_for_department": "Acting",
        "name": "Pietro De Silva",
        "original_name": "Pietro De Silva",
        "popularity": 2.216,
        "profile_path": "/tjP3YLGB3VNtqNgqGmLjZbJENzG.jpg",
        "cast_id": 15,
        "character": "Bartolomeo",
        "credit_id": "52fe4262c3a36847f801a141",
        "order": 8
        },
        {
        "adult": false,
        "gender": 2,
        "id": 9243,
        "known_for_department": "Acting",
        "name": "Francesco Guzzo",
        "original_name": "Francesco Guzzo",
        "popularity": 2.008,
        "profile_path": "/8HSTZitD85LIqOOhpTepILHyxW2.jpg",
        "cast_id": 18,
        "character": "Vittorino",
        "credit_id": "52fe4262c3a36847f801a14d",
        "order": 9
        },
        {
        "adult": false,
        "gender": 1,
        "id": 93726,
        "known_for_department": "Acting",
        "name": "Raffaella Lebboroni",
        "original_name": "Raffaella Lebboroni",
        "popularity": 0.98,
        "profile_path": "/uYtbQoNEtcZD1l9ioiVCgCHbpNl.jpg",
        "cast_id": 56,
        "character": "Elena",
        "credit_id": "6310a7620231f2007dbe4ef5",
        "order": 10
        },
        {
        "adult": false,
        "gender": 1,
        "id": 954,
        "known_for_department": "Acting",
        "name": "Marisa Paredes",
        "original_name": "Marisa Paredes",
        "popularity": 2.77,
        "profile_path": "/aDfNPZ2plaCmdrYkCkburjBqYnP.jpg",
        "cast_id": 16,
        "character": "Madre di Dora",
        "credit_id": "52fe4262c3a36847f801a145",
        "order": 11
        },
        {
        "adult": false,
        "gender": 2,
        "id": 5789,
        "known_for_department": "Acting",
        "name": "Horst Buchholz",
        "original_name": "Horst Buchholz",
        "popularity": 11.221,
        "profile_path": "/9V38Di9T0qsjKBl2dR7sZMN1N0i.jpg",
        "cast_id": 14,
        "character": "Dottore Lessing",
        "credit_id": "52fe4262c3a36847f801a13d",
        "order": 12
        },
        {
        "adult": false,
        "gender": 1,
        "id": 1581614,
        "known_for_department": "Acting",
        "name": "Adelaide Alaïs",
        "original_name": "Adelaide Alaïs",
        "popularity": 0.6,
        "profile_path": "/wvlaqClIHLPQQW3KJBddgChY9aa.jpg",
        "cast_id": 50,
        "character": "German Auxilliary",
        "credit_id": "56cb8257c3a36865eb0000e1",
        "order": 13
        },
        {
        "adult": false,
        "gender": 1,
        "id": 6289,
        "known_for_department": "Acting",
        "name": "Verena Buratti",
        "original_name": "Verena Buratti",
        "popularity": 0.6,
        "profile_path": "/yuauzvkee0BanUsUkh146mB7jco.jpg",
        "cast_id": 26,
        "character": "German Auxilliary",
        "credit_id": "568c81a4925141133402684a",
        "order": 14
        },
        {
        "adult": false,
        "gender": 2,
        "id": 45662,
        "known_for_department": "Acting",
        "name": "Hannes Hellmann",
        "original_name": "Hannes Hellmann",
        "popularity": 1.922,
        "profile_path": "/y9tEzBMQJb8wiP1YAmHoGtCPSib.jpg",
        "cast_id": 27,
        "character": "German Corporal",
        "credit_id": "568c82339251414ecb021ba3",
        "order": 15
        },
        {
        "adult": false,
        "gender": 2,
        "id": 991277,
        "known_for_department": "Acting",
        "name": "Wolfgang Hillinger",
        "original_name": "Wolfgang Hillinger",
        "popularity": 1.4,
        "profile_path": null,
        "cast_id": 28,
        "character": "German Major at Party",
        "credit_id": "568c825cc3a3684bcc03276c",
        "order": 16
        },
        {
        "adult": false,
        "gender": 2,
        "id": 51637,
        "known_for_department": "Acting",
        "name": "Antonio Prester",
        "original_name": "Antonio Prester",
        "popularity": 1.8,
        "profile_path": "/z8wGJL9bCiHrXi31zvmcngZP5S5.jpg",
        "cast_id": 30,
        "character": "Bruno",
        "credit_id": "568c838fc3a368362801940c",
        "order": 17
        },
        {
        "adult": false,
        "gender": 1,
        "id": 33928,
        "known_for_department": "Acting",
        "name": "Gina Rovere",
        "original_name": "Gina Rovere",
        "popularity": 1.851,
        "profile_path": "/hv2v5liqJKBtaNGQqRgkf2fN4bV.jpg",
        "cast_id": 31,
        "character": "Dora's Maid",
        "credit_id": "568c83b1c3a368227b0253aa",
        "order": 18
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1084894,
        "known_for_department": "Acting",
        "name": "Laura Susanne Ruedeberg",
        "original_name": "Laura Susanne Ruedeberg",
        "popularity": 0.98,
        "profile_path": null,
        "cast_id": 32,
        "character": "German Auxilliary",
        "credit_id": "568c83d8c3a36860e9030caf",
        "order": 19
        },
        {
        "adult": false,
        "gender": 2,
        "id": 49487,
        "known_for_department": "Acting",
        "name": "Richard Sammel",
        "original_name": "Richard Sammel",
        "popularity": 3.825,
        "profile_path": "/91IPxy0IuHhIqcrJdI0hYBpJmOg.jpg",
        "cast_id": 33,
        "character": "German Lieutenant at Station",
        "credit_id": "568c840fc3a3683628019424",
        "order": 20
        },
        {
        "adult": false,
        "gender": 2,
        "id": 147159,
        "known_for_department": "Acting",
        "name": "Andrea Tidona",
        "original_name": "Andrea Tidona",
        "popularity": 1.09,
        "profile_path": "/zAAumPfwVljPd3VHPuRKlEMNo2D.jpg",
        "cast_id": 34,
        "character": "Grand Hotel Doorman",
        "credit_id": "568c843692514131df02d11b",
        "order": 21
        },
        {
        "adult": false,
        "gender": 2,
        "id": 1369056,
        "known_for_department": "Directing",
        "name": "Dirk K. van den Berg",
        "original_name": "Dirk K. van den Berg",
        "popularity": 0.6,
        "profile_path": null,
        "cast_id": 35,
        "character": "German Soldier",
        "credit_id": "568c845d92514132db02e6d1",
        "order": 22
        },
        {
        "adult": false,
        "gender": 2,
        "id": 27208,
        "known_for_department": "Acting",
        "name": "Omero Antonutti",
        "original_name": "Omero Antonutti",
        "popularity": 1.918,
        "profile_path": "/2MWM2DCyuQM1fLoplTCeN2KsJY7.jpg",
        "cast_id": 36,
        "character": "Narrator (voice) (uncredited)",
        "credit_id": "568c8485c3a3686075030cae",
        "order": 23
        },
        {
        "adult": false,
        "gender": 1,
        "id": 3267059,
        "known_for_department": "Acting",
        "name": "Daniela Fedtke",
        "original_name": "Daniela Fedtke",
        "popularity": 0.98,
        "profile_path": "/ages9aTFkuOELH9r4JddFstjNK1.jpg",
        "cast_id": 52,
        "character": "German Auxiliary",
        "credit_id": "6164573b84591c00432fc2d1",
        "order": 24
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1884402,
        "known_for_department": "Acting",
        "name": "Claudio Alfonsi",
        "original_name": "Claudio Alfonsi",
        "popularity": 0.6,
        "profile_path": "/wXC4Zbg45JRUnF3ya8rk5lx4Yfj.jpg",
        "cast_id": 98,
        "character": "Amico Rodolfo",
        "credit_id": "63a2b37cbe6d8800a2c3b185",
        "order": 25
        },
        {
        "adult": false,
        "gender": 2,
        "id": 1397652,
        "known_for_department": "Directing",
        "name": "Gil Baroni",
        "original_name": "Gil Baroni",
        "popularity": 0.6,
        "profile_path": null,
        "cast_id": 99,
        "character": "Prefetto",
        "credit_id": "63a2b3b28ddc34149eefe666",
        "order": 26
        }
    ],
    "crew": [
        {
        "adult": false,
        "gender": 2,
        "id": 2361,
        "known_for_department": "Camera",
        "name": "Tonino Delli Colli",
        "original_name": "Tonino Delli Colli",
        "popularity": 2.713,
        "profile_path": "/sgr90whx93wMsLqRTFUzETI3Z8U.jpg",
        "credit_id": "52fe4262c3a36847f801a153",
        "department": "Camera",
        "job": "Director of Photography"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 4659,
        "known_for_department": "Crew",
        "name": "Giovanni Corridori",
        "original_name": "Giovanni Corridori",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "52fe4262c3a36847f801a171",
        "department": "Crew",
        "job": "Special Effects"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 4818,
        "known_for_department": "Acting",
        "name": "Roberto Benigni",
        "original_name": "Roberto Benigni",
        "popularity": 13.683,
        "profile_path": "/noelOhwX1oaNSvU9NLKhPrHTFI3.jpg",
        "credit_id": "52fe4262c3a36847f801a117",
        "department": "Writing",
        "job": "Screenplay"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 4818,
        "known_for_department": "Acting",
        "name": "Roberto Benigni",
        "original_name": "Roberto Benigni",
        "popularity": 13.683,
        "profile_path": "/noelOhwX1oaNSvU9NLKhPrHTFI3.jpg",
        "credit_id": "52fe4262c3a36847f801a0ff",
        "department": "Directing",
        "job": "Director"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 4818,
        "known_for_department": "Acting",
        "name": "Roberto Benigni",
        "original_name": "Roberto Benigni",
        "popularity": 13.683,
        "profile_path": "/noelOhwX1oaNSvU9NLKhPrHTFI3.jpg",
        "credit_id": "630de4b318864b00832a22d5",
        "department": "Writing",
        "job": "Story"
        },
        {
        "adult": false,
        "gender": 1,
        "id": 8753,
        "known_for_department": "Production",
        "name": "Shaila Rubin",
        "original_name": "Shaila Rubin",
        "popularity": 1.579,
        "profile_path": null,
        "credit_id": "6310ab13c048a90085039d92",
        "department": "Production",
        "job": "Casting"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 9232,
        "known_for_department": "Production",
        "name": "Gianluigi Braschi",
        "original_name": "Gianluigi Braschi",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "52fe4262c3a36847f801a105",
        "department": "Production",
        "job": "Producer"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 9233,
        "known_for_department": "Production",
        "name": "Elda Ferri",
        "original_name": "Elda Ferri",
        "popularity": 1.094,
        "profile_path": null,
        "credit_id": "52fe4262c3a36847f801a111",
        "department": "Production",
        "job": "Producer"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 9234,
        "known_for_department": "Writing",
        "name": "Vincenzo Cerami",
        "original_name": "Vincenzo Cerami",
        "popularity": 1.4,
        "profile_path": "/8YDpYwdW5V6EKPZiPO9xfsKKMnb.jpg",
        "credit_id": "52fe4262c3a36847f801a11d",
        "department": "Writing",
        "job": "Screenplay"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 9234,
        "known_for_department": "Writing",
        "name": "Vincenzo Cerami",
        "original_name": "Vincenzo Cerami",
        "popularity": 1.4,
        "profile_path": "/8YDpYwdW5V6EKPZiPO9xfsKKMnb.jpg",
        "credit_id": "630de4a923bcf4007bf4cfad",
        "department": "Writing",
        "job": "Story"
        },
        {
        "adult": false,
        "gender": 1,
        "id": 9244,
        "known_for_department": "Editing",
        "name": "Simona Paggi",
        "original_name": "Simona Paggi",
        "popularity": 1.094,
        "profile_path": "/2LCAI7o2iE2bYYlH2seYppYchdg.jpg",
        "credit_id": "52fe4262c3a36847f801a159",
        "department": "Editing",
        "job": "Editor"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 9245,
        "known_for_department": "Sound",
        "name": "Nicola Piovani",
        "original_name": "Nicola Piovani",
        "popularity": 1.4,
        "profile_path": "/56tRfEIn4RBPhjJ7JOGCOtTZApU.jpg",
        "credit_id": "52fe4262c3a36847f801a15f",
        "department": "Sound",
        "job": "Original Music Composer"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 9247,
        "known_for_department": "Costume & Make-Up",
        "name": "Danilo Donati",
        "original_name": "Danilo Donati",
        "popularity": 1.4,
        "profile_path": "/2xo4XyJZUYDVI3yEQA12M582ibf.jpg",
        "credit_id": "52fe4262c3a36847f801a165",
        "department": "Art",
        "job": "Production Design"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 9247,
        "known_for_department": "Costume & Make-Up",
        "name": "Danilo Donati",
        "original_name": "Danilo Donati",
        "popularity": 1.4,
        "profile_path": "/2xo4XyJZUYDVI3yEQA12M582ibf.jpg",
        "credit_id": "52fe4262c3a36847f801a16b",
        "department": "Costume & Make-Up",
        "job": "Costume Design"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 67138,
        "known_for_department": "Art",
        "name": "Maurizio Sabatini",
        "original_name": "Maurizio Sabatini",
        "popularity": 0.694,
        "profile_path": null,
        "credit_id": "6310aa2be78687007f5a388a",
        "department": "Art",
        "job": "Assistant Production Design"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 235398,
        "known_for_department": "Directing",
        "name": "Gianni Arduini",
        "original_name": "Gianni Arduini",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "6310a7d77fcab30091dba8a9",
        "department": "Directing",
        "job": "First Assistant Director"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 238075,
        "known_for_department": "Editing",
        "name": "Benni Atria",
        "original_name": "Benni Atria",
        "popularity": 1.4,
        "profile_path": null,
        "credit_id": "6310a7ab564ec7007ffa8c90",
        "department": "Sound",
        "job": "Sound Editor"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 238075,
        "known_for_department": "Editing",
        "name": "Benni Atria",
        "original_name": "Benni Atria",
        "popularity": 1.4,
        "profile_path": null,
        "credit_id": "6310aa17cb8028007d8bdf92",
        "department": "Editing",
        "job": "Assistant Editor"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1141912,
        "known_for_department": "Sound",
        "name": "Alberto Doni",
        "original_name": "Alberto Doni",
        "popularity": 0.98,
        "profile_path": null,
        "credit_id": "6310ab68126ec3007b3e8618",
        "department": "Sound",
        "job": "Sound Mixer"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1302370,
        "known_for_department": "Production",
        "name": "Tullio Lullo",
        "original_name": "Tullio Lullo",
        "popularity": 0.98,
        "profile_path": null,
        "credit_id": "6310a925be55b7008d7efdae",
        "department": "Production",
        "job": "Production Manager"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1339104,
        "known_for_department": "Acting",
        "name": "Leda Lojodice",
        "original_name": "Leda Lojodice",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "6310ab2de78687007a3c1e24",
        "department": "Crew",
        "job": "Choreographer"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 1343811,
        "known_for_department": "Production",
        "name": "Mario Cotone",
        "original_name": "Mario Cotone",
        "popularity": 5.612,
        "profile_path": null,
        "credit_id": "6310a84bbe55b7008d7efd6d",
        "department": "Production",
        "job": "Executive Producer"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1400016,
        "known_for_department": "Art",
        "name": "Roberto Magagnini",
        "original_name": "Roberto Magagnini",
        "popularity": 0.98,
        "profile_path": null,
        "credit_id": "6310aa687fcab3007a209372",
        "department": "Art",
        "job": "Property Master"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1438849,
        "known_for_department": "Production",
        "name": "Olivia Sleiter",
        "original_name": "Olivia Sleiter",
        "popularity": 0.98,
        "profile_path": null,
        "credit_id": "6310a933126ec3007b3e856c",
        "department": "Production",
        "job": "Unit Manager"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1559007,
        "known_for_department": "Production",
        "name": "Attilio Viti",
        "original_name": "Attilio Viti",
        "popularity": 1.4,
        "profile_path": null,
        "credit_id": "568d53e19251411334028694",
        "department": "Production",
        "job": "Production Manager"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1559015,
        "known_for_department": "Editing",
        "name": "Pasquale Cuzzupoli",
        "original_name": "Pasquale Cuzzupoli",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "6310ab411511aa007ba2fbe4",
        "department": "Editing",
        "job": "Colorist"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1565668,
        "known_for_department": "Costume & Make-Up",
        "name": "Federico Laurenti",
        "original_name": "Federico Laurenti",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "6310aa977fcab3007a20937c",
        "department": "Costume & Make-Up",
        "job": "Makeup Artist"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1575788,
        "known_for_department": "Costume & Make-Up",
        "name": "Enrico Iacoponi",
        "original_name": "Enrico Iacoponi",
        "popularity": 0.694,
        "profile_path": null,
        "credit_id": "6310aa890231f2007dbe4fec",
        "department": "Costume & Make-Up",
        "job": "Makeup Department Head"
        },
        {
        "adult": false,
        "gender": 1,
        "id": 1589495,
        "known_for_department": "Costume & Make-Up",
        "name": "Giusy Bovino",
        "original_name": "Giusy Bovino",
        "popularity": 0.98,
        "profile_path": null,
        "credit_id": "6310aaae564ec7007a8deceb",
        "department": "Costume & Make-Up",
        "job": "Hair Department Head"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 1603849,
        "known_for_department": "Sound",
        "name": "Tullio Morganti",
        "original_name": "Tullio Morganti",
        "popularity": 1.008,
        "profile_path": null,
        "credit_id": "6310a7a160620a007b4b3a1c",
        "department": "Sound",
        "job": "Sound"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1606272,
        "known_for_department": "Art",
        "name": "Luigi Urbani",
        "original_name": "Luigi Urbani",
        "popularity": 0.98,
        "profile_path": null,
        "credit_id": "6310aa3f60620a007e62dbb8",
        "department": "Art",
        "job": "Set Decoration"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1607656,
        "known_for_department": "Lighting",
        "name": "Carlo Vinciguerra",
        "original_name": "Carlo Vinciguerra",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "6310aad9564ec7007ffa8dfb",
        "department": "Lighting",
        "job": "Gaffer"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1716287,
        "known_for_department": "Camera",
        "name": "Roberto Brega",
        "original_name": "Roberto Brega",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "6310a7e6d7a70a007b211442",
        "department": "Camera",
        "job": "Camera Operator"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 1813984,
        "known_for_department": "Directing",
        "name": "Luigi Spoletini",
        "original_name": "Luigi Spoletini",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "6310a9a8564ec7007a8decb0",
        "department": "Directing",
        "job": "Second Assistant Director"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1946669,
        "known_for_department": "Costume & Make-Up",
        "name": "Walter Cossu",
        "original_name": "Walter Cossu",
        "popularity": 0.648,
        "profile_path": null,
        "credit_id": "6310aa7dc048a90085039d57",
        "department": "Costume & Make-Up",
        "job": "Makeup Department Head"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1956979,
        "known_for_department": "Sound",
        "name": "Ettore Mancini",
        "original_name": "Ettore Mancini",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "6310aa0bbe55b7008d7efdf0",
        "department": "Sound",
        "job": "Boom Operator"
        },
        {
        "adult": false,
        "gender": 1,
        "id": 1972290,
        "known_for_department": "Sound",
        "name": "Silvia Moraes",
        "original_name": "Silvia Moraes",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "6310a7c9d7a70a007b211439",
        "department": "Sound",
        "job": "Sound Editor"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 2019585,
        "known_for_department": "Camera",
        "name": "Aldo Colanzi",
        "original_name": "Aldo Colanzi",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "6310aae2e78687007f5a38e0",
        "department": "Camera",
        "job": "Key Grip"
        },
        {
        "adult": false,
        "gender": 1,
        "id": 2049822,
        "known_for_department": "Directing",
        "name": "Giorgia Onofri",
        "original_name": "Giorgia Onofri",
        "popularity": 0.98,
        "profile_path": null,
        "credit_id": "6310a9db0d2944007959723b",
        "department": "Directing",
        "job": "Script Supervisor"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 2087823,
        "known_for_department": "Production",
        "name": "Pietro Sassaroli",
        "original_name": "Pietro Sassaroli",
        "popularity": 0.98,
        "profile_path": null,
        "credit_id": "6310a91160620a0083e622f0",
        "department": "Production",
        "job": "Production Manager"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 2219982,
        "known_for_department": "Camera",
        "name": "Marco Cuzzupoli",
        "original_name": "Marco Cuzzupoli",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "6310a9f6564ec7007ffa8d92",
        "department": "Camera",
        "job": "Assistant Camera"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 2593216,
        "known_for_department": "Sound",
        "name": "Claudio Chiossi",
        "original_name": "Claudio Chiossi",
        "popularity": 0.614,
        "profile_path": null,
        "credit_id": "6310ab87126ec3007e184bee",
        "department": "Sound",
        "job": "Sound Mixer"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 2610123,
        "known_for_department": "Costume & Make-Up",
        "name": "Martina Cossu",
        "original_name": "Martina Cossu",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "6310aaa47fcab3007fbdf3f8",
        "department": "Costume & Make-Up",
        "job": "Makeup Artist"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 2660376,
        "known_for_department": "Editing",
        "name": "Maddalena Colombo",
        "original_name": "Maddalena Colombo",
        "popularity": 0.98,
        "profile_path": null,
        "credit_id": "6310aa200231f2007dbe4fc3",
        "department": "Editing",
        "job": "Assistant Editor"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 2781208,
        "known_for_department": "Production",
        "name": "Ettore Musco",
        "original_name": "Ettore Musco",
        "popularity": 0.98,
        "profile_path": null,
        "credit_id": "6310a96a0d29440081d89303",
        "department": "Production",
        "job": "Production Secretary"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 2838336,
        "known_for_department": "Camera",
        "name": "Sergio Strizzi",
        "original_name": "Sergio Strizzi",
        "popularity": 1.214,
        "profile_path": null,
        "credit_id": "6310aa02126ec30092a0c505",
        "department": "Camera",
        "job": "Still Photographer"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 3028600,
        "known_for_department": "Production",
        "name": "Nando Nibbi",
        "original_name": "Nando Nibbi",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "6310a93f564ec7007a8dec92",
        "department": "Production",
        "job": "Unit Manager"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 3050674,
        "known_for_department": "Costume & Make-Up",
        "name": "Maria Pia Crapanzano",
        "original_name": "Maria Pia Crapanzano",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "6310aac6d7a70a007e1befe2",
        "department": "Costume & Make-Up",
        "job": "Hairstylist"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 3114706,
        "known_for_department": "Camera",
        "name": "Salvatore Bognanni",
        "original_name": "Salvatore Bognanni",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "6310a9eb7fcab3007fbdf3cd",
        "department": "Camera",
        "job": "Assistant Camera"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 3328452,
        "known_for_department": "Art",
        "name": "Edoardo Di Iorio",
        "original_name": "Edoardo Di Iorio",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "6310aa36cb80280094fb6308",
        "department": "Art",
        "job": "Assistant Production Design"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 3428134,
        "known_for_department": "Costume & Make-Up",
        "name": "Fabio Lucchetti",
        "original_name": "Fabio Lucchetti",
        "popularity": 0.98,
        "profile_path": null,
        "credit_id": "6310aab77fcab30091dba9a5",
        "department": "Costume & Make-Up",
        "job": "Hairstylist"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 3442018,
        "known_for_department": "Production",
        "name": "Franco Fantini",
        "original_name": "Franco Fantini",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "6310a978126ec3007b3e8583",
        "department": "Production",
        "job": "Administration"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 3451161,
        "known_for_department": "Production",
        "name": "Marco Albertini",
        "original_name": "Marco Albertini",
        "popularity": 0.98,
        "profile_path": null,
        "credit_id": "6310a960be55b70083c64ef5",
        "department": "Production",
        "job": "Production Secretary"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 3684393,
        "known_for_department": "Directing",
        "name": "Giovanni Marino",
        "original_name": "Giovanni Marino",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "6310a99e0d2944007e83dbbc",
        "department": "Directing",
        "job": "Second Assistant Director"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 3684396,
        "known_for_department": "Directing",
        "name": "Daniele Cama",
        "original_name": "Daniele Cama",
        "popularity": 0.98,
        "profile_path": null,
        "credit_id": "6310a9bb0d2944007e83dbd2",
        "department": "Directing",
        "job": "Second Assistant Director"
        }
    ]
    }
}
```
    

### 추출해서 사용할 데이터(MOVIE)

```json
[영화 정보]
title (제목)
original_title (원제)
original_language (원어)
genre (장르)
tagline (간단소개)
overview (개요)
poster_path (포스터 이미지)
production_countries (제작 국가)
certifications (시청등급)

release_date (개봉일)
status (개봉 여부)
runtime (상영시간)

[감독 및 배우]
known_for_department (역할) : Acting(배우), Directing(감독)
id (인물 id, PEOPLE API 통해서 검색 가능)
name (이름)
gender (성별) : 1이 여자, 2가 남자. 0일 경우에는 ㅁ?ㄹ
character (배역명, 배우인 경우에만)
profile_path (프로필 사진)
```

이렇게 받아온 데이터 중에 배우와 감독은 각각 별도의 데이터베이스에 저장할 예정임

배우, 감독 모두 작품(art_work)과 M : N 관계이기 때문에 이를 위한 테이블 생성


## TV 프로그램 (드라마, 애니메이션 등) 데이터

[Details](https://developer.themoviedb.org/reference/tv-series-details)

### API REQUEST 예시 <<빅뱅 이론>>

```graphql
curl --request GET \
     --url 'https://api.themoviedb.org/3/tv/1418?language=ko-kr' \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4ODM2NWNmNmJkYzZjNDYwMTViZjg1YzczMWRmYWI4ZiIsInN1YiI6IjY0NTRlZmFhZDQ4Y2VlMDEzNmRhMWM1MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QZC-wgg4ipi9UgxmLjrTzUtrW6C8S5u_pINevgwr97k' \
     --header 'accept: application/json'
```

### 실제 수신 데이터(TV)

```json
{
    "adult": false,
    "backdrop_path": "/8X1BTSaUyF5rc0malaaQovpxC3f.jpg",
    "created_by": [
    {
        "id": 160172,
        "credit_id": "5256d00719c2956ff60a3d0e",
        "name": "Chuck Lorre",
        "gender": 2,
        "profile_path": "/8OTRD3d6N0GKy1Z0LJaWZ3MVxXr.jpg"
    },
    {
        "id": 163528,
        "credit_id": "5256d00719c2956ff60a3d14",
        "name": "Bill Prady",
        "gender": 2,
        "profile_path": null
    }
    ],
    "episode_run_time": [
    22
    ],
    "first_air_date": "2007-09-24",
    "genres": [
    {
        "id": 35,
        "name": "코미디"
    }
    ],
    "homepage": "http://www.cbs.com/shows/big_bang_theory/",
    "id": 1418,
    "in_production": false,
    "languages": [
    "en"
    ],
    "last_air_date": "2019-05-16",
    "last_episode_to_air": {
    "id": 2767846,
    "name": "스톡홀름 증후군",
    "overview": "비밀을 들키고, 마음을 다치고, 뒤늦게 진실에 눈뜨는 친구들. 그래도 다 괜찮다. 이 또한 함께 견디고 이겨낼 테니. 지금껏 그랬듯이 앞으로도 우정은 계속되리라, 쭉.",
    "vote_average": 7.556,
    "vote_count": 9,
    "air_date": "2019-05-16",
    "episode_number": 24,
    "production_code": "",
    "runtime": 22,
    "season_number": 12,
    "show_id": 1418,
    "still_path": "/eaC2VG6Iy63vIor6mfOfCZTDw3g.jpg"
    },
    "name": "빅뱅 이론",
    "next_episode_to_air": null,
    "networks": [
    {
        "id": 16,
        "logo_path": "/wju8KhOUsR5y4bH9p3Jc50hhaLO.png",
        "name": "CBS",
        "origin_country": "US"
    }
    ],
    "number_of_episodes": 279,
    "number_of_seasons": 12,
    "origin_country": [
    "US"
    ],
    "original_language": "en",
    "original_name": "The Big Bang Theory",
    "overview": "2007년 9월 CBS에서 방영을 시작한 시트콤. 캘리포니아공과대학(Caltech) 소속의 박사/석사인 쉘든, 레너드, 하워드, 그리고 라제쉬는 지적으로는 뛰어난 인재들이지만, 괴짜 같은 취향에 사회성도 떨어지는 친구 사이이다. 어느 날 실험 물리학자인 레너드와 이론 물리학자인 쉘든이 살고 있는 아파트 건너편에 매력적인 금발의 여배우를 꿈꾸는 종업원 페니가 이사온다. 한 눈에 페니에게 반한 레너드는 그녀의 마음을 얻기 위해 그녀를 점심 식사에 초대하지만, 쉘든은 이 둘이 잘 될 확률은 절대 없을 것이라며 코웃음을 친다.",
    "popularity": 88.867,
    "poster_path": "/ooBGRQBdbGzBxAVfExiO8r7kloA.jpg",
    "production_companies": [
    {
        "id": 35504,
        "logo_path": "/e70DaugzSRbTbVEhZV3e1nCofcY.png",
        "name": "Chuck Lorre Productions",
        "origin_country": "US"
    },
    {
        "id": 1957,
        "logo_path": "/pJJw98MtNFC9cHn3o15G7vaUnnX.png",
        "name": "Warner Bros. Television",
        "origin_country": "US"
    }
    ],
    "production_countries": [
    {
        "iso_3166_1": "US",
        "name": "United States of America"
    }
    ],
    "seasons": [
    {
        "air_date": null,
        "episode_count": 3,
        "id": 3732,
        "name": "스페셜",
        "overview": "",
        "poster_path": "/gtWHKUsG8de6LdZQoCsjUqrLJ1R.jpg",
        "season_number": 0
    },
    {
        "air_date": "2007-09-24",
        "episode_count": 17,
        "id": 3738,
        "name": "시즌 1",
        "overview": "겉은 스튜핏, 속은 스마트. 두 천재 과학도의 여심 잡기 개론. 옆집으로 이사 온 금발의 퀸카와 친해지려 하지만 이해할 수 없는 이론으로 실수 연발이다. 사랑은 이론이 아닌 감정의 화학작용이라는 걸, 둘은 언제쯤 알게 될까.",
        "poster_path": "/zqAL2rav7Tg8uwDtLurqZVN3mtr.jpg",
        "season_number": 1
    },
    {
        "air_date": "2008-09-22",
        "episode_count": 23,
        "id": 3733,
        "name": "시즌 2",
        "overview": "거짓말은 오해를 낳고, 오해는 사랑을 금 가게 한다. 이것이 사랑의 나비효과. 페니의 거짓말로 시작된 나비의 날갯짓이 결국 감당할 수 없는 이별로 돌아왔다. 숫자는 알아도 여자는 몰랐던 천재 과학도들의 연애 이론이 펼쳐진다.",
        "poster_path": "/2NBwUBZ4clwj6qO9fBinfxiB0dR.jpg",
        "season_number": 2
    },
    {
        "air_date": "2009-09-21",
        "episode_count": 23,
        "id": 3734,
        "name": "시즌 3",
        "overview": "세계에서 가장 큰 입자 가속기를 보게 될 행운아는 누구? 영화 《반지의 제왕》에 등장하는 반지 소품과 우정 중에서 이들의 선택은? 더 큰 사랑과 우정의 모험으로 돌아왔다. 괴짜 천재들의 에피소드는 여전히 팽창 중이다.",
        "poster_path": "/j64iUb52W2IYE9qV9pLi5tFq8IE.jpg",
        "season_number": 3
    },
    {
        "air_date": "2010-09-23",
        "episode_count": 24,
        "id": 3735,
        "name": "시즌 4",
        "overview": "국방부에서 일할 기회가 생긴 친구들. FBI의 보안 검사를 통과해야 하는데, 하필 요원이 절세 미인이다. 입도 못 떼는 친구가 있는가 하면, 들이대려는 친구와 잘 보이려다 실수하는 친구까지. 사랑에는 저마다의 속도가 있는 법.",
        "poster_path": "/hM2TYCmOVXop1xhLA1Mbqyg60ze.jpg",
        "season_number": 4
    },
    {
        "air_date": "2011-09-22",
        "episode_count": 24,
        "id": 3736,
        "name": "시즌 5",
        "overview": "머리는 이렇게 쓰는 것. 데이트가 무사히 진행되고 있음을 확인해주는 시스템 완성! 어쩌면 후손들의 연애사를 뒤바꿀 세기의 발명이 될지도? 한편 우주로 떠나는 친구를 위해 결혼식을 준비하는 괴짜 과학도들. 결실의 계절이 오는 걸까.",
        "poster_path": "/l08Z8ihAsTRPEuOehbwk4axg3cu.jpg",
        "season_number": 5
    },
    {
        "air_date": "2012-09-27",
        "episode_count": 24,
        "id": 3737,
        "name": "시즌 6",
        "overview": "사랑하면 닮아간다고 했던가? 금발 미녀 페니도 드디어 과학에 눈을 뜬다. 이제 이 천재 친구들만 빨리 사랑에 눈을 뜨면 좋을 텐데. 이성을 알아간다는 건 정말 어려운 일. 과학적으로 해결할 수 없는 미지의 영역에 그들이 있다.",
        "poster_path": "/2Rsb94mlt4OHhiO2UWatDOhnBqv.jpg",
        "season_number": 6
    },
    {
        "air_date": "2013-09-26",
        "episode_count": 24,
        "id": 3739,
        "name": "시즌 7",
        "overview": "사랑도 퀘스트처럼 임무를 완수하면 이루어질까? 미션 수행 게임에 임하는 괴짜 친구들. 게임이 계속될수록 최악의 결과를 향해 달려간다. 이론은 A+, 실전은 F. 철부지 과학도들의 고군분투 연애기.",
        "poster_path": "/j1FU0qKHx1F8FVBmK5DBOTrhsAr.jpg",
        "season_number": 7
    },
    {
        "air_date": "2014-09-22",
        "episode_count": 24,
        "id": 62016,
        "name": "시즌 8",
        "overview": "생각대로 되지 않는 것이 인생이다. 금발 미녀 페니는 연기를 포기하고 새로운 직업을 구한다. 기차를 타고 떠나버린 한 친구는 봉변을 당하고 돌아온다. 사랑도 그렇다. 뜻한 대로 된다면 누구나 사랑을 하게?",
        "poster_path": "/ltDFOllPbZOIInfdKH18vqztgN4.jpg",
        "season_number": 8
    },
    {
        "air_date": "2015-09-21",
        "episode_count": 24,
        "id": 70493,
        "name": "시즌 9",
        "overview": "라스베이거스에 도착해 마침내 결혼에 성공한 커플. 서약마저 범상치 않다. 우주가 어쩌고, 원자가 어쩌고. 게다가 결혼식은 인터넷 생중계다. 하지만 이게 웬일? 결혼식을 지켜보던 다른 커플이 깨질 위기. 아, 사랑 어렵다 어려워.",
        "poster_path": "/9CEQT1MPDsA0dfR4VeQYUUPvV6g.jpg",
        "season_number": 9
    },
    {
        "air_date": "2016-09-19",
        "episode_count": 24,
        "id": 80035,
        "name": "시즌 10",
        "overview": "마치 계절이 바뀌듯이, 연애하고 결혼하고 출산하며 권태기도 맞는 우리. 괴짜 천재들은 지금 어느 계절에 와 있을까? 각자 처한 상황이 다르더라도 한 가지는 분명하다. 아직 가본 적 없는 미지의 영역을 향하고 있다는 것.",
        "poster_path": "/hBiGEmm9z5xx4r9l8illHcEeRYA.jpg",
        "season_number": 10
    },
    {
        "air_date": "2017-09-25",
        "episode_count": 24,
        "id": 91000,
        "name": "시즌 11",
        "overview": "사랑은 아직 끝나지 않았다. 마침내 돌아오다! 괴짜 천재들과 주변인들의 사랑 찾기 대장정. 크고 작은 사건에 얽히고설키면서 펼쳐지는 또 다른 세상. 우주가 지금도 팽창하는 것처럼 그들의 사랑도 더 크게 자라고 있다.",
        "poster_path": "/9CNrMasILLVbu61P7oLtwRAMMG5.jpg",
        "season_number": 11
    },
    {
        "air_date": "2018-09-24",
        "episode_count": 24,
        "id": 107083,
        "name": "시즌 12",
        "overview": "",
        "poster_path": "/oTXONRjYLMy6fvqTzRnpsif4yf2.jpg",
        "season_number": 12
    }
    ],
    "spoken_languages": [
    {
        "english_name": "English",
        "iso_639_1": "en",
        "name": "English"
    }
    ],
    "status": "Ended",
    "tagline": "",
    "type": "Scripted",
    "vote_average": 7.879,
    "vote_count": 10019,
    "credits": {
    "cast": [
        {
        "adult": false,
        "gender": 2,
        "id": 5374,
        "known_for_department": "Acting",
        "name": "Jim Parsons",
        "original_name": "Jim Parsons",
        "popularity": 12.705,
        "profile_path": "/sa05slVgacuXe94UFnQs4rfqZL4.jpg",
        "character": "Sheldon Cooper",
        "credit_id": "5256d00319c2956ff60a3984",
        "order": 0
        },
        {
        "adult": false,
        "gender": 2,
        "id": 16478,
        "known_for_department": "Acting",
        "name": "Johnny Galecki",
        "original_name": "Johnny Galecki",
        "popularity": 10.499,
        "profile_path": "/kwMOVJvWDkiXEuKiyNJMaoFnhkj.jpg",
        "character": "Leonard Hofstadter",
        "credit_id": "5256d00319c2956ff60a393e",
        "order": 1
        },
        {
        "adult": false,
        "gender": 1,
        "id": 53862,
        "known_for_department": "Acting",
        "name": "Kaley Cuoco",
        "original_name": "Kaley Cuoco",
        "popularity": 18.56,
        "profile_path": "/c01Ma8Jrr2OJ6uoikPwDK34Y8eK.jpg",
        "character": "Penny",
        "credit_id": "5256d00419c2956ff60a39d8",
        "order": 2
        },
        {
        "adult": false,
        "gender": 2,
        "id": 53863,
        "known_for_department": "Acting",
        "name": "Simon Helberg",
        "original_name": "Simon Helberg",
        "popularity": 22.235,
        "profile_path": "/5fJgJzuikAYhIBCmT0PO57dVzD4.jpg",
        "character": "Howard Wolowitz",
        "credit_id": "5256d00419c2956ff60a3a1e",
        "order": 3
        },
        {
        "adult": false,
        "gender": 2,
        "id": 208099,
        "known_for_department": "Acting",
        "name": "Kunal Nayyar",
        "original_name": "Kunal Nayyar",
        "popularity": 17.494,
        "profile_path": "/8W16ABvzYBvMp9xMUV5FvM3QV8e.jpg",
        "character": "Rajesh Koothrappali",
        "credit_id": "5259c359760ee34460064936",
        "order": 4
        },
        {
        "adult": false,
        "gender": 1,
        "id": 1221716,
        "known_for_department": "Acting",
        "name": "Melissa Rauch",
        "original_name": "Melissa Rauch",
        "popularity": 13.686,
        "profile_path": "/pYcQdUodRdZLpDM2FA0LhW5KhkF.jpg",
        "character": "Bernadette Rostenkowski",
        "credit_id": "52714c5019c2952aba11a83b",
        "order": 5
        },
        {
        "adult": false,
        "gender": 1,
        "id": 167640,
        "known_for_department": "Acting",
        "name": "Mayim Bialik",
        "original_name": "Mayim Bialik",
        "popularity": 11.123,
        "profile_path": "/2wOA6gMuMojNih3Sh5KNTdmOxPq.jpg",
        "character": "Amy Farrah Fowler",
        "credit_id": "5256d00519c2956ff60a3b02",
        "order": 6
        }
    ],
    "crew": [
        {
        "adult": false,
        "gender": 2,
        "id": 1379356,
        "known_for_department": "Writing",
        "name": "Jeremy Howe",
        "original_name": "Jeremy Howe",
        "popularity": 1.26,
        "profile_path": "/iCX9ywvdxOsYHfx4aPMm3f6acpr.jpg",
        "credit_id": "5bbb9406c3a36858f5001c04",
        "department": "Production",
        "job": "Co-Executive Producer"
        },
        {
        "adult": false,
        "gender": 1,
        "id": 581616,
        "known_for_department": "Writing",
        "name": "Tara Hernandez",
        "original_name": "Tara Hernandez",
        "popularity": 2.808,
        "profile_path": "/yHGB8rxK4Py5wdWAIpvrCowkRal.jpg",
        "credit_id": "5bbb9ec49251413793002bd0",
        "department": "Production",
        "job": "Co-Executive Producer"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 1480277,
        "known_for_department": "Writing",
        "name": "Anthony Del Broccolo",
        "original_name": "Anthony Del Broccolo",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "5bbb9bb10e0a26661e0028a8",
        "department": "Production",
        "job": "Co-Executive Producer"
        },
        {
        "adult": false,
        "gender": 1,
        "id": 2153496,
        "known_for_department": "Production",
        "name": "Shannon Timberlake",
        "original_name": "Shannon Timberlake",
        "popularity": 1.532,
        "profile_path": "/7Sh0Eh0atqehjes6ygjVPZr8EC3.jpg",
        "credit_id": "5bc8692f0e0a263635014b75",
        "department": "Production",
        "job": "Production Coordinator"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 2153483,
        "known_for_department": "Camera",
        "name": "Jamie Hitchcock",
        "original_name": "Jamie Hitchcock",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "5bda2fc1c3a3680765000c07",
        "department": "Camera",
        "job": "Camera Operator"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 2153471,
        "known_for_department": "Art",
        "name": "Rick Puccio",
        "original_name": "Rick Puccio",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "5bda2fef0e0a2603ca0009d4",
        "department": "Art",
        "job": "Construction Coordinator"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1481429,
        "known_for_department": "Writing",
        "name": "Adam Faberman",
        "original_name": "Adam Faberman",
        "popularity": 0.98,
        "profile_path": null,
        "credit_id": "5bda2f2d92514153fd000868",
        "department": "Writing",
        "job": "Executive Story Editor"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 2153480,
        "known_for_department": "Camera",
        "name": "John DeChene",
        "original_name": "John DeChene",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "5bda2f4b925141540b0009d2",
        "department": "Camera",
        "job": "Camera Operator"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 2153491,
        "known_for_department": "Camera",
        "name": "Richard Price",
        "original_name": "Richard Price",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "5bda2f8c0e0a2603bf00094c",
        "department": "Camera",
        "job": "Camera Operator"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1565164,
        "known_for_department": "Camera",
        "name": "Brian W. Armstrong",
        "original_name": "Brian W. Armstrong",
        "popularity": 1.4,
        "profile_path": null,
        "credit_id": "5bda2fd8c3a368078f0008f9",
        "department": "Camera",
        "job": "Camera Operator"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 2126618,
        "known_for_department": "Crew",
        "name": "Alexandra Barbone",
        "original_name": "Alexandra Barbone",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "5b98ff1ec3a36802e900bbd2",
        "department": "Crew",
        "job": "Post Production Supervisor"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 1217296,
        "known_for_department": "Writing",
        "name": "Andy Gordon",
        "original_name": "Andy Gordon",
        "popularity": 0.98,
        "profile_path": null,
        "credit_id": "5b9866c70e0a263db2001e30",
        "department": "Production",
        "job": "Co-Executive Producer"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 2126695,
        "known_for_department": "Camera",
        "name": "David Pearce",
        "original_name": "David Pearce",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "5b9927adc3a36802e200e49e",
        "department": "Camera",
        "job": "Key Grip"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1553601,
        "known_for_department": "Production",
        "name": "Tara Treacy",
        "original_name": "Tara Treacy",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "5802abc69251413ecc0002c0",
        "department": "Production",
        "job": "Casting"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 1480275,
        "known_for_department": "Production",
        "name": "Robinson Green",
        "original_name": "Robinson Green",
        "popularity": 1.38,
        "profile_path": null,
        "credit_id": "567daf279251417ddd007ea6",
        "department": "Production",
        "job": "Producer"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1480266,
        "known_for_department": "Production",
        "name": "Ryan Berdan",
        "original_name": "Ryan Berdan",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "567db4bf92514132db0054e9",
        "department": "Production",
        "job": "Co-Producer"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 1553595,
        "known_for_department": "Production",
        "name": "Charlie Back",
        "original_name": "Charlie Back",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "567db6fbc3a3684bcc00816a",
        "department": "Production",
        "job": "Associate Producer"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 1224140,
        "known_for_department": "Production",
        "name": "Peter Chakos",
        "original_name": "Peter Chakos",
        "popularity": 1.4,
        "profile_path": "/aoyFlwgYbHeWnYbOrcf8fgdek2B.jpg",
        "credit_id": "567da93ac3a3684bd000764f",
        "department": "Production",
        "job": "Co-Executive Producer"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 1480278,
        "known_for_department": "Production",
        "name": "Justin D. Hetzel",
        "original_name": "Justin D. Hetzel",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "567db675c3a3684c1d005979",
        "department": "Production",
        "job": "Co-Producer"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1480302,
        "known_for_department": "Costume & Make-Up",
        "name": "Faye Woods",
        "original_name": "Faye Woods",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "5802ae769251417a330054df",
        "department": "Costume & Make-Up",
        "job": "Hair Department Head"
        },
        {
        "adult": false,
        "gender": 1,
        "id": 1222187,
        "known_for_department": "Production",
        "name": "Maria Ferrari",
        "original_name": "Maria Ferrari",
        "popularity": 1.767,
        "profile_path": "/u7ktJ29oqkAe3Vl85uZI3eOJbKD.jpg",
        "credit_id": "58028c8a9251417a050043f9",
        "department": "Production",
        "job": "Executive Producer"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 1224135,
        "known_for_department": "Writing",
        "name": "David Goetsch",
        "original_name": "David Goetsch",
        "popularity": 0.6,
        "profile_path": "/1woTfUvP7FGl1VLiKM3Z5TFMPPd.jpg",
        "credit_id": "58028c499251417a050043e9",
        "department": "Production",
        "job": "Executive Producer"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 1217231,
        "known_for_department": "Writing",
        "name": "Eric Kaplan",
        "original_name": "Eric Kaplan",
        "popularity": 1.851,
        "profile_path": null,
        "credit_id": "58028c57c3a3687968004338",
        "department": "Production",
        "job": "Executive Producer"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 1224134,
        "known_for_department": "Writing",
        "name": "Steve Holland",
        "original_name": "Steve Holland",
        "popularity": 0.6,
        "profile_path": "/m7FIFJs5ZP2DOSqg7HtLKG0zLvB.jpg",
        "credit_id": "58028c779251415da20051bc",
        "department": "Production",
        "job": "Executive Producer"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1480307,
        "known_for_department": "Costume & Make-Up",
        "name": "Sylvia Surdu",
        "original_name": "Sylvia Surdu",
        "popularity": 1.62,
        "profile_path": null,
        "credit_id": "567dc85bc3a3684c1d005baf",
        "department": "Costume & Make-Up",
        "job": "Key Hair Stylist"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1695056,
        "known_for_department": "Costume & Make-Up",
        "name": "Linda Cowan",
        "original_name": "Linda Cowan",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "58b7f7f59251412732007859",
        "department": "Costume & Make-Up",
        "job": "Key Makeup Artist"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1480306,
        "known_for_department": "Costume & Make-Up",
        "name": "Vikki McCarter",
        "original_name": "Vikki McCarter",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "5802adf7c3a3687597000379",
        "department": "Costume & Make-Up",
        "job": "Makeup Department Head"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 2126718,
        "known_for_department": "Editing",
        "name": "Todd Morris",
        "original_name": "Todd Morris",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "5b992c5f925141725700e1aa",
        "department": "Editing",
        "job": "Assistant Editor"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1480257,
        "known_for_department": "Production",
        "name": "Kristy Cecil",
        "original_name": "Kristy Cecil",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "5588127ac3a368385300663b",
        "department": "Production",
        "job": "Producer"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 1480275,
        "known_for_department": "Production",
        "name": "Robinson Green",
        "original_name": "Robinson Green",
        "popularity": 1.38,
        "profile_path": null,
        "credit_id": "567db93b9251417ddd007f96",
        "department": "Production",
        "job": "Unit Production Manager"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 1224133,
        "known_for_department": "Writing",
        "name": "Steven Molaro",
        "original_name": "Steven Molaro",
        "popularity": 2.051,
        "profile_path": "/2NZtxlNz5IWS1XoC0MdeBdkUZ5l.jpg",
        "credit_id": "5256d01319c2956ff60a40fa",
        "department": "Production",
        "job": "Executive Producer"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 1480298,
        "known_for_department": "Art",
        "name": "Francoise Cherry-Cohen",
        "original_name": "Francoise Cherry-Cohen",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "55881bca9251417f6f0078e5",
        "department": "Art",
        "job": "Art Direction"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1695062,
        "known_for_department": "Lighting",
        "name": "John Greene",
        "original_name": "John Greene",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "5802af41c3a3687968005146",
        "department": "Lighting",
        "job": "Gaffer"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1480256,
        "known_for_department": "Production",
        "name": "Mary T. Quigley",
        "original_name": "Mary T. Quigley",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "558811b2c3a368385300662c",
        "department": "Production",
        "job": "Co-Producer"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1480312,
        "known_for_department": "Crew",
        "name": "Scott L. London",
        "original_name": "Scott L. London",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "55881e1a9251415aa9000d2a",
        "department": "Crew",
        "job": "Property Master"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1480314,
        "known_for_department": "Sound",
        "name": "Charlie McDaniel",
        "original_name": "Charlie McDaniel",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "55881e839251411e8d006cac",
        "department": "Sound",
        "job": "Sound Re-Recording Mixer"
        },
        {
        "adult": false,
        "gender": 1,
        "id": 1480294,
        "known_for_department": "Production",
        "name": "Nikki Valko",
        "original_name": "Nikki Valko",
        "popularity": 3.076,
        "profile_path": null,
        "credit_id": "55881b3a9251411dec006e88",
        "department": "Production",
        "job": "Casting"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 1335451,
        "known_for_department": "Art",
        "name": "John Shaffner",
        "original_name": "John Shaffner",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "55881ba2c3a36837e9006695",
        "department": "Art",
        "job": "Production Design"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1480313,
        "known_for_department": "Sound",
        "name": "Bob La Masney",
        "original_name": "Bob La Masney",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "55881e3fc3a3683365006705",
        "department": "Sound",
        "job": "Sound Re-Recording Mixer"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1480300,
        "known_for_department": "Art",
        "name": "Ann Shea",
        "original_name": "Ann Shea",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "55881c15c3a368273b007766",
        "department": "Art",
        "job": "Set Decoration"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1480256,
        "known_for_department": "Production",
        "name": "Mary T. Quigley",
        "original_name": "Mary T. Quigley",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "55881c24c3a368274c007263",
        "department": "Costume & Make-Up",
        "job": "Costume Design"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 1224140,
        "known_for_department": "Production",
        "name": "Peter Chakos",
        "original_name": "Peter Chakos",
        "popularity": 1.4,
        "profile_path": "/aoyFlwgYbHeWnYbOrcf8fgdek2B.jpg",
        "credit_id": "55881ab9c3a3683365006669",
        "department": "Editing",
        "job": "Editor"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 1480292,
        "known_for_department": "Camera",
        "name": "Steven V. Silver",
        "original_name": "Steven V. Silver",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "567db8059251417ddf007ddc",
        "department": "Camera",
        "job": "Director of Photography"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1553604,
        "known_for_department": "Directing",
        "name": "Julie Fleischer",
        "original_name": "Julie Fleischer",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "567dc8c5c3a3684be3007edc",
        "department": "Directing",
        "job": "Script Supervisor"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1480293,
        "known_for_department": "Production",
        "name": "Ken Miller",
        "original_name": "Ken Miller",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "55881aee9251415aa9000c86",
        "department": "Production",
        "job": "Casting"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 163528,
        "known_for_department": "Writing",
        "name": "Bill Prady",
        "original_name": "Bill Prady",
        "popularity": 1.994,
        "profile_path": null,
        "credit_id": "5256d01319c2956ff60a4046",
        "department": "Production",
        "job": "Executive Producer"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 160172,
        "known_for_department": "Writing",
        "name": "Chuck Lorre",
        "original_name": "Chuck Lorre",
        "popularity": 9.776,
        "profile_path": "/8OTRD3d6N0GKy1Z0LJaWZ3MVxXr.jpg",
        "credit_id": "5256d01319c2956ff60a4082",
        "department": "Production",
        "job": "Executive Producer"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 1480315,
        "known_for_department": "Sound",
        "name": "Bruce Peters",
        "original_name": "Bruce Peters",
        "popularity": 0.652,
        "profile_path": null,
        "credit_id": "5802b0199251413ecc0004b6",
        "department": "Sound",
        "job": "Production Sound Mixer"
        },
        {
        "adult": false,
        "gender": 0,
        "id": 154607,
        "known_for_department": "Acting",
        "name": "Barenaked Ladies",
        "original_name": "Barenaked Ladies",
        "popularity": 0.6,
        "profile_path": null,
        "credit_id": "58b7f7c5c3a368352e006c3b",
        "department": "Sound",
        "job": "Theme Song Performance"
        },
        {
        "adult": false,
        "gender": 2,
        "id": 1483755,
        "known_for_department": "Writing",
        "name": "David Saltzberg",
        "original_name": "David Saltzberg",
        "popularity": 0.715,
        "profile_path": "/fUZLZjeLoHGJj2WtoeT6o8enlP4.jpg",
        "credit_id": "5ba130a9c3a3687118028861",
        "department": "Crew",
        "job": "Scientific Consultant"
        }
    ]
    }
}
```
    

### 추출해서 사용할 데이터(TV)

```graphql
[TV 프로그램 정보]
name (작품 이름)
original_name (원제)
original_language (원어)
genres (장르)
tagline (간단소개)
overview (개요)
poster_path (포스터 이미지)
production_countries (제작 국가)
certifications (시청등급)

first_air_date (최초 방영일)
last_air_date (마지막 방영일)
networks (방송사)
number_of_episodes (에피소드 개수)
number_of_seasons (시즌 개수)

[창작자 정보]
created_by
	id (인물 아이디)
	name (이름)
	gender (성별)
	profile_path (프로필 사진)

[시즌]
seasons

id (시즌 아이디)
air_date (방영일)
episode_count (에피소드 개수)
overview (개요)
poster_path (포스터 이미지)
season_number (시즌 넘버링, 0인 경우 스페셜 같은 예외 사항)

[감독 및 배우]
known_for_department (역할) : Acting(배우), Directing(감독)
id (인물 id, PEOPLE API 통해서 검색 가능)
name (이름)
gender (성별) : 1이 여자, 2가 남자
character (배역명, 배우인 경우에만)
profile_path (프로필 사진)
```

TV 프로그램은 영화와 다른 점이 몇 가지 있다. 여러 번에 걸쳐 방영되기 때문에 개봉일이 아닌 최초 방영일, 마지막 방영일 정보가 있고, 방송사와 에피소드, 시즌 개수 등의 정보도 가지고 있다. 또한 credits의 감독과는 별개로 created_by에 창작자, 작가 또는 PD 포지션의 인물 데이터가 존재한다.

시즌 정보도 있는데, 간략한 정보와 시즌 넘버링 정보를 가지고 있다. 따로 명시되어 있지는 않지만 season_number가 0인 경우 스페셜 같은 것에 해당하는 것 같다.

클라이언트와 이야기해야 할 내용

데이터 변경 및 UI 수정 필요성

방영사 데이터 보여주기

영화 시리즈나 배우 상세 정보도 보여줄 것인가?

한 달 / 전체선택

[API 사용 예시](https://www.notion.so/API-12ff10982804460daf9bcf81e730e680?pvs=21)
