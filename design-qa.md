# Design QA：页脚右下角语言与主题控制

**Findings**

- 无遗留 P0/P1/P2 问题。语言与主题控制已位于页脚底行右侧，文字主题切换已替换为清晰的月亮/太阳图标。

**Open Questions**

- 无。

**Implementation Checklist**

- [x] 移动端版权左对齐，语言与主题控制在同一底行右对齐。
- [x] 平板端和桌面端保持底行左右分布。
- [x] 亮色显示月亮图标，暗色显示太阳图标。
- [x] 主题按钮保留 `aria-label`、`aria-pressed` 与键盘焦点状态。
- [x] 检查 8 个中英文页面、375/532/768/1100 CSS px、语言切换、主题切换与控制台。

**Follow-up Polish**

- 无。

## Evidence

- Source visual truth：`qa/footer-controls-before.png`
- Implementation：`qa/footer-controls-after.png`
- Dark implementation：`qa/footer-controls-dark-after.png`
- Full-view comparison：`qa/footer-controls-comparison.png`
- Viewport：532 × 766 CSS px；另验证 375、768 与 1100 CSS px。
- Pixel dimensions：source 与 implementation 均为 517 × 744 px；并排对比为 1034 × 744 px。
- Density normalization：device scale factor 1；前后截图使用相同路由、主题、滚动位置、CSS 视口与像素尺寸，无缩放。
- State：英文首页页脚，亮色模式；另捕获暗色模式并回归中文页面。
- Primary interactions tested：月亮按钮切换至暗色太阳状态、中文/EN 链接双向切换。
- Console errors checked：是，0 条。
- Focused region comparison：页脚控制本身是本次唯一视觉目标，完整页脚截图中的位置、对齐、图标轮廓和底行关系均清晰可读，无需额外裁切。

## Required fidelity surfaces

- Fonts and typography：地址、联系信息、版权与语言文字的字体、字号、字重和行高未改；仅移除 DARK/LIGHT 文字。
- Spacing and layout rhythm：375/532/768 下控制组右边缘与页脚内容右边缘对齐，版权与控制组底边差 1px 且无重叠；1100 延续桌面 50px 内边距。
- Colors and visual tokens：图标继承现有黑白主题；亮色为黑色月亮，暗色为白色太阳，hover 与 focus 继续使用现有 token。
- Image quality and asset fidelity：月亮和太阳均为 Heroicons 24px outline 原始矢量资产，未使用字符、emoji、CSS 图形或手绘 SVG；两枚图标均正常加载。
- Copy and content：语言入口仍显示“中文”或“EN”；主题含义由图标表达，并由无障碍标签补充。

## Comparison history

- Earlier P2：移动端语言与 DARK 控制独占一行并靠左，版权另起下一行，未形成用户要求的页面右下角布局。
- Fix：在 375/532 下让版权与控制组共用网格底行，分别左对齐和右对齐；768 平板端明确放入左右两列的同一底行。
- Post-fix evidence：`qa/footer-controls-comparison.png` 右侧显示控制组贴齐页脚右下角，版权保持左侧，二者无重叠。
- Earlier P2：DARK/LIGHT 使用文字，视觉重量高于辅助控制且不符合图标要求。
- Fix：使用 Heroicons 月亮/太阳图标；由当前主题控制显隐，同时保留按钮状态和焦点轮廓。
- Post-fix evidence：`qa/footer-controls-after.png` 显示亮色月亮；`qa/footer-controls-dark-after.png` 显示暗色太阳。8 个页面在 4 个断点均无溢出、重叠或破图。

final result: passed

---

# Design QA：全站系统字体栈

**Findings**

- 无遗留 P0/P1/P2 问题。全站已统一使用用户指定的系统字体栈，英文长标签与中文正文均无裁切。

**Implementation Checklist**

- [x] `--font-sans` 与 `--font-mono` 的字体顺序与用户说明一致。
- [x] 正文、首页标题、能力标签和案例标题均复用同一 sans 变量。
- [x] 头部 Logo 与 INFO 图片字形、字号、行高和页面结构未改变。
- [x] 检查 8 个中英文页面及 375/532/768/1100/1280 CSS px。

## Evidence

- 英文首页 532 × 766：标题换行自然，作品区位置稳定。
- 中文 Info 375 × 766：正文无异常断行或裁切。
- 40 个路由/视口组合：0 个横向溢出、0 个破图、0 个能力标签裁切。
- Console errors checked：是，0 条。

final result: passed
