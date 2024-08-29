"""コード桁数が奇数"""
def _Calculation_digit_odd(data,code_long):
    i=0
    a=0
    b=0
    while i != (code_long-1):
            if (i%2)!=0:
                a=a+int(data[i])
            elif (i%2)==0:
                b=b+int(data[i])
            i=i+1
            
    return 10-int((b+(a*3))%10)

"""コード桁数奇数"""
def _Calculation_digit_even(data,code_long):
    i=0
    a=0
    b=0
    while i != (code_long-1):
        if (i%2)!=0:
            b=b+int(data[i])
        elif (i%2)==0:
            a=a+int(data[i])
        
        i=i+1
            
    return 10-int((b+(a*3))%10)

"""計算した値とチェックデジットの値を審議する"""
def isValid_digit(data,calculation_digit):
    if int(data[-1])==calculation_digit:
            return True
    else:
            return False

"""上記の関数を使いコードの誤りを検出する"""
def isCheck_code(data,code_long):
    if len(data)==code_long:
        
        if (code_long%2)==0:
            a=_Calculation_digit_even(data,code_long)
        else:
            a=_Calculation_digit_odd(data,code_long)
        
        return isValid_digit(data,a)
    else:
        return False



"""GTIN_13桁"""
def GTIN_13_check(data):
    return isCheck_code(data,13)

def Make_GTIN_13(maker_code,product_code):
    if len(maker_code)!=9:
        return False
    if len(product_code)!=3:
        return False
    data=str(maker_code+product_code)
    a=data+str(_Calculation_digit_odd(data,13))
    return a



"""GTIN短縮コード_13桁"""
def GTIN_8_check(data):
    return isCheck_code(data,13)

def Make_GTIN_8(product_code,item_code):
    if len(product_code)!=6:
        return False
    if len(item_code)!=1:
        return False
    data=str("00000"+product_code+item_code)
    a=data+str(_Calculation_digit_odd(data,13))
    return a



"""集合包装用商品コード_14桁"""
def GTIN_14_check(data):
    return isCheck_code(data,14)

def Make_GTIN_14(indicator_code,maker_code,product_code):
    if len(indicator_code)!=1:
        return False
    if len(maker_code)!=9:
        return False
    if len(product_code)!=3:
        return False
    data=str(indicator_code+maker_code+product_code)
    a=data+str(_Calculation_digit_even(data,14))
    return a



"""U.P.C._12桁"""
def UPC_12_check(data):
    return isCheck_code(data,12)

def Make_UPC_12(UPC_Company_Prefix,item_code):
    if len(UPC_Company_Prefix)!=7:
        return False
    if len(item_code)!=4:
        return False
    data=str(UPC_Company_Prefix+item_code)
    a=data+str(_Calculation_digit_even(data,12))
    return a



"""SSCC出荷包装シリアル番号_18桁"""
def GTIN_18_check(data):
    return isCheck_code(data,18)

def Make_GTIN_18(Extension_code,maker_code,Serial_code):
    if len(Extension_code)!=1:
        return False
    if len(maker_code)!=9:
        return False
    if len(Serial_code)!=7:
        return False
    data=str(Extension_code+maker_code+Serial_code)
    a=data+str(_Calculation_digit_even(data,18))
    return a



"""以下動作チェック"""
"""動作チェック"""
print("正常検出")
print(GTIN_13_check("4569951116179"))
print(GTIN_8_check("0000049968712"))
print(GTIN_14_check("14569951116176"))
print(UPC_12_check("012345678905"))
print(GTIN_18_check("045699511100000016"))
print("誤り検出")
print(GTIN_13_check("4569951116170"))
print(GTIN_8_check("0000049968711"))
print(GTIN_14_check("14569951116175"))
print(UPC_12_check("012345678904"))
print(GTIN_18_check("045699511100000014"))
"""生成チェック"""
print("正常出力")
print(Make_GTIN_13("456995111","617"))
print(Make_GTIN_8("499687","1"))
print(Make_GTIN_14("1","456995111","617"))
print(Make_UPC_12("0123456","7890"))
print(Make_GTIN_18("0","456995111","0000001"))
print("誤り検出")
print(Make_GTIN_13("4569951114","617"))
print(Make_GTIN_8("499687e","1d"))
print(Make_GTIN_14("1b","456d995111","617"))
print(Make_UPC_12("012d3456","d7890"))
print(Make_GTIN_18("01","45699d5111","50000001"))
"""コード内整合性チェック"""
print("正常検出のみ")
print(GTIN_13_check(Make_GTIN_13("456995111","617")))
print(GTIN_8_check(Make_GTIN_8("499687","1")))
print(GTIN_14_check(Make_GTIN_14("1","456995111","617")))
print(UPC_12_check(Make_UPC_12("0123456","7890")))
print(GTIN_18_check(Make_GTIN_18("0","456995111","0000001")))
