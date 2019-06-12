## js原生函数

js常用的原生函数有：
- String()
- Number()
- Boolean()
- Array()
- Object()
- Function()
- RegExp()
- Date()
- Error()
- Symbol() (ES6语法)

### String
```
// String

let hll = new String("Hello world!")
console.log(hll)
console.log(hll.toString())
console.log(typeof hll)
console.log(hll instanceof String)

// 执行结果 
// String {"Hello world!"}
// Hello world!
// object
// true
```
- chatAt //方法可返回指定位置的字符
- indexOf // 寻找某元素的`开始`位置
- lastIndexOf // 寻找某元素的`结束`位置
- subStr(start, length) // 可在字符串中抽取从 start 下标开始的指定数目的字符 返回新的字符串
- subString(start, end) // 方法用于提取字符串中介于两个指定下标之间的字符
- slice // 方法可从已有的数组中返回选定的元素
- toUpperCase // 字符串全都变成大写
- toLowerCase // 字符串全都变成小写
- trim // 字符串去除两边的空格

### Object相关知识
相关Api
Object.prototyppe.toString().call(/* 参数 */) // 用来识别typeof类型为Object的参数的内部分类 ---> [[class]]
```
Object.prototype.toString.call(new String("121")) // "[object String]"
Object.prototype.toString.call(["1", "2", "1"]) // "[object Array]"
Object.prototype.toString.call(/regex-literal/i) // "[object RegExp]"
Object.prototype.toString.call(null) // "[object Null]"
Object.prototype.toString.call(undefined) // "[object Undefined]"
... 
Object.prototype.toString.call( 42 ) // "[object Number]"
Object.prototype.toString.call( '42' ) // "[object String]"
Object.prototype.toString.call( true ) // "[object Boolean]"
```
valueOf()

### 原生函数作为构造行数

### Symbol()
> 符号并非对象，而是一种简单标量基本类型

