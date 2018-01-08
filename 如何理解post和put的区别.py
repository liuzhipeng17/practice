patch方法用来更新局部资源，这句话我们该如何理解？

假设我们有一个UserInfo，里面有userId， userName， userGender等10个字段。可你的编辑功能因为需求，

在某个特别的页面里只能修改userName，这时候的更新怎么做？

人们通常(为徒省事)把一个包含了修改后userName的完整userInfo对象传给后端，做完整更新。

但仔细想想，这种做法感觉有点二，而且真心浪费带宽(纯技术上讲，你不关心带宽那是你土豪)。

于是patch诞生，只传一个userName到指定资源去，表示该请求是一个局部更新，后端仅更新接收到的字段。

而put虽然也是更新资源，但要求前端提供的一定是一个完整的资源对象，

理论上说，如果你用了put，但却没有提供完整的UserInfo，那么缺了的那些字段应该被清空.



补充一下，PATCH 与 PUT 属性上的一个重要区别还在于：PUT 是幂等的，而 PATCH 不是幂等的。
幂等是一个数学和计算机学概念，在计算机范畴内表示一个操作执行任意次对系统的影响跟一次是相同。

在HTTP/1.1规范中幂等性的定义是:

Methods can also have the property of "idempotence" in that (aside from error or expiration issues) the side-effects of N > 0 identical requests is the same as for a single request.

如：POST 方法不是幂等的，若反复执行多次对应的每一次都会创建一个新资源。
如果请求超时，则需要回答这一问题：资源是否已经在服务端创建了？
能否再重试一次或检查资源列表？

而对于幂等方法不存在这一个问题，我们可以放心地多次请求。