<!--
 * @Author: DuYa
 * @LastEditors: DuYa
 -->

# IIFE

全称：Immediately-Invoked Function Expression

作用：

1. 隐藏实现
2. 不会污染外部（全局）命名空间

```javascript
(function() {
  // 匿名函数自调用
  var a = 3;
  console.log(a + 3);
})();

(function() {
  var a = 3;

  function test() {
    console.log(a);
  }

  windows.$ = function() {
    // 向外部暴露一个函数
    return {
      test: test
    };
  };
})();

$().test();
```
