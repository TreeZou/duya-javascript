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

9. localstorge怎么实现过期时间(2020-09-23日涂鸦智能)

10. localstorge session 和 cookies(2020-09-23涂鸦智能)

11. flex的几个参数和含义(2020-09-23阿里)

12. vue3的新特性（2020-9-23阿里和涂鸦智能）

13.
```javascript
function fn1(arg) { return arg + 1 }
function fn2(arg) { return arg * 2 }
function fn3(arg) { return arg + 3 }
function fn4(arg) { return arg * 3 }

function compose (...args) {
    let arr = args.reverse();
    return function (value) {
        return arr.reduce((prev, cur) => {
            return cur(prev)
        }, value)
    }
}

console.log(compose(fn1, fn2, fn3, fn4)(2))
``` 

14.
```js
// axios.request(requestParams)
// poll().then().catch()
async function poll (requestParams, { isValid, delay = 1000, maxTimes = 1 }) {
    let timeout = null;
    function request () {
        clearTimeout(timeout);
        let timeout = null;
        let result = {
            status: "success",
            value: null
        };

        maxTimes --;
        axios.request(requestParams)
        .then(res => {
            if (isValid) {
                result = {
                    status: "success",
                    value: res
                };
            } else if (isValid && maxTimes > 0) {
                result = request();
            } else {
                result = {
                    status: "failed",
                    value: "超时"
                }
            }

            return result;
        })
        .catch(error => {
            return {
                status: "failed",
                value: error
            }
        })
    }
    return new Promise((resolve, reject) => {
        try {
            // 如果maxTimes的次数还有
            resolve(request());
        } catch(error) {
            reject(error);
        }
    })
}

```
15. Promise.all的实现原理（2020-09-23 涂鸦智能）

16. 首屏加载是什么？怎么优化？（2020-09-23 涂鸦智能）

17. 动画的实现方式？怎么评测动画的的流畅度？ （2020-09-23 涂鸦智能）

18. 你所了解的设计模式有哪些？可以说一下订阅发布模式的实现原理吗?（2020-09-23 涂鸦智能）

19. ts中interface和type的区别(2020-09-23 阿里)

20. this.$set(2020-09-23 涂鸦智能)
