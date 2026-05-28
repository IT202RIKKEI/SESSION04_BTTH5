def main():
    total_revenue = 0
    total_high_revenue_bill = 0
    actual_bills = 0

    while True:
        # nhập giá trị hóa đơn
        while True:
            try:
                input_value_bill = float(
                    input(f"Hóa đơn {actual_bills + 1} - Nhập giá trị hóa đơn: ")
                )

                if input_value_bill < 0:
                    print("Lỗi! Không được nhập số âm")
                    continue

                break

            except ValueError:
                print("Không được nhập vào chuỗi")

        total_revenue += input_value_bill
        actual_bills += 1

        if input_value_bill >= 1000000:
            total_high_revenue_bill += 1

        user_choice = input("Bạn có muốn nhập tiếp không? (C/K): ").lower()

        if user_choice == "k":
            break

    if actual_bills == 0:
        print("Chưa có hóa đơn nào được nhập.")
        return

    higher_bill_revenue_percent = (
        total_high_revenue_bill / actual_bills
    ) * 100

    print("\n--- BÁO CÁO DOANH THU CUỐI NGÀY CỦA RIKKEI STORE ---")
    print(f"Tổng số hóa đơn đã nhập: {actual_bills} hóa đơn")
    print(f"Tổng doanh thu ngày hôm nay: {total_revenue} VND")
    print(f"Số hóa đơn lớn (>= 1tr VND): {total_high_revenue_bill} hóa đơn")
    print(f"Tỷ lệ hóa đơn lớn đạt: {higher_bill_revenue_percent:.2f}% trên tổng số đơn hàng")


if __name__ == "__main__":
    main()