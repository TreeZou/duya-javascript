# day03

## 队列

```javascript
// 单向队列
class Queue {
  constructor() {
    this.count = 0;
    this.lowersCount = 0;
    this.items = {};
  }

  enqueue(el) {
    this.items[this.count] = el;
    this.count ++;
  }

  // 从队列中移除元素
  dequeue() {
    if (this.isEmpty()) {
      return undefined;
    }

    const result = this.items[this.lowersCount];
    delete this.item[this.lowersCount];
    this.lowersCount ++;
    return result;
  }

  // 查看对头元素
  peek() {
    if (this.isEmpty()) {
      return undefined;
    }

    return this.items[this.lowersCount];
  }

  isEmpty() {
    return this.count === this.lowersCount;
  }

  size() {
    return this.count - this.lowersCount;
  }

  // 清空队列
  clear() {
    this.count = 0;
    this.lowersCount = 0;
    this.items = {};
  }

  // toString
  toString() {
    if (this.isEmpty()) {
      return '';
    }

    let objString = `${this.item[this.lowestCount]}`;
    for (let i = this.lowestCount + 1; i < this.count; i ++) {
      objString = `${objString}, ${this.items[i]}`;
    }

    return objString;
  }
}
```