import os

class MovieValidation:

    @staticmethod
    def validate_image(file_path):
        valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
        file_extension = os.path.splitext(file_path)[1].lower()  # Lấy phần mở rộng và chuyển thành chữ thường
        if file_extension in valid_extensions:
            return True, ""
        else:
            return False, "Không đúng định dạng ảnh"

    @staticmethod
    def validate_movie_info(movieInfo):

        for key, value in movieInfo.items():
            if isinstance(value, str) and not value.strip():  # Chuỗi rỗng
                return False, "Vui lòng nhập đầy đủ thông tin"

        # Kiểm tra thời lượng, giá vé, tổng số ghế, số ghế trống có phải là số không
        try:
            movieInfo['duration_minutes'] = int(movieInfo['duration_minutes'])
            movieInfo['ticket_price'] = int(movieInfo['ticket_price'])
            movieInfo['total_seats'] = int(movieInfo['total_seats'])
            movieInfo['available_seats'] = int(movieInfo['available_seats'])
        except ValueError:
            return False, "Thời lượng, Giá vé, Tổng số ghế và Số ghế trống phải là số nguyên!"

        return True, ""