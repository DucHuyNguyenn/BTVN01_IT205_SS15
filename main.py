# =====================================================
# TECHSTORE MANAGEMENT SYSTEM
# =====================================================

# ---------------- GLOBAL VARIABLES -------------------
# Biến toàn cục (Global Variables)
# Có thể được truy cập ở mọi hàm trong chương trình

inventory_stock = 100
total_revenue = 0.0


# ---------------- HELPER FUNCTIONS -------------------

def get_positive_int(message):
    """
    Nhập và kiểm tra số nguyên dương.

    Parameters:
        message (str): Nội dung hiển thị cho người dùng.

    Returns:
        int: Giá trị hợp lệ (>0)
        None: Nếu dữ liệu không hợp lệ
    """
    try:
        value = int(input(message))

        if value <= 0:
            print("Dữ liệu nhập vào phải lớn hơn 0.")
            return None

        return value

    except ValueError:
        print("Vui lòng nhập đúng kiểu dữ liệu số.")
        return None


def get_positive_float(message):
    """
    Nhập và kiểm tra số thực dương.

    Parameters:
        message (str): Nội dung hiển thị cho người dùng.

    Returns:
        float: Giá trị hợp lệ (>0)
        None: Nếu dữ liệu không hợp lệ
    """
    try:
        value = float(input(message))

        if value <= 0:
            print("Dữ liệu nhập vào phải lớn hơn 0.")
            return None

        return value

    except ValueError:
        print("Vui lòng nhập đúng kiểu dữ liệu số.")
        return None


# ---------------- BUSINESS FUNCTIONS -----------------

def add_stock(amount):
    """
    Thêm hàng vào kho.

    Parameters:
        amount (int): Số lượng sản phẩm muốn nhập thêm.

    Returns:
        None
    """

    # sử dụng global để thay đổi biến toàn cục
    global inventory_stock

    inventory_stock += amount

    print(f"Đã nhập thành công {amount} sản phẩm.")
    print(f"Tồn kho hiện tại: {inventory_stock}")


def process_sale(quantity):
    """
    Kiểm tra tồn kho trước khi bán.

    Parameters:
        quantity (int): Số lượng khách muốn mua.

    Returns:
        bool:
            True  -> đủ hàng
            False -> không đủ hàng
    """

    # inventory_stock là biến global
    if quantity > inventory_stock:
        print(
            f"Lỗi: Không đủ hàng trong kho. "
            f"Tồn kho hiện tại chỉ còn {inventory_stock}."
        )
        return False

    return True


def calculate_final_price(quantity, price):
    """
    Tính tổng tiền cuối cùng của hóa đơn.

    Parameters:
        quantity (int): Số lượng sản phẩm.
        price (float): Đơn giá sản phẩm.

    Returns:
        tuple:
            subtotal      : tiền trước giảm giá
            discount      : số tiền giảm giá
            vat           : thuế VAT
            final_total   : tổng thanh toán cuối cùng
    """

    # -------- LOCAL VARIABLES ----------
    # Các biến dưới đây chỉ tồn tại bên trong hàm
    # nên được gọi là Local Variables

    subtotal = quantity * price

    discount = 0

    if subtotal >= 1000:
        discount = subtotal * 0.10

    after_discount = subtotal - discount

    vat = after_discount * 0.08

    final_total = after_discount + vat

    return subtotal, discount, vat, final_total


def print_report():
    """
    Hiển thị báo cáo kinh doanh hiện tại.

    Chức năng:
    - In ra số lượng hàng tồn kho.
    - In ra tổng doanh thu đã ghi nhận.

    Sử dụng:
    - Đọc dữ liệu từ các biến toàn cục:
      inventory_stock
      total_revenue

    Returns:
        None
    """

    print("\n--- BÁO CÁO KINH DOANH ---")
    print(f"Tồn kho hiện tại: {inventory_stock} sản phẩm")
    print(f"Tổng doanh thu: ${total_revenue:.2f}")


# ---------------- MAIN PROGRAM -----------------------

def main():
    global inventory_stock
    global total_revenue

    while True:

        print("\n========== TECHSTORE MANAGEMENT SYSTEM ==========")
        print("1. Nhập thêm hàng vào kho")
        print("2. Bán hàng (Tính toán hóa đơn)")
        print("3. Xem báo cáo tổng quan")
        print("4. Thoát chương trình")
        print("=================================================")

        choice = input("Chọn chức năng (1-4): ")

        # ---------------- MENU 1 ----------------
        if choice == "1":

            print("\n--- NHẬP HÀNG ---")

            amount = get_positive_int(
                "Nhập số lượng sản phẩm muốn thêm: "
            )

            if amount is None:
                continue

            add_stock(amount)

        # ---------------- MENU 2 ----------------
        elif choice == "2":

            print("\n--- BÁN HÀNG ---")

            quantity = get_positive_int(
                "Nhập số lượng mua: "
            )

            if quantity is None:
                continue

            price = get_positive_float(
                "Nhập đơn giá ($): "
            )

            if price is None:
                continue

            # kiểm tra kho
            if not process_sale(quantity):
                continue

            subtotal, discount, vat, final_total = (
                calculate_final_price(quantity, price)
            )

            # cập nhật trạng thái hệ thống
            inventory_stock -= quantity
            total_revenue += final_total

            print("\n-> Hóa đơn chi tiết:")
            print(
                f"Số lượng: {quantity} | "
                f"Đơn giá: ${price}"
            )
            print(f"Tạm tính: ${subtotal}")

            if discount > 0:
                print(f"Giảm giá (10%): ${discount}")
            else:
                print("Giảm giá (10%): $0")

            print(f"Thuế VAT (8%): ${vat}")
            print(f"Tổng thanh toán: ${final_total}")

            print("Đã bán thành công!")

        # ---------------- MENU 3 ----------------
        elif choice == "3":
            print_report()

        # ---------------- MENU 4 ----------------
        elif choice == "4":
            print("\nĐang lưu dữ liệu...")
            print("Thoát chương trình thành công!")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4.")


# ---------------- RUN PROGRAM ------------------------

if __name__ == "__main__":
    main()