Tôi sử dụng môi trường ảo trên một thư mục bất kì (D:\djangoproject)

Đóng gói môi trường này bằng lệnh pip freeze > requirements.txt

Để cài đặt lại môi trường này trên máy của bạn thì dùng lệnh: 
pip install -r requirements.txt

Trong trường hợp bạn làm nhiều project khác nhau với các gói cài đặt khác nhau, môi trường ảo là cách đơn giản nhất để quản lý chúng

Các lệnh tiếp theo tôi dùng để khởi tạo web python: 
django-admin startproject WebBanTS
python manage.py migrate

Các lần vào lại môi trường đã tạo thì chạy activate: 
..\Phucenv\Scripts\activate

Sau đó ta tạo một server ảo cho nó:    http://127.0.0.1:8888
python manage.py runserver 8888

Để tạo tài khoản admin truy cập vào trang web:
python manage.py createsuperuser

Tạo mới app bằng lệnh: 
python manage.py startapp <name of app>   # app

Sau đó vào file settings.py thêm vào tên app vừa tạo:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app'                       # ở đây
]

