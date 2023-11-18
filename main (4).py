#1
def get_keys_with_value_true(input_dict):
    true_keys = []
    for key, value in input_dict.items(): #Проход по элементам словаря
    #.items для получения представления пар "ключ-значение" из словаря
        if value is True:
            true_keys.append(key)
    return true_keys


my_dict = {
    "a": True,
    "b": False,
    "c": True
}

result = get_keys_with_value_true(my_dict)
print(result) 





#2
def get_unique_elements(input_list): #вернуть уникальные элементы из списка
    unique_elements = []
    seen = set()  #Для отслеживания элементов, которые мы уже видели

    for element in input_list:
        #.count() используется для подсчета количества вхождений определенного элемента в последовательность
        if input_list.count(element) <= 1 and element not in seen: #Проверка на уникальность и добавление в список
            unique_elements.append(element) #для добавления элемента в конец списка
            seen.add(element) #для добавления элемента в множество

    return unique_elements


my_list = [1, 2, 3, 1, 2, 4]
result = get_unique_elements(my_list)
print(result)  # Output: [3, 4]







#3
def get_date_in_format(date): #преобразовать дату из одного формата в другой
    parts = date.split(".") #разделить входную дату на части (по точкам)
    day = parts[2] 
    month = parts[1]
    year = parts[0]
    formatted_date = f"{day}.{month}.{year}"
    return formatted_date


input_date = "2023.10.23"
result = get_date_in_format(input_date)
print(result)  




#4
def get_elements_with_no_more_than_two_occurrences(input_list):
    #вернуть элементы из списка, которые встречаются не более двух раз
    result = [] #будет содержать элементы с не более чем двумя вхождениями
    occurrences = {} #чтобы отслеживать количество вхождений каждого элемента

    for element in input_list:
        if element not in occurrences:
            occurrences[element] = 1
        else:
            occurrences[element] += 1

        if occurrences[element] <= 2: #проверяем, не превышает ли количество вхождений данного элемента два
            result.append(element)

    return result


my_list = [1, 2, 3, 1, 2, 4]
result = get_elements_with_no_more_than_two_occurrences(my_list)
print(result)  






#5
def get_words_from_string(input_string): #разделить строку на слова
    words = input_string.split() #разделяет строку по пробелам
    return words


my_string = "This a string with a several words."
result = get_words_from_string(my_string)
print(result)  




#6
def get_unique_elements_with_count(input_list):
    #подсчитать количество уникальных элементов в списке
    element_count = {} #для отслеживания количества вхождений каждого элемента
    for element in input_list:
        if element in element_count:
            element_count[element] += 1 #увеличиваем счетчик вхождений для каждого элемента в словаре
        else:
            element_count[element] = 1
    return element_count


my_list = [1, 2, 3, 1, 2, 4, 1, 2]
result = get_unique_elements_with_count(my_list)
print(result)  





#7
def get_prime_numbers(n): #вернуть список простых чисел до заданного числа n
    is_prime = [True] * (n + 1) #это список булевых значений, инициализированный True, представляющий, является ли число простым.
    p = 2 #переменная, используемая для перебора чисел
    prime_numbers = [] #это список, в который будут добавляться простые числа
#алгоритм Решето Эратосфена
    while p**2 <= n: #помечает числа, которые не являются простыми
        if is_prime[p]:
            for i in range(p**2, n + 1, p):
                is_prime[i] = False
        p += 1

    for i in range(2, n + 1): #range - последовательность чисел в заданном диапазоне
        if is_prime[i]:
            prime_numbers.append(i)

    return prime_numbers


n = 100
result = get_prime_numbers(n)
print(result)







#8 
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def get_prime_numbers_in_list(input_list):
    prime_numbers = [num for num in input_list if is_prime(num)]
    return prime_numbers


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 27, 36, 48, 54, 67, 71, 73, 75, 83, 89, 99]
result = get_prime_numbers_in_list(my_list)
print(result)  






#9
from datetime import datetime
#рассчитывает разницу в днях между двумя датами
def get_difference_between_dates(date1, date2):
    
    date1_obj = datetime.strptime(date1, '%Y.%m.%d') #для преобразования строк в объекты
    date2_obj = datetime.strptime(date2, '%Y.%m.%d')

   
    date_difference = abs((date2_obj - date1_obj).days) #Рассчитывает разницу в днях между двумя датами

    return date_difference


date1 = '2023.10.23'
date2 = '2023.10.24'
result = get_difference_between_dates(date1, date2)
print(result)  





#10 Преобразование двоичной строки в десятичное число
def get_decimal_number_from_binary_string(binary_string):
    decimal_number = int(binary_string, 2)
    return decimal_number


binary_string = "10110011"
result = get_decimal_number_from_binary_string(binary_string)
print(result)  




#11 
import math
#Получение списка perfect squares (полных квадратов)
def is_perfect_square(num):
    root = math.isqrt(num)
    return root * root == num

def get_perfect_squares(input_list):
    perfect_squares = [num for num in input_list if is_perfect_square(num)]
    return perfect_squares


my_list = [4, 25, 81]
result = get_perfect_squares(my_list)
print(result)  




#12 Сортировка списка покупок по цене
def sort_shopping_list_by_price(shopping_list):
    sorted_list = sorted(shopping_list, key=lambda item: item['price'])
    return sorted_list


shopping_list = [
    {"name": "Apple", "price": 100},
    {"name": "Banana", "price": 50},
    {"name": "Orange", "price": 20}
]
result = sort_shopping_list_by_price(shopping_list)
print(result)




#13 Получение слов, начинающихся с гласной
def get_words_starting_with_vowel(word_list):
    vowels = "aeiouAEIOU"
    vowel_words = [word for word in word_list if word[0] in vowels]
    return vowel_words


word_list = ["apple", "banana", "orange", "bear", "cat"]
result = get_words_starting_with_vowel(word_list)
print(result)  
