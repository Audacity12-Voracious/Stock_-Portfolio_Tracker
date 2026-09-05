def get_price_dict():
    return {"NVDA": 210, "AAPL": 313, "AMZN": 260, "META": 576, "GOOG": 339}

def parse_input(raw_line):
    entry = raw_line.split(",")      #Splits the whole input strings by commas, gives a raw list of values. eg ["NVDA 2","AAPL 313"]
    valid_entries = []
    for item in entry:
        cleaned = item.strip()      #Removes the leading & Trailing whitespaces from the values from entry
        parts = cleaned.split()      # Splits the results from cleaned from the whitespace
    
        if len(parts) != 2:     #Validates if the length of the parts is not equal to 2, then it is an invalid format.
            print(f"Invalid format: {cleaned}, ensure there's a space between the stock symbol and quantity, skipping")
            continue
        else:
            symbol = parts[0].upper()
            quantity_str = parts[1]  
            valid_entries.append((symbol, quantity_str))
    return valid_entries

def calculate_total(valid_entries, price_dict):
    total_investment = 0
    results = []

    for symbol, quantity_str in valid_entries:
        try:
            quantity = int(quantity_str)
        except (ValueError, TypeError):
            print(f"Invalid quantity: '{quantity_str}', ensure it's a valid integer.")
            continue

        if symbol in price_dict:
            price = price_dict[symbol]
            total_value = price * quantity
            total_investment += total_value
            results.append((symbol, quantity, price, total_value))
        else:
            print(f"Stock '{symbol}' not found in our price list,\n here's what we have 'NVDA', 'AMZN', 'AAPL', 'META', 'GOOG'")           
    return total_investment, results

def display_results(results, total_investment):
    print("\n===================================")
    print("Stock Portfolio Summary:")
    print("------------------------------------")
    for symbol, quantity, price, total_value in results:
        print(f"{symbol}: Quantity: {quantity}, Price: ${price}, Total Value: ${total_value}")
    print("-----------------------------------")
    print(f"\nTotal Investment Value: ${total_investment}")
    print("-----------------------------------")
    print("Thank you for using the Stock Portfolio Tracker!")   

def main():
    price_dict = get_price_dict()
    raw_line = input("Enter your stock portfolio (format: SYMBOL QUANTITY, SYMBOL QUANTITY, ...): ")
    valid_entries = parse_input(raw_line)
    total_investment, results = calculate_total(valid_entries, price_dict)
    display_results(results, total_investment)

    save_result(results, total_investment)

def save_result(results, total_investment):
    user_choice = input("Do you want to save the file? (y/n):  ")
    if user_choice == "y":
        preferred_type = input("Enter the the file type you want (.txt or .csv) ")
        if preferred_type == ".txt":
            with open(f"Stock Portfolio Summary{preferred_type}", "w") as file:
                file.write("Stock Portfolio Summary\n")
                file.write("------------------------------------\n")
                for symbol, quantity, price, total_value in results:
                    file.write(f"{symbol}: Quantity: {quantity}, Price: ${price}, Total Value: ${total_value}\n")
                file.write("-----------------------------------\n")
                file.write(f"\nTotal Investment Value: ${total_investment}\n")
                file.write("-----------------------------------\n")
                file.write("Thank you for using the Stock Portfolio Tracker!\n")     
            print("Saved to file")

        elif preferred_type == ".csv":
            with open(f"Stock Portfolio Summary{preferred_type}", "w") as file:
                file.write("Symbol,Quantity,Price,Total Value\n")
                for symbol, quantity, price, total_value in results:
                    file.write(f"{symbol},{quantity},{price},{total_value}\n")
                file.write(f"Total,,,{total_investment}\n")
            print("Saved to file")
        else:
            print(f"The file type {preferred_type} is Invalid, please choose either .txt or .csv")

    elif user_choice == "n":
        print("Result not saved. Goodbye..✌️")
    else:
        print(f"The input {user_choice} is Invalid")
main()
