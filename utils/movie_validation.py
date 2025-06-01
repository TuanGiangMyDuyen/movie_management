import os
from datetime import datetime

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
            if key == "description":
                continue
            if isinstance(value, str) and not value.strip():  # Chuỗi rỗng
                return False, "Vui lòng nhập đầy đủ thông tin"

        # Kiểm tra độ dài tối đa
        if len(movieInfo['name']) > 100:
            return False, "Tên phim không được vượt quá 100 ký tự!"
        elif len(movieInfo['director']) > 50:
            return False, "Đạo diễn không được vượt quá 50 ký tự!"
        elif len(movieInfo['actors']) > 50:
            return False, "Diễn viên không được vượt quá 50 ký tự!"
        elif len(movieInfo['language']) > 20:
            return False, "Ngôn ngữ không được vượt quá 20 ký tự!"
        elif len(movieInfo['rated']) > 5:
            return False, "Xếp hạng độ tuổi không được vượt quá 5 ký tự!"
        elif 'description' in movieInfo and movieInfo['description']:
            if len(movieInfo['description']) > 500:
                return False, "Mô tả phim không được vượt quá 500 ký tự!"

        #Kiểm tra số ghế hợp lệ
        if movieInfo['available_seats'] > movieInfo['total_seats']:
            return False, "Tổng số ghế phải lớn hơn số ghế trống!"

        # Kiểm tra thời lượng, giá vé, tổng số ghế, số ghế trống có phải là số không
        try:
            movieInfo['duration_minutes'] = int(movieInfo['duration_minutes'])
            movieInfo['ticket_price'] = int(movieInfo['ticket_price'])
            movieInfo['total_seats'] = int(movieInfo['total_seats'])
            movieInfo['available_seats'] = int(movieInfo['available_seats'])
        except ValueError:
            return False, "Thời lượng, Giá vé, Tổng số ghế và Số ghế trống phải là số nguyên!"

        try:
            show_date = datetime.strptime(movieInfo['show_date'], "%d/%m/%Y")
            today = datetime.today()
            if show_date.date() < today.date():
                return False, "Ngày phát hành không được nhỏ hơn ngày hôm nay!"
        except ValueError:
            return False, "Ngày phát hành phải theo định dạng DD/MM/YYYY (VD: 01/06/2025)"

        return True, ""