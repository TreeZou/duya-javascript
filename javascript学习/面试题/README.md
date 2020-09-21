<!--
 * @Author: DuYa
 * @LastEditors: DuYa
 -->

# 💯 面试题整理

1.  如何判断 0.1 + 0.2 月 0.3 想等？

            产生不相等情况的原理：

            - 首先，确定的时在执行 0.1 + 0.2 的过程中，会涉及三次精度的丢失。
            - 其次， 涉及一个技术点，关于 IEEE754 标准中 64 位的储存格式，比如 11 位存偏移值
            - 最后，这个你要确定这种现象不是 ECMAScript 独有的

            怎么判断呢？

            方法 1

            利用工具包 [math.js](https://mathjs.org/)

            ```HTML
            <!DOCTYPE html>
              <html lang="en">
                <head>
                  <meta charset="UTF-8" />
                  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                  <meta http-equiv="X-UA-Compatible" content="ie=edge" />
                  <title>如何判断 0.1 + 0.2 月 0.3 想等？</title>
                  <script src="https://unpkg.com/mathjs/dist/math.min.js"></script>
                </head>
                <body>
                  <script>
                    console.log(
                      math.format(math.add(math.bignumber(0.1), math.bignumber(0.2)))
                    );
              </script>

            </body>

          </html>

            ```

            方法2

            使用原生方法toFixed

            ```javascript
                console.log(parseFloat((0.1 + 0.2).toFixed(10)))
            ```
2. 以下代码的输出
```javascript
 function Foo() {
     getName = function () { alert (1); };
     return this;
 }
 Foo.getName = function () { alert (2);};
 Foo.prototype.getName = function () { alert (3);};
 var getName = function () { alert (4);};
 function getName() { alert (5);}

 //请写出以下输出结果：
 Foo.getName();
 getName();
 Foo().getName();
 getName();
 new Foo.getName();
 new Foo().getName();
 new new Foo().getName()
```

3. 前端安全(2020-9-19日面试阿里)

4. promise的用法(2020-9-19日面试阿里)

5. 项目介绍(2020-9-19日面试阿里)

6. 自我介绍(2020-9-19日面试阿里)

7. 跨域的几种(2020-9-19日面试阿里)

8. 源码的掌握度(2020-9-19日面试阿里)
