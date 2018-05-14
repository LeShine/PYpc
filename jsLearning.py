JS笔记

数据类型：

    Number:整数、浮点数、负数、NaN、Infinity（无限大）
        NaN != NaN, isNaN(NaN) == true
        ==: 自动转换数据类型再比较
        ===：先比较数据类型再比较值

    字符串：‘单引号’、”双引号“、`反引号代表多行字符串`
        
        字符串方法：
            获取长度：s.length
            *字符串是不可变的，s[i] = x 不会改变字符串的值
            全部变大写：s.toUpperCase()
            全部变小写: s.toLowerCase()
            搜索指定字符串出现位置：s.indexOf('x')
            返回指定索引区间的字符串：s.substring(m,n) m <= s < n
                                      s.substring(m) s >= m
            

    布尔值：ture false

    null undefined:

    数组：可包含任意数据类型

    对象：键值对的组合

    变量：英文、数字、$、_ 的组合，不能数字开头，不能是保留字


严格模式：严格模式下所有变量必须先声明再使用，不声明直接使用的变量是全局变量
    
    strict：”use strict“放在js代码第一行
