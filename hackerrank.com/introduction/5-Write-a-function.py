def is_leap(year):
    leap=False
    if 1900<=year<=10**5:
        if year%4==0:
            if year%100==0:
                if year%400==0:
                    return True
                else:
                    return leap
            else:
                return True
        else:
            return leap
    else:
        return leap
        
# print("Hesaplanacak yılı giriniz:")
year=int(input())
print(is_leap(year))
'''
if is_leap(year)==year:
    print(str(year) + " artik yildir.")
elif 
    print("Artik yil degildir")
    '''

