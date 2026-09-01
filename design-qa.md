# NAMU DESIGN 设计验收

## 对照目标

- 视觉真值：`design-reference/home.png`，1100 × 1562 px，Figma 首页 `119:213`
- 交互参考：`https://www.hugeinc.com/`；截图 `qa/huge-reference-home.png`，1265 × 712 px
- 实现页面：`http://127.0.0.1:8000/zh/` 与 `/en/`
- 状态：亮色模式、连续横向作品轨道

## 对照证据

- 桌面同屏对照：`qa/home-marquee-desktop-comparison.png`
  - Figma 裁为 1085 × 854 px。
  - 实现为 1085 × 854 px；CSS 视口 1100 × 866，device scale factor 1，浏览器滚动条占 15px。
- 桌面实现：`qa/home-marquee-desktop-qa.png`
- 手机实现：`qa/home-marquee-mobile-final.png`，360 × 780 px；CSS 视口 375 × 812，device scale factor 1。
- 动态证据：桌面轨道在 1.2 秒内从 `translateX(-44.2px)` 移至 `translateX(-100.5px)`；两组各 1185px、组间 60px、轨道 2430px，循环位移 1245px，与重复组起点精确重合。

## Findings

- 无 P0、P1 或 P2 差异。
- 字体与排版：Logo、INFO、Source Sans 3 / PingFang SC / Source Han Sans CN、36/56 标题节奏和换行保持 Figma 视觉。
- 间距与首屏：桌面 1100 × 866 时作品区从 `y=462` 延伸至 `y=866`；手机 375 × 812 时首页舞台从 `y=94` 延伸至 `y=812`。能力标签从下一屏开始，符合按 `100svh` 计算首屏的要求。
- 色彩：亮色与暗色变量保持一致，暗色实测背景为 `rgb(17, 17, 17)`；动画在两种主题下持续运行。
- 图片：继续使用四张 Figma 原始素材；尺寸比例和高低错落关系保留。重复组只用于无缝循环，不重复进入辅助技术内容。
- 文案与链接：第 1 张链接方太，第 2 张链接 FARFETCH China；中文与英文 URL 均正确。后两张为不跳转的 `<figure>` 占位图。
- 交互：借鉴 Huge 的整图点击与轻微 hover 放大，但按用户要求改为 28 秒线性、无限、自动横向循环。鼠标悬停、键盘聚焦和触摸按下时暂停，离开后恢复；`prefers-reduced-motion` 下停止自动运动并改为可横向滚动。

## 响应式与交互验证

- 375 × 812、768 × 800、1100 × 866、1280 × 900 的中英文首页均无横向溢出。
- 各视口中 `.home-stage` 底部与视口底部相同，能力标签从第二屏开始。
- 方太链接实测进入 `/zh/work/fotile/`；FARFETCH China 链接实测进入 `/zh/work/farfetch-china/`。
- 动画、亮暗模式、语言入口并存；浏览器控制台无 error 或 warning。

## Comparison history

1. 初版 P2：手机端沿用固定图库高度，375 × 812 时作品区比首屏多出 42px。
2. 修复：将文案和作品区组成 `.home-stage`，使用 `min(..., calc(100svh - header))` 与 `auto + 1fr` 网格分配剩余高度。
3. 初版 P2：移动中的链接在自动化点击时可能因轨道继续位移而命中相邻作品。
4. 修复：pointer down 时立即暂停轨道，pointer up/cancel 后延迟恢复；两条案例链接重新实测通过。
5. 最终复核：没有剩余 P0/P1/P2 差异。

## Follow-up polish

- 两张占位图未来获得正式案例页后，只需在内容数据中补充 `route` 与本地化 `link_label`。

final result: passed
