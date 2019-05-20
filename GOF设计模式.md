GOF(Gang of four)，也就是传说中的“四人组”。 

> 《设计模式》

那么设计模式到底有`哪些`呢？

GOF设计模式分三大类，这三个大类分别是：`创建型模式、结构型模式、行为模式`。

### 创建型模式
1. [工厂方法模式(factory method)](https://blog.csdn.net/qq_35023116/article/details/87369753) 
百度百科的解释：**核心工厂类不再负责所有产品的创建，而是将具体创建的工作交给子类去做，成为一个抽象工厂角色，仅负责给出具体工厂类必须实现的接口，而不接触哪一个产品类应当被实例化这种细节。**
举个栗子🌰 客户-员工-工厂
比如说，有一个`客户`需要一张a4纸打印东西，店员接收到`客户`的需求，立即向`Factory`寻求帮助，`Factory`让`客户`带到他面前来，`客户`不耐烦地又将需求说了一遍，`Factory`一脸嫌弃的跟店员说：“打印，a4，打印***内容，出来吧！”。然后，`客户`高高兴兴地走了。

```
// 打印店Factory
var Factory = function(type, paper, ctn) {
	if(this instanceof Factory) {
		return new this[type](paper, ctn)
	} else {
		return new Factory(type, paper, ctn)
	}
}
Factory.prototype = {
	print: function(paper, ctn) {
		return {
			content: "现在打印一张包含" +  ctn + "且大小为" + paper  + "的**"
		}
	}
}

// 客户A
var A = new Factory("print", "A4", "我是小A")

// 生成中 ---
console.log(A.content) // "现在打印一张包含我是小A且大小为A4的**"
```
2. [抽象工厂模式](https://blog.csdn.net/qq_35023116/article/details/87369753)
百度百科的解释：**客户类和工厂类分开。消费者任何时候需要某套产品集合时，只需向抽象工厂请求即可。抽象工厂会再向具体的工厂生产出符合产品集规格的产品.**
举个栗子🌰 用户-抽象工厂-具体工厂
A用户忘了B交流网站的第C条信息，他跟`Abract Factory`说：“Abract Factory, 你能告诉我昨天我在B交流网站发的第C条信息吗？”。`Abract Factory`想了想说：“好的，这我需要跟`Factory`说一下”。
```
// Factory
var Factory = function(sub, super) {
	if(typeof super === "function") {
		
	} else {
	
	}
}
```
--- 待续 ---

### 结构型模式
### 行为模式

`总结设计模式 不定时更新`


