def insert_in_middle(main_string, insert_string):
    if len(main_string) % 2 == 0:
        middle_index = len(main_string) // 2
        result_string = main_string[:middle_index] + insert_string + main_string[middle_index:]
    else:
        middle_index = len(main_string) // 2
        result_string = main_string[:middle_index] + insert_string + main_string[middle_index:]
    
    return result_string

main_str = "Parvadiya, Bhaveshbhai"
insert_str = "Yash "
result = insert_in_middle(main_str, insert_str)
print(result)