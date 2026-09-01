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

## Design QA：服务卡片去箭头与手机双列

**Findings**

- 无遗留 P0/P1/P2 问题。4 张卡片已移除箭头，并在 320px 起保持双列且无文字裁切。

**Implementation Checklist**

- [x] 删除全部箭头节点、样式和未使用图标文件。
- [x] 卡片结构收敛为标题与说明两行区域。
- [x] 320/375/532/768 为双列，1100/1280 为四列。
- [x] 中英文、亮暗模式、页脚布局与控制台通过检查。

## Evidence

- Source visual truth：用户本轮 532 × 766 浏览器标注截图，目标为去箭头、降低高度、手机双列。
- Implementation：浏览器本轮捕获的中文 375 × 766 与 532 × 766 CSS px 双列视图；另测 320、768、1100、1280。
- State：中英文首页亮色；另验证中文暗色。
- Full-view comparison：上一版 532px 单列卡片约 178px 高并带右下箭头；新版为 2 × 2，无箭头，中文约 133px 高。
- Focused region comparison：375px 中文卡片区已单独目视检查，四张卡片为等高双列，标题与说明均完整。
- Primary interactions tested：语言与主题切换保持工作；卡片无伪交互。
- Console errors checked：是，0 条。

## Required fidelity surfaces

- Fonts and typography：中文标题 22px、说明 13px；英文标题 17px，长词与说明无裁切。
- Spacing and layout rhythm：手机 2 列、12px 列间距；卡片使用紧凑内边距且不保留箭头空白。
- Colors and visual tokens：继续使用现有背景、文字、弱文字与 1px 边线 token，亮暗模式一致。
- Image quality and asset fidelity：服务卡片不再包含图像；箭头 SVG 已从源文件和构建产物删除。
- Copy and content：中文内容保持不变；英文做等义精简以适配最窄双列。

## Comparison history

- Earlier P2：手机为单列，4 张卡片纵向过长；箭头占据第三行并留下额外高度。
- Fix：删除箭头，卡片改为两行网格，手机使用 2 列并收紧字号、间距和内边距。
- Post-fix evidence：320px 中文 173px、英文 207px；375px 中文 153px、英文 187px；532px 中文约 133px、英文 147px，均无溢出。

final result: passed

---

## Design QA：首页移除两张占位作品

**Findings**

- 无遗留 P0/P1/P2 问题。用户标注的两张占位作品已经撤下，页面只循环展示方太与 FARFETCH 两个真实案例。

**Implementation Checklist**

- [x] 中英文内容模型均只保留两个带详情页链接的案例。
- [x] 删除第 3、4 项专用尺寸、顺序和移动端比例规则。
- [x] 保留双份轨道、28 秒线性无缝动画与 reduced-motion 静态横向浏览。
- [x] 检查 375/532/768/1100/1280 中英文视口、资源加载、链接与控制台。

## Evidence

- Source visual truth：本轮对话内两张 532 × 766 浏览器标注截图；蓝框分别指向两张待撤下的占位图（对话附件，无本地文件路径）。
- Implementation screenshot：[qa/home-gallery-two-cases-532.png](qa/home-gallery-two-cases-532.png)。
- Source pixels：532 × 766；implementation capture：517 × 744（浏览器内容区截图）；CSS viewport：532 × 766；deviceScaleFactor：1，无密度换算。
- State：中文首页、亮色、作品轨道运行中；另对英文首页做结构与响应式检查。
- Full-view comparison：标注截图中存在两张无详情链接的手机界面占位图；实现截图中只出现方太与 FARFETCH 的横向案例画面，没有占位节点或额外空白卡位。
- Focused region comparison：作品轨道是唯一变更区域，532px 截图中两张横向案例保持同高、间距连续；无需额外裁切图。
- Primary interactions tested：两张作品链接分别指向当前语言下的方太和 FARFETCH China 详情页；循环动画保持 `home-gallery-marquee`。
- Responsive evidence：375/532/768/1100/1280 × 中英文共 10 个组合均为 2 项、2 链接、0 占位、0 横向溢出，图片全部加载。
- Console errors checked：是，0 条 warning/error。

## Required fidelity surfaces

- Fonts and typography：本次未改字体、字号、字重、行高或标题换行；沿用现有系统字体栈。
- Spacing and layout rhythm：删除竖版占位图后，两个横向案例仍由现有 gap 和双份轨道连续衔接，第一屏高度不变。
- Colors and visual tokens：本次未改背景、前景、边线或亮暗模式 token。
- Image quality and asset fidelity：仅显示两个详情页已有真实素材；图片在 10 个响应式组合中均加载成功且保持原裁切规则。
- Copy and content：没有新增文案；仅撤下用户指定的两个占位内容，中英文同步。

## Comparison history

- Earlier P2：作品轨道包含两个未开放详情页的占位项目，用户明确要求先撤下。
- Fix：从中英文内容模型移除两项，并清理它们专用的桌面/手机布局规则；素材文件保留未删除。
- Post-fix evidence：532px 浏览器截图仅显示真实案例；DOM 和 10 个响应式组合均为 0 占位节点。

final result: passed

---

## Design QA：Info 移动端 Logo 与服务内容同步

**Findings**

- 无遗留 P0/P1/P2 问题。移动端 Logo 已整体收小，服务区在保留标题的同时与首页四张卡片完全一致。

**Implementation Checklist**

- [x] 767px 以下统一缩小 6 个真实客户 Logo，不修改品牌源文件。
- [x] Info 服务内容直接读取对应语言首页 `capabilities`，不再维护重复文案。
- [x] Info 服务列表复用首页卡片结构、双列/四列规则与亮暗模式 token。
- [x] 检查 375/532/768/1100/1280 中英文视口、内容一致性、图片加载与控制台。

