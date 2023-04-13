
import datetime
import time
to_list = ["vgb30xk@naver.com, vgb30xk@gmail.com"]
msg = ", ".join(to_list)
print(msg)

print(time.strftime('%d-%b-%Y'))

dt = datetime.datetime.strptime("2023-12-30", "%Y-%m-%d")
print(type(dt))
print(dt.strftime("%d-%b-%Y"))
