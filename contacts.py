# Biến lưu trữ dữ liệu: Mỗi liên hệ là một dict {'name': '...', 'phone': '...'}
phonebook = []

def add_contact():
    name = input("Nhập tên liên hệ: ")
    phone = input("Nhập số điện thoại: ")

    contact = {"name": name, "phone": phone}
    phonebook.append(contact)

    print("✔ Đã thêm liên hệ thành công!")

def view_contacts():
    if len(phonebook) == 0:
        print("⚠ Danh bạ đang trống!")
        return
    
    print("\n--- DANH SÁCH LIÊN HỆ ---")
    for i, c in enumerate(phonebook, start=1):
        print(f"{i}. {c['name']} - {c['phone']}")

def search_contact():
    name_search = input("Nhập tên cần tìm: ")
    found = False

    for c in phonebook:
        if c["name"].lower() == name_search.lower():
            print(f"📌 Số điện thoại của {name_search}: {c['phone']}")
            found = True
            break

    if not found:
        print("❌ Không tìm thấy liên hệ!")

def main():
    while True:
        print("\n--- DANH BẠ ĐIỆN THOẠI ---")
        print("1. Thêm liên hệ")
        print("2. Xem danh bạ")
        print("3. Tìm kiếm")
        print("4. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            print("Tạm biệt!")
            break
        else:
            print("⚠ Lựa chọn không hợp lệ, vui lòng nhập lại!")

if __name__ == "__main__":
    main()


def view_contacts():
    if len(phonebook) == 0:
        print("Danh bạ đang trống!")
        return

    print("\n--- DANH SÁCH LIÊN HỆ ---")
    for i, contact in enumerate(phonebook, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
