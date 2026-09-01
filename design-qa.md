# NAMU DESIGN 设计验收

## 对照目标

- 视觉真值：`design-reference/home.png`，1100 × 1562 px，Figma 首页 `119:213`
- 实现页面：`http://127.0.0.1:8000/zh/`
- 状态：中文、亮色模式、桌面版
- CSS 视口：1100 × 866，device scale factor 1

## 对照证据

- 整页同屏对照：`qa/home-final-stitched-comparison.png`
  - 设计稿裁为 1084 × 1550 px。
  - 实现由同一 1100px CSS 视口下的顶部与页脚截图按 `scrollY=696` 无缩放拼合为 1084 × 1550 px。
- 顶部聚焦对照：`qa/home-final-top-comparison.png`
- 能力区与页脚聚焦对照：`qa/home-final-footer-comparison.png`

## Findings

- 无 P0、P1 或 P2 差异。
- 字体与排版：Source Sans 3 / PingFang SC / Source Han Sans CN 的字重、36/56 标题节奏和换行与设计稿一致。
- 间距与布局：首页关键坐标保持为标题 `y=300`、图库 `y=462`、能力区 `y=962`、页脚 `y=1082`；删除 WORK 卡片后页脚恢复到 Figma 位置。
- 色彩：亮色背景、正文色、边框与设计稿一致；暗色模式仍由相同颜色变量驱动。
- 图片：四张 Figma 原始项目图的顺序、裁切、比例与清晰度保持一致，没有占位图或代码绘制替代品。
- 文案：设计稿正文与联系信息保持一致。年份使用当前年份；语言/主题入口为用户批准的页脚扩展；未核验备案号仍不展示。

## 响应式与交互

- 中文、英文首页在 375 / 768 / 1100 / 1280px 均无横向溢出。
- 两种语言首页的 WORK 卡片和 `.work-list` 均已完全移除。
- 语言入口仍指向对应语言页面；亮暗模式连续切换后可回到亮色状态并保持标签同步。
- 浏览器控制台无 error 或 warning。

## Comparison history

1. 先前 P2：设计稿不存在的两张 WORK 卡片将页脚推离 `y=1082`。
2. 修复：删除两种语言的数据、模板结构、生成逻辑与孤儿样式。
3. 复核：WORK 节点数量为 0，页脚恢复 `y=1082`，整页同屏对照没有剩余 P0/P1/P2 差异。

## Follow-up polish

- 设计稿中的 2025 年份改为当前年份属于预期内容更新。
- 页脚 EN / DARK 为用户批准的功能性扩展，不视为设计漂移。

final result: passed
