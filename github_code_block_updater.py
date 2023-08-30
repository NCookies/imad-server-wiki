import re
import sys
import base64

import requests

import github_auth


# GitHub API 엔드포인트 및 파일 정보
auth = github_auth.github_user_info

# 마크다운 파일 경로 및 코드 블록 패턴
markdown_file_path = './DTO-클래스-명세.md'


# 파일 내용을 가져오는 함수
def get_file_content(file_path):
    headers = {'Authorization': f'token {auth["access_token"]}'}
    url = f'https://api.github.com/repos/{auth["repo_owner"]}/{auth["repo_name"]}/contents/{file_path}?ref={auth["branch"]}'

    print(headers)
    print(url)
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        content_data = response.json()
        content = content_data.get("content", "")  # Base64 인코딩된 내용 가져오기
        decoded_bytes = base64.b64decode(content)  # Base64 디코딩된 bytes
        decoded_content = decoded_bytes.decode("utf-8")  # UTF-8로 디코딩

        return decoded_content
    else:
        print("Failed to retrieve file content:", response.status_code)
        return None


def main():
    new_markdown_content = None

    # 마크다운 파일 열기
    with open(markdown_file_path, "r", encoding="utf-8") as markdown_file:

        # 텍스트 읽어오기
        markdown_content = markdown_file.read()

        # 파일 경로와 코드 블럭을 정규표현식 사용하여 파싱
        file_paths = re.findall(r'> (.+)', markdown_content)
        code_blocks = re.findall(r'```java\n(.+?)```', markdown_content, re.DOTALL)

        # 파싱한 파일경로와 코드블럭의 갯수가 맞지 않으면 에러 발생
        if len(file_paths) != len(code_blocks):
            print("[ERROR] 파일 형식이 올바르지 않거나 파싱 도중 문제가 발생했습니다.")
            sys.exit(1)

        # 코드 블록을 대체할 코드로 변경
        for index, old_code in enumerate(code_blocks):
            new_code = get_file_content(file_paths[index])
            new_markdown_content = markdown_content.replace(old_code, new_code)

    with open(markdown_file_path, "w", encoding="utf-8") as markdown_file:
        markdown_file.write(new_markdown_content)


if __name__ == "__main__":
    main()
