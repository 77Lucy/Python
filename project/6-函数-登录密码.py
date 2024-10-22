#语法格式要求很严格
# def account_login():
#     password = input('Password:')
#     if password == '12345':
#         print('Login success！')
#     else:
#         print('Wrong password or invalid input!')
#         account_login()
# account_login()

#函数+if
# password_list = ['*#*#','12345']
# def account_login():
#     password = input('Password:')
#     password_correct = password == password_list[-1]
#     password_reset = password == password_list[0]
#     if password_correct:
#         print('Login success!')
#     elif password_reset:
#          new_password = input('Enter a new password:')
#          password_list.append(new_password)
#          print('Your password has changed successfully!')
#          account_login()
#     else:
#          print('Wrong password or invalid input!')
#          account_login()
# account_login()


#函数+if+while 如果输入三次出错，冻结账号
password_list = ['*#*#','12345']
def account_login():
    tries=3;
    while tries>0:
      password = input('Password:')
      password_correct = password == password_list[-1]
      password_reset = password == password_list[0]

      if password_correct:
        print('Login success!')
      elif password_reset:
         new_password = input('Enter a new password:')
         password_list.append(new_password)
         print('Your password has changed successfully!')
         account_login()
      else:
         print('Wrong password or invalid input!')
         tries = tries-1
         print(tries, 'times left')
    else:
        print('Your account has been suspended')
account_login()

