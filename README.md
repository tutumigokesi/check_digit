# check_digit
GTIN（JANコード）標準タイプ（１３桁）、関数`GTIN_13_check_(”GTINコード（ｓｔｒ型１３桁）”)`

GTIN（JANコード）短縮タイプ（８桁）、関数`GTIN_8_check("GTIN8短縮コード（ｓｔｒ型８桁）"):`

GTIN（集合包装用コード）（１４桁）、関数`GTIN_14_check(”集合包装用商品コード（ｓｔｒ型１４桁）”):`

U．P．C．（１２桁）、関数`UPC_12_check(”U.P.C.コード（ｓｔｒ型１２桁）”):`

SSCC（１８桁）、関数`GTIN_18_check(”SSCC出荷シリアル番号（ｓｔｒ型１８桁）”)`

の整合性をチェックデジットを使い、TrueかFalseを返す。

また、

GTIN（JANコード）標準タイプ（１３桁）、`Make_GTIN_13("GS1事業者コード（９桁）",”商品アイテムコード（３桁）”):`

GTIN（JANコード）短縮タイプ（８桁）、`Make_GTIN_13("GS1事業者コード（６桁）",”商品アイテムコード（１桁）”):`

GTIN（集合包装用コード）（１４桁）、`Make_GTIN_14("インジケーター（１桁）","GS1事業者コード（９桁）","617（３桁）")`

U.P.C.（１２桁）、`Make_UPC_12("U．P．C．Company（７桁）","商品アイテムコード（４桁）")`

SSCC（１８桁）、`Make_GTIN_18(”拡張子(１桁)”,"GS1事業者コード"（９桁）,”シリアル番号（７桁）”)`

の関数に使い、各種引用に値を渡し、GTIN（バーコードの数字）を生成する。


※バーコードの画像は生成されない。（そのうち作りたい）


引用： https://www.gs1jp.org/code/jan/check_digit.html