# doctor

## 프로젝트 기간
3월 16일 ~ 3월 17일

## 소개
csv 로 제공된 데이터를 활용하여 통계 API 구현

## 활용 프레임워크/DB/라이브러리
django
postgreSQL
django-cors-headers
django-postgres-copy
psycopg2

## 데이터 입력 방법 소개
장고의 BaseCommand 클래스의 handle 메서드를 이용하여, DB에 입력 (파일위치 : doctor/data/management/commands/myimportcommand.py)
models.py 를 작성하고 마이그레이션을 완료한 뒤에 명령어 실행
`python3 manage.py myimportcommand`

## 구현
간단한 통계를 제공하는 API 구현
- 환자 통계 
  - 전체 환자 수
  - 성별 환자 수
  - 인종별 환자 수
  - 민족별 환자 수
  - 사망 환자 수

- 방문 통계
  - 방문 유형(입원/외래/응급)별 방문 수
  - 성별 방문 수
  - 인종별 환자 수
  - 민족별 환자 수
  - 출생년도에 따른 환자 수

API 문서 : https://documenter.getpostman.com/view/14022514/Tz5tYFsV

## 개선 필요 사항
- annotate() 와 aggregate() 를 활용해 DB 튜닝 필요

## 클론 시 주의 사항
- csv 파일이 로컬 경로로 되있으니, doctor/data/management/commands/myimportcommand.py 에서 경로 수정 필요 
