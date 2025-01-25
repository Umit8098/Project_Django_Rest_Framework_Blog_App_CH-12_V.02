<!-- Please update value in the {}  -->

<h1 align="center">Project_Django_Rest_Framework_Blog_App</h1>


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
- [API Testing](#api-testing)
- [Overview](#overview)
  - [Blog Uygulaması Testi:](#blog-uygulaması-testi)
- [Built With](#built-with)
- [How To Use](#how-to-use)
- [About This Project](#about-this-project)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

## API Testing

API'leri Postman üzerinden test etmek için aşağıdaki adımları izleyebilirsiniz:

1. Postman'i yükleyin (eğer yüklü değilse): [Postman İndir](https://www.postman.com/downloads/).
2. Bu [Postman Collection](https://umit-dev.postman.co/workspace/Team-Workspace~7e9925db-bf34-4ab9-802e-6deb333b7a46/collection/17531143-00b58f75-ce21-4f00-9e94-24eaec4d32b0?action=share&creator=17531143) indirin ve içe aktarın.
3. API'leri Postman üzerinden test etmeye başlayın.

**Postman Collection Linki:**  
[Blog App API Postman Collection](https://umit-dev.postman.co/workspace/Team-Workspace~7e9925db-bf34-4ab9-802e-6deb333b7a46/collection/17531143-00b58f75-ce21-4f00-9e94-24eaec4d32b0?action=share&creator=17531143)


## Overview
- User Authentication Test
<!-- ![screenshot](project_screenshot/Blog_App_RF_CH-12_V.02-1.gif) -->
<img src="project_screenshot/Blog_App_RF_CH-12_V.02-1.gif" alt="User/Authentication app testing on Postman" width="400"/>
*Yukarıdaki görselde kullanıcı doğrulama API'si için Postman test sürecini görebilirsiniz.*

---

### Blog Uygulaması Testi:
<!-- ![screenshot](project_screenshot/Blog_App_RF_CH-12_V.02-2.gif) -->
<img src="project_screenshot/Blog_App_RF_CH-12_V.02-2.gif" alt="Blog app testing on Postman" width="400"/>
*Blog API'si için CRUD işlemlerini Postman üzerinde test ederken çekilen görsel.*

## Built With

<!-- This section should list any major frameworks that you built your project using. Here are a few examples.-->

- Djago Rest Framework
- dj-rest-auth
- drf-nested-routers

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

## About This Project
- This is an API service for a blog application built with Django Rest Framework.
- Users can register, write blogs, comment on blogs and like them.

<hr>

- Bu, Django Rest Framework ile oluşturulmuş bir blog uygulamasının API servisidir.
- Kullanıcılar kayıt olup, blog yazabilir, yazılan bloglara yorum yapabilir, beğeni yapabilirler.

## Acknowledgements
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/) - dj-rest-auth
- [Routers](https://github.com/alanjds/drf-nested-routers) - drf-nested-routers

## Contact

<!-- - Website [your-website.com](https://{your-web-site-link}) -->
- GitHub [@Umit8098](https://github.com/Umit8098)

- Linkedin [@umit-arat](https://linkedin.com/in/umit-arat/)
<!-- - Twitter [@your-twitter](https://{twitter.com/your-username}) -->
