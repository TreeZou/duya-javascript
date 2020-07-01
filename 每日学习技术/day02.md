# 每日学习

## 🐷javascript数组

> 内存数据结构

```javascript
let dayOfWeek = new Array();
dayOfWeek = new Array(7);
dayOfWeek = new Array("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday");
```

### 访问元素和迭代数组
```js
let arr = ["duya", "zoujun"];
for (let i = 0; i < arr.length; i ++) {
  console.log("My position " + i);
}

// 斐波那契数列
let fibonacci = [];
fibonacci[0] = 1;
fibonacci[1] = 1;

for (let i = 2; i < 20; i ++) {
  fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2];
}
console.log(fibonacci)

// 向数组的开头插入元素
数组.unshift();

Array.prototype.DIYUnshift = function(value) {
  for (let i = this.length; i >= 0; i --) {
    this[i] = this[i - 1];
  }

  this[0] = value;
}

// 删除元素
Array.prototype.DIYDelete = function(index) {
  this.splice(index, 1);
  return this;
}

// 删除末尾元素
数组.pop();

// 删除开头元素
for (let i = 0; i < 数组.length; i ++) {
  数组[i] = 数组[i + 1];
}

数组.shift();

数组.splice();

concat() 合并两个或多个数组

every() 遍历数组，满足要求则返回true, 否则返回false

filter() 根据自己的要求筛选数组

forEach() 遍历数组，返回值为undefined

join() 将数组以某个连接符进行拼接，拼接成字符串

indexOf() 返回从头部为地基开始查询满足要求的第一个位置

lastIndexOf() 返回从头部为地基开始查询满足要求的最后一个位置

map() 遍历数组，返回数组list

reverse() 将数组倒叙，返回倒叙后的数组

slice() 截取数组，返回截取的数组组成新的数组

some() 遍历数组，只要有一个满足自己设定的要求则返回true,否则返回false

sort() 对数组按照自己设定的要求进行一定的排序

totString() 将数组当作字符串返回

valueOf() 和toString()类似，将数组当作字符串输出

reduce((prev, current, index, array) => {
  // 返回累加值
})

ECMAScript 6 的数组的新功能
copyWithin()

entries()

includes()

find()

findIndex()

fill()

from()

keys()

of()

values()
```