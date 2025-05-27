import cloudinary
import cloudinary.uploader
import os

# Cấu hình Cloudinary (thay bằng thông tin của bạn)
cloudinary.config(
    cloud_name='dyvkrlz5i',
    api_key='147796282619694',
    api_secret='4Jcge9r8r6syYkUDfk6-1D0ELa4'
)

class Cloudinary:

    @staticmethod
    def upload_photo(filepath):
        try:
            # Upload ảnh lên Cloudinary
            result = cloudinary.uploader.upload(filepath)
            url = result.get("secure_url")

            if url:
                return url, ""
            else:
                return None, "Lỗi! Không thể tải ảnh lên!"
        except Exception as e:
            return None, f"Lỗi! Không thể tải ảnh lên {e}!"

    @staticmethod
    def delete_photo(url):
        filename = os.path.basename(url)
        public_id = os.path.splitext(filename)[0]
        cloudinary.uploader.destroy(public_id)