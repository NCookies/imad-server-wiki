import re
import sys
import base64

import requests

import github_auth


# GitHub API 엔드포인트 및 파일 정보
auth = github_auth.github_user_info

# 마크다운 파일 경로 및 코드 블록 패턴
original_file_path = './dto_class_original.md'
markdown_file_path = './DTO-클래스-명세.md'

# 파일 내용을 가져오는 함수
def get_file_content(file_path):
    headers = {'Authorization': f'token {auth["access_token"]}'}
    url = f'https://api.github.com/repos/{auth["repo_owner"]}/{auth["repo_name"]}/contents/{file_path}?ref={auth["branch"]}'

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
    new_markdown_content = ""

    # 마크다운 파일 열기
    with open(original_file_path, "r", encoding="utf-8") as original_file:

        lines = original_file.readlines()
        for line in lines:
            if line.startswith("### "):
                new_markdown_content += line
            elif line.startswith("## "):
                new_markdown_content += "---" + "\n"
                new_markdown_content += line + "\n"
            elif line.startswith(">/"):
                new_markdown_content += "```java\n"
                new_markdown_content += str(get_file_content(line[2:-1]))
                new_markdown_content += "```\n\n"

    with open(markdown_file_path, "w", encoding="utf-8") as markdown_file:
        markdown_file.write(new_markdown_content)


if __name__ == "__main__":
    main()