## Evidence

- Source visual truth：本轮对话内两张 532 × 766 浏览器标注截图；分别框选客户 Logo 区和旧服务列表（对话附件，无本地文件路径）。
- Implementation screenshots：[qa/info-mobile-logos-532.png](qa/info-mobile-logos-532.png)、[qa/info-mobile-logo-services-532.png](qa/info-mobile-logo-services-532.png)。
- Source pixels：532 × 766；implementation captures：517 × 744（浏览器内容区截图）；CSS viewport：532 × 766；deviceScaleFactor：1，无密度换算。
- State：中文 Info、移动端、亮色；另验证中文暗色和英文内容。
- Full-view comparison：原图 Logo 接近填满两列宽度，旧服务为四行文本列表；实现中 Logo 留白增加，服务标题下改为与首页一致的 2 × 2 线框卡片。
- Focused region comparison：单独捕获客户区与服务区；ByteDance、Louis Vuitton、FOTILE、Haier、Daikin、Starbucks 均保持原始图形比例和清晰度。
- Primary interactions tested：语言切换后的英文 Info 使用 Brand、Product、Websites、Development；主题按钮切换暗色后 Logo、卡片和文字正常。
- Responsive evidence：375/532/768/1100/1280 × 中英文共 10 个组合均为 6 个已加载 Logo、4 张无裁切卡片、0 横向溢出。
- Content parity：中英文 Info 四项标题与说明均逐项等于对应首页内容。
- Console errors checked：是，0 条 warning/error。

## Required fidelity surfaces

- Fonts and typography：服务卡片复用首页 27/22/17px 标题和 16/13px 说明规则，系统字体栈、字重、行高保持一致。
- Spacing and layout rhythm：移动端 Logo 宽度为列宽 86%，内部上下 padding 增至 18px；服务卡片保持手机双列、桌面四列。
- Colors and visual tokens：继续使用现有背景、前景、弱文字和 1px 边线 token，亮暗模式一致。
- Image quality and asset fidelity：6 个 Logo 均为已有真实 SVG/PNG；仅调整容器内尺寸，不裁切、不替换、不重绘。
- Copy and content：Info 保留“服务 / Services”标题，四项名称和说明直接来自首页唯一内容源。

## Comparison history

- Earlier P2：移动端 Logo 视觉尺寸过满；Info 服务文案和列表形态与首页不一致。
- Fix：移动端 Logo 宽度收至 86%、可视高度收紧；Info 服务改用首页内容源和卡片组件。
- Post-fix evidence：532px 客户/服务截图显示更充足留白和 2 × 2 卡片；10 个响应式组合无溢出或裁切。
- Earlier P2：1100px 客户区存在 15px 横向溢出。
- Fix：客户区宽度改为 `min(1100px, calc(100% + 100px))`，保留桌面六列比例并适配实际内容宽度。
- Post-fix evidence：1100px 中英文均为 0 横向溢出。

final result: passed

---

## Current build gate

- Latest report：`Info 团队头像卡片`。
- Browser-rendered screenshots、responsive checks、content parity、theme and console checks are recorded above.

final result: passed

---

## Design QA：Info 团队头像卡片

**Findings**

- 无遗留 P0/P1/P2 问题。原文字分隔列表已按参考图改为 8 人头像卡片网格，并保留既有姓名与职位本地化规则。

**Implementation Checklist**

- [x] 8 张用户原图按成员身份映射，输出为正方形头像并保留人物主体。
- [x] 768px 起四列，767px 以下双列；卡片由头像、姓名、职位组成。
- [x] 头像复用全站加载占位、渐显和失败隐藏规则。
- [x] 检查 375/736/1100/1280，中英文与亮暗模式。

## Evidence

- Source visual truth：用户本轮附加的团队参考图，目标结构为标题下 4 × 2 头像、姓名、职位卡片（对话附件，无本地文件路径）。
- Implementation：本轮浏览器实测中文 Info 团队区；1146 × 766 CSS px 下为 4 × 2，736 × 766 下为双列。
- Source portrait files：`/Users/a11/Desktop/头像/1.png` 至 `8.png`，均为 800 × 800 RGBA PNG；构建后 8 张自然尺寸仍为 800 × 800。
- Responsive evidence：375px 两列各 156px；736px 两列各 334.5px；1100px 四列各 195.25px；1280px 四列各 224px，四档横向溢出均为 0。
- Localization：中文只显示中文姓名与中文职位；英文显示“中文姓名＋既有英文名/昵称”及英文职位，8 人完整无裁切。
- Loading state：8 张头像均带 `media-placeholder` 与 `media-image`，构建检查已覆盖团队资源路径；正常加载时 8/8 成功。

## Required fidelity surfaces

- Fonts and typography：沿用现有系统 sans 字体、300 字重；姓名 16/15px、职位 14/13px，层级和参考图一致。
- Spacing and layout rhythm：桌面 68px 列间距与 42px 行间距，移动端 12px 列间距与 30px 行间距；标题与网格保持清晰留白。
- Colors and visual tokens：文字、弱文字、背景与占位均复用现有亮暗主题 token。
- Image quality and asset fidelity：使用用户提供的 800 × 800 原图，无二次生成、压缩或拉伸；仅以 `object-fit: cover` 保持统一方形卡片。
- Copy and content：本轮不改成员姓名、昵称或职位，只替换展示结构并添加对应头像。

## Comparison history

- Earlier P1：团队区只有文字行与分隔线，没有用户参考图中的人物视觉识别和卡片节奏。
- Fix：加入 8 张头像，列表改为响应式卡片网格，并接入统一图片加载状态。
- Post-fix evidence：1146px 视图呈现完整 4 × 2 阵列，375/736px 自动转双列；所有头像加载、文字完整且无溢出。

final result: passed
