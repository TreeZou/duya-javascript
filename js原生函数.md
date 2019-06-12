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
