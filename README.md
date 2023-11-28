# Prj: Website quản lý cửa hàng sách
Dự án quản lý cửa hàng sách:
+ Cho khách hàng mua sách qua web
+ Cho nhân viên cửa hàng thực hiện các công việc trong cửa hàng

## Các thư viện và môi trường sử dụng
Package             Version
------------------- ------------
asgiref             3.7.2       
distlib             0.3.7       
Django              4.2.7       
djangorestframework 3.14.0      
filelock            3.13.1      
Pillow              10.1.0      
pip                 23.3.1      
platformdirs        3.11.0      
pytz                2023.3.post1
sqlparse            0.4.4       
tzdata              2023.3      
virtualenv          20.24.6     


## Chuẩn bị 
1. ```$ git clone https://github.com/xltsun10/MyWeb```
2. ```$ venv/Scripts/activate```
3. Hoàn thành: Thấy môi trường ảo được kích hoạt => Có thể thao tác bình thường

## Thông tin cấu hình
1. Các thư viện được cài đặt: Trong file requirement.txt
    Để cài đặt các thư viện có trong file requirements.txt, chạy
        câu lệnh: ```$ pip install -r requirements.txt```
2. DB dùng sẽ là SQLite - có sẵn trong django (tải extension để xem file "db.sqlite3" trên vscode)
3. Đổi cổng mặc định của django(nếu lỗi inuse port): Thêm số cổng sau câu lệnh 1.
        ```$ py manage.py runserver <port>```
        vd: ```$ py manage.py runserver 8080```

## Các câu lệnh thường dùng (có một số máy cần viết rõ là python)
1. ```$ py manage.py runserver```
2. ```$ py manage.py makemigrations``` (Chuyển code thành các câu lệnh sql)
3. ```$ py manage.py migrate``` (Thực thi các câu lệnh sql trên)

## Tài khoản để test:
1 Tài khoản admin đăng nhập http://127.0.0.1:8000/admin/ : admin|141010
2. User:nhat002|Nhat1234@ hoặc đăng kí tài khoản mới để sử dụng



## Cấu trúc prj
1. **venv/**: Môi trường ảo để  project chạy
2. **requirements.txt**: Thông tin các gói thư viện được cài đặt trong venv
3. **home/**: app chính của prj - nơi điều hướng/cài đặt các thứ liên quan 
4. **main/templates/**: Nơi để chung các component xác định sẽ được dùng 
5. ... 

