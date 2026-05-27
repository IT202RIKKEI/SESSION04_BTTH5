
def main():
    
    total_revenue: float = 0
    total_high_revnue_bill: int = 0
    actual_bills = 0
    # nhập vào số hơn đơn muốn nhập
    while True:
        try:
            number_of_bills = int(input("Số hóa đơn cần nhập vào giá trị: "))
            
            if number_of_bills <= 0:
                print("Lỗi! Không được để số bé hơn 0")
                continue
            else:
                break
        except ValueError:
            print("Không được nhập vào chuỗi")


    # nhập vào cho từng hóa đơn

    for bill in range(1, number_of_bills + 1):
        
        # nhập vào giá trị cho từng hóa đơn
        while True:
            try:
                input_value_bill = float(input(f"Khách hàng {bill} - Nhập giá trị hóa đơn: "))
                    
                if input_value_bill < 0:
                    print("Lỗi! Không được để số bé hơn 0")
                    continue
                else:
                    break
            except ValueError:
                print("Không được nhập vào chuỗi")
                

        # nếu ổn rồi thì cộng dồn tiền hóa đơn
        total_revenue = total_revenue + input_value_bill
        
        # cộng dồn cái hóa đơn lớn hơn 1tr
        
        if input_value_bill >= 1000000:
            total_high_revnue_bill += 1
        
        # số ng nhập vào thực tế 
        actual_bills += 1
        
        # xem coi có muốn nhập tiếp ôn
        user_choice = input("Bạn có muốn nhập tiếp không? (C,K)").lower()
        
        # nếu k thì break
        if user_choice == "k":
            
            # Tỷ lệ phần trăm (%) của nhóm hóa đơn lớn trên tổng số hóa đơn đã bán
            higer_bill_revenue_percent = (total_high_revnue_bill / number_of_bills) * 100
            
            print("--- BÁO CÁO DOANH THU CUỐI NGÀY CỦA RIKKEI STORE---")
            print(f"tổng số hóa đơn đã nhập: {actual_bills} hóa đơn")
            print(f"tổng doanh thu ngày hôm nay: {total_revenue} VND")
            print(f"số hóa đơn lớn (> 1tr VND): {total_high_revnue_bill} hóa đơn")
            print(f"Tỷ lệ hóa đơn lớn đạt: {higer_bill_revenue_percent} trên tổng số đơn hàng")
            
            break
    

if __name__ == "__main__":
    main()


    
    