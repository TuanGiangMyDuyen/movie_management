import os
import json

class JSONHandler:
    def __init__(self, filename):
        self.filepath = os.path.join("datas", filename)

        # Tạo thư mục nếu chưa tồn tại
        if not os.path.exists("datas"):
            try:
                os.makedirs("datas")
            except OSError as e:
                print(f"Lỗi khi tạo thư mục 'datas': {e}")

        # Tạo file nếu chưa có
        if not os.path.exists(self.filepath):
            try:
                with open(self.filepath, "w", encoding="utf-8") as f:
                    json.dump([], f)
            except Exception as e:
                print(f"Lỗi khi tạo file {self.filepath}: {e}")

    def read_json(self):
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Không tìm thấy file: {self.filepath}")
        except json.JSONDecodeError:
            print(f"File {self.filepath} bị lỗi định dạng JSON.")
        except PermissionError:
            print(f"Không có quyền đọc file: {self.filepath}")
        except Exception as e:
            print(f"Lỗi khi đọc file {self.filepath}: {e}")
        return []  # Trả về danh sách rỗng nếu xảy ra lỗi

    def write_json(self, data):
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except PermissionError:
            print(f"Không có quyền ghi file: {self.filepath}")
        except Exception as e:
            print(f"Lỗi khi ghi file {self.filepath}: {e}")