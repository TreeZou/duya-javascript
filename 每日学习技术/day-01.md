<!--
 * @Author: DuYa
 * @LastEditors: DuYa
 -->

# day-01 掘金

[Dom Diff   初探](https://juejin.im/post/5e8445bfe51d4546ce27b5a6?utm_source=gold_browser_extension)

<image src="https://img-blog.csdn.net/20180717182348969" width="600" height="500" title="csdn上的copy的DOM diff树"/>

对于   DOM diff   而言，相对于直接操作   DOM，有很多好处

对于，我刚学习   javascript   的时候，很多人会跟我说：尽量少操作   dom   元素，因为操作越多，页面的加载就会越卡越慢。相对于直接操作   DOM，页面修改可能做不要局部的刷新，全局的更新会非常的损耗性能。DOM diff   有利于节省资源，是的，在一定的意义上能做到提高页面加载的性能，但你知道  VirtualDOM  为什么能提高页面加载的性能吗？它到底怎么做的呢？

对于掘金的这篇文章来说，能初步认识   DOM Diff   的执行的流程，能做到入门，还是不错的。对于，DOM   的知识有很多，还需要查阅这方面的资料，需要看很多知识呀

> 技术，是要实践才有意义的
> 技术，要精

> DIFF 算法在执行过程中会有有三个维度，分别是 Tree DIFF、Component DIFF 和 Element DIFF，
> 执行时按顺序依次执行，它们的差异仅仅因为 DIFF 粒度不同、执行先后顺序不同。

在网上找了一张图

<image src="https://img-blog.csdn.net/2018071718264787" />

可以从图中看出一下过程：

1. R 作为新老树的根节点， Tree Diff 发现没有改变，进入下一个阶段（失望的走了，溜了溜了~）
2. Component DIFF 从左侧老新会开始对比，发现 A 组件没有了（是真的没有了），然后，新的那边就会直接进行销毁（痛苦，技术的更新怎么这么残酷）。
3. 到 Element DIFF 的时候，突然发现新 Tree 有了新节点（哇~），也就是树，新 Tree，有了新的子节点，在实现与底层就是创建了新的节点

##   假设现在有一个需求，就是  Mock  一个   VirtualDOM，你该怎么做呢？<VirtualDOM> （必须做）（泛型类型为   VirtualDOM<也就是返回值类型>）

<解题>?:any

## 传送门

DEMO: [DEMO](./demo/diff.html)
