# 장고 챌린지
### 영화 리뷰 사이트

  - 환경설정
```sh
$ pip install pipenv
```
```sh
$ pip uninstall virtualenv
```
```sh
$ pip uninstall pipenv
```
```sh
$ pipenv --three
```
```sh
$ pipenv shell
```
```sh
$ pipenv install Django==2.2.5
```
```sh
$ pipenv install black --dev --pre
```
```sh
$ pipenv install flake8 --dev --pre
```
[ Precautions : 만약 설치 중에 Locking Failed! 에러가 뜨면 "pipenv lock --pre --clear" 명령어 치고 다시 설치 ]
```sh
$ python extension 설치
```
```sh
$ VSC reload
```

  - 시작
```sh
$ django-admin startproject config
```
config폴더 이름을 Aconfig 바꿈 

Aconfig 폴더속 config폴더랑 manage.py 밖으로 빼고 Aconfig 삭제

```sh
$ touch README.md
```
```sh
$ touch .gitignore
```
```sh
$ django-admin startapp 모델명
```
```sh
$ python manage.py makemigrations
```
```sh
$ python manage.py migrate
```
```sh
$ python manage.py createsuperuser
```
```sh
$ python manage.py runserver
```
[ 종료 : ctrl + C]
