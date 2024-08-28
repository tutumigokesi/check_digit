#GTIN_13桁
def GTIN_13_check(data):
    i=0
    a=0
    b=0
    if len(data)==13:
        while i!=12:
            if(i%2!=0):
                a=a+int(data[i])
            elif i%2==0:
                b=b+int(data[i])
            i=i+1
        a=10-int((b+(a*3))%10)
        
        if int(data[-1])==a:
            return True
        else:
            return False
        
    else:
        return False

def Make_GTIN_13(maker_code,product_code):
    if len(maker_code)!=9:
        return False
    if len(product_code)!=3:
        return False
    i=0
    a=0
    b=0
    data=str(maker_code+product_code)
    if len(data)==12:
        while i!=12:
            if(i%2!=0):
                a=a+int(data[i])
            elif i%2==0:
                b=b+int(data[i])
            i=i+1
        a=10-int((b+(a*3))%10)
        data=str(maker_code+product_code+str(a))
        return data
    else:
        return False


#GTIN短縮コード_13桁
def GTIN_8_check(data):
    i=0
    a=0
    b=0
    if len(data)==13:
        while i!=12:
            if(i%2!=0):
                a=a+int(data[i])
            elif i%2==0:
                b=b+int(data[i])
            i=i+1
        a=10-int((b+(a*3))%10)
        if int(data[-1])==a:
            return True
        else:
            return False
    else:
        return False  

def Make_GTIN_8(product_code,item_code):
    if len(product_code)!=6:
        return False
    if len(item_code)!=1:
        return False
    i=0
    a=0
    b=0
    data=str("00000"+product_code+item_code)
    if len(data)==12:
        while i!=12:
            if(i%2!=0):
                a=a+int(data[i])
            elif i%2==0:
                b=b+int(data[i])
            i=i+1
        a=10-int((b+(a*3))%10)
        data=str("00000"+product_code+item_code+str(a))
        return data
    else:
        return False     

#集合包装用商品コード_１４桁
def GTIN_14_check(data):
    i=0
    a=0
    b=0
    if len(data)==14:
        while i!=13:
            if(i%2!=0):
                b=b+int(data[i])
            elif i%2==0:
                a=a+int(data[i])
            i=i+1
        a=10-int((b+(a*3))%10)
        if int(data[-1])==a:
            return True
        else:
            return False
    else:
        return False

def Make_GTIN_14(indicator_code,maker_code,product_code):
    if len(indicator_code)!=1:
        return False
    if len(maker_code)!=9:
        return False
    if len(product_code)!=3:
        return False
    i=0
    a=0
    b=0
    data=str(indicator_code+maker_code+product_code)
    if len(data)==13:
        while i!=13:
            if(i%2!=0):
                b=b+int(data[i])
            elif i%2==0:
                a=a+int(data[i])
            i=i+1
        a=10-int((b+(a*3))%10)
        data=str(indicator_code+maker_code+product_code+str(a))
        return data
    else:
        return False

#U.P.C._12桁
def UPC_12_check(data):
    i=0
    a=0
    b=0
    if len(data)==12:
        while i!=11:
            if(i%2!=0):
                b=b+int(data[i])
            elif i%2==0:
                a=a+int(data[i])
            i=i+1
        a=10-int((b+(a*3))%10)
        if int(data[-1])==a:
            return True
        else:
            return False
    else:
        return False

def Make_UPC_12(UPC_Company_Prefix,item_code):
    if len(UPC_Company_Prefix)!=7:
        return False
    if len(item_code)!=4:
        return False
    i=0
    a=0
    b=0
    data=str(UPC_Company_Prefix+item_code)
    if len(data)==11:
        while i!=11:
            if(i%2!=0):
                b=b+int(data[i])
            elif i%2==0:
                a=a+int(data[i])
            i=i+1
        a=10-int((b+(a*3))%10)
        data=str(UPC_Company_Prefix+item_code+str(a))
        return data
    else:
        return False

 
#SSCC出荷包装シリアル番号_18桁
def GTIN_18_check(data):
    i=0
    a=0
    b=0
    if len(data)==18:
        while i!=17:
            if(i%2!=0):
                b=b+int(data[i])
            elif i%2==0:
                a=a+int(data[i])
            i=i+1
        a=10-int((b+(a*3))%10)
        if int(data[-1])==a:
            return True
        else:
            return False
    else:
        return False

def Make_GTIN_18(Extension_code,maker_code,Serial_code):
    if len(Extension_code)!=1:
        return False
    if len(maker_code)!=9:
        return False
    if len(Serial_code)!=7:
        return False
    i=0
    a=0
    b=0
    data=str(Extension_code+maker_code+Serial_code)
    if len(data)==17:
        while i!=17:
            if(i%2!=0):
                b=b+int(data[i])
            elif i%2==0:
                a=a+int(data[i])
            i=i+1
        a=10-int((b+(a*3))%10)
        data=str(Extension_code+maker_code+Serial_code+str(a))
        return data
    else:
        return False
    

print(GTIN_13_check("4569951116179"))
print(GTIN_8_check("0000049968712"))
print(GTIN_14_check("14569951116176"))
print(UPC_12_check("012345678905"))
print(GTIN_18_check("045699511100000016"))
print(Make_GTIN_13("456995111","617"))
print(Make_GTIN_8("499687","1"))
print(Make_GTIN_14("1","456995111","617"))
print(Make_UPC_12("0123456","7890"))
print(Make_GTIN_18("0","456995111","0000001"))
