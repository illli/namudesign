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

# Design QA：首页服务能力卡片与局部排版

**Findings**

- 无遗留 P0/P1/P2 问题。服务卡片保留参考图的信息层级，并按 NAMU 现有线框视觉与页面宽度完成响应式适配。

**Open Questions**

- 4 个箭头当前是非交互视觉提示；待用户提供对应目标页面后再升级为链接。

**Implementation Checklist**

- [x] 中文首页标题移除硬编码换行，窄屏自然折行。
- [x] 品牌、产品、网站、开发 4 张卡片含标题、说明与官方线性箭头。
- [x] 桌面 4 列、平板 2 列、手机 1 列。
- [x] 页脚语言与主题图标间距为 40px。
- [x] 检查中英文、亮暗模式、375/532/768/1100/1280 CSS px。

## Evidence

- Source visual truth：用户本轮附加的 4 卡片参考图，原始 2760 × 410 px；会话预览归一化为 2048 × 304 px。
- Implementation：浏览器本轮捕获的中文首页 1280 × 800 与 532 × 766 CSS px 视图。
- State：中文首页，亮色与暗色；另回归英文首页及全部 8 个页面页脚。
- Full-view comparison：参考图为超宽四列；实现桌面保持四列与相同标题/说明/右下箭头层级，并将填充卡片适配为 NAMU 现有 1px 线框。
- Focused region comparison：桌面卡片区与移动端单列卡片区均已单独目视检查；标题、说明、箭头、边框与间距清晰可读。
- Primary interactions tested：语言切换保留；主题切换后边框、文字与箭头均正确反色；箭头无虚假交互。
- Console errors checked：是，0 条。

## Required fidelity surfaces

- Fonts and typography：沿用用户指定系统字体栈；标题 27/24px、正文 16/15px，卡片内无裁切。
- Spacing and layout rhythm：桌面 4 列、平板 2 列、手机 1 列；卡片内为上标题、中说明、右下箭头。
- Colors and visual tokens：沿用 `--color-line`、`--color-muted` 与亮暗模式现有 token，不复制参考图灰色填充。
- Image quality and asset fidelity：箭头来自 Heroicons 24px outline 官方矢量资产；无文本符号、CSS 图形或手绘 SVG。
- Copy and content：中英文均为品牌、产品、网站、开发四类；中文内容与参考图一致。

## Comparison history

- Earlier P2：首页仍为 6 个短标签，无法承载参考图的服务说明层级。
- Fix：重构为 4 张标题、说明、箭头卡片，并增加中英文内容模型。
- Post-fix evidence：1280 桌面四列、768 平板两列、375/532 手机单列，无内容裁切或横向溢出。
- Earlier P2：中文标题在内容数据中强制断行，532px 出现不自然的 3 行结构；页脚实际间距被高优先级规则压回 7px。
- Fix：删除硬换行并按自然宽度排版；提高页脚控制规则优先级并设为 40px。
- Post-fix evidence：532px 标题为自然 2 行；页脚实测语言链接与主题按钮间距 40px。

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

---

## Current build gate

- Latest report：`首页服务能力卡片与局部排版`。
- Required browser evidence、responsive checks、theme checks and console checks are recorded above.

final result: passed
