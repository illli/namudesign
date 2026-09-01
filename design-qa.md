# NAMU DESIGN 设计验收

## 对照目标

- 视觉真值：用户在英文首页 Capabilities 区域的浏览器标注；本地复现截图 `qa/en-capabilities-overflow-before.png`，360 × 780 px。
- 实现页面：`http://127.0.0.1:8000/en/`。
- 状态：英文首页、Capabilities 区域、亮色模式。
- 目标：英文长标签在卡片边框内完整显示，不影响中文版或其他响应式尺寸。

## 对照证据

- 同屏对照：`qa/en-capabilities-overflow-comparison.png`，720 × 780 px；左侧为修复前复现，右侧为相同 375 × 812 CSS 视口下的修复后页面。
- 修复前：`qa/en-capabilities-overflow-before.png`，375 × 812 CSS 视口，设备像素比 2，浏览器内容截图为 360 × 780 px。
- 修复后同视口：`qa/en-capabilities-overflow-fixed.png`，相同像素尺寸与状态。
- 用户标注尺寸复核：`qa/en-capabilities-responsive-final.png`，489 × 766 CSS 视口，设备像素比 2，浏览器内容截图为 474 × 743 px。
- 两张同视口截图未缩放，直接并排比较；关键标签文字在整图中清晰可读，无需额外聚焦裁切。

## Findings

- 无剩余 P0、P1 或 P2 差异。
- 字体与排版：375px 与 489px 下继续使用 Source Sans 3、20px、300 字重、28px 行高；两行标签卡片高度由 50px 调整到 78px 并垂直居中。1100px 下英文标签使用 18px 单行显示，全部完整落在边框内。
- 间距与布局：窄屏保持三列与 14px 间距；桌面保持 920px 总宽度和六列，仅将英文列间距收紧为 14px，不改变能力区的结构与中文版布局。
- 色彩：边框、背景和文字颜色变量未修改；暗色模式实测背景 `rgb(17, 17, 17)`，标签无溢出。
- 图片：本次不修改首页作品图片、裁切、比例或滚动轨道。
- 文案：Brand Design、Concept Design、Experience Design、GEO、Campaign Design、3D & Motion 六项完整保留，无截断、重叠或越界。

## 响应式与交互验证

- 375、489、768、1100 四个 CSS 视口均无页面横向溢出。
- 六个标签在四个视口中 `scrollWidth <= width` 且 `scrollHeight <= height`。
- 375 与 489 为 78px 两行容器；768 为宽三列、50px 容器；1100 为六列单行、50px 容器。
- 中文首页 489px 下仍为原 50px 标签，六项均无溢出。
- 亮色与暗色模式均通过；浏览器日志无 error 或 warning；`make check` 通过。

## Comparison history

1. [P2] 修复前固定 50px 高度无法容纳 28px 行高的两行英文标签，五个标签的内容高度为 66px，文字越过卡片下边框。
2. 修复：640px 以下的英文标签改为 78px 高并居中；1024px 以上收紧英文六列间距并使用 18px 单行文字。
3. 修复后同视口并排复核，六个标签均完整显示；多视口、中文回归和暗色模式均无剩余 P0/P1/P2 差异。

## Follow-up polish

- 无。本轮仅修正英文本地化文案的响应式承载，不改相邻内容。

final result: passed
