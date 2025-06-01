
# 🎬 Movie Management App

## 📖 Giới thiệu

**Movie Management App** là một ứng dụng đơn giản và tiện lợi giúp người dùng quản lý danh sách phim và thông tin người dùng. Ứng dụng được phát triển bằng **Python** với giao diện người dùng thân thiện sử dụng thư viện **Tkinter**. Đây là giải pháp lý tưởng cho các rạp chiếu phim nhỏ hoặc người dùng cá nhân muốn quản lý lịch chiếu phim và tài khoản đăng nhập.

### 🔑 Các tính năng chính:
- Quản lý danh sách phim (thêm, sửa, xóa).
- Quản lý thông tin người dùng (đăng nhập, đăng ký).
- Hiển thị thông tin phim với hình ảnh minh họa (poster).

---

## 🚀 Tính năng chi tiết

- **Giao diện đăng nhập**: Người dùng có thể đăng nhập bằng tài khoản đã đăng ký.
- **Quản lý phim**: Thêm, sửa, xóa thông tin phim như tên phim, ngày chiếu, hình ảnh poster,...
- **Lưu trữ dữ liệu**: Sử dụng file JSON (`movies.json`, `users.json`) trong thư mục `datas`.
- **Hỗ trợ hình ảnh**: Hiển thị hình ảnh phim (poster) với khả năng upload từ máy lên cloud.
- **Đóng gói tiện lợi**: Ứng dụng được đóng gói thành file `.exe` duy nhất, cài đặt dễ dàng bằng **Inno Setup**.

---

## 🖥️ Yêu cầu hệ thống

- **Hệ điều hành**: Windows 7 trở lên.
- **Dung lượng**: Khoảng 60MB (bao gồm trình cài đặt và dữ liệu).
- **Quyền truy cập**: Không yêu cầu quyền quản trị viên.

---

## 📦 Hướng dẫn cài đặt

### 1. Tải file cài đặt
- Tải file `Z+PlusCinema.exe` [Z+PlusCinema](https://github.com/TuanGiangMyDuyen/movie_management/releases/download/v1.5/Z+PlusCinema.exe).

### 2. Cài đặt
- Chạy file `Z+PlusCinema.exe`.
- Làm theo hướng dẫn trên màn hình để cài vào thư mục mặc định:  
  `C:\Program Files\MovieManagementApp`

### 3. Chạy ứng dụng
- Mở ứng dụng từ Start Menu.
- Tạo tài khoản mới để sử dụng.

---

## 🧑‍💻 Hướng dẫn sử dụng

### Đăng nhập
- Nhập tên người dùng và mật khẩu để truy cập.
- **Tài khoản mặc định (admin)**:  
  `Username: admin`  
  `Password: admin`

### Đăng ký tài khoản mới
- Nhấn vào nút **"Đăng ký"** tại giao diện đăng nhập.
- Nhập đầy đủ thông tin người dùng: tên đăng nhập, mật khẩu, email,...
- Nhấn **"Hoàn thành"** để tạo tài khoản.
- Sau khi đăng ký thành công, bạn có thể quay lại giao diện đăng nhập để sử dụng tài khoản mới.

### Quản lý phim
- **Thêm phim**: Nhập thông tin phim đầy đủ.
- **Sửa/Xóa phim**: Chọn phim từ danh sách và thao tác trực tiếp.

### Quản lý người dùng
- Đăng ký tài khoản mới nếu chưa có.
- Dữ liệu người dùng được lưu tại: `MovieManagementApp/datas/users.json`

---

## 📂 Cấu trúc dự án

```
MovieManagementApp/
├── main.py                  # File chính của ứng dụng
├── views/                   # Giao diện người dùng (UI)
│   ├── login_user_view.py
│   ├── user_view.py
│   └── ...
├── controllers/             # Xử lý logic (Controller)
│   ├── movie_controller.py
│   ├── user_controller.py
│   └── ...
├── models/                  # Quản lý dữ liệu (Model)
│   ├── movie_model.py
│   ├── user_model.py
│   └── ...
├── utils/                   # Các chức năng tiện ích
│   ├── get_api.py
│   ├── send_mail.py
│   └── ...
├── images/                  # Hình ảnh minh họa
│   ├── logo.png
│   └── movie.png
├── datas/                   # Dữ liệu lưu trữ
│   ├── movies.json
│   └── users.json
```

---

## 🛠️ Công nghệ sử dụng

| Công nghệ       | Vai trò                                 |
|----------------|------------------------------------------|
| Python 3.x     | Ngôn ngữ chính                           |
| Tkinter        | Giao diện người dùng                     |
| Pillow         | Hiển thị và xử lý hình ảnh               |
| Cloudinary     | Lưu trữ hình ảnh poster trên cloud       |
| JSON           | Lưu trữ dữ liệu người dùng và phim       |
| PyInstaller    | Đóng gói ứng dụng thành `.exe`           |
| Inno Setup     | Tạo trình cài đặt chuyên nghiệp           |

---

## 📧 Liên hệ

Nếu bạn gặp lỗi hoặc cần hỗ trợ, vui lòng liên hệ nhà phát triển để được hỗ trợ nhanh nhất.

---

⭐ **Cảm ơn bạn đã sử dụng Movie Management App!**
