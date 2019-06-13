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
- chatAt(/* 位置 */) //方法可返回指定位置的字符
- indexOf(searchvalue,fromindex) // 寻找某元素的`开始`位置
- lastIndexOf(searchvalue,fromindex) // 寻找某元素的`结束`位置
- subStr(start, length) // 可在字符串中抽取从 start 下标开始的指定数目的字符 返回新的字符串
- subString(start, end) // 方法用于提取字符串中介于两个指定下标之间的字符
- slice(start,end) // 方法可从已有的数组中返回选定的元素
- toUpperCase // 字符串全都变成大写
- toLowerCase // 字符串全都变成小写
- trim(str) // 字符串去除两边的空格

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

### 讲一下JSON序列化的一些`偏激`方法
当要序列化的对象中具有toJSON方法的时候，JSON.stringify()会以toJSON方法进行解析。当JSON序列化对象的时候，如果出现死循环，会出现错误的`学生报道`

> tip: 在JSON序列化的时候有一些不怎么友善的`小东西`（不安全），我们尽可能的避免这些错误，这些包括：undefined、function、symbol（这些会自动化为null），但值得注意的是JSON.stringify( undefined ) =>  undefined  JSON.stringify(function() {}) => undefined JSON.stringify({a: 1, b: function() {}}) => "{"a":1}"

```
var hll = {
  val: [1, 2, 3],
  toJSON: function() {
    return "["+ this.val.slice(1).join("-") +"]"
  }
}

JSON.stringify(hll)

// 执行结果 ""[2-3]""
```
```
var r = {
	a: [1, 2, 3],
	b: 1,
	c: 'dd',
	d: function() {}
}

JSON.stringify(r, function (k, v) { if(k !== 'b') return v }, 3)

// 执行结果
// "{
//    "a": [
//       1,
//       2,
//       3
//    ],
//    "c": "dd"
// }"
```
this is very amazing!

