在 Jupyterlab 笔记中使用 LlamaIndex ，需要加入有关异步处理。

为支持嵌套事件循环，需要：

```python
import nest_asyncio
nest_asyncio.apply()
```
