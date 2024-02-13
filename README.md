
# Haber Bülteni Api Projesi

Django Rest framework ile Haber Bülteni Api Projesi



## Kurulum

Not: Sol taraftaki veriler Mac kurulumu için sağ taraftaki veriler Windows kurulumu içindir.

Projeyi Kurma  

```bash
  git clone https://github.com/tarikberkay/haberbulteni-api.git
```

Sanal Ortam Oluşturma
```bash
  python3 -m venv venv || python -m venv venv
```

Sanal Ortamı Aktif Etme
```bash
  source venv/bin/activate  ||  venv/scripts/bin/activate
```

Gerekli Paketleri Kurma
```bash
  pip3 install -r requirements.txt  ||  pip install -r requirements.txt
```


Projeyi Çalıştırma
```bash
  python3 manage.py runserver || python manage.py runserver
```

  
## API Kullanımı

#### Öğeyi Getir

```http
  http://127.0.0.1:8000/api/articles/
```

<img src="https://github.com/tarikberkay/haberbulteni-api/blob/main/images/article-list.png" alt="Posts" width="450" height="450">

Tüm Makaleleri getirir.

#### Öğeyi getir

```http
  http://127.0.0.1:8000/api/articles/3
```

<img src="https://github.com/tarikberkay/haberbulteni-api/blob/main/images/article-detail.png" alt="Tags" width="450" height="450">

Makale detayını getirir.

#### Öğeyi getir

```http
  http://127.0.0.1:8000/api/writers/
```

<img src="https://github.com/tarikberkay/haberbulteni-api/blob/main/images/writer-list.png" width="450" height="450">

Yazarları getirir.




  
