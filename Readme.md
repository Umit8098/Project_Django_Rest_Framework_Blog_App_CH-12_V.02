<!-- Please update value in the {}  -->

<h1 align="center">Project_Django_Rest_Framework_Blog_App</h1>

<p align="center">🚀 Kullanıcıların blog oluşturmasına, yorum yapmasına ve diğer kullanıcılarla etkileşim kurmasına olanak tanıyan bir API 🚀</p>

<!-- <div align="center">
  <h3>
    <a href="https://umit8114.pythonanywhere.com/">
      Demo
    </a>
     | 
    <a href="https://umit8114.pythonanywhere.com/">
      Project
    </a>
 
  </h3>
</div> -->

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Table of Contents](#table-of-contents)
- [API Endpoints](#api-endpoints)
  - [User/Authentication Endpoints:](#userauthentication-endpoints)
  - [Blog Endpoints:](#blog-endpoints)
  - [Comment Endpoints:](#comment-endpoints)
- [API Testing](#api-testing)
- [Overview](#overview)
  - [Kullanıcı Doğrulama Testi](#kullanıcı-doğrulama-testi)
  - [Blog CRUD Testi](#blog-crud-testi)
- [Built With](#built-with)
- [How To Use](#how-to-use)
  - [Örnek Kullanım](#örnek-kullanım)
- [About This Project](#about-this-project)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)


## API Endpoints

Bu API aşağıdaki endpoint'leri sağlar:

### User/Authentication Endpoints:
- `POST https://umit8114.pythonanywhere.com/users/register/` - Yeni kullanıcı kaydı
- `POST https://umit8114.pythonanywhere.com/users/auth/login/` - Kullanıcı girişi
- `POST https://umit8114.pythonanywhere.com/users/auth/logout/` - Kullanıcı çıkışı

### Blog Endpoints:
- `GET https://umit8114.pythonanywhere.com/blog/posts/` - Tüm blogları listele
- `POST https://umit8114.pythonanywhere.com/blog/posts/` - Yeni bir blog oluştur
- `GET https://umit8114.pythonanywhere.com/blog/posts/14/` - Belirli bir blog detayları
- `PUT https://umit8114.pythonanywhere.com/blog/posts/14/` - Blog güncelleme
- `DELETE https://umit8114.pythonanywhere.com/blog/posts/16/` - Blog silme

### Comment Endpoints:
- `GET https://umit8114.pythonanywhere.com/blog/comments/` - Blog yorumlarını listele
- `POST https://umit8114.pythonanywhere.com/blog/comments/` - Yeni bir yorum ekle


## API Testing

Postman Collection, API'nizin her bir endpoint'ini test etmek için gerekli istekleri içerir. API'nin işlevselliğini hızlı bir şekilde anlamak için kullanabilirsiniz.

API'leri Postman üzerinden test etmek için aşağıdaki adımları izleyebilirsiniz:

1. Postman'i yükleyin (eğer yüklü değilse): [Postman İndir](https://www.postman.com/downloads/).
2. Bu [Postman Collection](https://umit-dev.postman.co/workspace/Team-Workspace~7e9925db-bf34-4ab9-802e-6deb333b7a46/collection/17531143-00b58f75-ce21-4f00-9e94-24eaec4d32b0?action=share&creator=17531143) indirin ve içe aktarın.
3. API'leri Postman üzerinden test etmeye başlayın.

**Postman Collection Linki:**  
[Blog App API Postman Collection](https://umit-dev.postman.co/workspace/Team-Workspace~7e9925db-bf34-4ab9-802e-6deb333b7a46/collection/17531143-00b58f75-ce21-4f00-9e94-24eaec4d32b0?action=share&creator=17531143)


## Overview

Blog API uygulaması, kullanıcıların blog oluşturmasına, yorum yapmasına ve diğer kullanıcılarla etkileşim kurmasına olanak tanır. Bu uygulama şunları sağlar:
- Kullanıcı doğrulama ve yetkilendirme
- Blog CRUD işlemleri
- Yorum yapma ve beğeni ekleme
- Hiyerarşik veri modeli için drf-nested-routers kullanımı

### Kullanıcı Doğrulama Testi
<!-- ![screenshot](project_screenshot/Blog_App_RF_CH-12_V.02-1.gif) -->
<img src="project_screenshot/Blog_App_RF_CH-12_V.02-1.gif" alt="User/Authentication Test" width="400"/>
➡ *Kullanıcı doğrulama işlemleri için Postman üzerinde yapılan test sürecini görebilirsiniz.*

---

### Blog CRUD Testi
<!-- ![screenshot](project_screenshot/Blog_App_RF_CH-12_V.02-2.gif) -->
<img src="project_screenshot/Blog_App_RF_CH-12_V.02-2.gif" alt="Blog CRUD Test" width="400"/>
➡ *Blog API'si üzerindeki CRUD işlemlerini Postman ile test etme.*

## Built With

<!-- This section should list any major frameworks that you built your project using. Here are a few examples.-->

Bu proje aşağıdaki araçlar ve kütüphanelerle inşa edilmiştir:
- [Django Rest Framework](https://www.django-rest-framework.org/) - Güçlü bir REST API framework'ü.
- [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/) - Kullanıcı yetkilendirme modülü.
- [drf-nested-routers](https://github.com/alanjds/drf-nested-routers) - Hiyerarşik routing için.


## How To Use

<!-- This is an example, please update according to your application -->

To clone and run this application, you'll need [Git](https://github.com/Umit8098/Project_Django_Rest_Framework_Blog_App_CH-12_V.02.git) 

When installing the required packages in the requirements.txt file, review the package differences for windows/macOS/Linux environments. 

Complete the installation by uncommenting the appropriate package.

---

requirements.txt dosyasındaki gerekli paketlerin kurulumu esnasında windows/macOS/Linux ortamları için paket farklılıklarını inceleyin. 

Uygun olan paketi yorumdan kurtararak kurulumu gerçekleştirin. 

```bash
# Clone this repository
$ git clone https://github.com/Umit8098/Project_Django_Rest_Framework_Blog_App_CH-12_V.02.git

# Install dependencies
    $ python -m venv env
    $ python3 -m venv env (for macOs/linux OS)
    $ env/Scripts/activate (for win OS)
    $ source env/bin/activate (for macOs/linux OS)
    $ pip install -r requirements.txt
    $ python manage.py migrate (for win OS)
    $ python3 manage.py migrate (for macOs/linux OS)

# Create and Edit .env
# Add Your SECRET_KEY in .env file

"""
# example .env;

SECRET_KEY =123456789abcdefg...

"""

# Run the app
    $ python manage.py runserver
```

### Örnek Kullanım

1. **Login Request:**
   - URL: `https://umit8114.pythonanywhere.com/users/auth/login/`
   - Method: `POST`
   - Body (JSON):
```json
  {
  "email": "umit@gmail.com",
  "password": "umit123456"
  }
```

2. **Blog Oluşturma:**
   - URL: `https://umit8114.pythonanywhere.com/blog/posts/`
   - Method: `POST`
   - Headers:
  
```text
  Authorization: Token <login olunduğunda dönen token key>
```
- 
   - Body (JSON):

```json
  {
  "title": "fifth Post",
  "content": "Second Content",
  "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Sport_balls.svg/400px-Sport_balls.svg.png",
  "is_published": true 
  }
```


## About This Project
- This is an API service for a blog application built with Django Rest Framework.
- Users can register, write blogs, comment on blogs and like them.

<hr>

- Bu, Django Rest Framework ile oluşturulmuş bir blog uygulamasının API servisidir.
- Kullanıcılar kayıt olup, blog yazabilir, yazılan bloglara yorum yapabilir, beğeni yapabilirler.

## Acknowledgements
- [Django Rest Framework](https://www.django-rest-framework.org/) - REST API oluşturmak için kullanılan framework.
- [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/) - Kullanıcı doğrulama için kullanıldı.
- [Routers](https://github.com/alanjds/drf-nested-routers) - Hiyerarşik veri modeli için kullanıldı.

## Contact

<!-- - Website [your-website.com](https://{your-web-site-link}) -->
- GitHub [@Umit8098](https://github.com/Umit8098)

- Linkedin [@umit-arat](https://linkedin.com/in/umit-arat/)
<!-- - Twitter [@your-twitter](https://{twitter.com/your-username}) -->
