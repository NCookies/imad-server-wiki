> 블로그 링크 : https://velog.io/@ncookie/IMAD-API-%EC%A1%B0%EC%82%AC#imdb-api

# 시작하며

지금 진행하고 있는 프로젝트인 `IMAD`는 미디어 작품에 대한 리뷰와 토론 장소를 제공하는 서비스이다. 때문에 영화나 TV 프로그램 등의 정보가 필수인데, 이는 구글이나 네이버에서 파싱하거나 외부 API를 사용해서 정보를 얻어와야 한다. 그래서 국내외의 API들에 대해 조사하고 서비스에서 사용하게 될 API 선택까지 해보았다.

---

# API 후보

## [영화진흥위원회 API](https://www.kobis.or.kr/kobisopenapi/homepg/main/main.do)

- 영화진흥위원회 영화관입장권통합전산망에서 제공하는 오픈 API
- 상업적 이용 가능
- **영화 관련된 정보만 제공**하고 영화 정보 중 감독명, 배우들의 데이터가 없는 경우가 많음. 특히 외국 영화의 경우 더욱 그러한 경향이 있음
- 상세
    - **박스오피스** - 일일박스오피스, 주간/주말 박스오피스
    - **영화정보** - 영화목록, 영화상세정보
    - **영화사정보** - 영화사목록, 영화사상세정보
    - **영화인정보** - 영화인목록, 영화인상세정보

