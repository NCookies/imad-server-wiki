# Spring Security

IMAD 프로젝트의 Spring 서버에서는 세 가지의 커스텀 필터를 사용한다.

## JWT 관련

### JWT 인증 필터
- "/login" 이외의 URI 요청이 왔을 때 처리하는 필터
- 기본적으로 사용자는 요청 헤더에 AccessToken만 담아서 요청한다.
- AccessToken이 만료되었을 때만 RefreshToken을 요청 헤더에 AccessToken과 함께 요청한다.

### JWT 처리
1. RefreshToken이 없고, AccessToken이 유효한 경우 -> 인증 성공 처리, RefreshToken은 재발급하지는 않는다.
2. RefreshToken이 없고, AccessToken이 없거나 유효하지 않은 경우 -> 인증 실패 처리, 403 ERROR
3. RefreshToken이 있는 경우 -> DB에 저장되어 있는 RefreshToken과 비교하여 일치하면 AccessToken과 RefreshToken 재발급(RTR 방식)
