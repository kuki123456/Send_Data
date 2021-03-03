a=100
for i in range(7,107):
    str02="INSERT INTO `t_sdk_bas_error_code`(`ID`, `ERROR_ID`, `NAME`, `ERROR_TYPE`, `NAME_EN`) VALUES ({}, {}, 'NSPOSIXErrorDomain Code={}', 2, 'NSPOSIXErrorDomain Code={}');".format(a,i,i,i)
    print(str02)
    a+=1

