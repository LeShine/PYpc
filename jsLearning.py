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
            *改变arr的length会导致arr大小变化，对arr索引赋值会修改arr，如果赋值超过arr length，arr的大小会变化
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


    对象：键值对的组合,键必须是字符串
        检测随想是否有某属性：prop in obj   
            *in判断属性存在不一定是对象的，也可能是对象继承的。eg：'toString' in obj == true
            要判断属性是否是对象本身的用 obj.hasOwnProperty(prop)

    变量：英文、数字、$、_ 的组合，不能数字开头，不能是保留字

    条件判断：if(){}else{}

    循环：for(;;){}
          for in : for(var key in a){}
          while(){}
          do()while{}

    Map:
        var m = new Map()
        添加元素：m.set()
        是否存在：m.has()
        获取：m.get()
        删除：m.delete()
            *多次对同一个key赋值，后面的会覆盖前面的

    Set:也是一个key集合，但不存储value,重复元素在set中自动过滤
        var s1 = new Set()
        var s2 = new Set([1,2,3])
        添加元素：s.add()
        删除元素：s.delete()
        

        * map和set是ES6标准新增的数据类型，视浏览器兼容情况使用,无法用下标访问
    
    iterable: 包含Array,Map，Set
        *具有iterable类型的集合可以使用for...of循环遍历
        for(var x of a){}
        for of 与 for in 的区别：
            for in :遍历的是对象的属性，但不包含数组的length 属性
            for of :只循环集合本身的元素
        forEach:iterable的内置方法
            a.forEach(function(element,index,array){})
            * set 没有索引，回调函数的前两个参数都是元素本身，map的参数依次是vaule,key,map本身
            js的函数调用不要求参数一致，因此可只获得element eg:a.forEach(function(element){})
        

严格模式：严格模式下所有变量必须先声明再使用，不声明直接使用的变量是全局变量
    
    strict：”use strict“放在js代码第一行


