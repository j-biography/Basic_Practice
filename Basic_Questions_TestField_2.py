# print("|\_/|")
# print("|q p|   /}")
# print('( 0 )"""\ ')
# print('|"^"`    |')
# s = '||_/=\ \__|'
# print(s.replace(' ', ''))


# print("         ,r'"+'"7')
# print("r`-_   ,'  ,/")
# print(' \. ".'+" L_r' ")
# print("   `~\/")
# print('      |')
# print('      |')


# A, B = map(int, input().split())

# if A > B:
#     print('>')
# elif A < B:
#     print('<')
# elif A == B:
#     print('==')

# Test = int(input())

# if 100 >= Test >= 90:
#     print('A')
    
# elif 89 >= Test >= 80:
#     print('B')
    
# elif 79 >= Test >= 70:
#     print('C')

# elif 69 >= Test >= 60:
#     print('D')

# else:
#     print('F')


Year = int(input())

if Year % 4 == 0:
    if Year % 100 != 0 or Year % 400 == 0:
        print('1')
    else:
        print('0')       
else:
    print('0')
    