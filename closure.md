### Closure
`闭包的本质是词法作用域和函数`

> javascript闭包无处不在，前提你必须认出它并接纳它

> 词法作用域  

词法作用域，被绝大多数语言所使用，非常常见。要理解词法作用域的原理，就需要先了解一下词法分析这个概念。
词法分析出现在javascript的编译阶段且是第一阶段。词法分析阶段处理一串源代码字符串，将字符串解析成词法单元（token），并将token赋予含义作为某种状态解析然后输出。
在某些方面来说，词法分析在很大程度上决定了词法作用域（也有一些欺骗元素决定词法作用域，比如：with 和 eval）。通俗的讲，也就是词法作用域基于写程序时，变量和作用域的块在何处被编写定义所决定的。

```
function foo() {

  // 内部函数 A
  function A() {
    // TODO
  } // this is a simple closure
  
}
```

```
function bar() {
  // TODO
}

function foo() {
  bar() // this is a closure
}
```

> 函数

函数作为参数传递给其它的函数或者foo函数返回内部的函数 以便其它的对象能够访问

```
function foo(fn) {
  fn() // 这也是一种闭包 将函数作为参数传递
}

function bar() {
  // TODO
}

foo(bar)
```
or

```
function foo() {
  
  function bar() {
    // TODO
  }
  
  return {
    bar: bar
  }
}
```


