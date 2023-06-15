# potal_service_project(Spleeter)

![OIG eJup4](https://github.com/NAMUORI00/potal_service_project/assets/46620366/348ddb28-01be-4bbd-903c-63313b6ed218)

프로젝트는 시작 목적은 개발연습, 대학 과제용으로 시작된 AI API 서비스 프로젝트입니다.
롤 모델은 [LALAL.ai](https://www.lalal.ai/) 라는 음원분리 AI 서비스를 참고하고 만들었습니다.


## 프로젝트 소개

본 프로젝트는 Spleeter와 FastAPI 프레임워크를 사용하여 음원 분리 기능을 웹과 API로 구현한 프로젝트입니다.

- [Spleeter Web UI](https://github.com/NAMUORI00/potal_service_project/blob/main/Spring/README.md) : Python 라이브러리인 Spleeter를 이용하여 음악 파일에서 소리를 분리하는 기능을 웹에서 사용할 수 있도록 구현하였습니다. 사용자는 웹 페이지에서 음악 파일을 업로드하고, 분리하고자 하는 소리를 선택하여 분리 결과를 다운로드 받을 수 있습니다.

- [Portal Service API](https://github.com/NAMUORI00/potal_service_project/blob/main/API/README.md) : FastAPI 프레임워크를 사용하여 음원 분리 API를 구현한 예시입니다. `/audio` API 엔드포인트를 통해 음원 파일을 업로드하고, Spleeter를 사용하여 분리된 음원을 생성합니다. 분리된 음원은 `/output` API 엔드포인트를 통해 다운로드할 수 있습니다.

모든 코드는 각각의 프로젝트에 대한 README.md에 작성되어 있으며, 각 프로젝트의 개발 환경과 설치/실행 방법이 자세히 설명되어 있습니다.


## 프로젝트 작동영상
https://user-images.githubusercontent.com/46620366/246123423-43fdbebd-e9bf-4fe4-9b8f-673d8dbb8dca.mp4

모든 코드는 각각의 프로젝트에 대한 README.md에 작성되어 있으며, 각 프로젝트의 개발 환경과 설치/실행 방법이 자세히 설명되어 있습니다.

## TO-DO, 짧은말

- 기존에는 AWS 람다를 이용해 서버리스 형식으로 배포를 목적, 제작하려 했으나, 시간의 부족으로 로컬환경에서 작동이 되도록 서비스를 만들었습니다.
- 자바 로그인, 회원가입, 권한 인증부분은 SPRING SECURITY를 이용하여 구현하였습니다. 이 부분에 이해가 아직 부족하여 관리자 페이지를 완성하지 못하였습니다.
- 파이썬 FAST_API 자체에서 CORS 로 API 화이트리스트 제어는 가능하나, 로컬환경기준으로 하여 백엔드 AI API 호출 부분에 인증, 혹은 자바 컨트롤 라우팅 부분에서 백엔드 API 호출을 진행할지 정하여야 할것 같습니다.
- 다만 3번째 경우 AWS 람다, S3버킷을 활용하여 처리하는걸 고려중이기 때문에 백엔드 API 호출 보안은 해결될것으로 보입니다. 
- 최종적으론 클라이언트에서 직접 Back엔드 API를 호출하는게 아닌, 자바스프링 UI 부분에서 호출하면 될것 같습니다
 
