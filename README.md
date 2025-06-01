Movie Management App
Giới thiệu
Movie Management App là một ứng dụng đơn giản và tiện lợi giúp người dùng quản lý danh sách phim và thông tin người dùng. Ứng dụng được phát triển bằng Python với giao diện người dùng thân thiện sử dụng thư viện tkinter. Đây là giải pháp lý tưởng cho các rạp chiếu phim nhỏ hoặc người dùng cá nhân muốn quản lý lịch chiếu phim và thông tin tài khoản.
Ứng dụng hỗ trợ các tính năng chính như:

Quản lý danh sách phim (thêm, sửa, xóa phim).
Quản lý thông tin người dùng (đăng nhập, đăng ký).
Hiển thị thông tin phim với hình ảnh minh họa.

Tính năng

Giao diện đăng nhập: Người dùng có thể đăng nhập với tài khoản đã đăng ký.
Quản lý phim: Thêm, sửa, xóa thông tin phim bao gồm tên phim, ngày chiếu, và hình ảnh poster.
Lưu trữ dữ liệu: Dữ liệu phim và người dùng được lưu trong các file JSON (movies.json, users.json) trong thư mục datas.
Hỗ trợ hình ảnh: Hiển thị hình ảnh phim (upload ảnh từ máy cục bộ lên cloud).
Đóng gói tiện lợi: Ứng dụng được đóng gói thành file .exe duy nhất, dễ dàng cài đặt qua trình cài đặt được tạo bởi Inno Setup.

Yêu cầu hệ thống

Hệ điều hành: Windows 7 trở lên.
Dung lượng: Khoảng 60MB (bao gồm file cài đặt và dữ liệu).
Quyền truy cập: Người dùng không cần quyền quản trị viên để chạy ứng dụng .

Hướng dẫn cài đặt

Tải file cài đặt:

Tải file MovieManagementSetup.exe từ kho lưu trữ hoặc liên hệ nhà phát triển.


Cài đặt:

Chạy file MovieManagementSetup.exe.
Làm theo hướng dẫn trên màn hình để cài đặt vào thư mục mặc định (C:\Program Files\MovieManagementApp).


Chạy ứng dụng:

Sau khi cài đặt, mở ứng dụng từ Start Menu (biểu tượng "Movie Management").
Đăng nhập bằng tài khoản mặc định (nếu có) hoặc đăng ký tài khoản mới.



Hướng dẫn sử dụng

Đăng nhập:

Nhập tên người dùng và mật khẩu để truy cập.
Tài khoản mặc định của admin: admin / admin (nếu chưa thay đổi).


Quản lý phim:

Thêm phim: Nhập thông tin phim.
Sửa/xóa phim: Chọn phim từ danh sách và thực hiện thao tác.


Quản lý người dùng:

Đăng ký tài khoản mới nếu cần.
Dữ liệu người dùng được lưu tự động trongMovieManagementApp\datas.



Cấu trúc dự án
MovieManagementApp/
├── main.py              # File chính của ứng dụng
├── views/               # Thư mục chứa các file giao diện
│   ├── login_user_view.py
│   ├── user_view.py
│   └── ...
├── controllers/               # Thư mục chứa các file logic code
│   ├── movie_controller.py
│   ├── user_controller.py
│   └── ...
├── models/               # Thư mục chứa các file xử lý dữ liệu
│   ├── user_model.py
│   ├── movie_model.py
│   └── ...
├── utils/               # Thư mục chứa các file tiện ích
│   ├── get_api.py
│   ├── send_mail.py
│   └── ...
├── images/              # Thư mục chứa hình ảnh
│   ├── logo.png
│   └── movie.png
├── datas/               # Thư mục lưu file JSON
│   ├── movies.json
│   └── users.json

Công nghệ sử dụng

Ngôn ngữ: Python 3.x
Giao diện: tkinter
Hình ảnh: Pillow (hỗ trợ hiển thị hình ảnh), Cloundinary (Hỗ trợ lưu trữ hình ảnh)
Lưu trữ: File JSON
Đóng gói: PyInstaller (tạo file .exe), Inno Setup (tạo trình cài đặt)
