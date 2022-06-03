
second = int(input("sanie ra vared konid")) 

seconds = second % (24 * 3600)
hour = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

print("sanie", seconds ,"daghighe" , minutes ,  "saat" ,hour  )


