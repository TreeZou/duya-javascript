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
