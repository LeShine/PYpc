JS笔记

数据类型：

    Number:整数、浮点数、负数、NaN、Infinity（无限大）
        NaN != NaN, isNaN(NaN) == true
        ==: 自动转换数据类型再比较
        ===：先比较数据类型再比较值

    字符串：'单引号'、"双引号"、`反引号代表多行字符串`
        
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
        
        数组方法：
            获取长度：arr.length
            *改变arr的length会导致arr大小变化，对arr索引赋值会修改arr，如果赋值                 索引超过arr length，arr的大小会变化
            搜索指定元素位置：arr.indexOf('x')
            截取arr部分元素：arr.slice(m,n)  m <= arr < n
                             arr.slice(m) m <= arr
                             arr.slice() arr
            向arr末尾添加若干元素：arr.push(x)
            删除arr末尾元素：arr.pop()
            向arr头部添加若干元素：arr.unshift(x)
            删除arr头部元素：arr.shift()
            arr排序：arr.sort()
            arr反转：arr.reverse()
            修改arr的万能方法：splice()
                arr.splice(m,n,a,b):从m索引开始删除n个元素，添加a,b
                arr.splice(m,n)：从m索引开始删除n个元素，不添加
                arr.splice(2,0)：不删除
            连接两个arr：arr.concat(arr) *返回新的arr
            用指定字符连接arr所有元素：arr.join('char') *返回字符串


    对象：键值对的组合

    变量：英文、数字、$、_ 的组合，不能数字开头，不能是保留字


严格模式：严格模式下所有变量必须先声明再使用，不声明直接使用的变量是全局变量
    
    strict：”use strict“放在js代码第一行


