写一个函数满足以下要求：
第 N 个泰波那契数 T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 满足 Tn+3 = Tn + Tn+1 + Tn+2
// n的取值范围 0 <= n <= 37

```javascript
export function tribonacci(n) {
  let res = 0;
  const AUX = {
    // 辅助函数
    0: 0,
    1: 1,
    2: 1
  };
  if (n < 3) return AUX[n];
  return get(n);
  function get(num) {
    if (num >= 3) {
      return get(num - 1) + get(num - 2) + get(num - 3);
    } else {
      return res + AUX[num];
    }
  }
}
```
