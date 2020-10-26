# vuex

vuex的5个属性：
- state
- getters
- mutations
- actions
- modules

### 1. state
```bash
state为vuex存基本属性的地方
vuex使用单一状态树，即用一个对象就包含了全部的状态数据。state作为构造器选项，定义了所有我们需要的状态基本参数

平时我们在项目中使用vuex的state可以在, computed中去调用

e.g.
import { mapGetters } from "vuex";

export default {
  ...
  computed: {
    ...mapGetters(["app"])
  }
  ...
}
```

### 2. getters
```bash

```

### 3. mutations

### 4. actions

### 5. mudules

