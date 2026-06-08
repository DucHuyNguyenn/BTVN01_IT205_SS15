inventory_stock = 100
total_revenue = 0.0


# ================= HÀM NHẬP DỮ LIỆU =================
def input_positive_int(message):
    try:
        value = int(input(message))
        if value <= 0:
            print("Dữ liệu nhập vào phải lớn hơn 0.")
            return None
        return value
    except ValueError:
        print("Vui lòng nhập số hợp lệ.")
        return None


def input_positive_float(message):
    try:
        value = float(input(message))
        if value <= 0:
            print("Dữ liệu nhập vào phải lớn hơn 0.")
            return None
        return value
    except ValueError:
        print("Vui lòng nhập số hợp lệ.")
        return None


# ================= CHỨC NĂNG 1 =================
def add_stock(amount):
    global inventory_stock

    inventory_stock += amount

    print(f"Đã nhập thành công {amount} sản phẩm.")
    print(f"Tồn kho hiện tại: {inventory_stock}")


# ================= HÀM TÍNH TIỀN =================
def calculate_final_price(quantity, price):
    subtotal = quantity * price

    discount = 0

    if subtotal >= 1000:
        discount = subtotal * 0.1

    after_discount = subtotal - discount
    vat = after_discount * 0.08

    final_total = after_discount + vat

    return subtotal, discount, vat, final_total


# ================= CHỨC NĂNG 2 =================
def process_sale(quantity, price):
    global inventory_stock
    global total_revenue

    if quantity > inventory_stock:
        print(
            f"Lỗi: Không đủ hàng trong kho. Tồn kho hiện tại chỉ còn {inventory_stock}."
        )
        return

    subtotal, discount, vat, final_total = calculate_final_price(
        quantity, price
    )

    # cập nhật kho và doanh thu
    inventory_stock -= quantity
    total_revenue += final_total

    print("-> Hóa đơn chi tiết:")
    print(f"Số lượng: {quantity} | Đơn giá: ${price}")
    print(f"Tạm tính: ${subtotal}")
    print(f"Giảm giá (10%): ${discount}")
    print(f"Thuế VAT (8%): ${vat}")
    print(f"Tổng thanh toán: ${final_total}")
    print("Đã bán thành công!")


# ================= CHỨC NĂNG 3 =================
def print_report():
    """
    Hiển thị báo cáo kinh doanh tổng quan.

    Bao gồm:
    - Số lượng sản phẩm còn trong kho.
    - Tổng doanh thu đã bán được.
    """

    print("--- BÁO CÁO KINH DOANH ---")
    print(f"Tồn kho hiện tại: {inventory_stock} sản phẩm")
    print(f"Tổng doanh thu: ${total_revenue}")


# ================= MAIN =================
def main():
    while True:
        print("\n========== TECHSTORE MANAGEMENT SYSTEM ==========")
        print("1. Nhập thêm hàng vào kho")
        print("2. Bán hàng (Tính toán hóa đơn)")
        print("3. Xem báo cáo tổng quan")
        print("4. Thoát chương trình")
        print("=================================================")

        choice = input("Chọn chức năng (1-4): ")

        match choice:
            case "1":
                print("\n--- NHẬP HÀNG ---")

                amount = input_positive_int(
                    "Nhập số lượng sản phẩm muốn thêm: "
                )

                if amount is not None:
                    add_stock(amount)

            case "2":
                print("\n--- BÁN HÀNG ---")

                quantity = input_positive_int(
                    "Nhập số lượng mua: "
                )

                if quantity is None:
                    continue

                price = input_positive_float(
                    "Nhập đơn giá ($): "
                )

                if price is None:
                    continue

                process_sale(quantity, price)

            case "3":
                print_report()

            case "4":
                print("Thoát chương trình.")
                break

            case _:
                print("Vui lòng chọn từ 1 đến 4.")


main()