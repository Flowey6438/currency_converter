def currency_converter(amount, from_currency, to_currency, exchange_rate):
    converted_amount = amount * exchange_rate
    return converted_amount

if __name__ == "__main__":
    print("欢迎使用汇率转换器！")
    
    try:
        amount = float(input(f"请输入要转换的金额："))
        from_currency = input("请输入原货币（例如USD）：").upper()
        to_currency = input("请输入目标货币（例如CNY）：").upper()
        exchange_rate = float(input(f"请输入 {from_currency} 到 {to_currency} 的汇率："))

        converted_amount = currency_converter(amount, from_currency, to_currency, exchange_rate)
        print(f"{amount} {from_currency} 等于 {converted_amount:.2f} {to_currency}")
    except ValueError:
        print("输入的金额或汇率无效，请输入有效的数字。")
