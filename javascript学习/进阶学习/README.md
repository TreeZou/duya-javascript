<!--
 * @Author: DuYa
 * @LastEditors: DuYa
 -->

# 进阶教程

1. [原型](./原型.md)
2. [高阶函数](./高阶函数.md)

## 原型链的面试题

### 第一题

```javascript
function A() {}

A.prototype.n = 1;

var b = new A();

A.prototype = {
  n: 2,
  m: 3
};

var c = new A();

console.log(b.n, b.m, c.n, c.m);
```

### 第二题

```javascript
var F = function() {};
Object.prototype.a = function() {
  console.log("a()");
};

Function.prototype.b = function() {
  console.log("b()");
};

var f = new F();
// var c = new Function();

f.a && f.a();
f.b && f.b();
F.a();
F.b();

// c.a();
// c.b();
```
