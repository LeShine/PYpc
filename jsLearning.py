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
        
        作用域：用var声明的为局部变量，内层可访问外层声明的变量，反之不可，不用var声明的是全局变量，js中应避免全局变量。

        变量提升：js中变量可以先使用后声明，但是变量的值不会提升，所以应遵守先声明后使用。

        全局作用域：不在任何函数内定义的变量具有全局作用域，eg:window，全局作用域的变量实际上被绑到window的一个属性。
            以变量方式定义的函数也是一个全局变量，因此顶层函数也是一个全局变量，并绑定到window对象。

        名字空间：不同JavaScript文件如果使用了相同的全局变量，或者定义了相同顶层函数，都会造成命名冲突，为此应把所有变量和函数绑定到一个全局变量中。
            //唯一的全局变量MYAPP
            var MYAPP = {};
            //其他变量
            MYAPP.name = '';
            MYAPP.version = '';
            //其他函数
            MYAPP.foo = function(){};


        局部作用域：由于js的变量作用域实际上是函数内部，所以在for循环等语句块中是无法定义局部变量的，因此ES6引入了 let ，其可以声明一个块级作用域变量。

        
    常量：ES6引入const来定义一个常量，在此之前用全部大写的变量表示一个常量。const与let都具有块级作用域。

    解构赋值：ES6引入，可同时对一组变量赋值
        var [x,y,z] = ['a','b','c'];
        let [x,[y,z]] = ['a',['b','c']];
        快速获取对象的属性也可用解构赋值
        var person = {
            name:'xl',
            age:20,
            gender:male,
            phone:'123456'
        };
        var {name,age,phone} = person;

        *解构赋值也可忽略一些元素，如person的gender属性，在对嵌套对象进行解构赋值时要保证对应的层次一样。
        对象进行解构赋值时如果属性不存在，变量将被赋值undefined，如果使用的变量名和属性名不一致，可使用 let {name,phone:pho} = person;解构赋值也可使用默认值 let {name,single=true} = person;解决属性返回undefined的情况。
        


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
        

    函数：底层代码的一种抽象体，不考虑具体实现过程
        js允许函数传入任意个参数，比定义的多或少都行
        arguments：只在函数内部有用，永远指向函数调用者传入的参数，类似arr但不是arr，即使函数不定义任何参数，函数内部还是可以通过arguments获取传入的所有参数值
        rest参数：获取定义参数之外的多余参数
            function f(a, b, ...rest){}
                *传入的参数先绑定已定义参数，多余的以数组形式赋值给rest，传递参数不够已定义参数，rest接受一个空数组
            
    高阶函数：一个函数接收另一个函数作为参数
        
    
严格模式：严格模式下所有变量必须先声明再使用，不声明直接使用的变量是全局变量
    
    strict：”use strict“放在js代码第一行