## [네이버 오픈 API - 영화](https://developers.naver.com/docs/serviceapi/search/movie/movie.md)
- 네이버에서 제공하는 오픈 API
- 네이버에서 검색되는 대부분의 작품은 볼 수 있는 것 같음
- 기본적으로 무료 API임. 대신 하루 요청 25,000회로 제한
- 검색 시 작품의 고유 id가 없다는 점이 아쉬움
- **[영화 서비스 API 지원 종료 안내 [23.3.31.예정]](https://developers.naver.com/notice/article/9553)**

## [TMDB API](https://www.themoviedb.org/settings/api)

- 영화, 드라마, 다큐, 애니메이션 등 특정 장르에 국한되지 않고 대부분의 영상물 정보를 찾아볼 수 있음
- 완전한 오픈소스를 추구하며, 위키 형식으로 운영되고 있음
- 기본적으로 오픈 API이지만,  상업적으로 사용하게 될 경우 사이트 측과 상의하여 비용을 지불해야 함
    - [API 이용약관](https://www.themoviedb.org/settings/api/new?type=developer)
    - 위의 이용약관에서 살펴볼 수 있듯이, 광고를 포함하여 상업용 목적의 서비스 개발은 별도로 TMDB 사에 문의하여 API 이용에 대해 문의해야 함
    - **Your site is a "destination" site that uses TMDB content to drive traffic and generate revenue.** - 해당 API를 사용하여 사이트에 트래픽을 **“유도”**한다는 점에서 서비스에 광고를 붙여서 수익을 얻는 것도 상업적 목적으로 분류되는 것 같음

```
A. RULES AND RESTRICTIONS
If the primary purpose of your application is to derive revenue, it is considered a commercial application. TMDB reserves the right to make these evaluations at the time that you apply for the license. TMDB may also monitor your site or application over time to ensure continued compliance with the appropriate type of API key.

If you're in doubt about whether your application is commercial, here are a few common examples of commercial use that may provide you some guidance:

Users are charged a fee for your product or a 3rd party's product or service or a 3rd party's service that includes some sort of integration using the TMDB APIs.
You sell services using TMDb's APIs to bring users' TMDB content into your service.
Your site is a "destination" site that uses TMDB content to drive traffic and generate revenue.
Your site generates revenue by charging users for access to content related to TMDB content such as movies, television shows and music.
```

- 특정 요청 횟수 이상부터는 API 사용 시 요금이 청구됨
- 작품명은 한글화가 되어있지만, 감독명과 배우명, 그리고 배역이름은 **영문**으로 되어 있음
  - TMDB의 로컬라이징 정책에 대해서는 [관련 문서](https://developer.themoviedb.org/docs/languages) 참고
  - TV 프로그램 <오징어 게임> 조회 페이지
  
 ![](https://velog.velcdn.com/images/ncookie/post/b6ecb05d-446d-4604-a656-44aac4772b9e/image.png)


  - 이 부분은 추후 DB에서 수작업으로 한글화시키거나, 구글 검색 결과를 파싱해서 별도로 업데이트 해야할 것으로 보임
  - 그 전까지는 유저에게 아직 한글화 작업 중임을 알리고, 원한다면 해당 정보를 업데이트하게 하는 것도 방법일 듯
  
  
## [IMDB API](https://developer.imdb.com/)

- IMDB는 전 세계 최대 규모의 영화 사이트로, 관련 사이트 중 가장 많은 유저와 데이터를 가지고 있음
- 한글화에 대해서는 미흡한 경우가 많음
  - TV 프로그램 <오징어 게임> 조회 페이지
![](https://velog.velcdn.com/images/ncookie/post/21cc5f9f-5a93-479a-8990-93852c0e0c6a/image.png)

---

# API 선정

## TMDB

위에서 여러 종류의 API에 대해 찾아보고 내용에 대해 나열해보았다. 한글 지원 측면에서 본다면 영화진흥위원회나 네이버가 가장 베스트이다. 하지만 영화진흥위원회는 말 그대로 영화 작품 정보만 제공하고, 네이버는 API가 서비스가 곧 종료된다는 점(조사 시점) 때문에 아쉽게 포기하게 되었다. 새로운 API 출시를 기다리거나 네이버 검색창에서 파싱한다는 선택지도 있을 수 있긴 하지만 손이 너무가서 매력적인 선택지는 아니었다.

그럼 남은건 해외 API 중에서 선택해야 하는데, 로컬라이징(한글화)에 대해서 더 적극적인 `TMDB`를 선택하게 되었다. 

오랜 기간 동안 넷플릭스에서 인기를 누리며 전세계적으로 인지도가 높은 <오징어 게임>을 검색해도, IMDB는 제목만이 한글로 되어있고 나머지 정보는 영어나 불어, 일본어 같이 특정 언어들만 지원한다. 여기에 한글은 포함되어 있지 않다. 반면 TMDB는 영화제목, 장르, 개요 등이 한글로 지원된다. 다른 해외 영화들도 검색해보았는데 국내 개봉 버전의 이름으로 로컬라이징이 잘 되어있었다.

TMDB는 유저가 위키처럼 직접 참여하여 직접 수정할 수 있다는 점 때문에 이러한 차이를 보이는 것 같다. IMDB도 유저가 수정 신청을 할 수 있긴 하지만 별도로 심사를 받아야 한다는 조건 때문에 많이 까다롭다.

최종적으로, 서비스가 안정적으로 쭉 제공될 수 있고 영화 뿐만 아니라 TV 시리즈, 애니메이션 등을 폭 넓게 지원하며, 한글화까지 비교적 잘 되어있는 `TMDB`를 선택하게 되었다.

## 한글화

TMDB 측에서 각국의 로컬라이징에 대해 많은 신경을 쓰고 있다고는 하지만, 여기서 배우명과 배역명(캐릭터 이름)은 제외된다. 이들 또한 지원하기 위해 사이트 측에서 노력하고 있다고는 하지만 당장 기대하기는 힘들 것으로 보인다. 때문에 IMAD 프로젝트에서 서비스를 제공할 때 위의 정보들을 한글로 제공하기 위한 방법에 대해 구상해보았다.

여기서도 <오징어 게임>을 예시로 들어 설명해보자면, 유명한 배우인 `이정재`는 `Lee Jung-jae / Seong Gi-hun / 'No. 456'`로 작성되어 있다. 이를 만약 구글에 검색해본다면 다음과 같은 화면을 볼 수 있다.

![](https://velog.velcdn.com/images/ncookie/post/93bd0842-8ab5-4f92-84ba-7614b0252442/image.png)

![](https://velog.velcdn.com/images/ncookie/post/441efa1f-3a20-466a-9522-e9251f74d519/image.png)

아마 위키 내용을 긁어와서 저렇게 보여주는 것 같은데, IMAD 프로젝트에서는 저 정보를 이용하려고 한다. 구글에 영어로 되어있는 배우명/배역명을 검색하고, 저렇게 한글로 변환된 내용을 파싱할 예정이다. 만약 해당하는 정보가 검색되지 않는다면 영어-한글 표기 변환기나 관련 API를 사용할 것이다. 

---

# 마치며

이렇게 프로젝트에서 사용할 영화, TV 프로그램 등의 작품 API에 대해 조사해보고 선택까지 해보았다. 네이버 API의 지원이 종료되지만 않았다면 정말 좋았을텐데 아쉽게 되었다. 다음에는 TMDB API의 간략한 소개와 사용방법 등에 대해 써보려고 한다.