# Leop0ld's Page

AWS S3 Setting 완료

Thumbnail + Image 업로드 
> use django-imagekit

Login + Register
> use LoginView, CreateView

Post
> Model 직접 구현

## AWS 실행 환경

Ubuntu 14.04 LTS

Python 3.4.3

virtualenv + virtualenvwrapper 사용

Nginx+uWSGI 사용해서 배포중

접속 링크: [AWS LINK](http://ec2-52-78-107-140.ap-northeast-2.compute.amazonaws.com)


## 툴

Pycharm Professional version 2016.02 버전 사용


## 실행 방법

```shell
$ git clone https://github.com/Leop0ld/Leopold.git
$ cd Leopold
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py collectstatic
$ python manage.py runserver
```
